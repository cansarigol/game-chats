import React from 'react'
import ReactDOM from 'react-dom'

import IndexContainer from "./containers/indexContainer"

class Index extends React.Component {
    render() {
        return (
            <IndexContainer/>
            
        );
    }
}

ReactDOM.render(<Index />, document.getElementById('react-div'))