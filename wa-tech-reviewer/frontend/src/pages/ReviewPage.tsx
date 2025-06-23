import { useState } from "react";
import Dropdowns from "../components/Dropdowns";
import PDFUpload from "../components/PDFUpload";
import PDFViewer from "../components/PDFViewer";
import CommentForm from "../components/CommentForm";
import CommentList from "../components/CommentList";

export default function ReviewPage() {
  const [uploadedPdf, setUploadedPdf] = useState<string | null>(null);

  return (
    <div className="p-6 flex flex-col gap-6 max-w-4xl mx-auto">
      <h1 className="text-2xl font-semibold">Tech Review Tool</h1>
      <div className="p-6">
        <Dropdowns />
      </div>
      <PDFUpload onUpload={(filename: string) => setUploadedPdf(filename)} />
      <PDFViewer filename={uploadedPdf} />
      {/* <CommentForm /> */}
      {/* <CommentList /> */}
    </div>
  );
}
