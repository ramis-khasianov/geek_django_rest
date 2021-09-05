import React from 'react'
import {Link} from "react-router-dom";

const ProjectItem = ({project}) => {
    return (
        <div className='user-list-item'>
            <p>
                <Link to={`/projects/${project.id}`}>
                    {project.name}
                </Link>
            </p>
            <p>{project.repository}</p>
        </div>
    )
}

const ProjectsList = ({projects}) => {
    return (
        <div className='user-list'>
            <div className="user-list-header">
                <p>Project Name</p>
                <p>Repository url</p>
            </div>
            {projects.map((project) => (
                <ProjectItem project={project}/>
            ))}
        </div>
    )
}

export default ProjectsList