import "./HomePage.css"
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'

function HomePage() {
    const [query, setQuery] = useState("");
    const navigate = useNavigate();

    const handleKeyDown = (e) => {
        if (e.key === "Enter" && query.trim() !== "") {
            navigate(`/download/search/${encodeURIComponent(query.trim())}`);
        }
    };

    return (
        <div className="home-container">
            <div className="search-card">
                <i className="fas fa-search search-icon"></i>
                <input
                    type="text"
                    className="search-input"
                    placeholder="Search..."
                    onChange={(e) => setQuery(e.target.value)}
                    onKeyDown={handleKeyDown}
                />
            </div>

            <section className="how-it-works">
                <h2>About</h2>
                <p>This site currently includes:</p>
                <ul>
                    <li>
                        <a href="https://en.wikipedia.org/wiki/Feature_film" target="_blank" rel="noopener noreferrer">
                            Feature Films
                        </a> — sourced from&nbsp;
                        <a href="https://archive.org/details/feature_films" target="_blank" rel="noopener noreferrer">The Internet Archive</a>
                    </li>
                    <li>
                        <a href="https://en.wikipedia.org/wiki/Public_domain" target="_blank" rel="noopener noreferrer">
                            Public Domain Films
                        </a> — sourced from&nbsp;
                        <a href="https://www.publicdomaintorrents.info/nshowcat.html?category=ALL" target="_blank" rel="noopener noreferrer">
                            Public Domain Torrents
                        </a>
                    </li>
                </ul><br></br>

                <h3>Get Started</h3>
                <ul>
                    <li>Enter a movie title into the search bar above</li>
                    <li>Select a result to view available download options</li>
                    <li>Use the "Local" tab to play downloaded media</li>
                </ul>
            </section>
        </div>
    )
}

export default HomePage;
