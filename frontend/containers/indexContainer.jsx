import React from "react"

import Header from "../components/headerComponent"

export default class IndexContainer extends React.Component {
  render() {
    return (
        <div className="body">
        <Header/>
      <div className="container">
        <div className="row">
          <div className="col-sm-12">
            <h1>Sample App!</h1>
          </div>
        </div>
      </div>
      </div>
    )
  }
}