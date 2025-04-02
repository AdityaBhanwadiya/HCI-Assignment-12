import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [name, setName] = useState('');
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    
    try {
      const response = await axios.post('http://127.0.0.1:5001/api/hello', { name });
      setMessage(response.data.message);
    } catch (err) {
      setError('Failed to get message. Please try again.');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <div className="container">
        <h1>Welcome to AI Greetings</h1>
        <form onSubmit={handleSubmit} className="form">
          <div className="input-group">
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="Enter your name"
              required
              className="input"
            />
          </div>
          <button type="submit" disabled={loading} className="button">
            {loading ? 'Getting Message...' : 'Get Greeting'}
          </button>
        </form>
        
        {error && <p className="error">{error}</p>}
        
        {message && (
          <div className="message-container">
            <p className="message">{message}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
