import axios from 'axios';
import './App.css';
import React from "react";
import Menu from "./components/Menu";
import Footer from "./components/Footer";
import UserList from "./components/Users";

const API_ROOT = 'http://127.0.0.1:8000/api/';
const getUrl = url => `${API_ROOT}${url}`;


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      users: []
    }
  }

  componentDidMount() {
    axios
        .get(getUrl('users'))
        .then((response) => {
          const users = response.data;
          this.setState({
            users: users
          });
        })
        .catch((error) => console.log(error));
  }

  render() {
    return (
        <div className='App'>
            <Menu/>
            <UserList users={this.state.users}/>
            <Footer/>
        </div>
    );
  }
}

export default App;
