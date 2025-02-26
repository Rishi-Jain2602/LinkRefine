import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import './styles/Navbar.css';

export default function Navbar() {
  const location = useLocation();
  return (
    <nav className="custom-navbar">
      <div className="navbar-container">
        <Link className="navbar-brand" to="/">LinkRefine</Link>
        
        <input type="checkbox" id="menu-toggle" className="menu-toggle" />
        <label htmlFor="menu-toggle" className="hamburger">&#9776;</label>
        
        <div className="navbar-links">
          {location.pathname === '/' ? (
            <>
            <a className="nav-link" href="https://github.com/Rishi-Jain2602/LinkRefine.git" target="_blank" rel="noopener noreferrer">Github</a>
          </>
          ) :
          location.pathname === '/upload' ? (
            <Link className="nav-link" to="/review">Review</Link>
          ) : location.pathname === '/review' ? (
            <Link className="nav-link" to="/upload">Upload</Link>
          ) : null}
        </div>
      </div>
    </nav>
  );
}