import axios from "axios";
import { useEffect, useState } from "react";
import { problem } from "../types";
import { useParams } from "react-router-dom";
import {
  Button,
  Col,
  Divider,
  Dropdown,
  FlexboxGrid,
  Grid,
  Panel,
  Row,
  Stack,
  Tag,
  TagGroup,
} from "rsuite";
import StackItem from "rsuite/esm/Stack/StackItem";

export default function Problem() {
  const [problemDetails, setProblemDetails] = useState<problem | null>(null);
  const { problemId } = useParams() as {
    problemId: string;
    [key: string]: unknown;
  };
  useEffect(() => {
    const url = `http://localhost:8000/api/problem/${problemId}`;
    console.log(url);
    axios
      .get<problem>(url)
      .then((res) => {
        console.log(res.data);
        setProblemDetails(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  if (!problemDetails) return <></>;
  const tags = (
    <TagGroup>
      {problemDetails.tags.map((tag, i) => (
        <Tag key={i}>{tag}</Tag>
      ))}
    </TagGroup>
  );
  return (
    <Grid fluid>
      <Row>
        <FlexboxGrid justify="center">
          <h2>{problemDetails?.name}</h2>
        </FlexboxGrid>
      </Row>
      <div style={{ margin: "4em" }}></div>
      <Row>
        <Col mdOffset={1} md={19}>
          <p style={{fontSize:'17.0px'}}>{problemDetails?.statement}</p>
        </Col>
        <Col md={4}>
          <Stack
            direction="column"
            alignItems="center"
            justifyContent="center"
            style={{ height: "50vh" }}
          >
            <StackItem alignSelf="flex-start">
              <Panel header="Tags">{tags}</Panel>
            </StackItem>
            <StackItem alignSelf="flex-start">
              <Panel header="Select Language">
                <Dropdown title="Language" style={{ marginBottom: "0.2em" }}>
                  {/* use on select to set value */}
                  <Dropdown.Item>C++ 17</Dropdown.Item>
                  <Dropdown.Item>Java 18</Dropdown.Item>
                  <Dropdown.Item>Python 3.10</Dropdown.Item>
                </Dropdown>
                <br />
                <Button>Select File</Button>
              </Panel>
            </StackItem>
            <Divider />
            <StackItem>
              <Button appearance="primary">Submit</Button>
            </StackItem>
          </Stack>
        </Col>
      </Row>
    </Grid>
  );
}
