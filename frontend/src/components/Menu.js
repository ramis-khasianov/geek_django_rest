import React from 'react'
import {Link} from "react-router-dom";

const Menu = () => {
    return (
        <div className='menu'>
            <div className={'logo'}><Link to={'/'}>ToDoIst</Link></div>
            <div className={'menu-item'}><Link to={'/users'}>Пользователи</Link></div>
            <div className={'menu-item'}><Link to={'/projects'}>Проекты</Link></div>
            <div className={'menu-item'}><Link to={'/todos'}>ToDoСписок</Link></div> {/* Блин, PyCharm ToDo_выделяет (*/}
        </div>)
}

export default Menu
