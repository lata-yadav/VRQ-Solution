import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Header from './components/Header';
import PatientsList from './pages/PatientsList';
import AddPatient from './pages/AddPatient';
import UploadPrescription from './pages/UploadPrescription';
import './App.css';

function App() {
  return (
    <Router>
      <div className="app-container">
        <Sidebar />
        <div className="main-content">
          <Header />
          <Routes>
            <Route path="/" element={<PatientsList />} />
            <Route path="/add-patient" element={<AddPatient />} />
            <Route path="/upload-prescription/:id" element={<UploadPrescription />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
