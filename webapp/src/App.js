import React from 'react';
import {
  RecoilRoot,
} from 'recoil';
import TeamGetter from "./Components/TeamGetter";

function App() {
  return (
      <RecoilRoot>
        <TeamGetter />
      </RecoilRoot>
  );
}

export default App;
