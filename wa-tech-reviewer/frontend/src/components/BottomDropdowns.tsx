import { useEffect, useState } from "react";
import api from "../services/api";

type WireframeDropdownData = {
  projects: string[];
  devices_by_project: Record<string, string[]>;
  pages_by_project_device: Record<string, { name: string; path: string }[]>;
};

type BottomDropdownsProps = {
  selectedProject: string;
  selectedDevice: string;
  selectedPage: string;
  onPageChange: (pageName: string, pagePath: string) => void;
  data: WireframeDropdownData;
};

export function BottomDropdowns({
  selectedProject,
  selectedDevice,
  selectedPage,
  onPageChange,
  data,
}: BottomDropdownsProps) {
  const pageOptions =
    selectedProject && selectedDevice
      ? data.pages_by_project_device[`${selectedProject}_${selectedDevice}`] || []
      : [];

  return (
    <div className="flex flex-wrap gap-4">
      <select
        value={selectedPage}
        onChange={(e) => {
          const selName = e.target.value;
          const entry = pageOptions.find((x) => x.name === selName);
          onPageChange(selName, entry?.path ?? "");
        }}
        className="p-2 border rounded"
      >
        <option value="">Select page</option>
        {pageOptions.map((p) => (
          <option key={p.path} value={p.name}>
            {p.name}
          </option>
        ))}
      </select>

      <input
        type="text"
        placeholder="Write the name of the UI Component"
        className="p-2 border rounded w-full max-w-md"
        disabled
      />
    </div>
  );
}
