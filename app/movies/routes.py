# within your blueprint's routes file - the first step is to instantiate the blueprint and make sure that the blueprint is registered and can communicate with the larger app
# imports
from flask import Blueprint, render_template

# create the instance of our blueprint
movies = Blueprint('movies',  __name__, template_folder='movies_templates')

# when we're using blueprints - our routing decorator syntax is slightly changed
# @<blueprint_name>.route('/<url_endpoint>', [methods=<'GET''POST''PUT'>])
# def <routefuncname>():


# from here its like our other routes.py file - just creating routes for our movies blueprint
@movies.route('/actoroftheday')
def actoroftheday():
    movie_of_the_day='Pirates of the Caribbean: The Curse of the Black Pearl'
    actor_of_the_day=['Orlando Bloom', 'Geoffrey Rush', 'Kiera Knightley', 'Johnny Depp']
    return render_template('actoroftheday.html', actors=actor_of_the_day, movie=movie_of_the_day)