import React from 'react';
import {
    atom,
    useRecoilState,
} from 'recoil';

import './index.css';

const textState = atom({
    key: 'textState', // unique ID (with respect to other atoms/selectors)
    default: '', // default value (aka initial value)
});

const teamState = atom({
    key: 'teamState', // unique ID (with respect to other atoms/selectors)
    default: '', // default value (aka initial value)
});

function TeamForm() {
    const [text, setText] = useRecoilState(textState);
    const [team, setTeam] = useRecoilState(teamState);

    const onSubmit = (event, text) => {
        event.preventDefault()
        fetch("http://127.0.0.1:8000/predict", {
            method: 'post',
            body: JSON.stringify({text: event.target[0].value})
        })
            .then(response => response.json())
            .then(data => setTeam(data.team));
    }

    const onChange = (event) => {
        setText(event.target.value);
    };

    return (
        <form className="team-form" onSubmit={onSubmit}>
            <div>
                <textarea className="team-form__textarea" name="text" onChange={(e) => onChange(e)} value={text} />
            </div>
            <div className="team-form__button-wrapper">
                <button className="team-form__button" type="submit">Get Team!</button>
            </div>
            <div className="team-form__result">
                Result: <span className="team-form__team-name">{team}</span>
            </div>
        </form>
    );
}

export default TeamForm;
