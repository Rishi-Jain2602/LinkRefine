import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSpinner } from '@fortawesome/free-solid-svg-icons';
import './styles/Upload.css'

export default function Upload() {
  const [selectedUrl, setSelectedUrl] = useState(null);
  const [uploadResponse, setUploadResponse] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();

  const handleUrlChange = (e) => {
    setSelectedUrl(e.target.value);
    setUploadResponse(null); 
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!selectedUrl) return;

    setIsLoading(true); // Start loading
   
    try {
      const res = await fetch("http://127.0.0.1:8000/linkrefine/upload", {
        method: "POST",
        headers: {'Content-Type': 'application/json',},
        body: JSON.stringify({ "url": selectedUrl }),
      });
      const data = await res.json();
      setUploadResponse(data);

      if (data.message) {
        localStorage.setItem('link_id', data.link_id);
        setTimeout(() => {
          navigate("/review");
        }, 3000);
      }else{
        alert("Error in uploading URL")
      }

    } catch (error) {
      console.error("Error uploading file:", error);
    } finally {
      setIsLoading(false); // Stop loading in all cases
    }
  };

  return (
    <div className='upload-container'>
      <form className='upload-form' onSubmit={handleSubmit}>
        <label htmlFor="formFileLg" className="form-label">
          Upload Your Document Here
        </label>
        <input class="form-control form-control-lg" type="text" onChange={handleUrlChange} placeholder="Enter LinkedIn Profile URL here…" readonly></input>
        <button type="submit" className="btn btn-primary mt-3">Upload</button>
      </form>

      <div className="status-section">
        {isLoading && (
          <div className="mt-3 spinner-text">
            <FontAwesomeIcon icon={faSpinner} spin /> Uploading... Please wait.
          </div>
        )}
        {uploadResponse && (
          <div className="mt-3">
            <p className="text-success">Upload successful! Redirecting to Review Page...</p>
          </div>
        )}
      </div>
    </div>
  );
}