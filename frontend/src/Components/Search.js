export function SearchBarPage({ search, handleSearchChange, onSearch }) {
  const handleKeyPress = (event) => {
    if (event.key === "Enter") {
      onSearch();
    }
  };
  return (
    <div className="search-container">
      <div className="container">
        <input
          type="text"
          placeholder="Search..."
          value={search}
          onChange={(e) => handleSearchChange(e.target.value)}
          onKeyPress={(e) => handleKeyPress(e)}
        />
        <div className="search"></div>
      </div>
    </div>
  );
}
