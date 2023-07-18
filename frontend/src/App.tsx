import { RouterProvider, createBrowserRouter } from "react-router-dom";
import Problems from "./routes/problems";
import ErrorPage from "./error-page";
import Login from "./routes/login";
import { useImmer } from "use-immer";
import Menu from "./components/menu";
import Singup from "./routes/singup";
import { Footer, Header } from "rsuite";
import Problem from "./routes/problem";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Problems />,
    errorElement: <ErrorPage />,
  },
  {
    path: '/:problemId',
    element: <Problem />

  },
  {
    path: "/users/login",
    element: <Login />,
  },
  {
    path: "/users/signup",
    element: <Singup />,
  },
]);

export default function App() {
  const [activeKey, setActiveKey] = useImmer<string | null>(null);
  return (
    <>
      <Header>
        <Menu activeKey={activeKey} onSelect={setActiveKey} />{" "}
      </Header>
      <RouterProvider router={router} />
      <Footer></Footer>
    </>
  );
}
