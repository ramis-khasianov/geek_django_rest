import requests

user_data = {
    'username': 'username3',  # username0 - admin, 1 - project_owner, 2-4 - developers
    'password': 'geekbrains'
}

response = requests.post(
    'http://127.0.0.1:8000/api-token-auth/',
    data=user_data
)

if response.status_code == 200:
    token = response.json().get('token')

    response = requests.post(
        'http://127.0.0.1:8000/api/projects/',
        headers={
            'Authorization': f'token {token}'
        }
    )

    print(f'Using regular Token Auth you\'ve got code {response.status_code}, '
          f'json: {response.json()}')


# JWT - потестил как все это работает.
response_jwt = requests.post(
    'http://127.0.0.1:8000/api/token/',
    data=user_data
)

if response_jwt.status_code == 200:
    refresh_token = response_jwt.json().get('refresh')

    response_jwt_refresh = requests.post(
        'http://127.0.0.1:8000/api/token/refresh/',
        data={
            'refresh': refresh_token
        }
    )

    if response_jwt_refresh.status_code == 200:
        access_token = response_jwt_refresh.json().get('access')

        access_jwt_response = requests.post(
            'http://127.0.0.1:8000/api/projects/',
            headers={
                'Authorization': f'Bearer {access_token}'
            }
        )

        print(f'Using JWT you\'ve got code {access_jwt_response.status_code}, '
              f'json: {access_jwt_response.json()}')
