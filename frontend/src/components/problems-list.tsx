import { FunctionComponent } from "react";
import { problem } from "../types";
import { Table } from "rsuite";
const { Column, HeaderCell, Cell } = Table;

interface ProblemsListProps {
  problemList: Array<problem>;
}

const ProblemsList: FunctionComponent<ProblemsListProps> = ({
  problemList,
}) => {
  return (
    <Table
      data={problemList}
      onRowClick={(rowData) => {
        console.log(rowData);
      }}
      height={600}
    >
      <Column flexGrow={2}>
        <HeaderCell>Problem Name</HeaderCell>
        <Cell dataKey="name" />
      </Column>

      <Column flexGrow={2}>
        <HeaderCell>Tags</HeaderCell>
        <Cell dataKey="tags" />
      </Column>

      <Column flexGrow={1}>
        <HeaderCell>Difficulty</HeaderCell>
        <Cell dataKey="difficulty" />
      </Column>
    </Table>
  );
};

export default ProblemsList;
