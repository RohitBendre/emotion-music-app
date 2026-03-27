import React from "react";

const SongCard = ({ song }) => {
  return (
    <div className="song-card">
      <h3>{song.name}</h3>
      <p>{song.artist}</p>
      <a href={song.url} target="_blank" rel="noopener noreferrer">
        <button className="spotify-btn">Listen on Spotify</button>
      </a>
    </div>
  );
};

export default SongCard;
