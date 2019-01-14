import React from 'react';
import { Alert, FormGroup, FormControl, ControlLabel, Button } from 'react-bootstrap';
import { Redirect } from 'react-router-dom';

import './LoginComponent.css';
import { post } from './../../utils/api';

class LoginComponent extends React.Component {
    state = {
        username: '',
        password: '',
        responseStatus: undefined,
        redirect: false,
    }

    loginUser = () => {
        post('/users/login/', JSON.stringify({
                username: this.state.username,
                password: this.state.password
            })).then(response => {
                this.setState({responseStatus: response.status});
                return response.json();
            }).then(responseData => {
                if(this.state.responseStatus === 200){
                    localStorage.setItem('token', responseData);
                    localStorage.setItem('username', this.state.username);
                    this.setState({redirect: true});
                }
            })
    }

    renderError = () => {
        if(this.state.responseStatus === 400) {
            return <Alert bsStyle="danger">
                <strong>Holy guacamole!</strong> Username or password is incorrect!
            </Alert>;
        }
        return;
    }

    redirectIfOk = () => {
        if(this.state.redirect) {
            return <Redirect to='/search'/>
        }
        return;
    }

    render() {
        return (
            <div className="LoginComponent">
                <ControlLabel> Welcome in MovieDatabase! </ControlLabel>
                <form>
                    <FormGroup>
                        <ControlLabel> Username: </ControlLabel>
                        <FormControl 
                            type="text"
                            value={this.state.username}
                            onChange={event => this.setState({username: event.target.value})}
                        />
                    </FormGroup>
                    <FormGroup>
                        <ControlLabel> Password: </ControlLabel>
                        <FormControl 
                            type="password"
                            value={this.state.password}
                            onChange={event => this.setState({password: event.target.value})}
                        />
                    </FormGroup>
                    <Button bsStyle="primary" onClick={this.loginUser}> Log in </Button>
                </form>
                { this.renderError() }
                { this.redirectIfOk() }
            </div>
        )
    }
}

export default LoginComponent;