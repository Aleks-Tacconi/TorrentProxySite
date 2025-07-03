import "./MovieDetail.css"
import { useLocation } from 'react-router-dom'
import { useEffect, useState } from 'react'
import MovieDetailCard from "./MovieDetailCard";
import TorrentButton from "./TorrentButton";
import axios from 'axios'

function MovieDetail() {
    const { movie } = useLocation().state || {};
    const [array, setArray] = useState([]);

    if (!movie) return <div>Error</div>;

    const fetchAPI = async (link, id) => {
        try {
            const token = localStorage.getItem('token');
            const response = await axios.get(`http://127.0.0.1:8000/api/torrents?link=${encodeURIComponent(link)}&key=${encodeURIComponent(id)}`, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });
            setArray(response.data.data);
        } catch (error) {
            console.error(error);
        }
    };

    useEffect(() => {
        fetchAPI(movie.link, movie.id);
    }, []);


    return (
        <div className="parent">
            <div className="desc-card">
                <div className="card-layout">
                    <MovieDetailCard {...movie} />
                    <div className="button-space">
                        <div className="button-column">
                            <h1 className="button-heading">Choose a download option</h1>
                            {array.map((torrent, index) => (
                                <TorrentButton key={index} {...torrent} />
                            ))}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default MovieDetail;
