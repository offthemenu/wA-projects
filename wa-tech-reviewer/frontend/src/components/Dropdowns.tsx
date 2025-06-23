import { useEffect, useState } from "react";
import api from "../services/api";

type WireframeDropdownData = {
  projects: string[];
  devices_by_project: Record<string, string[]>;
  pages_by_project_device: Record<string, { name: string; path: string }[]>;
};

type DropdownsProps = {
  selectedProject: string;
  selectedDevice: string;
  selectedPage: string;
  onProjectChange: (value: string) => void;
  onDeviceChange: (value: string) => void;
  onPageChange: (pageName: string, pagePath: string) => void;
};

export default function Dropdowns({
  selectedProject,
  selectedDevice,
  selectedPage,
  onProjectChange,
  onDeviceChange,
  onPageChange,
}: DropdownsProps) {
  const [data, setData] = useState<WireframeDropdownData | null>(null);

  useEffect(() => {
    api.get("/wireframe")
      .then((res) => setData(res.data))
      .catch(console.error);
  }, []);

  if (!data) return <div>Loading...</div>;

  const projectOptions = data.projects;
  const deviceOptions = selectedProject ? data.devices_by_project[selectedProject] || [] : [];
  const pageOptions = selectedProject && selectedDevice
    ? data.pages_by_project_device[`${selectedProject}_${selectedDevice}`] || []
    : [];

  return (
    <div className="flex flex-col gap-4">
      <select value={selectedProject} onChange={e => {
        onProjectChange(e.target.value);
        onDeviceChange("");
        onPageChange("", "");
      }}>
        <option value="">Select project</option>
        {projectOptions.map(p => <option key={p} value={p}>{p}</option>)}
      </select>

      {selectedProject && (
        <select value={selectedDevice} onChange={e => {
          onDeviceChange(e.target.value);
          onPageChange("", "");
        }}>
          <option value="">Select device</option>
          {deviceOptions.map(d => <option key={d} value={d}>{d}</option>)}
        </select>
      )}

      {selectedProject && selectedDevice && (
        <select
          value={selectedPage}
          onChange={e => {
            const selName = e.target.value;
            const entry = pageOptions.find(x => x.name === selName);
            onPageChange(selName, entry?.path ?? "");
          }}
        >
          <option value="">Select page</option>
          {pageOptions.map(p => (
            <option key={p.path} value={p.name}>
              {p.name}
            </option>
          ))}
        </select>
      )}
    </div>
  );
}