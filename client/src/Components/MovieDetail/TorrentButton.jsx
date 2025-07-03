import React, { useState } from "react";
import "./TorrentButton.css";
import axios from "axios";

function TorrentButton(props) {
    const [showConfirm, setShowConfirm] = useState(false);
    const [showDownloading, setShowDownloading] = useState(false);

    const handleClick = () => setShowConfirm(true);

    const handleConfirm = () => {
        setShowConfirm(false);
        setShowDownloading(true);
        const token = localStorage.getItem('token');

        axios(`http://127.0.0.1:8000/api/download?link=${encodeURIComponent(props.url)}&name=${encodeURIComponent(props.name)}`, {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        });
    };

    const handleCancel = () => setShowConfirm(false);
    const handleCloseDownloading = () => setShowDownloading(false);

    return (
        <>
            <button type="button" onClick={handleClick}>
                {props.name}
            </button>

            {showConfirm && (
                <div className="modal-backdrop">
                    <div className="modal">
                        <p>Are you sure you want to download<br /><br />{props.name}?</p>
                        <div className="modal-buttons">
                            <button onClick={handleCancel}>No</button>
                            <button onClick={handleConfirm}>Yes</button>
                        </div>
                    </div>
                </div>
            )}

            {showDownloading && (
                <div className="modal-backdrop">
                    <div className="modal">
                        <p>Downloading <strong>{props.name}</strong>...</p>
                        <div className="modal-buttons">
                            <button onClick={handleCloseDownloading}>Close</button>
                        </div>
                    </div>
                </div>
            )}
        </>
    );
}

export default TorrentButton;

