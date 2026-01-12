import React, { useState } from "react";
import { uploadFile } from "../api/upload";

export default function FileUpload() {
  const [file, setFile] = useState(null);
  const [msg, setMsg] = useState("");

  const submit = async () => {
    if (!file) {
      setMsg("Please select a file first!");
      return;
    }

    const res = await uploadFile(file);
    setMsg(res.message);
  };

  return (
    <div className="upload-box">
      <h3>Upload Data File</h3>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={submit}>Upload</button>
      <p>{msg}</p>
    </div>
  );
}
