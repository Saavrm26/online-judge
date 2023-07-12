import React from "react";
import ReactDOM from "react-dom/client";
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import Problems from "./routes/problems";
import ErrorPage from "./error-page";
import "./styles/dark-mode.less";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Problems />,
    errorElement: <ErrorPage />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
