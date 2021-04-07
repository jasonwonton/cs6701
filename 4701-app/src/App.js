import logo from './logo.svg';
import './App.css';
import {
  BrowserRouter as Router,
  Route,
} from "react-router-dom";
import Home from './contents/Home';
import CornellTopic1 from './contents/CornellTopic1'
import CornellTopic2 from './contents/CornellTopic2'
import CornellTopic3 from './contents/CornellTopic3'
import CornellTopic4 from './contents/CornellTopic4'
import CornellTopic5 from './contents/CornellTopic5'
import BuildTopic1 from './contents/BuildTopic1'
import BuildTopic2 from './contents/BuildTopic2'
import BuildTopic3 from './contents/BuildTopic3'
import BuildTopic4 from './contents/BuildTopic4'
import BuildTopic5 from './contents/BuildTopic5'
import WorldTopic1 from './contents/WorldTopic1'
import WorldTopic2 from './contents/WorldTopic2'
import WorldTopic3  from './contents/WorldTopic3'
import WorldTopic4 from './contents/WorldTopic4'
import WorldTopic5 from './contents/WorldTopic5'

function App() {
  return (
    <Router>
      <div className="App">
      <Route exact path="/">
      <Home />
      </Route>
      <Route path="/cornelltopic1">
      <CornellTopic1 />
      </Route>
      <Route path="/cornelltopic2">
      <CornellTopic2/>
      </Route>
      <Route path="/cornelltopic3">
      <CornellTopic3/>
      </Route>
      <Route path="/cornelltopic4">
      <CornellTopic4/>
      </Route>
      <Route path="/cornelltopic5">
      <CornellTopic5/>
      </Route>
      <Route path="/buildtopic1">
      <BuildTopic1/>
      </Route>
      <Route path="/buildtopic2">
      <BuildTopic2 />
      </Route>
      <Route path="/buildtopic3">
      <BuildTopic3 />
      </Route>
      <Route path="/buildtopic4">
      <BuildTopic4 />
      </Route>
      <Route path="/buildtopic5">
      <BuildTopic5 />
      </Route>
      <Route path="/worldtopic1">
      <WorldTopic1 />
      </Route>
      <Route path="/worldtopic2">
      <WorldTopic2 />
      </Route>
      <Route path="/worldtopic3">
      <WorldTopic3 />
      </Route>
      <Route path="/worldtopic4">
      <WorldTopic4/>
      </Route>
      <Route path="/worldtopic5">
      <WorldTopic5/>
      </Route>
      </div>
    </Router>

  );
}

export default App;
