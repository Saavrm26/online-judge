import { FunctionComponent } from "react";
import { Problem } from "../types";
import { Table } from "rsuite";
const { Column, HeaderCell, Cell } = Table;

interface ProblemsListProps {
  problemList: Array<Problem>;
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
    >
      <Column flexGrow={2}>
        <HeaderCell>Problem Name</HeaderCell>
        <Cell dataKey="problemName" />
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
