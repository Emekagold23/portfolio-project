from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, SelectField, HiddenField, DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import User, Job
from flask_login import current_user

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', choices=[('client', 'Client'), ('worker', 'Worker')], validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class JobForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=3, max=50)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=10)])
    location = StringField('Location', validators=[DataRequired(), Length(min=3, max=100)])
    budget = IntegerField('Budget', validators=[DataRequired()])
    submit = SubmitField('Post Job')

class ReviewForm(FlaskForm):
    rating = SelectField('Rating', choices=[
        (1, '⭐'), 
        (2, '⭐⭐'), 
        (3, '⭐⭐⭐'), 
        (4, '⭐⭐⭐⭐'), 
        (5, '⭐⭐⭐⭐⭐')
    ], validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Submit Review')

class BookingForm(FlaskForm):
    client_id = HiddenField('Client ID', validators=[DataRequired()])
    worker_id = HiddenField('Worker ID', validators=[DataRequired()])
    job_id = HiddenField('Job ID', validators=[DataRequired()])
    start_time = DateTimeField('Start Time', validators=[DataRequired()])
    end_time = DateTimeField('End Time', validators=[DataRequired()])
    submit = SubmitField('Book')

class ContactForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired(), Length(min=3, max=100)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Send Message')

# Admin management forms
class AdminUserForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=8)])
    role = SelectField('Role', choices=[('client', 'Client'), ('worker', 'Worker'), ('admin', 'Admin')], validators=[DataRequired()])
    submit = SubmitField('Save')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class AdminJobForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=3, max=50)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=10)])
    location = StringField('Location', validators=[DataRequired(), Length(min=3, max=100)])
    budget = IntegerField('Budget', validators=[DataRequired()])
    status = SelectField('Status', choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], validators=[DataRequired()])
    submit = SubmitField('Save')

class ReportForm(FlaskForm):
    report_type = SelectField('Report Type', choices=[('job', 'Job'), ('user', 'User')], validators=[DataRequired()])
    reported_id = HiddenField('Reported ID', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Submit Report')

class SearchForm(FlaskForm):
    search_query = StringField('Search', validators=[DataRequired(), Length(min=3)])
    submit = SubmitField('Search')
