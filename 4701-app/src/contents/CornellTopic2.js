import React, { Component } from 'react';
import topics from '../cornell_data.json';
import {
  BrowserRouter as Router,
  Route,
  Link
} from "react-router-dom";

function PostList(props) {
  const posts = props.posts;
  const listItems = posts.map((post) =>
    <h3 key={post.toString()}><a target="_blank" href={post[1]}>{post[0]}</a></h3>
  );
  return (
    <h4>{listItems}</h4>
  );
}

class CornellTopic2 extends Component{
  render(){
    return(
      <div class="condiv">
        <h3><Link to="/">home</Link></h3>
        <h1 className="name">Posts for {topics[1].topic}</h1>
        <br></br>
        <div className='posts'>
        <PostList posts={topics[1].posts} />
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

export default CornellTopic2;