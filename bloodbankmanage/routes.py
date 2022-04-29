from datetime import date
from bloodbankmanage import app,db,bcrypt
from flask import Flask,render_template,url_for,redirect,flash,session,request
from bloodbankmanage.forms import AdminRegForm,AdminLoginForm,DonorRegForm,Donateform,Donorlogin,Updatedonor,BloodReqForm
from bloodbankmanage.models import Admin,Donor,Bloodtest_Report,BloodDonate,Bloodbank,BloodApproved,Handover,Bloodreq,Bloodreqapproved,BloodReqHandover 
from flask_login import login_user,logout_user,current_user,login_required
from sqlalchemy import func


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/donorregister", methods=['POST','GET'])
def donorregister():
    if current_user.is_authenticated:
        return redirect(url_for('donorhome'))
    
    form=DonorRegForm()
    if form.validate_on_submit():
        blood_req=Bloodtest_Report.query.filter_by(uhid=form.uhid.data).first()
        if blood_req:
            if blood_req.bloodgroup == form.bloodgroup.data:
                donor=Donor.query.filter_by(username=form.username.data).first()
                if donor:
                    print("User Already Exists")

                else:
                    print("Welcome")
                    encrypted_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') #genearte hash of 60 characters     
                    newdonor=Donor(name=form.name.data, phone=form.phone.data, uhid=form.uhid.data, bloodgroup=form.bloodgroup.data, district=form.district.data, username=form.username.data, email=form.email.data, password=encrypted_password)
                    db.session.add(newdonor)
                    db.session.commit()
                    flash(f'Account created successfully for {form.username.data}',category='success')
                    return redirect(url_for('donorlogin'))

            else:
               #print("Blood does not Matched")
                flash(f'Blood Group does Matched {form.username.data}',category='danger')

        else:
            print("Access Denied")
            flash(f'Invalid Registration',category='danger')
           

    return render_template('donorregister.html',form=form)
 
@app.route("/donorlogin",methods=['POST','GET'])
def donorlogin():
    if current_user.is_authenticated:
        return redirect(url_for('donorhome'))
    form=Donorlogin()
    if form.validate_on_submit():
         donor=Donor.query.filter_by(username=form.username.data).first()
         if  donor and bcrypt.check_password_hash(donor.password,form.password.data):
           print(donor.username)
           print(donor.password)
           login_user(donor)
           flash(f'{donor.username} login Successfully ',category='success')
           return redirect(url_for('banner'))
         
         else:
            flash(f'{form.username.data} login unsuccessfully ',category='danger')
            return redirect(url_for('donorlogin'))
        
    
    return render_template('donorlogin.html',form=form)

@app.route("/donorhome")
@login_required
def donorhome():
    bloodstocks= Bloodbank.query.all()
    donor=Donor.query.all()
    return render_template('homedonor.html',bloodstocks=bloodstocks,donor=donor)

@app.route("/banner")
@login_required
def banner():
  
    return render_template('banner.html')
   

@app.route('/donateform',methods=['POST','GET'])
@login_required
def donateform():
    form= Donateform()
    if form.validate_on_submit():
        date_now= date.today()
        donation=BloodDonate(name=form.name.data,phone=form.phone.data,username=form.username.data,email=form.email.data,bloodgroup=form.bloodgroup.data, district=form.district.data,bloodunit=form.bloodunit.data,date=date_now)
        print("Hello")

        db.session.add(donation)
        db.session.commit()

        flash(f'BloodDonation of {form.username.data}',category='success')
    return render_template('donateform.html',form=form)


@app.route('/bloodreqform',methods=['POST','GET'])
@login_required
def bloodreqform():
    form= BloodReqForm()
    if form.validate_on_submit():
        date_now= date.today()
        bloodreq=Bloodreq(name=form.name.data,phone=form.phone.data,username=form.username.data,email=form.email.data,bloodgroup=form.bloodgroup.data, district=form.district.data,bloodunit=form.bloodunit.data,date=date_now)
        print("Hello")

        db.session.add(bloodreq)
        db.session.commit()

        flash(f'Blood Request of {form.username.data}',category='success')
    return render_template('bloodreqform.html',form=form)


@app.route("/donoraccount", methods=['POST','GET'])
@login_required
def donoraccount():
    form=Updatedonor()
    if form.validate_on_submit():

        updateaccount = Donor.query.filter_by(uhid=form.uhid.data).first()
        #print(updateaccount.name)
        updateaccount.name =form.name.data
        updateaccount.phone = form.phone.data
        updateaccount.email= form.email.data
        updateaccount.district= form.district.data
        db.session.commit()
        print("Update Sucessfull")
        flash(f'Account Updateed successfully for {form.username.data}',category='success')

    return render_template('donoraccountupdate.html',form=form)

@app.route('/donorstatus')
@login_required
def donorstatus():
    username=current_user.username
    print(username)
    blooddonate=BloodDonate.query.filter_by(username=username).all()
    handover=Handover.query.filter_by(username=username).all()

    return render_template('donorstatus.html',blooddonate=blooddonate,handover=handover)

@app.route('/donorlogout')
@login_required
def donorlogout():
    logout_user()
    return redirect(url_for('donorlogin'))



#admin 

@app.route("/adminregister", methods=['POST','GET'])
def adminregister():
    form= AdminRegForm()
    if form.validate_on_submit(): 
        encrypted_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        admin = Admin(name=form.name.data,username=form.username.data,email=form.email.data,password=encrypted_password)
        db.session.add(admin)
        db.session.commit()
        flash(f'Account created successfully for {form.username.data}',category='success')
        return redirect(url_for('adminlogin'))

    return render_template('adminregister.html',form=form)



@app.route("/adminlogin",methods=['POST','GET'])
def adminlogin():
    form=AdminLoginForm()
    if form.validate_on_submit():
        admin=Admin.query.filter_by(username=form.username.data).first()
        if admin and bcrypt.check_password_hash(admin.password,form.password.data):
            session['name'] =admin.name
            session['email']=admin.email
            session['username']=admin.username

            flash(f'{form.username.data} login Successfully ',category='success')
            return redirect(url_for('homeadmin'))
        
        else:
           if 'username' in session:
               return redirect(url_for('homeadmin'))
           else:
                flash(f'{form.username.data} login unsuccessfully ',category='danger')
                return redirect(url_for('adminlogin'))    

    return render_template('adminlogin.html',form=form)

@app.route("/homeadmin")
def homeadmin():
    if 'username' in session:
        name=session["name"]
        username= session["username"]
        email=session["email"]
        
        bloodstocks= Bloodbank.query.all()
        
        bloodhandover=db.session.query(func.count(Handover.id)).scalar()
        bloddapproved=db.session.query(func.count(BloodApproved.id)).scalar()
        print(bloodhandover)
        print(bloddapproved)

    else:
        return redirect(url_for('adminlogin'))    

    return render_template('homeadmin.html',bloodstocks=bloodstocks,bloodhandover=bloodhandover,bloddapproved=bloddapproved)


@app.route("/adminaccount")
def adminaccount():
    if 'username' in session:
        name=session["name"]
        username= session["username"]
        email=session["email"]

    else:
        return redirect(url_for('adminlogin'))   
  
    return render_template('adminaccountpage.html')


#Blood Donate
@app.route("/blooddonatelist")
def blooddonatelist():
    blooddonate= BloodDonate.query.all()
 
    return render_template('blooddonatelist.html',blooddonate=blooddonate)

@app.route("/approved/<int:id>")
def approved(id):
    blooddonate=BloodDonate.query.filter_by(id=id).first()

    approvedblood=BloodApproved(name=blooddonate.name,phone=blooddonate.phone,username=blooddonate.username,email=blooddonate.email,bloodgroup=blooddonate.bloodgroup, district=blooddonate.district,bloodunit=blooddonate.bloodunit,date=blooddonate.date)
    db.session.add(approvedblood)
    print("Data Added to Approved Table")

    db.session.delete(blooddonate)
    db.session.commit()
    flash(f'Blood Donate is Approved ',category='success')

    return redirect(url_for("blooddonatelist"))

@app.route("/reject/<int:id>")
def reject(id):
    blooddonate=BloodDonate.query.filter_by(id=id).first()
    print(blooddonate.name)
    db.session.delete(blooddonate)
    db.session.commit()
  

    return redirect(url_for("blooddonatelist"))

@app.route("/bloodapproved")
def bloodapproved():
    blood_approve=BloodApproved.query.all()
    
    return render_template('bloodapproved.html',blood_approve=blood_approve)


@app.route("/handover/<int:id>")
def handover(id):
    print(id)
    blood_approve=BloodApproved.query.filter_by(id=id).first()
    
    date_now= date.today()
    bloodhandin=Handover(name=blood_approve.name,phone=blood_approve.phone,username=blood_approve.username,email=blood_approve.email,bloodgroup=blood_approve.bloodgroup, district=blood_approve.district,bloodunit=blood_approve.bloodunit,date=date_now)
    db.session.add(bloodhandin)
    print("Data Added to Handover Table")

    bloodstocks=Bloodbank.query.filter_by(bloodgroup=bloodhandin.bloodgroup).first()
    
    oldstock=int(bloodstocks.bloodquanity)
    donatestock=int(bloodhandin.bloodunit)
    
    total=oldstock+donatestock
    newstock=str(total)
    

    print(oldstock)
    print(donatestock)
    print(newstock)
    print("Bank Stock")
    print(bloodstocks.bloodquanity)
    bloodstocks.bloodquanity=newstock

    db.session.delete(blood_approve)

    db.session.commit()
    flash(f'Blood Donate is Handover Successfully ',category='success')
    return redirect(url_for("bloodapproved"))


@app.route("/bloodhandover")
def bloodhandover():
    bloodhandin=Handover.query.all()
    bloodhandover=db.session.query(func.count(Handover.id)).scalar()
    bloddapproved=db.session.query(func.count(BloodApproved.id)).scalar()
    print(bloodhandover)
    print(bloddapproved)

    return render_template('bloodhandover.html',bloodhandin=bloodhandin,bloodhandover=bloodhandover,bloddapproved=bloddapproved)




#BLOODREQUEST
@app.route('/bloodreqlist')
def bloodreqlist():
    bloodreq= Bloodreq.query.all()
    return render_template('bloodreqlist.html', bloodreq=bloodreq)


@app.route('/bloodreqapproved')
def bloodreqapproved():
    bloodreq_approv= Bloodreqapproved.query.all()

    return render_template('bloodreqapproved.html',bloodreq_approv=bloodreq_approv)
  

@app.route("/reqapproved/<int:id>")
def reqapproved(id):
    bloodreq=Bloodreq.query.filter_by(id=id).first()

    approvedblood=Bloodreqapproved(name=bloodreq.name,phone=bloodreq.phone,username=bloodreq.username,email=bloodreq.email,bloodgroup=bloodreq.bloodgroup, district=bloodreq.district,bloodunit=bloodreq.bloodunit,date=bloodreq.date)
    db.session.add(approvedblood)
    print("Data Added to BloodReqApprove Table")

    db.session.delete(bloodreq)
    db.session.commit()
    flash(f'Blood Donate is Approved ',category='success')
    return redirect(url_for("bloodreqlist"))


@app.route("/reqreject/<int:id>")
def reqreject(id):
    blooddonate=Bloodreq.query.filter_by(id=id).first()
    print(blooddonate.name)
    db.session.delete(blooddonate)
    db.session.commit()
    return redirect(url_for("bloodreqlist"))

@app.route("/bloodreqhandover")
def bloodreqhandover():
    blooreqhandin=BloodReqHandover.query.all()
    return render_template('bloodreqhandover.html',blooreqhandin=blooreqhandin)

@app.route("/reqhandover/<int:id>")
def reqhandover(id):
    print(id)
    blood_req_approve=Bloodreqapproved.query.filter_by(id=id).first()
    
    date_now= date.today()
    bloodreqhandin=BloodReqHandover(name=blood_req_approve.name,phone=blood_req_approve.phone,username=blood_req_approve.username,email=blood_req_approve.email,bloodgroup=blood_req_approve.bloodgroup, district=blood_req_approve.district,bloodunit=blood_req_approve.bloodunit,date=date_now)
    db.session.add(bloodreqhandin)
    print("Data Added to Handover Table")

    bloodstocks=Bloodbank.query.filter_by(bloodgroup=bloodreqhandin.bloodgroup).first()
    
    oldstock=int(bloodstocks.bloodquanity)
    donatestock=int(bloodreqhandin.bloodunit)
    
    if(oldstock < donatestock or oldstock==0):
           flash(f'Blood Stock is not available ',category='danger')
                      
    else: 
        total=oldstock-donatestock
        newstock=str(total)
        print(oldstock)
        print(donatestock)
        print(newstock)
       
        bloodstocks.bloodquanity=newstock
        db.session.delete(blood_req_approve)
        db.session.commit()
        flash(f'Blood Donate is Handover Successfully ',category='success')
    
    return redirect(url_for("bloodreqapproved"))


@app.route('/adminlogout')
def adminlogout():
    session.pop("name",None)
    session.pop("username",None)
    session.pop("email",None)
    return redirect(url_for('adminlogin'))    
       






