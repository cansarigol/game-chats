import React from "react"
import Radium from "radium"

function SignInOrUp(){
    if(window.django.user.is_authenticated == "true"){
        return <ul className="nav navbar-nav ml-auto">
                <li className="nav-item"> <a className="nav-link" href="/user-manage/">{window.django.user.username}</a></li>
               </ul>;
    }
    return <ul className="nav navbar-nav ml-auto">
                <li class="nav-item"> 
                    <a className="nav-link" href="/login/">Login</a>
                </li> 
                <li class="nav-item">
                    <a className="btn btn-success btn-raised" href="/signup/">Sign Up</a>
                </li>
            </ul>;
}

const styles = {
    logoheader: {
        'border-radius': "50%",
        width: "50px",
        'margin-right': "5px"
    }
}
@Radium
export default class Header extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            logo: window.django.logo,
            q: "",
            api_key: window.django.api_key,
            api_url: window.django.api_url,
        };

        this.onSubmit = this.onSubmit.bind(this)
    }
    onSubmit(e){
        e.preventDefault();
        console.log(this.state.api_key);
        let q = document.getElementsByName("q")[0].value;
        let headers = new Headers();
        let options = {};
        headers.append("user-key", "application/json")
        headers.append("Accept", "application/json")
        options["headers"] = headers
        fetch(this.state.api_url+'/games/?search='+q+'&fields=id,name,slug,websites,rating,rating_count,cover,genres,summary,first_release_date&limit=20&order=popularity:desc',
        options)
        .then(res => res.json())
        .then(data => console.log(data))
        
    }
    render(){
        return(
            <header className="navbar navbar-expand-lg navbar-dark bg-primary">
                <div className="container">
                    <img style={[styles.logoheader]} src={this.state.logo} alt="Logo" />
                    <a className="navbar-brand" href="/">Game Chats</a>
                    <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarResponsive">
                    <ul className="navbar-nav">
                        <form className="form-inline my-2 my-lg-0" onSubmit={this.onSubmit}>
                            <input className="form-control mr-sm-4" name="q" type="search" placeholder="Search" aria-label="Search" />
                        </form>
                    </ul>
                        <SignInOrUp/>
                    </div>
                </div>
            </header>
        )
    }
}