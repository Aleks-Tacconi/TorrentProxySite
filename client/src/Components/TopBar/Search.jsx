import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import "./Search.css"

function Search() {
    const [query, setQuery] = useState("");
    const navigate = useNavigate();

    const handleKeyDown = (e) => {
        if (e.key === "Enter" && query.trim() !== "") {
            navigate(`/download/search/${encodeURIComponent(query.trim())}`);
        }
    };

    return (
        <div className="search-wrapper">
            <div className="search">
                <i className="fas fa-search"></i>
                <input
                    type="text"
                    placeholder="Search..."
                    onChange={(e) => setQuery(e.target.value)}
                    onKeyDown={handleKeyDown}
                />
            </div>
        </div>
    )
}

export default Search
