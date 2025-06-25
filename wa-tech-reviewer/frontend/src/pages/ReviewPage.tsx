import {Button} from "@mui/material";
import { useEffect, useState } from "react";
import api from "../services/api";
import PDFUpload from "../components/PDFUpload";
import PDFViewer from "../components/PDFViewer";
import CommentForm from "../components/CommentForm";
import CommentList from "../components/CommentList";
import { TopDropdowns } from "../components/TopDropdowns";
import { BottomDropdowns } from "../components/BottomDropdowns";

type WireframeDropdownData = {
  projects: string[];
  devices_by_project: Record<string, string[]>;
  pages_by_project_device: Record<string, { name: string; path: string }[]>;
};

export default function ReviewPage() {
  const [data, setData] = useState<WireframeDropdownData | null>(null);
  const [uploadedPdf, setUploadedPdf] = useState<string | null>(null);

  const [project, setProject] = useState("");
  const [device, setDevice] = useState("");
  const [pageName, setPageName] = useState("");
  const [pagePath, setPagePath] = useState("");

  const [refreshFlag, setRefreshFlag] = useState(false);
  const triggerRefresh = () => setRefreshFlag((prev) => !prev);

  useEffect(() => {
    api.get("/wireframe").then((res) => setData(res.data)).catch(console.error);
  }, []);

  if (!data) return <div>Loading...</div>;

  return (
    <div className="w-full max-w-screen-xl mx-auto p-6 flex flex-col gap-8">
      <h1 className="text-2xl font-semibold">wA Frontend Technical Reviewer</h1>

      <TopDropdowns
        selectedProject={project}
        selectedDevice={device}
        onProjectChange={(p) => {
          setProject(p);
          setDevice("");
          setPageName("");
          setPagePath("");
        }}
        onDeviceChange={(d) => {
          setDevice(d);
          setPageName("");
          setPagePath("");
        }}
        data={data}
      />

      <PDFUpload onUpload={(filename) => setUploadedPdf(filename)} />

      <PDFViewer filename={uploadedPdf} />

      <BottomDropdowns
        selectedProject={project}
        selectedDevice={device}
        selectedPage={pageName}
        onPageChange={(name, path) => {
          setPageName(name);
          setPagePath(path);
        }}
        data={data}
      />

      {project && device && pageName && uploadedPdf && (
        <CommentForm
          context={{
            project,
            device,
            pageName,
            pagePath,
            filename: uploadedPdf,
          }}
          onSuccess={triggerRefresh}
        />
      )}

      <CommentList project={project} device={device} refreshFlag={refreshFlag} />
    </div>
  );
}
