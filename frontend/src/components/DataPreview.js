import React, { useState } from "react";
import axios from "axios";

export default function DataPreview() {
  const [data, setData] = useState(null);

  const load = async () => {
    const res = await axios.get("http://localhost:8000/api/preview");
    setData(res.data);
  };

  return (
    <div className="preview-container">
      <h3>Preview Uploaded Data</h3>
      <button onClick={load}>Load Data</button>
      <pre>{data ? JSON.stringify(data, null, 2) : "No data"}</pre>
    </div>
  );
}
