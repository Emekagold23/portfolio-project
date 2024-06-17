from flask import Blueprint, render_template
from forms import LocationForm

geolocation_bp = Blueprint('geolocation', __name__)

@geolocation_bp.route('/geolocation', methods=['GET', 'POST'])
def geolocation():
    form = LocationForm()
    if form.validate_on_submit():
        pass
    return render_template('geolocation.html', form=form)
