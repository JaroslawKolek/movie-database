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
              <Link className="NavbarItem" to="/search">Search</Link>
              <Link className="NavbarItem" to="/login">Login</Link>
              <Link className="NavbarItem" to="/logout">Logout</Link>
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
