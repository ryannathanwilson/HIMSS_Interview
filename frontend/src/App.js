import React, { useEffect, useState } from "react";
import Refill from "./components/Refill";
import SpamCard from "./components/SpamCard";

function App() {
    const [reports, setReports] = useState([]);

    const getReports = async () => {
        let response = await fetch("http://127.0.0.1:8000/api/reports_open/")
        let reports = await response.json();
        if (response.status === 200) {
			setReports(reports);
			console.log("reports collected");
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
            <Refill getReports={getReports} />
            {reports.map((report) => (
                <SpamCard
                    key={report.id}
                    reportId={report.id}
					referenceId={report.reference.referenceId}
                    state={report.reference.status}
                    type={report.payload.reportType}
                    message={report.payload.message}
                    getReports={getReports}
                />
            ))}
        </div>
    );
}

export default App;
