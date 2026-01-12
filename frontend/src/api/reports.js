import axios from "axios";

const BASE = "http://localhost:8000/api";

export async function downloadReport() {
  const res = await axios.get(`${BASE}/reports/download`, {
    responseType: "blob",
  });
  return res.data;
}
