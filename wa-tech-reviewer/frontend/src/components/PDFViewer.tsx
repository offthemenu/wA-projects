import { Viewer, Worker } from '@react-pdf-viewer/core';
import { defaultLayoutPlugin } from '@react-pdf-viewer/default-layout';
import '@react-pdf-viewer/core/lib/styles/index.css';
import '@react-pdf-viewer/default-layout/lib/styles/index.css';

type PDFViewerProps = { filename: string | null };

export default function PDFViewer({ filename }: PDFViewerProps) {
  if (!filename) return <p className="text-gray-500">No PDF selected</p>;

  const fileUrl = `${import.meta.env.VITE_API_BASE_URL}/uploads/${filename}`;
  const defaultLayoutPluginInstance = defaultLayoutPlugin();

  return (
    <div
      className="border bg-white p-4 mt-6 w-full"
      style={{
        border: '1px solid rgba(0, 0, 0, 0.3)',
        height: '80vh',
      }}
    >
      <Worker workerUrl="https://unpkg.com/pdfjs-dist@3.4.120/build/pdf.worker.min.js">
        <Viewer
          fileUrl={fileUrl}
          plugins={[defaultLayoutPluginInstance]}
        />
      </Worker>
    </div>
  );
}
