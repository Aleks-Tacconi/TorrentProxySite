import { useEffect } from 'react'
import './SearchRedirect.css'
import axios from 'axios'
import { useParams } from "react-router-dom";
import { useNavigate } from 'react-router-dom';

function toSlug(title) {
    return title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
}

function SearchRedirect() {
    const { title } = useParams();
    const navigate = useNavigate();

    const fetchAPI = async () => {
        const token = localStorage.getItem('token');
        const response = await axios.get(`http://127.0.0.1:8000/api/movies?query=${encodeURIComponent(title)}`, {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        });
        const data = response.data.data;
        navigate(`/download/search/result/${toSlug(title)}`, { state: { data } });
    }

    useEffect(() => {
        fetchAPI();
    }, [title])


    return (
        <></>
    )
}

export default SearchRedirect
