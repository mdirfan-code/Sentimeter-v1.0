import logo from "./logo.svg";
import "./App.css";
import { SearchBarPage } from "./Components/Search";
import { useState } from "react";
import Charts from "./Components/Charts";
function App() {
  const [search, setSearch] = useState("");
  const [submitSearch, setSubmitSearch] = useState("");
  const handleSearchChange = (changedValue) => {
    console.log(changedValue);
    setSearch(changedValue);
  };
  const onSearch = () => {
    setSubmitSearch(search);
  };

  return (
    <div className="App">
      {submitSearch === "" ? (
        <SearchBarPage
          search={search}
          handleSearchChange={handleSearchChange}
          onSearch={onSearch}
        />
      ) : (
        <Charts search={submitSearch} />
      )}
    </div>
  );
}

export default App;
