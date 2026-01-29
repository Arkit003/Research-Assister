import React, { useState } from "react";
import { Document, Page, pdfjs } from "react-pdf";

// Set up the worker for react-pdf (standard boilerplate)
pdfjs.GlobalWorkerOptions.workerSrc = `//unpkg.com/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.js`;

export default function PdfViewer({ file }) {
  const [numPages, setNumPages] = useState(null);

  function onDocumentLoadSuccess({ numPages }) {
    setNumPages(numPages);
  }

  return (
    <div className="pdf-viewer-content">
      <Document
        file={file}
        onLoadSuccess={onDocumentLoadSuccess}
        loading={
          <div style={{ color: "#64748b", marginTop: "20px" }}>
            Loading PDF...
          </div>
        }
        error={
          <div style={{ color: "#ef4444", marginTop: "20px" }}>
            Failed to load PDF.
          </div>
        }
      >
        {/* Render ALL pages so the user can scroll naturally */}
        {Array.from(new Array(numPages), (el, index) => (
          <Page
            key={`page_${index + 1}`}
            pageNumber={index + 1}
            renderTextLayer={false} y
            renderAnnotationLayer={false}
            width={600} 
            className="pdf-page-shadow"
          />
        ))}
      </Document>
    </div>
  );
}