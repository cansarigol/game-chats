import React from 'react'
import ReactDOM from 'react-dom'

export default class GetFromApi extends React.Component{
    async loadData(url, headers){
        const response = await fetch(url, {
            method: 'get',
            headers: 'headers'
        });
        const data = response.json();
        this.setState(data);
    }
    onRefresh(){
        this.loadData()
    }
}