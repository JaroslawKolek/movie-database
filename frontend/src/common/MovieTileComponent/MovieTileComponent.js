import React from 'react';

import './MovieTileComponent.css';

class MovieTileComponent extends React.Component {
    render() {
        const movieInformation = this.props.movieInformation;
        return (
            <div className="MovieTile">
                <img className="Poster" src={movieInformation.poster_url} alt={movieInformation.imdb_id} />
                <div>
                    { movieInformation.title }
                </div>
            </div>
        )
    }
}

export default MovieTileComponent;