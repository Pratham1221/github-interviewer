import '../styles/LoadingSpinner.css'

function LoadingSpinner() {
  return (
    <div className="loading-spinner">
      <div className="spinner"></div>
      <p>Analyzing GitHub profile and generating interview...</p>
    </div>
  )
}

export default LoadingSpinner
