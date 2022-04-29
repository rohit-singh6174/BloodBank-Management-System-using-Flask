from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField
from wtforms.validators import DataRequired,Length,EqualTo,Email

district=[('Ahmednaga','Ahmednaga'),
('Akola','Akola'),
('Aurangabad','Aurangabad'),
('Bhandara','Bhandara'),
('Buldhana','Buldhana'),
('Chandrapur','Chandrapur'),
('Mumbai City','Mumbai City'),
('Mumbai Suburban','Mumbai Suburban')
]  

bloodgroups=[('A+','A Positive'),
('A-','A Negative'),
('B+','B Positive'),
('B-','B Negative'),
('C+','C Positive'),
('C-','C Negative'),
('O+','O Positive'),
('O-','O Negative'),
('AB+','AB Positive'),
('AB-','AB Negative')
]         

bloodunit=[('350','350 ml'),
('450','450 ml'),
]         


class AdminRegForm(FlaskForm):
    name = StringField('name',validators=[DataRequired(),Length(min=3,max=20)])
    username = StringField('Username',validators=[DataRequired(),Length(min=3,max=20)])
    email= StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=6,max=20)])
    confirm_password= PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField(label='Sign Up')

class AdminLoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=3,max=20)])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=6,max=20)])
    submit=SubmitField(label='Sign Up')


class DonorRegForm(FlaskForm):
    name = StringField('name',validators=[DataRequired(),Length(min=3,max=20)])
    phone= StringField('name',validators=[DataRequired(),Length(min=10,max=10)])
    #phone = StringField('phone',Regexp('^[0-9]{10}$', message="Phone number must contains inputs between 0 to 9"))

    uhid = StringField('uhid',validators=[DataRequired(),Length(min=10,max=12)])
    bloodgroup=SelectField('bloodgroup',choices=bloodgroups)
    district=SelectField('district',choices=district)
    username = StringField('Username',validators=[DataRequired(),Length(min=3,max=20)])
    email= StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=6,max=20)])
    confirm_password= PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])

    submit=SubmitField(label='Sign Up')


class Donorlogin(FlaskForm):
     username = StringField('Username',validators=[DataRequired(),Length(min=3,max=20)])
     password=PasswordField('Password',validators=[DataRequired(),Length(min=6,max=20)])
     submit=SubmitField(label='Login')


class Updatedonor(FlaskForm):
     name = StringField('name',validators=[DataRequired(),Length(min=3,max=20)])
     phone= StringField('name',validators=[DataRequired(),Length(min=10,max=10)])
     uhid = StringField('uhid',validators=[DataRequired(),Length(min=10,max=12)])
     bloodgroup=StringField('bloodgroup',validators=[DataRequired()])
     district=SelectField('district',choices=district)
     username = StringField('Username',validators=[DataRequired(),Length(min=3,max=20)])
     email= StringField('Email',validators=[DataRequired(),Email()])
     submit=SubmitField(label='Update')

class Donateform(FlaskForm):
     name = StringField('name',validators=[DataRequired(),Length(min=3,max=20)])
     phone= StringField('phone',validators=[DataRequired(),Length(min=10,max=10)])
     username = StringField('Username',validators=[DataRequired(),Length(min=3,max=20)])
     email= StringField('Email',validators=[DataRequired(),Email()])
     bloodgroup=StringField('bloodgroup',validators=[DataRequired()])
     district=SelectField('district',choices=district)
     bloodunit=SelectField('bloodunit',choices=bloodunit)
     submit=SubmitField(label='Donate')

class  BloodReqForm(FlaskForm):
     name = StringField('name',validators=[DataRequired(),Length(min=3,max=20)])
     phone= StringField('phone',validators=[DataRequired(),Length(min=10,max=10)])
     username = StringField('Username',validators=[DataRequired(),Length(min=3,max=20)])
     email= StringField('Email',validators=[DataRequired(),Email()])
     bloodgroup=StringField('bloodgroup',validators=[DataRequired()])
     district=SelectField('district',choices=district)
     bloodunit=SelectField('bloodunit',choices=bloodunit)
     submit=SubmitField(label='Request')

