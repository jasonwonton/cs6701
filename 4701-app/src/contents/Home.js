import React, { Component } from 'react';
import CornellTopics from '../components/CornellTopics'
import BuildAPCSalesTopics from '../components/BuildAPCSalesTopics'
import WorldNewsTopics from '../components/WorldNewsTopics'


class Home extends Component {
  render() {
      return (
          <div className="condiv home">
            <h1 className="name">Trending Subreddit Topics</h1>
            <div className='rowC'>
              <CornellTopics/>
              <BuildAPCSalesTopics/>
              <WorldNewsTopics/>
            </div>
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
  
  export default Home