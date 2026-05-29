import '../styles/InterviewResult.css'

function InterviewResult({ result }) {
  const { username, interview, profile } = result

  const downloadInterview = () => {
    const element = document.createElement('a')
    const file = new Blob([interview], { type: 'text/markdown' })
    element.href = URL.createObjectURL(file)
    element.download = `${username}-interview.md`
    document.body.appendChild(element)
    element.click()
    document.body.removeChild(element)
  }

  const copyToClipboard = () => {
    navigator.clipboard.writeText(interview)
  }

  return (
    <div className="interview-result">
      <div className="profile-header">
        <h2>@{username}</h2>
        {profile && (
          <div className="profile-info">
            <p><strong>Bio:</strong> {profile.bio || 'N/A'}</p>
            <p><strong>Public Repos:</strong> {profile.public_repos}</p>
            <p><strong>Followers:</strong> {profile.followers}</p>
            {profile.languages && profile.languages.length > 0 && (
              <p><strong>Top Languages:</strong> {profile.languages.join(', ')}</p>
            )}
          </div>
        )}
      </div>

      <div className="interview-content">
        <h3>Generated Interview</h3>
        <div className="interview-text">
          {interview.split('\n').map((line, idx) => (
            <p key={idx}>{line}</p>
          ))}
        </div>
      </div>

      <div className="action-buttons">
        <button onClick={downloadInterview} className="btn-download">
          📥 Download as Markdown
        </button>
        <button onClick={copyToClipboard} className="btn-copy">
          📋 Copy to Clipboard
        </button>
      </div>
    </div>
  )
}

export default InterviewResult
