import MovieCard from "./MovieCard"
import "../MovieGrid/MovieGrid.css"
import axios from "axios";
import { useEffect, useState } from "react";


function MovieGrid() {
    const [movies, setArray] = useState([]);

    const fetchAPI = async () => {
        const token = localStorage.getItem('token');
        const response = await axios.get(`http://127.0.0.1:8000/api/local`, {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        });

        setArray(response.data.data);
    }

    useEffect(() => {
        fetchAPI();
    }, [])

    return (
        <div className="grid">
            {movies.map((movie, index) => (
                <MovieCard key={index} {...movie} />
            ))}
        </div>
    )
}

export default MovieGrid;
