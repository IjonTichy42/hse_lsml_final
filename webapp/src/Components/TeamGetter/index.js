import React from 'react';
import TeamForm from "../TeamForm";
import "./index.css";

function TeamGetter() {
    return (
        <div className="team-getter">
            <h1>Enter news!</h1>
            <TeamForm />
        </div>
    );
}

export default TeamGetter;
