import { Link } from "react-router-dom";
import { useEffect, useState } from 'react'
import axios from 'axios'
import "./MovieCard.css"

function toSlug(title) {
    return title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
}


function MovieCard(props) {
    const [array, setArray] = useState(null);

    const fetchAPI = async (link, title, id) => {
        const token = localStorage.getItem('token');
        const response = await axios.get(`http://127.0.0.1:8000/api/metadata?link=${encodeURIComponent(link)}&title=${encodeURIComponent(title)}&id=${encodeURIComponent(id)}`, {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        });
        setArray(response.data.data);
    }

    useEffect(() => {
        fetchAPI(props.torrent_access_point, props.title, props.id);
    }, [])

    if (array === null) {
        return (<></>)
    }

    return (
        <Link to={`/movie/${toSlug(array.title)}`} state={{ movie: array }} className="card">
            <img src={array.cover_url} width="200"></img>
            <h1>{array.title}</h1>
            <h2>{array.year}</h2>
        </Link>
    )
}

export default MovieCard;
