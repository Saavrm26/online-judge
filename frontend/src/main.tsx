import React from "react";
import ReactDOM from "react-dom/client";
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import ProlemsList from "./routes/problem-list";
import ErrorPage from "./error-page";

const router = createBrowserRouter([
  {
    path: "/",
    element: <ProlemsList />,
    errorElement: <ErrorPage />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
