import { useState } from "react";
import api from "../services/api";

export default function PDFUpload({ onUpload }: { onUpload: (filename: string)  => void }) {
  const [file, setFile] = useState<File | null>(null);
  const [status, setStatus] = useState<string | null>(null);

  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await api.post("/upload_pdf", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setStatus(`✅ Uploaded: ${res.data.filename}`);
      onUpload(res.data.filename);
    } catch (err) {
      console.error("Upload failed:", err);
      setStatus("❌ Upload failed");
    }
  };

  return (
    <div className="border p-4 rounded bg-white text-black">
      <label className="block mb-2 font-medium">Upload PDF</label>
      <input
        type="file"
        accept="application/pdf"
        onChange={(e) => setFile(e.target.files?.[0] || null)}
      />
      <button
        onClick={handleUpload}
        className="mt-2 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      >
        Upload
      </button>
      {status && <p className="mt-2 text-sm">{status}</p>}
    </div>
  );
}
