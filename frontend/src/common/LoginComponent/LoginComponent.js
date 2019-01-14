import React from 'react';
import { Alert } from 'react-bootstrap';
import { Redirect } from 'react-router-dom';

import './LoginComponent.css';

class LoginComponent extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            username: '',
            password: '',
            error: false,
            success: false,
        }
        this.loginUser = this.loginUser.bind(this);

    }

    loginUser() {
        fetch('http://localhost:8000/api/users/login/', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type':'application/json'
            },
            body: JSON.stringify({
                username: this.state.username,
                password: this.state.password
            })
        })
            .then(response => {
                if(response.status === 400){
                    this.setState({error: true});
                } 
                return response.json();
            })
            .then( (responseData) => {
                localStorage.setItem('token', responseData);
                localStorage.setItem('username', this.state.username);
                this.setState({success: true});
            },
            (error) => {
                console.error(error);
            }
        )
    }

    renderError = () => {
        if(this.state.error) {
            return <Alert bsStyle="danger">
                <strong>Holy guacamole!</strong> Username or password is incorrect!
            </Alert>;
        }
        return;
    }

    redirectIfOk = () => {
        if(this.state.success) {
            return <Redirect to='/search'/>
        }
        return;
    }

    render() {
        return (
            <div>
                <div>
                    LOGIN 
                </div>
                <form>
                    <label>
                        Username:
                        <input
                         type="text"
                         value={this.state.username} 
                         onChange={(event) => this.setState({username: event.target.value})}
                        />  
                    </label>
                    <label>
                        Password:
                        <input
                         type="password"
                         value={this.state.password} 
                         onChange={(event) => this.setState({password: event.target.value})}
                        />  
                    </label>
                    <button type="button" onClick={this.loginUser}>Log in</button>
                </form>
                { this.renderError() }
                { this.redirectIfOk() }
            </div>
        )
    }
}

export default LoginComponent;