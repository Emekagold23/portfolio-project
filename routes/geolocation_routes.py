from flask import Blueprint, render_template
from forms import LocationForm

geolocation_routes = Blueprint('geolocation_routes', __name__)

@geolocation_routes.route('/geolocation', methods=['GET'])
def geolocation_page():
    form = LocationForm()
    return render_template('geolocation.html', form=form)
