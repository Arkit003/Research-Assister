import { useState } from "react";
import PdfViewer from "./components/PdfViewer"; 
import ChatPanel from "./components/ChatPanel";
import Header from "./components/Header";
import { uploadPdf } from "./api/upload"; 

export default function App() {
  const [pdfFile, setPdfFile] = useState(null);
  const [status, setStatus] = useState("");

  async function handleFileSelect(e) {
    const file = e.target.files[0];
    if (!file) return;

    setPdfFile(file);
    setStatus("Uploading...");

    try {
      await uploadPdf(file);
      setStatus("Indexed & Ready ");
    } catch {
      setStatus("Upload failed");
    }
  }

  return (
    <div className="app-layout">
      <Header />

      <div className="main-container">
        
        {/* Left Side: PDF Viewer */}
        <div className="pdf-panel">
          <div className="pdf-toolbar">
            <div className="file-input-wrapper">
              <input type="file" accept="application/pdf" onChange={handleFileSelect} />
            </div>
            <span className="status-text">{status}</span>
          </div>

          <div className="pdf-viewer-container">
            {pdfFile ? (
              <PdfViewer file={pdfFile} />
            ) : (
              <div style={{ 
                color: '#94a3b8', 
                marginTop: '100px', 
                textAlign: 'center' 
              }}>
                <p>Upload a PDF to begin research</p>
              </div>
            )}
          </div>
        </div>

        {/* Right Side: Chat */}
        <div className="chat-panel">
          <ChatPanel />
        </div>
        
      </div>
    </div>
  );
}