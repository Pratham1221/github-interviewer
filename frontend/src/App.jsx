import { useState } from 'react'
import axios from 'axios'
import './App.css'
import InterviewForm from './components/InterviewForm'
import InterviewResult from './components/InterviewResult'
import LoadingSpinner from './components/LoadingSpinner'

function App() {
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)

  const handleSubmit = async (username) => {
    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const response = await axios.post('/api/analyze', { username })
      
      if (response.data.status === 'error') {
        setError(response.data.error)
      } else {
        setResult(response.data)
      }
    } catch (err) {
      setError(err.message || 'Failed to generate interview. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>📊 GitHub AI Interviewer</h1>
        <p>Generate personalized technical interviews from GitHub profiles</p>
        <p className="repo-link">
          <a href="https://github.com/Pratham1221/github-interviewer" target="_blank" rel="noopener noreferrer">
            View repository on GitHub
          </a>
        </p>
      </header>

      <main className="app-main">
        {!result ? (
          <>
            <InterviewForm onSubmit={handleSubmit} disabled={loading} />
            {loading && <LoadingSpinner />}
            {error && <div className="error-message">{error}</div>}
          </>
        ) : (
          <>
            <InterviewResult result={result} />
            <button 
              className="btn-back"
              onClick={() => setResult(null)}
            >
              ← Analyze Another Profile
            </button>
          </>
        )}
      </main>

      <footer className="app-footer">
        <p>Built with FastAPI & React | Powered by Google Gemini</p>
      </footer>
    </div>
  )
}

export default App
