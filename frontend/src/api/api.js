import axios from "axios";

const api = axios.create({
  baseURL: "https://emotion-music-app-production.up.railway.app/analyze", // backend root
});

export async function analyzeEmotion(text) {
  const response = await api.post("/analyze", { text });
  return response.data;
}
