import { FormEvent, FunctionComponent } from "react";
import { TagPicker, Button, FlexboxGrid, Divider } from "rsuite";
import { Filter } from "../types";

interface ProblemFilterProps {
  handleSearch: (e: FormEvent, updatedFilter: Filter) => void;
}

const difficulty = ["easy", "medium", "hard"].map((item) => ({
  label: item,
  value: item,
}));
const tags = ["maths", "greedy", "implementation", "graph", "dfs"].map(
  (item) => ({ label: item, value: item })
);

const ProblemFilter: FunctionComponent<ProblemFilterProps> = ({
  handleSearch,
}) => {
  return (
    <FlexboxGrid justify="center">
      <FlexboxGrid.Item>
        <TagPicker
          data={difficulty}
          style={{ width: 300 }}
          placeholder="Difficulty"
        />
        <Divider vertical />
      </FlexboxGrid.Item>
      <FlexboxGrid.Item>
        <TagPicker data={tags} style={{ width: 300 }} placeholder="Tags" />
        <Divider vertical />
      </FlexboxGrid.Item>
      <FlexboxGrid.Item>
        <Button
          onClick={(e) => {
            handleSearch(e, {
              difficulty: ["Med"],
              tags: ["DFS"],
            });
          }}
        >
          submit
        </Button>
      </FlexboxGrid.Item>
    </FlexboxGrid>
  );
};

export default ProblemFilter;
