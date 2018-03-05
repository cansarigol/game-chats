import React from 'react'
import ReactDOM from 'react-dom'

class Container extends React.Component {
    render() {
        return (
            <h1> Welcome To Game Chats</h1>
            
        );
    }
}

ReactDOM.render(<Container />, document.getElementById('container_div'))