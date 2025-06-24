import { useState } from "react";
import Dropdowns from "../components/Dropdowns";
import PDFUpload from "../components/PDFUpload";
import PDFViewer from "../components/PDFViewer";
import CommentForm from "../components/CommentForm";
import CommentList from "../components/CommentList";

export default function ReviewPage() {
  const [uploadedPdf, setUploadedPdf] = useState<string | null>(null);

  // Dropdown selections
  const [project, setProject] = useState<string>("");
  const [device, setDevice] = useState<string>("");
  const [pageName, setPageName] = useState<string>("");
  const [pagePath, setPagePath] = useState<string>("");

  // Refresh trigger state for comments
  const [refreshFlag, setRefreshFlag] = useState(false);
  const triggerRefresh = () => setRefreshFlag(prev => !prev);

  return (
    <div className="w-full max-w-screen-xl mx-auto p-6 flex flex-col gap-8">
      <h1 className="text-2xl font-semibold">Tech Review Tool</h1>

      <Dropdowns
        selectedProject={project}
        selectedDevice={device}
        selectedPage={pageName}
        onProjectChange={setProject}
        onDeviceChange={setDevice}
        onPageChange={(name, path) => {
          setPageName(name);
          setPagePath(path);
        }}
      />


      <PDFUpload onUpload={(filename: string) => setUploadedPdf(filename)} />

      <PDFViewer
        filename={uploadedPdf}
      />

      {project && device && pageName && uploadedPdf && (
        <CommentForm
          context={{
            project,
            device,
            pageName,
            pagePath,
            filename: uploadedPdf!,

          }}
          onSuccess={triggerRefresh}
        />
      )}

      <CommentList
        project={project}
        device={device}
        refreshFlag={refreshFlag}
      />
    </div>
  );
}
