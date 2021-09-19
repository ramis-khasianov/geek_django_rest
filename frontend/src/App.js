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
import Cookies from "universal-cookie/lib";
import LoginForm from "./components/Auth";

const API_ROOT = 'http://127.0.0.1:8000/api/';
const API_AUTH_ROOT = 'http://127.0.0.1:8000/api-token-auth/';
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
            todos: [],
            token: ''
        }
    };

    setToken(token){
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.loadData())
    }

    isAuthenticated(){
        return this.state.token !== ''
    }

    logout() {
        this.setToken('')
        this.setState({
            'users': [],
            'projects': [],
            'todos': []
        })
    };

    getTokenFromStorage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.loadData())
    }

    getToken(username, password) {
        axios.post(API_AUTH_ROOT, {username: username, password: password})
            .then(response => {
                this.setToken(response.data['token'])
            })
            .catch(error => alert('Неверный логин или пароль'))
    };

    getHeaders() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.isAuthenticated()) {
            headers['Authorization'] = `Token ${this.state.token}`
        }
        return headers
    }

    loadData() {
        const headers = this.getHeaders()
        axios
            .get(getUrl('users'), {headers})
            .then(response => {
                    this.setState({users: response.data.results});
            })
            .catch((error) => console.log(error));

        axios
            .get(getUrl('projects'), {headers})
            .then(response => {
                this.setState({projects: response.data.results});
            })
            .catch((error) => console.log(error));

        axios
            .get(getUrl('todos'), {headers})
            .then(response => {
                this.setState({todos: response.data.results});
            })
            .catch((error) => console.log(error));
    }

    componentDidMount() {
        this.getTokenFromStorage()
    }

    render() {
        return (
            <div className='App'>
                <BrowserRouter>
                    <Menu isAuthenticated={this.isAuthenticated()} logoutAction={() => this.logout()}/>
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
                        <Route exact path={'/projects/:id'} component={() =>
                            <ProjectDetails  projects={this.state.projects}/>
                        }/>
                        <Route exact path={'/login'}>
                            {this.isAuthenticated() ?
                                <Redirect to={'/'}/> :
                                <LoginForm getToken={(username, password) => this.getToken(username, password)}/>}
                        </Route>
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
