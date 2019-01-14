import React from 'react';
import { Alert } from 'react-bootstrap';

class LogoutComponent extends React.Component {
    constructor(props){
        super(props)

        this.state = {
            responseStatus: undefined
        };
        this.logout();
    }

    getToken() {
        return localStorage.getItem('token');
    }

    logout = () => {
        if(this.getToken() !== undefined){
            fetch('http://localhost:8000/api/users/logout/', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type':'application/json',
                    'Authorization': `Token ${this.getToken()}`
                },
            })
                .then(response => {
                    this.setState({responseStatus: response.status});
                    if(response.status === 200){
                        localStorage.setItem('token', undefined);
                        localStorage.setItem('username', '');
                    }
                })
        }     
    }

    renderAlert = () => {
        if(this.state.responseStatus === 200) {
            return <Alert bsStyle="success"> You Have Successfully Logged Out Of Your Account. </Alert>
        } else if (this.state.responseStatus === 401) {
            return <Alert bsStyle="danger"> You are logged out. Please, log in to use search section</Alert>
        }
        return;
    }

    render() {
        return (
            <div>
                { this.renderAlert() }
            </div>
        )
    }
}

export default LogoutComponent;