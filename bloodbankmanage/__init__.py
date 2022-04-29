
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY']='thisismybloodbank'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:''@localhost/v_bloodbank'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)

login_manager =LoginManager(app)
 

from bloodbankmanage import routes