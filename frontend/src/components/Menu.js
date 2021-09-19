import React from 'react'
import {Link} from "react-router-dom";

const Menu = ({isAuthenticated, logoutAction}) => {
    let loginButton = ''
    if (isAuthenticated) {
        loginButton = <button className={'logout-btn'} onClick={logoutAction}>Выйти</button>
    } else {
        loginButton = <div className={'menu-item'}><Link to={'/login'}>Войти</Link></div>
    }
    return (
        <div className='menu'>
            <div className={'logo'}><Link to={'/'}>ToDoIst</Link></div>
            <div className={'menu-item'}><Link to={'/users'}>Пользователи</Link></div>
            <div className={'menu-item'}><Link to={'/projects'}>Проекты</Link></div>
            <div className={'menu-item'}><Link to={'/todos'}>ToDoСписок</Link></div>
            {loginButton}
        </div>)
}

export default Menu
