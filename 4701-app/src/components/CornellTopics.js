import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Link
} from "react-router-dom";
import topics from '../cornell_data.json';

class CornellTopics extends Component{
  render(){
    return(
      <div class="container">
        <h2 className="subheading">r/cornell (TF-IDF)</h2>
        <br></br>
        <div class="topics">
          <h3><Link to="/cornelltopic1">{topics[0].topic}</Link></h3>
          <h3><Link to="/cornelltopic2">{topics[1].topic}</Link></h3>
          <h3><Link to="/cornelltopic3">{topics[2].topic}</Link></h3>
          <h3><Link to="/cornelltopic4">{topics[3].topic}</Link></h3>
          <h3><Link to="/cornelltopic5">{topics[4].topic}</Link></h3>
        </div>
      </div>
    )
  }
}

export default CornellTopics;