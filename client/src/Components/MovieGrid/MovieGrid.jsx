import MovieCard from "./MovieCard"
import { useLocation } from "react-router-dom";
import "./MovieGrid.css"


function MovieGrid() {
    const movies = useLocation().state.data || [];

    return (
        <div className="grid">
            {movies.map((movie, index) => (
                <MovieCard key={index} {...movie} />
            ))}
        </div>
    )
}

export default MovieGrid;
