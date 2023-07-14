import { FunctionComponent } from "react";
import { Navbar, Nav, FlexboxGrid } from "rsuite";
import { Updater } from "use-immer";
interface MenuProps {
  activeKey: string | null;
  onSelect: Updater<string | null>;
}

const Menu: FunctionComponent<MenuProps> = function ({ activeKey, onSelect }) {
  return (
    <Navbar appearance="inverse">
      <Navbar.Brand href="/">
        <FlexboxGrid justify="center">OnlineJudge</FlexboxGrid>
      </Navbar.Brand>
      <Nav onSelect={onSelect} activeKey={activeKey}>
        <Nav.Item eventKey="1" href="/">
          All Problems
        </Nav.Item>
        <Nav.Item eventKey="2">Help</Nav.Item>
      </Nav>
      <Nav pullRight>
        <Nav.Item eventKey="3" href="/users/signup">
          Signup
        </Nav.Item>
        <Nav.Item eventKey="4" href="/users/login">
          Login
        </Nav.Item>
      </Nav>
    </Navbar>
  );
};
export default Menu;
