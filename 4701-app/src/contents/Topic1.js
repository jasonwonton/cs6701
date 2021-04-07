import React, { Component } from 'react';
import topics from '../cornell_data.json';
import {
  BrowserRouter as Router,
  Route,
  Link
} from "react-router-dom";

class CornellTopic1 extends Component{
  render(){
    return(
      <div class="condiv">
        <h3><Link to="/">home</Link></h3>
        <h1 className="name">{topics[0].topic} Posts</h1>
        <div className='posts'>
        {/* change this to be able to support topic array of any size by iterating through array .. ? */}
          <h3 className="subheading"><a target="_blank" href={topics[0].posts[0][1]}>{topics[0].posts[0][0]}</a></h3>
          <h3 className="subheading"><a target="_blank" href={topics[0].posts[1][1]}>{topics[0].posts[1][0]}</a></h3>
          {/* <h3 className="subheading"><a target="_blank" href={topics[0].posts[2][1]}>{topics[0].posts[2][0]}</a></h3>
          <h3 className="subheading"><a target="_blank" href={topics[0].posts[3][1]}>{topics[0].posts[3][0]}</a></h3>
              */}
        </div>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
      </div>
    )
  }
}

export default CornellTopic1;