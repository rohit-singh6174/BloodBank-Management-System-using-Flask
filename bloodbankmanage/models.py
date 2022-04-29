from bloodbankmanage import db,login_manager #login_manager # it will look from _init_ file by default in that it will look for db variable if it there it will import   
from flask_login import UserMixin
from flask import url_for, redirect
from datetime import date


@login_manager.user_loader
def load_user(user_id):
    return Donor.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('donorregister'))



class Admin(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40),unique=False,nullable=False)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(40),unique=True,nullable=False)
    password=db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return f'\n name: {self.name},\n username: {self.username},\n email: {self.email},\npassword: {self.password}'

class Donor(db.Model,UserMixin):
    id =db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40),unique=False,nullable=False)
    phone=db.Column(db.BigInteger,unique=True,nullable=False)
    uhid=db.Column(db.BigInteger,unique=True,nullable=False)
    bloodgroup=db.Column(db.String(10),unique=False,nullable=False)
    district=db.Column(db.String(20),unique=False,nullable=False)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(40),unique=True,nullable=False)
    password=db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return f'\nname :{self.name},\nphone : {self.phone},\nuhid : {self.uhid},\nbloodgroup : {self.bloodgroup},\ndistrict : {self.district}, \nusername : {self.username},\nemail : {self.email},password : {self.password} '



class Bloodtest_Report(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40),unique=False,nullable=False)
    phone=db.Column(db.BigInteger,unique=True,nullable=False)
    uhid=db.Column(db.BigInteger,unique=True,nullable=False)
    bloodgroup=db.Column(db.String(10),unique=False,nullable=False)

    def __repr__(self):
        return f'\nsr_no : {self.sr_no}, \nname :{self.name},\nphone : {self.phone},\nuhid : {self.uhid},\nbloodgroup : {self.bloodgroup}'
   

class BloodDonate(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40),unique=False,nullable=False)
    phone=db.Column(db.BigInteger,unique=False,nullable=False)
    username=db.Column(db.String(20),unique=False,nullable=False)
    email=db.Column(db.String(40),unique=True,nullable=False)
    bloodgroup=db.Column(db.String(10),unique=False,nullable=False)
    district=db.Column(db.String(20),unique=False,nullable=False)
    bloodunit=db.Column(db.Integer,nullable=False)
    date=db.Column(db.Date)

    def __repr__(self):
        return f'\nname :{self.name},\nphone : {self.phone}, \nusername : {self.username},\nbloodgroup : {self.bloodgroup},\ndistrict : {self.district},\nemail : {self.email},bloodunit : {self.bloodunit},\ndate :{self.date} '


class Bloodbank(db.Model):
     id =db.Column(db.Integer,primary_key=True)
     bloodgroup=db.Column(db.String(10),unique=True,nullable=False)
     bloodquanity=db.Column(db.String(10),unique=False,nullable=False)

     def __repr__(self):
         return f'\id : {self.id},\nBlood Group : {self.bloodgroup} , \nBlood Unit : {self.bloodquanity}'

class BloodApproved(db.Model):
     id =db.Column(db.Integer,primary_key=True)
     name=db.Column(db.String(40),unique=False,nullable=False)
     phone=db.Column(db.BigInteger,unique=False,nullable=False)
     username=db.Column(db.String(20),unique=False,nullable=False)
     email=db.Column(db.String(40),unique=False,nullable=False)
     bloodgroup=db.Column(db.String(10),unique=False,nullable=False)
     district=db.Column(db.String(20),unique=False,nullable=False)
     bloodunit=db.Column(db.Integer,nullable=False)
     date=db.Column(db.Date)
     
     def __repr__(self):
        return f'\nname :{self.name},\nphone : {self.phone}, \nusername : {self.username},\nbloodgroup : {self.bloodgroup},\ndistrict : {self.district},\nemail : {self.email},bloodunit : {self.bloodunit},\ndate :{self.date} '


class Handover(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40),unique=False,nullable=False)
    phone=db.Column(db.BigInteger,unique=False,nullable=False)
    username=db.Column(db.String(20),unique=False,nullable=False)
    email=db.Column(db.String(40),unique=False,nullable=False)
    bloodgroup=db.Column(db.String(10),unique=False,nullable=False)
    district=db.Column(db.String(20),unique=False,nullable=False)
    bloodunit=db.Column(db.Integer,nullable=False)
    date=db.Column(db.Date)
     
    def __repr__(self):return f'\nname :{self.name},\nphone : {self.phone}, \nusername : {self.username},\nbloodgroup : {self.bloodgroup},\ndistrict : {self.district},\nemail : {self.email},bloodunit : {self.bloodunit},\ndate :{self.date} '


class Bloodreq(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40),unique=False,nullable=False)
    phone=db.Column(db.BigInteger,unique=False,nullable=False)
    username=db.Column(db.String(20),unique=False,nullable=False)
    email=db.Column(db.String(40),unique=True,nullable=False)
    bloodgroup=db.Column(db.String(10),unique=False,nullable=False)
    district=db.Column(db.String(20),unique=False,nullable=False)
    bloodunit=db.Column(db.Integer,nullable=False)
    date=db.Column(db.Date)
     
    def __repr__(self):return f'\nname :{self.name},\nphone : {self.phone}, \nusername : {self.username},\nbloodgroup : {self.bloodgroup},\ndistrict : {self.district},\nemail : {self.email},bloodunit : {self.bloodunit},\ndate :{self.date} '


class Bloodreqapproved(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40),unique=False,nullable=False)
    phone=db.Column(db.BigInteger,unique=False,nullable=False)
    username=db.Column(db.String(20),unique=False,nullable=False)
    email=db.Column(db.String(40),unique=True,nullable=False)
    bloodgroup=db.Column(db.String(10),unique=False,nullable=False)
    district=db.Column(db.String(20),unique=False,nullable=False)
    bloodunit=db.Column(db.Integer,nullable=False)
    date=db.Column(db.Date)
     
    def __repr__(self):return f'\nname :{self.name},\nphone : {self.phone}, \nusername : {self.username},\nbloodgroup : {self.bloodgroup},\ndistrict : {self.district},\nemail : {self.email},bloodunit : {self.bloodunit},\ndate :{self.date} '

class BloodReqHandover(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40),unique=False,nullable=False)
    phone=db.Column(db.BigInteger,unique=False,nullable=False)
    username=db.Column(db.String(20),unique=False,nullable=False)
    email=db.Column(db.String(40),unique=False,nullable=False)
    bloodgroup=db.Column(db.String(10),unique=False,nullable=False)
    district=db.Column(db.String(20),unique=False,nullable=False)
    bloodunit=db.Column(db.Integer,nullable=False)
    date=db.Column(db.Date)
     
    def __repr__(self):return f'\nname :{self.name},\nphone : {self.phone}, \nusername : {self.username},\nbloodgroup : {self.bloodgroup},\ndistrict : {self.district},\nemail : {self.email},bloodunit : {self.bloodunit},\ndate :{self.date} '
    