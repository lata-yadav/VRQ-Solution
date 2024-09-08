import React, { useState } from 'react';
import axios from 'axios';
import './AddPatient.css';

function AddPatient() {
  const [formData, setFormData] = useState({ name: '', email: '' });
  const [error, setError] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Send the form data to your FastAPI backend
      const response = await axios.post('http://127.0.0.1:8000/patients/', formData);
      console.log('Patient added successfully:', response.data);
      // Handle success (e.g., redirect or show a success message)
    } catch (err) {
      console.error('Error adding patient:', err);
      setError('Failed to add patient');
    }
  };

  return (
    <div className="add-patient">
      <h2>Add Patient</h2>
      <form onSubmit={handleSubmit}>
        <label>Name</label>
        <input type="text" name="name" value={formData.name} onChange={handleChange} required />

        <label>Email</label>
        <input type="email" name="email" value={formData.email} onChange={handleChange} required />

        <button type="submit">Add Patient</button>
      </form>
      {error && <p className="error">{error}</p>}
    </div>
  );
}

export default AddPatient;