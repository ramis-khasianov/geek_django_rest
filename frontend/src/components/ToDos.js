import React from 'react'

const ToDoItem = ({todo}) => {
    return (
        <div className='user-list-item'>
            <p>{todo.id}</p>
            <p>{todo.author}</p>
            <p>{todo.text}</p>
        </div>
    )
}

const ToDosList = ({todos}) => {
    return (
        <div className='user-list'>
            <div className="user-list-header">
                <p>Id</p>
                <p>Author</p>
                <p>Text</p>
            </div>
            {todos.map((todo) => (
                <ToDoItem todo={todo}/>
            ))}
        </div>
    )
}

export default ToDosList