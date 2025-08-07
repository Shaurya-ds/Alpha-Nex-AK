from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SelectField, IntegerField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, NumberRange, Optional, Email, EqualTo
from models import User

class SignupForm(FlaskForm):
    """User registration form with validation"""
    name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', 
                                   validators=[DataRequired(), EqualTo('password', message='Passwords must match')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

class LoginForm(FlaskForm):
    """User authentication form"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class UploadForm(FlaskForm):
    file = FileField('File', validators=[FileRequired()])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=10, max=1000)])
    category = SelectField('Category', validators=[DataRequired()], choices=[
        ('audio', 'Audio'), 
        ('document', 'Document/PDF'),
        ('code', 'Code'),
        ('text', 'Text'),
        ('image', 'Image'),
        ('archive', 'Archive')
    ])
    ai_consent = BooleanField(
        'I agree that this content belongs to me, does not violate any rules, and can be used by AI companies for training',
        validators=[DataRequired()]
    )

class ReviewForm(FlaskForm):
    rating = SelectField('Rating', validators=[DataRequired()], choices=[
        ('good', 'Good - High quality content'),
        ('bad', 'Bad - Poor quality or inappropriate')
    ])
    description = TextAreaField('Review Description', 
                              validators=[DataRequired(), Length(min=20, max=500)],
                              render_kw={"placeholder": "Explain your rating in detail..."})

class WithdrawalForm(FlaskForm):
    amount_xp = IntegerField('XP Amount', validators=[DataRequired()])
    payment_method = SelectField('Payment Method', validators=[DataRequired()], choices=[
        ('paypal', 'PayPal'),
        ('bank', 'Bank Transfer'),
        ('crypto', 'Cryptocurrency')
    ])
    payment_details = TextAreaField('Payment Details', validators=[DataRequired()])

class RatingForm(FlaskForm):
    rating = IntegerField('Rating', validators=[DataRequired(), NumberRange(min=1, max=5)])
    category = SelectField('Category', choices=[
        ('general', 'General Feedback'),
        ('upload', 'Upload System'),
        ('review', 'Review System'),
        ('interface', 'User Interface'),
        ('performance', 'Performance'),
        ('bug', 'Bug Report'),
        ('feature', 'Feature Request')
    ], validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=10, max=500)])
    contact_email = StringField('Contact Email (Optional)', validators=[Optional()])
    submit = SubmitField('Submit Rating')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class SignupForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Create Account')