import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Link
} from "react-router-dom";
import topics from '../worldnews_data.json';

class WorldNewsTopics extends Component{
  render(){
    return(
      <div class="container">
        <h2 className="subheading">r/worldnews (BERT + TF-IDF)</h2>
        <br></br>
        <div class="topics">
          <h3><Link to="/worldtopic1">{topics[0].topic}</Link></h3>
          <h3><Link to="/worldtopic2">{topics[1].topic}</Link></h3>
          <h3><Link to="/worldtopic3">{topics[2].topic}</Link></h3>
          <h3><Link to="/worldtopic4">{topics[3].topic}</Link></h3>
          <h3><Link to="/worldtopic5">{topics[4].topic}</Link></h3>
        </div>
      </div>
    )
  }
}

export default WorldNewsTopics;