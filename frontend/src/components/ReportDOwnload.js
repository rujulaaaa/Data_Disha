import React from "react";
import { downloadReport } from "../api/reports";

export default function ReportDownload() {
  const download = async () => {
    const blob = await downloadReport();
    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "magicbus_report.pdf";
    document.body.appendChild(a);
    a.click();
    a.remove();
  };

  return (
    <div className="report-box">
      <h3>Download Latest Report</h3>
      <button onClick={download}>Download PDF</button>
    </div>
  );
}
