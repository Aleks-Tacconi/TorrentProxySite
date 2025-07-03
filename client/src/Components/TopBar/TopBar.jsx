import "./TopBar.css"
import Search from "./Search";

function TopBar() {
    return (
        <div className="topbar">
            <div className="left">
                <a href="/" className="logo">TPS</a>
                <a href="/local">Local</a>
            </div>
            <Search />
        </div>
    )
}

export default TopBar;
