import { FormEvent, useEffect } from "react";
import { useImmer } from "use-immer";
import ProblemFilter from "../components/problem-filter";
import { Filter, Problem } from "../types";
import ProblemsList from "../components/problems-list";
import { Container, Content, Divider, Panel } from "rsuite";

export default function Problems() {
  const [filter, setFilter] = useImmer<Filter>({
    difficulty: [],
    tags: [],
  });

  const [problemList, setProblemList] = useImmer<Array<Problem>>([]);

  useEffect(() => {
    // fetch problem list using api, using an example util backend has been developed
    const response: Array<Problem> = [
      {
        problemName: "Two Sum",
        difficulty: "easy",
        tags: ["two pointer", " greedy"],
      },
      { problemName: "KnapSack", difficulty: "medium", tags: ["dp"] },
    ];
    setProblemList(response);
  }, [filter, setProblemList]);

  function handleSearch(e: FormEvent, updatedFilter: Filter) {
    e.preventDefault();
    setFilter(updatedFilter);
  }

  return (
    <Content>
      <Panel header="Search Problems" shaded>
        <ProblemFilter handleSearch={handleSearch}></ProblemFilter>
      </Panel>
      <Panel header="Problems">
        <ProblemsList problemList={problemList}></ProblemsList>
      </Panel>
    </Content>
  );
}
