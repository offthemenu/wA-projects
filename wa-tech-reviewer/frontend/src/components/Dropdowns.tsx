import { useEffect, useState } from "react";
import api from "../services/api";

type WireframeDropdownData = {
  projects: string[];
  devices_by_project: Record<string, string[]>;
  pages_by_project_device: Record<string, { name: string; path: string }[]>;
};

export default function Dropdowns() {
  const [data, setData] = useState<WireframeDropdownData | null>(null);

  const [project, setProject] = useState("");
  const [device, setDevice] = useState("");
  const [page, setPage] = useState("");

  useEffect(() => {
    api
      .get("/wireframe")
      .then((res) => setData(res.data))
      .catch((err) => console.error("Failed to fetch wireframe data:", err));
  }, []);

  if (!data) return <div className="text-gray-500">Loading...</div>;

  const deviceOptions = project ? data?.devices_by_project?.[project] || [] : [];
  const pageOptions =
    project && device
      ? data?.pages_by_project_device?.[`${project}_${device}`] || []
      : [];

  return (
    <div className="flex flex-col gap-4 bg-white text-black p-4 border">
      {/* Project dropdown */}
      <div>
        <label className="block text-sm font-medium mb-1">Project</label>
        <select
          value={project}
          onChange={(e) => {
            setProject(e.target.value);
            setDevice("");
            setPage("");
          }}
          className="border rounded p-2 w-full"
        >
          <option value="">Select project</option>
          {data?.projects.map((p) => (
            <option key={p} value={p}>
              {p}
            </option>
          ))}
        </select>
      </div>

      {/* Device dropdown */}
      {project && (
        <div>
          <label className="block text-sm font-medium mb-1">Device</label>
          <select
            value={device}
            onChange={(e) => {
              setDevice(e.target.value);
              setPage("");
            }}
            className="border rounded p-2 w-full"
          >
            <option value="">Select device</option>
            {deviceOptions.map((d) => (
              <option key={d} value={d}>
                {d}
              </option>
            ))}
          </select>
        </div>
      )}

      {/* Page dropdown */}
      {project && device && (
        <div>
          <label className="block text-sm font-medium mb-1">Page</label>
          <select
            value={page}
            onChange={(e) => setPage(e.target.value)}
            className="border rounded p-2 w-full"
          >
            <option value="">Select page</option>
            {pageOptions.map((p) => (
              <option key={p.path} value={p.name}>
                {p.name}
              </option>
            ))}
          </select>
        </div>
      )}
    </div>
  );
}
