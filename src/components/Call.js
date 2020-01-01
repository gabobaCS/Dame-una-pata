import React, { Component } from 'react'
import Axios from 'axios'

export class Call extends Component {
    componentDidMount(){
        Axios.get('http://127.0.0.1:8000/api/mascotas')
        .then(res => {
            console.log(res)
        })
    }
    render() {
        return (
            <div>
                
            </div>
        )
    }
}

export default Call

