import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import JobBoard from './Component/JobBoard.js';
import JobOpportunity from './Component/JobOpportunity.js'
import './App.css';


export default class App extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <BrowserRouter>
        <Route exact={true} path='/' component={JobBoard}></Route>
        <Route path='/jobs/:boardname/:boardId' component={JobOpportunity}></Route>
      </BrowserRouter>
    )
  }
}
