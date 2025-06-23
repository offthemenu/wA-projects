import { useState } from "react";
import Dropdowns from "../components/Dropdowns";
import PDFUpload from "../components/PDFUpload";
import PDFViewer from "../components/PDFViewer";
import CommentForm from "../components/CommentForm";
import CommentList from "../components/CommentList";

export default function ReviewPage() {
  const [uploadedPdf, setUploadedPdf] = useState<string | null>(null);
  const [currentPage, setCurrentPage] = useState<number>(1);

  return (
    <div className="w-full max-w-screen-xl mx-auto p-6 flex flex-col gap-8">
      <h1 className="text-2xl font-semibold">Tech Review Tool</h1>

      <Dropdowns />

      <PDFUpload onUpload={(filename: string) => setUploadedPdf(filename)} />

      <PDFViewer
        filename={uploadedPdf}
        onPageChange={setCurrentPage}
      />

      {/* <CommentForm /> */}
      {/* <CommentList /> */}
    </div>
  );
}
