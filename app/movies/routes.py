# within your blueprint's routes file - the first step is to instantiate the blueprint and make sure that the blueprint is registered and can communicate with the larger app
# imports
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.forms import newActorForm

# database imports
from app.models import db, Actor

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


@movies.route('/addactor', methods=['GET', 'POST'])
def addactor():
    form = newActorForm()
    if request.method == 'POST':
        # do stuff with the form that the user has submitted
        # first, we need to check if the form validates
        
        if form.validate_on_submit():
            print('form validated') # any time you see a print in flask - it is just the developer giving themselves more information for debugging and/or writing code
        
            # create an instance of our actor object from form data
            newactor = Actor(first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            age=form.age.data,
                            nationality=form.nationality.data,
                            hiringprice=form.hiringprice.data,
                            bestrole=form.bestrole.data,
                            bestmovie=form.bestmovie.data)
            
            # put that instance of an actor into our database
            db.session.add(newactor)
            db.session.commit()

            flash('New actor added to our database.', category='alert-info')
            flash(f'{newactor.to_dict()}', category='alert-info')
        else:
            flash('You entered incomplete or incorrect data, please try again.', category='alert-danger')
        
        return redirect(url_for('movies.addactor'))
    # implied else when request.method == 'GET'
    # we just render the html file like normal
    return render_template('addactor.html', form=form)