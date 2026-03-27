import React from "react";
import SongCard from "./SongCard";

const Results = ({ result, onBack }) => {
  return (
    <div className="results-container">
      <div className="top-bar">
        <button onClick={onBack} className="back-btn">⬅ Home</button>
      </div>

      <h2>
        Detected Emotion: <strong>{result.emotion}</strong>
      </h2>
      <p>Suggested Genres: {result.genres.join(", ")}</p>

      <div className="songs-grid">
        {result.songs.map((song, idx) => (
          <SongCard key={idx} song={song} />
        ))}
      </div>
    </div>
  );
};

export default Results;
