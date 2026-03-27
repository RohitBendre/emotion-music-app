import React, { useState } from "react";
import InputForm from "./components/InputForm";
import Results from "./components/Results";
import { analyzeEmotion } from "./api/api";
import "./App.css";

function App() {
  const [result, setResult] = useState(null);

  const handleAnalyze = async (text) => {
    try {
      const response = await analyzeEmotion(text);
      setResult(response);
    } catch (error) {
      console.error("Error fetching results:", error);
    }
  };

  const handleBack = () => {
    setResult(null);
  };

  return (
    <div className="app-container">
      {!result ? (
        <InputForm onAnalyze={handleAnalyze} />
      ) : (
        <Results result={result} onBack={handleBack} />
      )}
    </div>
  );
}

export default App;
