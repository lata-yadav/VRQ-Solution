import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import './UploadPrescription.css';

function UploadPrescription() {
  const { id } = useParams();
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Uploading prescription for patient', id, file);
    // Logic for uploading file and linking it to the patient
  };

  return (
    <div className="upload-prescription">
      <h2>Upload Prescription for Patient {id}</h2>
      <form onSubmit={handleSubmit}>
        <label>Prescription</label>
        <input type="file" onChange={handleFileChange} required />

        <button type="submit">Upload</button>
      </form>
    </div>
  );
}

export default UploadPrescription;
