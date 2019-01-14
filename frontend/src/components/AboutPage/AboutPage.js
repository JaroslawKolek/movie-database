import React from 'react';
import Jumbotron from 'react-bootstrap/lib/Jumbotron';

import './AboutPage.css';

class AboutPage extends React.Component {
    render() {
        return (
            <div>
                <Jumbotron>
                    <h1>Hi!</h1>
                    <p>
                        This is a simple web app for movies browsing.
                        ʕ•ᴥ•ʔ
                    </p>
                </Jumbotron>
            </div>
        )
    }
}

export default AboutPage;