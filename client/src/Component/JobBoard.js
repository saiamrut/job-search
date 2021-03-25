import React from 'react';
import 'antd/dist/antd.css';
import { Card, Col, Row, Avatar } from 'antd';
import { Link } from 'react-router-dom';


export default class JobBoard extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      jobBoards: []
    }
    this.displayCards = this.displayCards.bind(this)
  }
  componentDidMount() {
    fetch('/jobboards').then((response) => response.json()).then(boards => this.setState({ jobBoards: boards }))
  }
  displayCards() {
    if (this.state.jobBoards.length > 0) {
      return (
        <Row type={"flex"} align={"middle"} justify={"space-around"}>
          {this.state.jobBoards.map(board =>
            <Col xs={8} key={board.id} span={8}>
              <Card
                title={
                  <Link
                    to={`jobs/${board.name}/${board.id}`}
                    params={{ jobSource: board.name }}>
                    {board.name}
                  </Link>}
                extra={board.rating}>
                <Card.Meta
                  avatar={<Avatar src={board.logo_file} />}
                  description={board.description}
                />
              </Card>
            </Col>)}
        </Row>
      )
    }
  }
  render() {
    return (
      <div>{this.displayCards()}</div>
    )
  }
}
