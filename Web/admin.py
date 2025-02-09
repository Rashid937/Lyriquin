from flask import *
from database import *
import uuid

admin=Blueprint("admin",__name__)



@admin.route('/adminhome')
def adminhome():

    return render_template("adminhome.html")
    
@admin.route('/viewartist')
def viewartist():
    data={}
    qry="SELECT * FROM artist INNER JOIN login USING(loginid)"
    res=select(qry)
    if res:
        data['view']=res

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
   

        if action=='accept':
            qry1="update login set usertype='artist' where loginid='%s'"%(id)
            update(qry1)
            return "<script>alert('success');window.location='/viewartist'</script>" 

        if action=='reject':
            qry2="update login set usertype='rejected' where loginid='%s'"%(id) 
            update(qry2)
            return "<script>alert('success');window.location='/viewartist'</script>"    
        
        if action is None:
             qry3="update login set usertype='pending' where loginid='%s'"%(id)
             update(qry3)

    

    return render_template("viewartist.html",data=data)

@admin.route('/viewuser')
def viewuser():
    data={}
    qry="select * from user"
    res=select(qry)
    if res:
        data['view']=res
    return render_template("viewuser.html",data=data)

@admin.route('/viewfeedback')
def viewfeedback():
    data={}
    qry="select * from feedback"
    res=select(qry)
    if res:
        data['view']=res
    return render_template("viewfeedback.html",data=data)

@admin.route('/viewcomplaint')
def viewcomplaint():
    data={}
    qry="select * from complaint inner join artist using(artistid) where reply='pending'"
    res=select(qry)
    if res:
        data['view']=res
    return render_template("viewcomplaint.html",data=data)

@admin.route('/reply',methods=['POST','GET'])
def reply():
    id=request.args['id']
    if 'send'in request.form:
         reply=request.form['reply']

         qry="update complaint set reply='%s' where complaintid='%s'"%(reply,id)
         update(qry)
         return "<script>alert('reply success');window.location='/viewcomplaint'</script>"
    

    return render_template("reply.html")
    
@admin.route('/viewworks')
def viewworks():
    data={}
    qry="select * from works"
    res=select(qry)
    if res:
        data['view']=res
    return render_template("viewworks.html",data=data)
    
    