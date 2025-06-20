## 🖥️ Frontend Setup (React + TailwindCSS + Vite)

This guide walks you through setting up the frontend on a fresh machine to the point where Tailwind is working with PostCSS and Vite.

---

### ⚙️ 1. Prerequisites

Ensure the following are installed:

- **Node.js** (v18+ recommended)
- **npm** (v9+)
- Optional: VS Code + Tailwind IntelliSense extension for syntax support

---

### 🚀 2. Project Bootstrapping

```bash
cd wa-tech-reviewer
npm create vite@latest frontend --template react
cd frontend
```
#### Choose:
* **Framework**: React
* **Variant**: Typescript

### 📦 3. Install Dependencies

Inside the `frontend/` directory:

```bash
cd frontend
npm install
```

If `node_modules` or `package-lock.json` don’t exist yet, this will install:

- React + React DOM
- Vite
- Tailwind CSS v4
- PostCSS + Autoprefixer
- TypeScript + ESLint support

---

### 🛠 4. PostCSS & Tailwind Setup

Ensure `postcss.config.js` contains:

```js
import tailwindcss from '@tailwindcss/postcss';
import autoprefixer from 'autoprefixer';

export default {
  plugins: [
    tailwindcss(),
    autoprefixer()
  ],
};
```

Check `tailwind.config.js` looks like:

```js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

---

### 💡 5. VS Code Configuration (Recommended)

Install the following extensions:

- Tailwind CSS IntelliSense
- ESLint (optional)

---

### 💻 6. Start the Dev Server

```bash
npm run dev
```

---

### 🏗️ 7. Building the Frontend App Structure

This section tracks how we’re progressively assembling the actual interface:

#### 🛠️ Environment Variable Setup

Add a `.env` file at the root level of the project (same level as `frontend/` and `backend/`):

```env
VITE_API_BASE_URL=http://localhost:8000/v01
```

#### 🔗 API Client

Create a reusable `api.ts` Axios client in `/src/services` to connect with the FastAPI backend using the environment base URL.

#### 📄 Page Structure

Create `ReviewPage.tsx` inside `/src/pages`. This serves as the main screen for wireframe reviews and pulls in all components.

#### 🧩 Component Scaffolding (all inside `/src/components`)

- **Dropdowns.tsx** – Fetches project/device/page info from `/wireframe`
- **PdfViewer.tsx** – (to be implemented) Renders paginated PDF view
- **CommentForm.tsx** – Input field and button to submit a comment
- **CommentList.tsx** – Renders the list of comments from `/comments`

#### ⚛️ App Integration

Refactor `App.tsx` to render `<ReviewPage />`, which assembles all core components in a vertical layout using Tailwind utility classes.