import React from 'react';
import { Pager } from 'react-bootstrap';
import { DebounceInput } from 'react-debounce-input';
import { Redirect } from 'react-router-dom';

import './MoviesBrowserComponent.css';
import MovieTileComponent from '../MovieTileComponent/MovieTileComponent';

class MoviesBrowserComponent extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            searchValue: '',
            pageNumber: 1,
            moviesList: [],
        };        
    }

    componentDidMount() {
        this.getMovies();
    }

    componentDidUpdate(prevProps, prevState){
        if(prevState.pageNumber !== this.state.pageNumber || prevState.searchValue !== this.state.searchValue){
            this.getMovies();
        }
    }

    handlePageChange = (number) => {
        this.setState({pageNumber: number})
    }

    renderRedirect = () => {
        if(typeof(this.state.moviesList) != "object"){
            return <Redirect to='/login'/>;
        };
    }


    getToken() {
        return localStorage.getItem('token');
    }

    getMovies = () => {
        fetch(`http://localhost:8000/api/movies/search/?title=${this.state.searchValue}&page=${this.state.pageNumber}`, {
            headers: {
                'Authorization': `Token ${this.getToken()}`
            },
            method: 'GET'
        })
            .then(res => res.json())
            .then(result => this.setState({moviesList: result}))
    }

    showEmptyPageInfoIfEmpty = () => {
        if(this.state.moviesList.length === 0) {
            return <div className="EmptyPageInfo">
                <p className="EmptyPageTitle"> No movies here ¯\_(ツ)_/¯ </p>
                <p className="EmptyPageTitle EmptyPageSubTitle"> Please, change filter or page number </p>
            </div>; 
        }
    }

    render() {
        return (
            <div className="MovieBrowser">
                <div className="FiltersSection">
                    <DebounceInput
                        type="text"
                        placeholder="Movie title..."
                        value={this.state.searchValue}
                        minLength={2}
                        debounceTimeout={700}
                        onChange={event => this.setState({searchValue: event.target.value})}
                    />
                </div>
                <div>
                    { this.showEmptyPageInfoIfEmpty() }
                    <div>
                        { this.renderRedirect() }
                        { this.state.moviesList.map((movie, index) => 
                            <MovieTileComponent movieInformation={movie} key={index}/>
                        )}
                    </div>
                    <div className="PagerSection">
                        <Pager>
                            <Pager.Item
                              previous
                              disabled={this.state.pageNumber === 1}
                              onClick={() => this.handlePageChange(this.state.pageNumber - 1)}
                            >
                                &larr; Previous Page
                            </Pager.Item>
                            <li> Pager Number: { this.state.pageNumber } </li>
                            <Pager.Item
                              next
                              disabled={this.state.moviesList.length === 0} 
                              onClick={() => this.handlePageChange(this.state.pageNumber + 1)}
                            >
                                Next Page &rarr;
                            </Pager.Item>
                        </Pager>
                    </div>
                </div>
            </div>
        )
    }
}

export default MoviesBrowserComponent;