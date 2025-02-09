from flask import *
from database import *

public=Blueprint("public",__name__)



@public.route('/')
def homepage():

    return render_template("homepage.html")


@public.route('/login',methods=['get','post'])
def login():

    if 'login' in request.form:

        u=request.form['uname']
        p=request.form['psw']

        a="select  * from login where username='%s' and password='%s'"%(u,p)
        res=select(a)
        if res:
            session['log']=res[0]['loginid']


        print(res[0]['usertype'],"////////////res")

        if res[0]['usertype']=='admin':
            return redirect(url_for('admin.adminhome'))
        
        if res[0]['usertype']=='artist':
            qry="select * from artist where loginid='%s'"%(session['log'])
            res1=select(qry)
            if res1:
                session['artist']=res1[0]['artistid']
            return redirect(url_for('artist.artisthome'))
        
        if res[0]['usertype']=='user':
            return redirect(url_for('user.userhome'))
        
        if res[0]['usertype']=='pending':
            return "<script>alert('Your account has yet to be accepted!');window.location='/login'</script>"
        
        if res[0]['usertype'] == 'rejected':
            return "<script>alert('You are rejected for some reasons!!');window.location='/login'</script>"
        
        
 

      

    return render_template("login.html")

@public.route('/artist',methods=['get','post'])
def artist():
   
   if 'artist' in request.form:
       
       fn=request.form['fname']
       ln=request.form['lname']
       e=request.form['femail']
       g=request.form['fgender']
       fp=request.form['fnumb']
       pl=request.form['fplace']
       q=request.form['fqual']
       u=request.form['uname']
       p=request.form['psw']



       print(fn,ln,e,g,fp,pl,q,u,p,"///////////")

       qry="insert into login values(null,'%s','%s','pending')"%(u,p)
       res=insert(qry)

       qry="insert into artist values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(res,fn,ln,e,g,fp,pl,q)
       res=insert(qry)

       return "<script>alert('Your registeration was successfully sent, pls wait for confirmation');window.location='/artist'</script>"


       

   return render_template("artist.html")


@public.route('/user',methods=['get','post'])
def user():
   
   if 'user' in request.form:
       
       ufn=request.form['ufname']
       uln=request.form['ulname']
       upl=request.form['ufplace']
       ufp=request.form['ufnumb']
       ue=request.form['ufemail']
       ug=request.form['ufgender']
       u=request.form['uname']
       p=request.form['psw']



       print(ufn,uln,upl,ufp,ue,ug,u,p,"///////////")

       qry="insert into login values(null,'%s','%s','user')"%(u,p)
       res=insert(qry)

       qry="insert into user values(null,'%s','%s','%s','%s','%s','%s','%s')"%(res,ufn,uln,upl,ufp,ue,ug)
       res=insert(qry)


       

   return render_template("user.html")


@public.route('/about_me')
def aboutme():
    return render_template("about.html")