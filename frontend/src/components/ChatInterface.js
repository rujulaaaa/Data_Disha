import React, { useState } from "react";
import { askQuery } from "../api/query";

export default function ChatInterface() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState([]);

  const sendQuery = async () => {
    if (!query.trim()) return;

    const res = await askQuery(query);
    setResponse(res.output || []);
  };

  return (
    <div className="chat-container">
      <h3>Ask a Question</h3>
      <textarea
        placeholder="Example: Show donor-wise budget vs expenditure"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <button onClick={sendQuery}>Submit</button>

      <div className="response-box">
        {response.length > 0 ? (
          <pre>{JSON.stringify(response, null, 2)}</pre>
        ) : (
          <p>No response yet.</p>
        )}
      </div>
    </div>
  );
}
