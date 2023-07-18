import { Col, FlexboxGrid, Panel } from "rsuite";
import { Form, ButtonToolbar, Button } from "rsuite";
import FlexboxGridItem from "rsuite/esm/FlexboxGrid/FlexboxGridItem";

export default function Login() {
  return (
    <>
      <FlexboxGrid justify="center">
        <FlexboxGridItem as={Col} colspan={12} md={6}>
          <Panel header={<h3>Login</h3>} bordered>
            <Form fluid>
              <Form.Group controlId="email">
                <Form.ControlLabel>Email</Form.ControlLabel>
                <Form.Control name="email" type="email" />
                <Form.HelpText tooltip>Email is required</Form.HelpText>
              </Form.Group>
              <Form.Group controlId="password">
                <Form.ControlLabel>Password</Form.ControlLabel>
                <Form.Control
                  name="password"
                  type="password"
                  autoComplete="off"
                />
              </Form.Group>
              <Form.Group>
                <ButtonToolbar>
                  <Button appearance="primary">Login</Button>
                </ButtonToolbar>
              </Form.Group>
            </Form>
          </Panel>
        </FlexboxGridItem>
      </FlexboxGrid>
    </>
  );
}
