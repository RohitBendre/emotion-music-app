import React, { useState } from "react";

const InputForm = ({ onAnalyze }) => {
  const [text, setText] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (text.trim()) {
      onAnalyze(text);
    }
  };

  return (
    <div className="input-container">
      <div className="hero-section">
        <h1 className="main-title">🎶 Moodify</h1>
        <p className="subtitle">Tell us how you feel, and we'll play the vibe 🎧</p>
      </div>

      <form onSubmit={handleSubmit} className="input-card">
        <textarea
          className="text-area"
          placeholder="Type how you're feeling... (e.g. I feel relaxed, I feel energetic)"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
        <button type="submit" className="btn">
          Find Songs 🎵
        </button>
      </form>
    </div>
  );
};

export default InputForm;
