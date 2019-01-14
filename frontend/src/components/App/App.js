import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import { Navbar, Nav, NavItem } from 'react-bootstrap';

import './App.css';

import AboutPage from '../AboutPage/AboutPage';
import LoginPage from '../LoginPage/LoginPage';
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
                <Link to="/">Home</Link>
              </NavItem>
              <NavItem>
                <Link to="/movies">Movies</Link>
              </NavItem>
              <NavItem>
                <Link to="/login">Login</Link>
              </NavItem>
            </Nav>
          </Navbar>
          <Route exact path="/" component={ AboutPage } />
          <Route path="/movies" component={ MoviesPage } />
          <Route path="/login" component={ LoginPage } />
        </div>
      </Router>
    );
  }
}

export default App;
