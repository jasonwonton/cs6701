import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Link
} from "react-router-dom";
import topics from '../buildapcsales_data.json';

class BuildAPCSalesTopics extends Component{
  render(){
    return(
      <div class="container">
        <h2 className="subheading">r/buildapcsales (BERT+TF-IDF)</h2>
        <br></br>
        <div class="topics">
          <h3><Link to="/buildtopic1">{topics[0].topic}</Link></h3>
          <h3><Link to="/buildtopic2">{topics[1].topic}</Link></h3>
          <h3><Link to="/buildtopic3">{topics[2].topic}</Link></h3>
          <h3><Link to="/buildtopic4">{topics[3].topic}</Link></h3>
        </div>
      </div>
    )
  }
}

export default BuildAPCSalesTopics;
