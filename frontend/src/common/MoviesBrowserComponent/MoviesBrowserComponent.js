import React from 'react';
import { Pager } from 'react-bootstrap';
import { DebounceInput } from 'react-debounce-input';
import { Redirect } from 'react-router-dom';

import './MoviesBrowserComponent.css';
import { get } from './../../utils/api';
import MovieTileComponent from '../MovieTileComponent/MovieTileComponent';

class MoviesBrowserComponent extends React.Component {
    state = {
        searchValue: '',
        loading: true,
        pageNumber: 1,
        moviesList: [],
        responseStatus: undefined,
    };        
    
    componentDidMount() {
        this.getMovies();
    }

    componentDidUpdate(prevProps, prevState){
        if(prevState.pageNumber !== this.state.pageNumber || prevState.searchValue !== this.state.searchValue){
            this.getMovies();
        }
    }

    handlePageChange = (number) => {
        this.setState({pageNumber: number});
    }

    renderRedirect = () => {
        if(this.state.responseStatus === 401) {
            return <Redirect to='/login'/>;
        };
    }

    getMovies = () => {
        this.setState({
            moviesList: [],
            loading: true,
        });
        
        get(`/movies/search/?title=${this.state.searchValue}&page=${this.state.pageNumber}`).then(data => {
                this.setState({
                    moviesList: data.data,
                    loading: false,
                    responseStatus: data.status
                })
            }
        );
    }

    showEmptyPageInfoIfEmpty = () => {
        if(this.state.moviesList.length === 0 && !this.state.loading) {
            return <div className="EmptyPageInfo">
                <p className="EmptyPageTitle"> No movies here ¯\_(ツ)_/¯ </p>
                <p className="EmptyPageTitle EmptyPageSubTitle"> Please, change filter or page number </p>
            </div>; 
        }
    }

    showLoadingScreen = () => {
        if(this.state.loading){
            return <p className="EmptyPageInfo EmptyPageTitle"> Loading... (ง°ل͜°)ง </p>
        }
        return;
    }

    renderMoviesList = () => {
        if(this.state.responseStatus === 200){
            return this.state.moviesList.map((movie, index) => 
                <MovieTileComponent movieInformation={movie} key={index}/>
            )
        }
        return;
    }

    render() {
        return (
            <div className="MovieBrowser">
                { this.renderRedirect() }
                <div className="FiltersSection">
                    <DebounceInput
                        type="text"
                        placeholder="Movie title..."
                        value={this.state.searchValue}
                        minLength={2}
                        debounceTimeout={800}
                        onChange={event => this.setState({searchValue: event.target.value})}
                    />
                </div>
                <div>
                    { this.showEmptyPageInfoIfEmpty() }
                    <div>
                        { this.showLoadingScreen() }
                        { this.renderMoviesList() }
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