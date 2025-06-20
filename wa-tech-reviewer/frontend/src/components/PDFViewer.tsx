import { useState, useMemo } from "react";
import { Document, Page, pdfjs } from "react-pdf";
import "react-pdf/dist/Page/AnnotationLayer.css";

pdfjs.GlobalWorkerOptions.workerSrc = "/pdf.worker.min.mjs";

type PDFViewerProps = { filename: string | null };

export default function PDFViewer({ filename }: PDFViewerProps) {
  const [numPages, setNumPages] = useState(0);

  if (!filename) {
    console.log("No filename prop provided");
    return <p className="text-gray-500">No PDF selected</p>;
  }

  const fileUrl = `${import.meta.env.VITE_API_BASE_URL}/uploads/${filename}`;
  console.log("Loading PDF from:", fileUrl);

  const fileProp = useMemo(() => ({ url: fileUrl }), [fileUrl]);  // critical

  return (
    <div className="mt-6 border p-4 rounded bg-white text-black">
      <Document
        file={fileProp}
        onLoadSuccess={({ numPages }) => setNumPages(numPages)}
        onSourceError={(error) => console.error("Source load error:", error)}
        onLoadError={(error) => console.error("PDF load error:", error)}
      >
        {Array.from({ length: numPages }).map((_, index) => (
          <Page key={index} pageNumber={index + 1} />
        ))}
      </Document>
    </div>
  );
}
