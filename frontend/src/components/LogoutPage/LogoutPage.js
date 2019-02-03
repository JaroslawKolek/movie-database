import React from 'react';
import { Alert } from 'react-bootstrap';

import { post, getToken } from '../../utils/api';

class LogoutPage extends React.Component {
    state = {
        responseStatus: undefined
    };

    componentDidMount() {
        this.logout();
    }

    logout = () => {
        if(getToken() !== undefined){
            post('/users/logout/', {}).then(response => {
                let status = response.status;
                this.setState({responseStatus: status})
                if(status === 200){
                    localStorage.setItem('token', '');
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

export default LogoutPage;