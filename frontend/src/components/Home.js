import React from 'react';
import './styles/Home.css';
import { useNavigate } from 'react-router-dom';

export default function Home() {
  const navigate = useNavigate()
  const handleNavigate = () =>{
    navigate("/upload")
  }
  return (
    <div className="home-container">
        <div className="home-content">

      <h1 className="home-title">Welcome to LinkRefine</h1>
      <p className="home-description">
      Optimize your LinkedIn profile for better visibility and professional impact. 
          LinkRefine helps enhance your profile by improving key sections like your 
          profile picture, experience, about section, and more. Get noticed by recruiters 
          and professionals with a polished, standout profile.
      </p>
      <button className="home-button" onClick={handleNavigate}>Get Started</button>
        </div>
    </div>
  );
}