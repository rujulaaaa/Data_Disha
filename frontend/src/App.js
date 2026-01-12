import React, { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Dashboard from "./pages/Dashboard";
import Login from "./pages/Login";

export default function App() {
  const [token, setToken] = useState(null);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route
          path="/login"
          element={<Login onLogin={(t) => setToken(t)} />}
        />
        <Route
          path="/dashboard"
          element={
            token ? (
              <Dashboard />
            ) : (
              <p>Please login first.</p>
            )
          }
        />
      </Routes>
    </BrowserRouter>
  );
}