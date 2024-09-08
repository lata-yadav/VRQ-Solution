import React from 'react';
import { Link } from 'react-router-dom';
import './Sidebar.css';

function Sidebar() {
  return (
    <div className="sidebar">
      <ul>
        <li><Link to="/">Patients List</Link></li>
        <li><Link to="/add-patient">Add Patient</Link></li>
      </ul>
    </div>
  );
}

export default Sidebar;
