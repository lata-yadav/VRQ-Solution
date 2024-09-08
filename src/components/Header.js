import React from 'react';
import './Header.css';
import logo from './logo.png';

function Header() {
  return (
    <header className="header">
      <img src={logo} alt="Logo" className="logo" />
      <h1>Electronic Medical Record (EMR)</h1>
    </header>
  );
}

export default Header;
