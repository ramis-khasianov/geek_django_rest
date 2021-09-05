import React from 'react'

const UserItem = ({user}) => {
    return (
        <div className='user-list-item'>
            <p>{user.firstName}</p>
            <p>{user.lastName}</p>
            <p>{user.email}</p>
        </div>
    )
}

const UsersList = ({users}) => {
    return (
        <div className='user-list'>
            <div className="user-list-header">
                <p>Name</p>
                <p>Last Name</p>
                <p>Email</p>
            </div>
            {users.map((user) => (
                <UserItem user={user}/>
            ))}
        </div>
    )
}

export default UsersList
