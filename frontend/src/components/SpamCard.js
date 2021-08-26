import React from "react";
import styles from "./SpamCard.module.scss"
const SpamCard = (props) => {

	const handleBlocking = async (id) => {
		let reponse = await fetch(`http://127.0.0.1:8000/api/references/${id}/`, {
			method: "PUT",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({
				status:"BLOCKED",
			}),
		});
		let data = await reponse.json();
		props.getReports()
	}
	

	const handleResolving = async (id) => {
		let reponse = await fetch(`http://127.0.0.1:8000/api/reports/${id}/`, {
			method: "PUT",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({
				ticketState:"CLOSED",
			}),
		});
		let data = await reponse.json();
		props.getReports()
	}
	
    return (
        <div className={styles.card}>
            <div className={styles.column}>
                <div className="report-id">Id: {props.reportId}</div>
                <div className="state">State: {props.state}</div>
                <div className={styles.details}>Details</div>
            </div>
            <div className={styles.column}>
                <div className="type">Type: {props.type}</div>
                <div className="message">Message: {props.message}</div>
            </div>
            <div className={styles.column}>
                <div className={styles.button} role="button" onClick={() => handleBlocking(props.referenceId)}>Block</div>
                <div className={styles.button} role="button" onClick={() => handleResolving(props.reportId)}>Resolve</div>
            </div>
        </div>
    );
};

export default SpamCard;
