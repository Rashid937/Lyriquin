from flask import *
from database import *
import uuid

artist=Blueprint("artist",__name__)



@artist.route('/artisthome')
def artisthome():

    return render_template("artisthome.html")

@artist.route('/viewuser_artist')
def viewuser():
    data={}
    qry="select * from user"
    res=select(qry)
    if res:
        data['view']=res
    return render_template("viewuser_artist.html",data=data)



@artist.route('/artist_chat',methods=['post','get'])
def artist_chat():
    data={}
    name=''
    if 'action' in request.args:
        action=request.args['action']
        session['id']=request.args['id']
        name=request.args['name']

    else:
        action=None
    
    f="SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' UNION SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' ORDER BY date , time"%(session['id'],session['log'],session['log'],session['id'])
    rg=select(f)
    print(rg)
    data['rg']=rg

    if 'submit' in request.form:
        chat=request.form['chat']
        print(chat,"000000000000000000000000000000000000000000000000")
        a="insert into chat values(null,'%s','artist','%s','user','%s',curdate(),curtime())"%(session['log'],session['id'],chat)
        insert(a)
        return redirect(url_for('artist.artist_chat'))
    return render_template("artist_chat.html",data=data,name=name)





@artist.route('/viewrating')
def viewrating():
    data={}
    qry="select * from rating where artistid='%s'"%(session['artist']) 
    res=select(qry)
    if res:
        data['view']=res
    return render_template("viewrating.html",data=data)

@artist.route('/viewpayment')
def viewpayment():
    data={}
    # qry=" SELECT * FROM booking_child RIGHT JOIN booking_master USING(bookingmasterid) INNER JOIN works USING(workid) INNER JOIN USER WHERE artistid='%s' GROUP BY bookingmasterid" % (session['artist'])
    # qry = "SELECT * FROM payment INNER JOIN booking_master USING(bookingmasterid) INNER JOIN booking_child USING(bookingmasterid) INNER JOIN works USING(workid) LEFT JOIN USER ON user.userid = booking_master.userid WHERE artistid='%s' GROUP BY paymentid "  % (session['artist'])
    qry = "SELECT * FROM payment INNER JOIN booking_master USING(bookingmasterid) INNER JOIN booking_child USING(bookingmasterid) INNER JOIN works USING(workid) LEFT JOIN USER ON user.userid = booking_master.userid WHERE artistid='%s' GROUP BY user.userid"  % (session['artist'])
    res=select(qry)
    if res:
        data['view']=res
    return render_template("viewpayment.html",data=data)

@artist.route('/viewguidance')
def viewguidance():
    data={}
    random = None
    
    qry = "SELECT * FROM request INNER JOIN user WHERE artistid='%s' GROUP BY requestid" % (session['artist'])
    res = select(qry)
    if res:
        data['view']=res
        print(data,"&&&&&&&&&&&&&&&&777")

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']

    else:
        action=None

    if action=='accept':
        qry1="update request set status='Accepted' where requestid='%s'"%(id)
        update(qry1)
        res1=update(qry1)
        if res1:
            random="something"
        
        return f"<script>alert('success');window.location='/artist_assign_amt?r_id={id}'</script>" 

    if action=='reject':
        qry2="update request set status='Rejected' where requestid='%s'"%(id) 
        update(qry2)
        return "<script>alert('success');window.location='/viewguidance'</script>" 
    
    if 'accept' in request.form:

        amount=request.form['amount']       

        qry2="update request set amount='%s' where requestid='%s'"%(amount,id)
        update(qry2)
        return "<script>alert('success');window.location='/viewquidance'</script>"
    
    print(random,"++++++++++=")
    return render_template("viewguidance.html",data=data)

@artist.route('/r_reply',methods=['POST','GET'])
def r_reply():
    id=request.args['id']
    if 'send'in request.form:
         reply=request.form['reply']

         qry="update request set reply='%s' where requestid='%s'"%(reply,id)
         update(qry)
         return "<script>alert('success');window.location='/viewguidance'</script>" 


    return render_template("reply.html")


@artist.route('/artist_assign_amt',methods=['POST','GET'])
def artist_assign_amt():
    request_id=request.args['r_id']
    if 'update' in request.form:
        amount=request.form['amount']
        
        qry1="update request set amount='%s' where requestid='%s'"%(amount,request_id)
        update(qry1)
        return "<script>alert('success');window.location='/viewguidance'</script>"

    return render_template("artist_assign_amt.html")

@artist.route('/vieworders')
def vieworders():
    data={}
    qry="SELECT * FROM booking_child RIGHT JOIN booking_master USING(bookingmasterid) INNER JOIN works USING(workid) WHERE artistid='%s'"%(session['artist'])

    res=select(qry)
    if res:
        data['view']=res
    return render_template("vieworders.html",data=data)




@artist.route('/manage_work',methods=['POST','GET'])
def manage_work():
    if 'submit' in request.form:
        work_name=request.form['work_name']
        file=request.files['path']
        path='static/work/'+ str(uuid.uuid4())+file.filename
        file.save(path)
        amount=request.form['amount']


        qry="insert into works values(null,'%s','%s','%s','%s','availabe')"%(session['artist'],work_name,path,amount)
        insert(qry)
        return "<script>alert('success');window.location='/manage_work'</script>"
  


    data={}
    qry="select * from works where artistid='%s'"%(session['artist'])
    res=select(qry)
    if res:
        data['view']=res



    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None

    if action=='update':
        qry1="select * from works where workid='%s'"%(id)
        res1=select(qry1)
        if res1:
            data['up']=res1


    if action=='delete':
        qry3="delete from works where workid='%s' "%(id)     
        delete(qry3)
        return "<script>alert('success');window.location='/manage_work'</script>"   

    if 'update' in request.form:
        work_name=request.form['work_name']
        status=request.form['status']
        amount=request.form['amount']     

        qry2="update works set workname='%s',status='%s',amount='%s' where workid='%s'"%(work_name,status,amount,id)
        update(qry2)
        return "<script>alert('success');window.location='/manage_work'</script>" 


    return render_template("manageworks.html",data=data)



@artist.route('/manage_tutorial',methods=['POST','GET'])
def manage_tutorial():
    if 'submit' in request.form:
        title=request.form['title']
        file=request.files['path']
        path="static/"+str(uuid.uuid4())+file.filename
        file.save(path)
        date=request.form['date']


        qry="insert into tutorials values(null,'%s','%s','%s','%s')"%(session['artist'],title,path,date)
        insert(qry)
        return "<script>alert('success');window.location='/manage_tutorial'</script>"

    data={}
    qry="select * from tutorials where artistid='%s'"%(session['artist'])
    res=select(qry)
    if res:
        data['view']=res



    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None

    if action=='update':
        qry1="select * from tutorials where tutorialid='%s'"%(id)
        res1=select(qry1)
        if res1:
            data['up']=res1


    if action=='delete':
        qry3="delete from tutorials where tutorialid='%s' "%(id)     
        delete(qry3)  
        return "<script>alert('success');window.location='/manage_tutorial'</script>"
 

    if 'update' in request.form:
        title=request.form['title']
        date=request.form['date']       

        qry2="update tutorials set title='%s',date='%s' where tutorialid='%s'"%(title,date,id)
        update(qry2)
        return "<script>alert('success');window.location='/manage_tutorial'</script>"




    return render_template("managetutorials.html",data=data)