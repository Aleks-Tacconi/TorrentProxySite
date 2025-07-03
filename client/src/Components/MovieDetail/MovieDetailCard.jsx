import "./MovieDetailCard.css"

function MovieDetailCard(props) {
    return (
        <div className="detail-card">
            <img src={props.cover_url} width="200"></img>
            <h1>{props.title}</h1>
            <h2>{props.year}</h2>
        </div>
    )
}

export default MovieDetailCard;
