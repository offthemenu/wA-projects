import { useState } from 'react';
import api from '../services/api';

interface CommentFormProps {
  context: {
    project: string;
    device: string;
    pageName: string;
    pagePath: string;
    filename: string;
  };
  onSuccess?: () => void;
}

export default function CommentForm({ context, onSuccess }: CommentFormProps) {
  const { project, device, pageName, pagePath, filename } = context;
  const [uiComponent, setUiComponent] = useState('');
  const [text, setText] = useState('');

  const submit = async () => {
    console.log("👋 submit called", { project, device, pageName, pagePath, uiComponent, text, filename });
    if (!text.trim()) return;
    try {
      await api.post('/add_comment', {
        project,
        device,
        page_name: pageName,
        page_path: pagePath,       
        ui_component: uiComponent,
        comment: text,
        filename,
      });
      setText('');
      setUiComponent('');
      onSuccess?.();
    } catch (err) {
      console.error("Failed to submit comment", err);
    }
  };

  return (
    <div className="border bg-white p-4 mt-6 space-y-4">
      <input
        type="text"
        value={uiComponent}
        onChange={(e) => setUiComponent(e.target.value)}
        placeholder="UI component (e.g. BUTTON, TEXT)"
        className="w-full p-2 border rounded"
      />

      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Add technical review comment for this component"
        className="w-full p-2 border rounded"
      />

      <button
        onClick={submit}
        className="mt-2 bg-blue-600 text-white px-4 py-2 rounded disabled:opacity-50"
        disabled={!text.trim() || !uiComponent.trim()}
      >
        Submit Comment
      </button>
    </div>
  );
}
