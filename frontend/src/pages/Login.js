import React, { useState } from "react";
import axios from "axios";

export default function Login({ onLogin }) {
  const [username, setU] = useState("");
  const [password, setP] = useState("");

  const login = async () => {
    const res = await axios.post("http://localhost:8000/api/login", {
      username,
      password,
    });
    onLogin(res.data.token);
  };

  return (
    <div>
      <h2>Login</h2>
      <input placeholder="Username" onChange={(e) => setU(e.target.value)} />
      <input
        placeholder="Password"
        type="password"
        onChange={(e) => setP(e.target.value)}
      />
      <button onClick={login}>Login</button>
    </div>
  );
}
