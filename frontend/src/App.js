import React from "react";
import {BrowserRouter, Redirect, Route, Switch} from "react-router-dom";
import axios from 'axios';
import './App.css';
import Menu from "./components/Menu";
import Footer from "./components/Footer";
import UsersList from "./components/Users";
import ToDosList from "./components/ToDos";
import ProjectsList from "./components/Projects";
import ProjectDetails from "./components/ProjectDetails";

const API_ROOT = 'http://127.0.0.1:8000/api/';
const getUrl = url => `${API_ROOT}${url}`;


const pageNotFound404 = ({location}) => {
    return (
        <h2>Page at '{location.pathname}' not found</h2>
    )
}


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            users: [],
            projects: [],
            todos: []
        }
    }

    componentDidMount() {
        console.log('Hello')
        axios
            .get(getUrl('users'))
            .then((response) => {
                const users = response.data.results;
                this.setState({
                    users: users
                });
            })
            .catch((error) => console.log(error));
        axios
            .get(getUrl('projects'))
            .then((response) => {
                const projects = response.data.results;
                this.setState({
                    projects: projects
                });
            })
            .catch((error) => console.log(error));
        axios
            .get(getUrl('todos'))
            .then((response) => {
                const todos = response.data.results;
                this.setState({
                    todos: todos
                });
            })
            .catch((error) => console.log(error));
    }

    render() {
        return (
            <div className='App'>
                <BrowserRouter>
                    <Menu/>
                    <Switch>
                        <Route exact path={'/'}>
                            <ToDosList todos={this.state.todos}/>
                        </Route>
                        <Route exact path={'/users'}>
                            <UsersList users={this.state.users}/>
                        </Route>
                        <Route exact path={'/projects'}>
                            <ProjectsList projects={this.state.projects}/>
                        </Route>
                        <Route exact path={'/projects/:id'} component={
                            () => <ProjectDetails projects={this.state.projects}/>
                        }/>
                        <Redirect from={'/todos'} to={'/'}/>
                        <Route component={pageNotFound404}/>
                    </Switch>
                    <Footer/>
                </BrowserRouter>
            </div>
        );
    }
}

export default App;
