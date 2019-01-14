import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import { Navbar, Nav, NavItem, Button } from 'react-bootstrap';

import './App.css';

import LoginPage from '../LoginPage/LoginPage';
import LogoutPage from '../LogoutPage/LogoutPage';
import MoviesPage from '../MoviesPage/MoviesPage';

class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <Navbar inverse>
            <Navbar.Header>
              <Navbar.Brand>
                <p> MovieDatabase </p>
              </Navbar.Brand>
            </Navbar.Header>
            <Nav>
              <Navbar.Text>
                Signed in as: {localStorage.getItem('username')}
              </Navbar.Text>
              <NavItem>
                <Link to="/search">Search</Link>
              </NavItem>
              <NavItem>
                <Link to="/login">Login</Link>
              </NavItem>
              <NavItem>
                <Link to="/logout">Logout</Link>
              </NavItem>
            </Nav>
          </Navbar>
          <Route path="/search" component={ MoviesPage } />
          <Route path="/login" component={ LoginPage } />
          <Route path="/logout" component={ LogoutPage } />
        </div>
      </Router>
    );
  }
}

export default App;
