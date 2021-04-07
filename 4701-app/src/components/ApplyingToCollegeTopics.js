import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Link
} from "react-router-dom";
import topics from '../data.json';

class BuildAPCSalesTopics extends Component{
  render(){
    return(
      <div class="container">
        <h2 className="subheading">r/buildapcsales</h2>
        <br></br>
        <div class="topics">
          <h3><Link to="/topic1">{topics[1][0].topic}</Link></h3>
          <h3><Link to="/topic1">{topics[1][1].topic}</Link></h3>
          <h3><Link to="/topic1">{topics[1][2].topic}</Link></h3>
          <h3><Link to="/topic1">{topics[1][3].topic}</Link></h3>
          <h3><Link to="/topic1">{topics[1][4].topic}</Link></h3>
        </div>
      </div>
    )
  }
}

export default BuildAPCSalesTopics;