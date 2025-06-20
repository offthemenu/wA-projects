import Dropdowns from "../components/Dropdowns";
import PDFViewer from "../components/PDFViewer";
import CommentForm from "../components/CommentForm";
import CommentList from "../components/CommentList";

export default function ReviewPage() {
  return (
    <div className="p-6 flex flex-col gap-6 max-w-7xl mx-auto">
      <h1 className="text-2xl font-semibold">🧪 Tech Review Tool</h1>
      <Dropdowns />
      <PDFViewer />
      <CommentForm />
      <CommentList />
    </div>
  );
}
