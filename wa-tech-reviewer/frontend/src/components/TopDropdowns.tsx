import { useEffect, useState } from "react";
import api from "../services/api";

type WireframeDropdownData = {
  projects: string[];
  devices_by_project: Record<string, string[]>;
  pages_by_project_device: Record<string, { name: string; path: string }[]>;
};

type TopDropdownsProps = {
  selectedProject: string;
  selectedDevice: string;
  onProjectChange: (value: string) => void;
  onDeviceChange: (value: string) => void;
  data: WireframeDropdownData;
};

export function TopDropdowns({
  selectedProject,
  selectedDevice,
  onProjectChange,
  onDeviceChange,
  data,
}: TopDropdownsProps) {
  const projectOptions = data.projects;
  const deviceOptions = selectedProject ? data.devices_by_project[selectedProject] || [] : [];

  return (
    <div className="flex flex-wrap gap-4">
      <select
        value={selectedProject}
        onChange={(e) => {
          onProjectChange(e.target.value);
          onDeviceChange("");
        }}
        className="p-2 border rounded"
      >
        <option value="">Select project</option>
        {projectOptions.map((p) => (
          <option key={p} value={p}>
            {p}
          </option>
        ))}
      </select>

      {selectedProject && (
        <select
          value={selectedDevice}
          onChange={(e) => onDeviceChange(e.target.value)}
          className="p-2 border rounded"
        >
          <option value="">Select device</option>
          {deviceOptions.map((d) => (
            <option key={d} value={d}>
              {d}
            </option>
          ))}
        </select>
      )}
    </div>
  );
}
