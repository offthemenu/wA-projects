import { useEffect, useState } from 'react';
import api from '../services/api';

type Comment = {
  id: number;
  project: string;
  device: string;
  ui_component: string;
  comment: string;
  created_at: string;
  page_name: string;
  page_path: string;
};

export default function CommentList({ project, device }: { project: string; device: string }) {
  const [comments, setComments] = useState<Comment[]>([]);
  const [selectedIds, setSelectedIds] = useState<Set<number>>(new Set());

  useEffect(() => {
    if (!project || !device) return;

    api
      .get('/comments', { params: { project, device } })
      .then(res => {
      console.log("Comments fetched:", res.data); // confirm IDs are present
      setComments(res.data);
    })
      .catch(console.error);
  }, [project, device]);

  const toggle = (id: number) => {
    setSelectedIds(prev => {
      const next = new Set(prev);
      next.has(id) ? next.delete(id) : next.add(id);
      return next;
    });
  };

  const handleDelete = async () => {
    for (const id of selectedIds) {
      console.log(`Deleting comment with id: ${id}`); // verify ID
      await api.delete(`/comment/${id}`);
    }
    setComments(prev => prev.filter(c => !selectedIds.has(c.id)));
    setSelectedIds(new Set());
  };

  return (
    <div className="border bg-white p-4 mt-6">
      <h2 className="text-lg font-semibold mb-4">Comments</h2>
      <table className="w-full table-auto border-collapse">
        <thead>
          <tr className="bg-gray-100">
            <th />
            <th>Device</th>
            <th>Project</th>
            <th>Page Name</th>
            <th>Page Path</th>
            <th>UI Component</th>
            <th>Comment</th>
            <th>Created</th>
          </tr>
        </thead>
        <tbody>
          {comments.map(c => (
            <tr key={c.id}>
              <td>
                <input
                  type="checkbox"
                  checked={selectedIds.has(c.id)}
                  onChange={() => toggle(c.id)}
                />
              </td>
              <td>{c.device}</td>
              <td>{c.project}</td>
              <td>{c.page_name}</td>
              <td>{c.page_path}</td>
              <td>{c.ui_component}</td>
              <td>{c.comment}</td>
              <td>{new Date(c.created_at).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>

      {selectedIds.size > 0 && (
        <div className="mt-4 flex items-center">
          <span>{selectedIds.size} item(s) selected</span>
          <button
            onClick={handleDelete}
            className="ml-auto px-4 py-2 bg-red-600 text-white rounded"
          >
            DELETE
          </button>
        </div>
      )}
    </div>
  );
}
