import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import './PatientsList.css';

function PatientsList() {
  const [patients, setPatients] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    // Fetching patient data from the backend
    const fetchPatients = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/patients/');
        setPatients(response.data);
      } catch (err) {
        console.error('Error fetching patients:', err);
        setError('Failed to fetch patients');
      }
    };

    fetchPatients();
  }, []);

  return (
    <div className="patients-list">
      <h2>Patients List</h2>
      {error && <p className="error">{error}</p>}
      <ul>
        {patients.map((patient) => (
          <li key={patient.id}>
            {patient.name} ({patient.email})
            <Link to={`/upload-prescription/${patient.id}`}>Upload Prescription</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PatientsList;