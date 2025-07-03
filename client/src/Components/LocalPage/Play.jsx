import "./Play.css"
import { useLocation } from 'react-router-dom'

function Play() {
    const { movie } = useLocation().state || {};
    const path = movie.link.replace(/^\.\/client\/public/, '');

    const subtitlePath = path.replace(/[^/]+$/, 'subtitle.vtt');

    return (
        <div className="video-container">
            <video controls autoPlay className="video-player">
                <source src={path} />
                <track 
                    src={subtitlePath} 
                    kind="subtitles" 
                    srcLang="en" 
                    label="English" 
                    default 
                />
                Your browser does not support the video tag.
            </video>
        </div>
    );
}

export default Play;
