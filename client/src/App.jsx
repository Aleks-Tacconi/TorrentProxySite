import './App.css'

import { Routes, Route, Navigate } from "react-router-dom"
import MovieDetail from "./Components/MovieDetail/MovieDetail"
import SearchRedirect from './Components/SearchRedirect'
import TopBar from "./Components/TopBar/TopBar"
import MovieGrid from './Components/MovieGrid/MovieGrid'
import HomePage from './Components/HomePage/HomePage'
import LocalPage from './Components/LocalPage/LocalPage'
import Play from './Components/LocalPage/Play'
import Login from './Components/Login'

function isLoggedIn() {
    return !!localStorage.getItem("token");
}

function PrivateRoute({ children }) {
    return isLoggedIn() ? children : <Navigate to="/login" />;
}

function App() {
    return (
        <div className="bg">
            <TopBar />

            <Routes>
                <Route path="/login" element={<Login />} />

                <Route
                    path="/"
                    element={
                        <PrivateRoute>
                            <HomePage />
                        </PrivateRoute>
                    }
                />

                <Route
                    path="/movie/:title"
                    element={
                        <PrivateRoute>
                            <MovieDetail />
                        </PrivateRoute>
                    }
                />

                <Route
                    path="/local"
                    element={
                        <PrivateRoute>
                            <LocalPage />
                        </PrivateRoute>
                    }
                />

                <Route
                    path="/local/play"
                    element={
                        <PrivateRoute>
                            <Play />
                        </PrivateRoute>
                    }
                />

                <Route
                    path="/download/search/:title"
                    element={
                        <PrivateRoute>
                            <SearchRedirect />
                        </PrivateRoute>
                    }
                />

                <Route
                    path="/download/search/result/:title"
                    element={
                        <PrivateRoute>
                            <MovieGrid />
                        </PrivateRoute>
                    }
                />
            </Routes>
        </div>
    );
}

export default App;

