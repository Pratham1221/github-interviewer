import { useState } from 'react'
import '../styles/InterviewForm.css'

function InterviewForm({ onSubmit, disabled }) {
  const [username, setUsername] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    if (username.trim()) {
      onSubmit(username.trim())
      setUsername('')
    }
  }

  return (
    <form onSubmit={handleSubmit} className="interview-form">
      <div className="form-group">
        <label htmlFor="username">GitHub Username</label>
        <input
          id="username"
          type="text"
          placeholder="e.g., torvalds, gvanrossum"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          disabled={disabled}
          required
        />
      </div>
      <button type="submit" disabled={disabled} className="btn-submit">
        {disabled ? 'Generating...' : 'Generate Interview'}
      </button>
    </form>
  )
}

export default InterviewForm
