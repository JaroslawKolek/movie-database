import React from 'react';
import { Button } from 'react-bootstrap';

import './MovieTileComponent.css';

class MovieTileComponent extends React.Component {
    constructor(props){
        super(props)

        this.state = {
            inFavorites: this.props.movieInformation.is_favorite
        }
    }

    IMAGE_NOT_AVAIABLE = 'https://upload.wikimedia.org/wikipedia/commons/f/fc/No_picture_available.png';

    getToken() {
        return localStorage.getItem('token');
    }

    addOrRemoveToFavorites = () => {
        fetch('http://localhost:8000/api/users/favorite-movies/', {
            method: 'PUT',
            headers: {
                'Accept': 'application/json',
                'Content-Type':'application/json',
                'Authorization': `Token ${this.getToken()}`
            },
            body: JSON.stringify({
                imdb_id: this.props.movieInformation.imdb_id
            })
        })
            .then(response => {
                if(response.status === 200) {
                    this.setState({inFavorites: !this.state.inFavorites});
                }
            })        
    }

    addOrRemove = () => {
        if(this.state.inFavorites) {
            return "Remove from favorties";
        }
        return "Add to favorites";
    }

    getPoster = () => {
        let poster = this.props.movieInformation.poster_url;
        if(this.props.movieInformation.poster_url){
            return poster;
        }
        return this.IMAGE_NOT_AVAIABLE;
    }

    render() {
        const movieInformation = this.props.movieInformation;
        return (
            <div className="MovieTile">
                <img className="Poster" src={this.getPoster()} alt={movieInformation.imdb_id} />
                <div>
                    { movieInformation.title }
                </div>
                <Button bsStyle="primary" onClick={this.addOrRemoveToFavorites}> { this.addOrRemove() } </Button>
            </div>
        )
    }
}

export default MovieTileComponent;