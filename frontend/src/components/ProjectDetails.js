import React from 'react'
import UsersList from "./Users";
import ToDosList from "./ToDos";
import {useParams} from "react-router-dom";

const ProjectDetails = ({projects}) => {
    let {id} = useParams();
    let project = projects.filter((project) => project.id === +id)[0]

    return (
        <div>
            <h1>Команда проекта {project.name}</h1>
            <UsersList users={project.members}/>
            <h1>В списке ToDo</h1>
            <ToDosList todos={project.todos}/>
        </div>
    )
}

export default ProjectDetails