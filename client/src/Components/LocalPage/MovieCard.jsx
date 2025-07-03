import { Link } from "react-router-dom";
import "../MovieGrid/MovieCard.css"


function MovieCard(props) {
    return (
        <Link to="/local/play" className="card" state={{ movie: props }}>
            <img src={props.cover_url} width="200"></img>
            <h1>{props.title}</h1>
            <h2>{props.year}</h2>
        </Link>
    )
}

export default MovieCard;
