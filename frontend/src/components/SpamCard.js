import React from "react";
import styles from "./SpamCard.module.scss"
const SpamCard = (props) => {
    return (
        <div className={styles.card}>
            <div className="column">
                <div className="report-id">id: l;aksdjfl</div>
                <div className="state">state: l;aksdjfl</div>
                <div className="details">details</div>
            </div>
            <div className="column">
                <div className="type">Type: Spam</div>
                <div className="message">Message: l;kasdjf;jalks</div>
            </div>
            <div className="column">
                <div class="button" role="button">Block</div>
                <div class="button" role="button">Resolve</div>
            </div>
        </div>
    );
};

export default SpamCard;
