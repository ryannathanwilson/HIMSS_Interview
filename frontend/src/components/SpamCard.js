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
            <div className={`${styles.column} ${styles.column_content}`}>
                <div><strong>Id: </strong>{props.reportId}</div>
                <div><strong>State: </strong><span className={props.state === 'OPEN' ? styles.open_text : styles.blocked_text}>{props.state}</span></div>
                <div className={styles.details}>Details</div>
            </div>
            <div className={`${styles.column} ${styles.column_content}`}>
                <div><strong>Type: </strong>{props.type}</div>
                <div><strong>Message: </strong>{props.message}</div>
            </div>
            <div className={`${styles.column} ${styles.column_buttons}`}>
                <button className={styles.button} role="button" onClick={() => handleBlocking(props.referenceId)}>Block</button>
                <button className={styles.button} role="button" onClick={() => handleResolving(props.reportId)}>Resolve</button>
            </div>
        </div>
    );
};

export default SpamCard;
