import React from 'react'
function GetImageUrl(url){
    if(url){
        return url;
    }
    return 'images/noimage.png';
}
class GameCard extends React.Component{
    render(){
        return(<div class="card margin-vertical-10">
        <div class="card-body ">
            <div class="row">
                <div class="col-md-2 col-sm-2 col-xs-12">
                    <img class="rounded float-left" src="{GetImageUrl(this.props.cover_url)}"
                     width=100 height=150 alt="{{ game.name }}">
                </div>
                <div class="col-md-10 col-sm-10 col-xs-12">
                    <h5 class="card-title text-left">{ this.props.name }</h5>
                    <small>{ this.props.first_release_date }</small>
                    <div class="row">
                        <div class="col-md-9 col-sm-9 col-xs-12">
                            <p>{ this.props.summary }</p>
                            <div>
                                {% for genre in game.genres_with_name %}
                                <span class="badge badge-success">{{ genre.name }}</span>
                                {% endfor %}
                            </div>
                            <div class="margin-top-10">
                                <small>More details at {% for website in game.websites %}
                                    {% if website.name %}
                                    <span>
                                        <a class="btn btn-xs btn-outline-secondary mini-link-button" href="{{ website.url }}" target="_blank">
                                            {{ website.name }}</a>
                                    </span>
                                        
                                    {% endif %}
                                    {% endfor %}
                                </small>
                            </div>
                        </div>
    
                        <div class="col-md-3 col-sm-3 col-xs-12">
                            <div>
                                <h1>
                                    <span class="badge badge-pill badge-primary">5.0</span>
                                </h1>
                            </div>
                            <hr>
                            <div>
                                {% if game.rating > 0 %}
                                <p>IGDB Rating</p>
                                <div class="progress" data-toggle="tooltip" data-placement="top" title="Count {{ game.rating_count }}">
                                    <div class="progress-bar progress-bar-striped bg-secondary" role="progressbar" style="width: {{ game.rating|floatformat }}%"
                                        aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">{{ game.rating|floatformat }}%</div>
    
                                </div>
                                {% endif %}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>);
    }
}