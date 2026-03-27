import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000", // backend root
});

export async function analyzeEmotion(text) {
  const response = await api.post("/analyze", { text });
  return response.data;
}
