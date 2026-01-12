import React from "react";
import ChatInterface from "../components/ChatInterface";
import ReportDownload from "../components/ReportDownload";

export default function Dashboard() {
  return (
    <div>
      <h2>Dashboard</h2>
      <ChatInterface />
      <ReportDownload />
    </div>
  );
}
