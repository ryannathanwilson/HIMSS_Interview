import React, { useEffect} from "react";
import SpamCard from "./components/SpamCard";

function App() {

  const getReports = async () => {
    let response = await fetch("http://127.0.0.1:8000/api/reports/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    //   body: JSON.stringify({
    //     refresh: localStorage.getItem("refresh"),
    //   }),
    });
    let data = await response.json();
    if (response.status === 200) {
      console.log(data);
    } else {
      console.log("failed to refresh");
    }
  };

  useEffect(() => {
    getReports();
  }, []); // empty dependency array just runs once!

  return (
    <div className="RNW REACT">
      <h1>BUDGET</h1>
	  <SpamCard />
	  <SpamCard />
	  <SpamCard />
	  <SpamCard />
    </div>
  );
}

export default App;
