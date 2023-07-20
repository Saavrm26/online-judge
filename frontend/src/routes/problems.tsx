import { FormEvent, useEffect } from "react";
import { useImmer } from "use-immer";
import ProblemFilter from "../components/problem-filter";
import { Filter, problem } from "../types";
import ProblemsList from "../components/problems-list";
import { Panel } from "rsuite";
import axios from "axios";

export default function Problems() {
  const [filter, setFilter] = useImmer<Filter>({
    difficulty: [],
    tags: [],
  });

  const [problemList, setProblemList] = useImmer<Array<problem>>([]);

  useEffect(() => {
    // fetch problem list using api, using an example util backend has been developed, localhost 8000 is only being used for development
    // TODO: Add row click
    const url = "http://localhost:8000/api/problem";
    axios
      .get<Array<problem>>(url)
      .then((res) => {
        console.log(res.data);
        setProblemList(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, [filter, setProblemList]);

  function handleSearch(e: FormEvent, updatedFilter: Filter) {
    e.preventDefault();
    setFilter(updatedFilter);
  }

  return (
    <>
      <Panel header="Search Problems" shaded>
        <ProblemFilter handleSearch={handleSearch}></ProblemFilter>
      </Panel>
      <Panel header="Problems" bodyFill={true}>
        <ProblemsList problemList={problemList}></ProblemsList>
      </Panel>
    </>
  );
}
