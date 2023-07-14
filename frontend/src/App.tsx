import { RouterProvider, createBrowserRouter } from "react-router-dom";
import Problems from "./routes/problems";
import ErrorPage from "./error-page";
import Login from "./routes/login";
import { useImmer } from "use-immer";
import Menu from "./components/menu";
import Singup from "./routes/singup";
import { Container, Content, Footer, Header, Stack } from "rsuite";
import StackItem from "rsuite/esm/Stack/StackItem";
const router = createBrowserRouter([
  {
    path: "/",
    element: <Problems />,
    errorElement: <ErrorPage />,
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
    <Container>
      <Header>
        <Menu activeKey={activeKey} onSelect={setActiveKey} />{" "}
      </Header>
      <Content>
        <RouterProvider router={router} />
      </Content>
    </Container>
  );
}
