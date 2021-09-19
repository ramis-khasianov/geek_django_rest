import React from "react";

class LoginForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: '',
            password: ''
        }
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value})
    }

    handleSubmit(event) {
        this.props.getToken(this.state.username, this.state.password)
        event.preventDefault()
    }

    render() {
        return (
            <form className={'login-form'} onSubmit={(event) => this.handleSubmit(event)}>
                <div className={'form-item'}>
                    <label htmlFor={'username'} className={'form-label'}>Логин</label>
                    <input type={'text'} name={'username'} className={'form-input'} id={'username'}
                           value={this.state.username}
                           onChange={(event => this.handleChange(event))}/>
                </div>
                <div>
                    <label htmlFor={'password'} className={'form-label'}>Пароль:</label>
                    <input type={'password'} name={'password'} className={'form-input'} id={'password'}
                           value={this.state.password}
                           onChange={(event => this.handleChange(event))}/>
                </div>
                <input type={'submit'} className={'form-submit-button'} value={'Login'}/>
            </form>
        )
    }
}

export default LoginForm