import uuid
from flask import *
from database import *

user=Blueprint("user",__name__)



# @user.route('/userhome')
# def userhome():

#     return render_template("userhome.html")


# @user.route('/feedback')
# def feedback():

#     return render_template("feedback.html")


@user.route('/user_registration')
def user_registration():
    fname=request.args['first_name']
    lname=request.args['last_name']
    place=request.args['place']
    number=request.args['number']
    email=request.args['email']
    gen=request.args['gender']
    uname=request.args['username']
    psw=request.args['password']

    data={}


    qry="insert into login values(null,'%s','%s','user')"%(uname,psw)
    res=insert(qry)

    qry="insert into user values(null,'%s','%s','%s','%s','%s','%s','%s')"%(res,fname,lname,place,number,email,gen)
    res=insert(qry)
    if res:
        data['status']='success'
    else:
        data['status']='failed'
    print(data,"++++++++++++")

    return data




@user.route('/user_login')
def user_login():
    data={}
    uname=request.args['uname']
    psw=request.args['psw']

    # print(uname,psw)
    a="select  * from login where username='%s' and password='%s'"%(uname,psw)
    res=select(a)
    if res:
        data['status']='success'
        data['view']=res
    else:
        data['status']='failed'

    print(data,"+++++++++++++")

    return data





@user.route('/user_view_works')
def user_view_works():
    data={}

    artist_id=request.args['artist_id']
    

    # print(uname,psw)
    a="select * from works where artistid='%s'"%(artist_id)
    res=select(a)
    if res:
        data['status']='success'
        data['view']=res
    else:
        data['status']='failed'

    print(data,"+++++++++++++") 

    return data

@user.route('/user_view_all_works')
def user_view_all_works():
    data={}
    

    # print(uname,psw)
    a="select * from works"
    res=select(a)
    if res:
        data['status']='success'
        data['view']=res
    else:
        data['status']='failed'

    print(data,"+++++++++++++") 

    return data
    

@user.route('/user_view_tutorials')
def user_view_tutorials():
    data={}
    art_id=request.args['artist_id']

    # print(uname,psw)
    a="select  * from tutorials where artistid='%s'"%(art_id)
    res=select(a)
    if res:
        data['status']='success'
        data['view']=res
    else:
        data['status']='failed'

    print(data,"+++++++++++++") 

    return data

@user.route('/user_send_complaint',methods=['POST','GET'])
def user_complaint():
    data={}
  
    Aid=request.args['artist_id']
    Uid=request.args['lid']
    title=request.args['title']
    comp=request.args['comp']
 

    a="insert into complaint values(null,'%s','%s','%s','%s','pending',curdate())"%(Uid,Aid,title,comp)
    
    res=insert(a)
    if res:
        data['status']='success'
    else:
        data['status']='failed'
    print(data,"++++++++++++")

    data['method']='send'

    return data


@user.route('/user_view_complaint')
def user_view_complaint():
   data={}
   lid=request.args['lid']
   art_id=request.args['artist_id']
  
   a="select  * from complaint where userid='%s' and artistid='%s'"%(lid,art_id)
   res=select(a)

   if res:
        data['status']='success'
        data['data']=res
   else:
        data['status']='failed'

   print(data,"+++++++++++++")

   data['method']='view'

   return data

@user.route('/user_request_guidance',methods=['POST','GET'])
def user_request_guidance():
    lid=request.args['lid']
    art_id=request.args['artist_id']
    desc=request.args['description']
    

 

    data={}


    a="insert into request values(null,'%s','%s','%s','pending',curdate(),'pending','pending')"%(art_id,lid,desc)
    
    res=insert(a)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    print(data,"++++++++++++")

    data['method']='send'

    return data

@user.route('/user_view_request')
def user_view_request():
   data={}
   lid=request.args['lid']
   art_id=request.args['artist_id']
  
   a="select * from request where userid='%s' and artistid='%s'"%(lid,art_id)
   res=select(a)
   print(res,"--"*100)

   if res:
        data['status']='success'
        data['data']=res
   else:
        data['status']='failed'

   print(data,"+++++++++++++")

   data['method']='view'

   return str(data)

@user.route('/user_send_feedback',methods=['POST','GET'])
def user_send_feedback():
    data={}
  
    lid=request.args['lid']
    fdbk=request.args['feedback']
  

    a="insert into feedback values(null,(select userid from user where loginid='%s'),'%s',curdate())"%(lid,fdbk)
    
    res=insert(a)
    if res:
        data['status']='success'
    else:
        data['status']='failed'
    print(data,"++++++++++++")

    data['method']='send'

    return data

@user.route('/user_Add_to_cart')
def user_Add_to_cart():
    wid=request.args['wid']
    qty=request.args['quantity']
    amt=request.args['amt']
    lid=request.args['lid']

    print(qty,'++++++++++++++++++++')
    print(amt,'++++++++++++++++++++++++++++')


    a="select * from user where loginid='%s'"%(lid)
    xs=select(a)
    uid=xs[0]['userid']

    tt=int(qty)*int(amt)
   



    data={}

    r="select * from booking_master where userid='%s' and status='pending'"%(uid)
    rr=select(r)

    if rr:
        tot=rr[0]['totalamount']
        bid=rr[0]['bookingmasterid']

        final=int(tot)+int(tt)

        cc="update booking_master set totalamount='%s' where bookingmasterid='%s'"%(final,bid)
        update(cc)

        qry="insert into booking_child values(null,'%s','%s','%s','%s','pending')"%(bid,wid,qty,amt)
        res=insert(qry)



    else:



        z="insert into booking_master values(null,'%s','%s',curdate(),'pending')"%(uid,tt)
        id=insert(z)


        qry="insert into booking_child values(null,'%s','%s','%s','%s','pending')"%(id,wid,qty,amt)
        res=insert(qry)

    if res:
        data['status']='success'
    else:
        data['status']='failed'
    print(data,"++++++++++++")

    return data

@user.route('/user_view_cart')
def user_view_cart():
    data={}

    lid=request.args['lid']
    

    # print(uname,psw)
    a="select *,booking_child.amount as book_prod_amt from booking_child inner join booking_master using(bookingmasterid) inner join works using(workid) where userid=(select userid from user where loginid='%s') and booking_master.status='pending'"%(lid)
    res=select(a)
    if res:
        data['status']='success'
        data['view']=res
    else:
        data['status']='failed'

    print(data,"+++++++++++++") 
    data['method']='view'

    return data

# @user.route('/user_view_orders')
# def user_view_orders():
#     return "print"


@user.route('/user_search_artists', methods=['GET'])
def user_search_artists():
    q=request.args['q']
    data={}
    
    
    q=f"select * from artist where firstname like '%{q}%'"
    res=select(q)
    print(res,"************")

    if res:
        data['status']='success'
        data['view']=res
    else:
        data['status']='failed'

    print(data,"++++++++")
    return data




@user.route('/view_gen')
def view_gen():
    data={}

    lid=request.args['lid']
    

    # print(uname,psw)
    a="select  * from ai_generation where login_id='%s'"%(lid)
    res=select(a)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'

    print(data,"------------------") 

    return data





    

@user.route('/user_view_orders',methods=['POST','GET'])
def user_view_orders():
    data={}

    lid=request.args['lid']
    

    # print(uname,psw)
    a="SELECT  * FROM booking_child INNER JOIN booking_master USING(bookingmasterid) INNER JOIN works USING(workid) INNER JOIN payment USING(bookingmasterid) WHERE userid=(SELECT userid FROM USER WHERE loginid='%s') and booking_master.status ='Processing'"%(lid)
    res=select(a)
    if res:
        data['status']='success'
        data['view']=res
    else:
        data['status']='failed'

    print(data,"+++++++++++++")  

    return data



@user.route('/payment',methods=['POST','GET'])
def payment():
    data={}
    id = request.args['id']
   

    qry3 = "insert into payment values(null, '%s', 'Paid')" % (id)
    a=insert(qry3)

    qry1 = "update booking_master set status='processing' where bookingmasterid='%s'" % (id)
    res1=update(qry1)
    if res1:
        data['status']="success"
        data['method']="user_pay"
    else:
        data['status']="failed"
    return str(data)


# @user.route('/payment',methods=['POST','GET'])
# def guidance_payment():
#     data={}
#     id = request.args['id']
   
#     qry1 = "update request set status='Paid' where requestid='%s'" % (id)
#     res1=update(qry1)
#     if res1:
#         data['status']="success"
#         data['method']="req_pay"
#     else:
#         data['status']="failed"
#     return str(data)


@user.route('/guidance_payment',methods=['POST','GET'])
def guidance_payment():
    data={}
    id = request.args['id']
   
    qry1 = "update request set status='Paid' where requestid='%s'" % (id)
    res1=update(qry1)
    if res1:
        data['status']="success"
        data['method']="req_pay"
    else:
        data['status']="failed"
    return str(data)

@user.route('/user_add_review',methods=['POST','GET'])
def user_add_review():
    wid=request.args['wid']
    lid=request.args['lid']
    desc=request.args['description']
    

 

    data={}


    a="insert into review values(null,'%s',userid=(select userid from user where loginid='%s','%s',curdate())"%(wid,lid,desc)
    
    res=insert(a)
    if res:
        data['status']='success'
    else:
        data['status']='failed'
    print(data,"++++++++++++")

    data['method']='send'

    return data

@user.route('/user_rating',methods=['POST','GET'])
def user_rating():
    data={}
  
    lid=request.args['lid']
    artist_id=request.args['artist_id']
    review=request.args['review']
    rating=request.args['rating']

  

    a="insert into rating values(null,'%s',(select userid from user where loginid='%s'),'%s','%s',curdate())"%(artist_id,lid,rating,review)
    
    res=insert(a)
    if res:
        data['status']='success'
    else:
        data['status']='failed'
    print(data,"++++++++++++")

    data['method']='send'

    return data

@user.route('/user_delete_single_product', methods=['POST', 'GET'])
def user_delete_single_product():
    data = {}
    booking_master_id = request.args['bmid']
    booking_child_id = request.args['bcid']
    amount = request.args['amount']
    tot_amt = request.args['tot_amt']
    qty = request.args['quantity']

    tt=int(qty)*int(amount)



    a="delete from booking_child where bookingchildid='%s'"%(booking_child_id)
    res=delete(a)

    qry="update booking_master set totalamount='%s' where bookingmasterid='%s'"%((int(tot_amt)-int(tt)),booking_master_id)
    res1=update(qry)


    if res1:
        data['status'] = 'success'
    else:
        data['status'] = 'failed'

    print(data, "++++++++++++")
    
    data['method']='delete'

    return str(data)






from img import *

@user.route('/generate_image')
def generate_image_route():
    data = {}

    description = request.args.get('description')
    lid = request.args.get('lid')

    if description:
        res = generate_image(description)
        print(res, "/////////////")
       

        if res:
            a = "insert into ai_generation values(null,'%s','%s',curdate(),'%s')" % (description, res, lid)
            cc = insert(a)
            data['status'] = 'success'
            data['view'] = res
        else:
            data['status'] = 'failed'
    else:
        data['status'] = 'failed'
        data['error'] = 'No description provided'

    print(data, "+++++++++++++")

    return jsonify(data)



import os
import uuid
from flask import Flask, request, jsonify
import cv2
import numpy as np
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from sklearn.metrics.pairwise import cosine_similarity

# Initialize Flask app
app = Flask(__name__)

# Load Pre-trained Model (ResNet50 without top layers)
model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

# Function to extract features
def extract_features(image_path, model):
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    features = model.predict(image)
    return features.flatten()

# Step 1: Build a feature database (without subfolders, only direct images)
def build_feature_database(dataset_folder, model):
    feature_db = {}
    for filename in os.listdir(dataset_folder):
        if filename.endswith(('.jpg', '.png', '.jpeg', '.webp')):  # File extensions
            file_path = os.path.join(dataset_folder, filename)
            features = extract_features(file_path, model)
            feature_db[file_path] = features
    return feature_db

# Step 2: Find the most similar image
def find_similar_image(uploaded_image_path, feature_db, model):
    uploaded_features = extract_features(uploaded_image_path, model)
    max_similarity = -1
    most_similar_image = None

    for file_path, features in feature_db.items():
        similarity = cosine_similarity([uploaded_features], [features])[0][0]
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_image = file_path

    return most_similar_image, max_similarity

# Main Execution
@user.route('/check_similarity', methods=['GET','POST'])
def check_similarity():
    data = {}
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image = request.files['image']

    # Save the uploaded image to a temporary location
    uploaded_image_path = f'static/similar/{str(uuid.uuid4())}_{image.filename}'
    image.save(uploaded_image_path)

    # Dataset folder - replace with your own dataset path
    dataset_folder = r'C:\Users\RASHID U\OneDrive\Desktop\project\Web\Web\static\work'  # Ensure this path is correct on your server

    # Build feature database
    print("Building feature database...")
    feature_db = build_feature_database(dataset_folder, model)

    # Find the most similar image
    print("Finding similar image...")
    similar_image, similarity_score = find_similar_image(uploaded_image_path, feature_db, model)
    print(similar_image,'//////////////////////////////////////')
    if similar_image:
        similarity_score = float(similarity_score)
        print(similarity_score,"kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")

     


        # Extract folder name (use file name if there are no subfolders)
        similar_image_filename = os.path.basename(similar_image)
        print(similar_image_filename)
        image_name_without_extension = os.path.splitext(similar_image_filename)[0]

        qry = "select * from works where workname='%s'"%(image_name_without_extension)
        res = select(qry)
        print(res,"=="*100)

        data = {
            "similar_image": similar_image_filename,
            "similarity_score": round(similarity_score, 4),
            "similar_image_path": similar_image,
            "status":"success",
            "data":res
        }
        print(data,"pppppppppppppp")


        return jsonify(data)
    else:
        return jsonify({"error": "No similar image found."}), 404


################################################

from hybrid_rec import *

@user.route('/user_view_artist')
def user_view_artist():
    data={}
    data['view'] = []
    lid=request.args['lid']

    z="select * from user where loginid='%s'"%(lid)
    cc=select(z)
    uid=cc[0]['userid']
    user_id=int(uid)

    query = "SELECT * FROM rating"
    # df = get_data_from_db(query)
    res = select(query)

    if res:
        df = pd.DataFrame(res)

        result = hybrid_recommendation(user_id, df)
        print(result,"_____________")
        if result:

            for i in result:
                qry2 = "SELECT * FROM artist INNER JOIN login USING(loginid) left JOIN rating USING(artistid) WHERE artistid='%s' group by artist.firstname" % (i)
                res2 = select(qry2)
                data['status']='success'
                data['view'].extend(res2)

        else:
            qry1="select * from artist inner join login using(loginid)"
            result=select(qry1)
            if result:
                data['status']='success'
                data['view']=result

        # print(data,"))))))))))))))))")
            
    else:
        qry1="select * from artist"
        result=select(qry1)
        if result:
            data['status']='success'
            data['view']=result
        else: 
            data['status']='failed'
        

    

    return data


# @user.route('/user_view_artist')
# def user_view_artist():
#     data={}
    

#     # print(uname,psw)
#     a="select  * from artist"
#     res=select(a)
#     if res:
#         data['status']='success'
#         data['view']=res
#     else:
#         data['status']='failed'

#     print(data,"------------------") 

#     return data




@user.route('/user_chat')
def user_chat():
    data={}
    sender_id=request.args['sender_id']
    receiver_id=request.args['receiver_id']
    details=request.args['details']

    a="insert into chat values(null,'%s','user',(select loginid from artist where artistid='%s'),'artist','%s',curdate(),curtime())"%(sender_id,receiver_id,details)
    res=insert(a)
    if res:
        data['status']="success"
    else:
        data['status']="failed"
    data['method']="chat"

    return str(data)  




@user.route('/chat_details')
def chat_details():
    data={}
    sender_id=request.args['sender_id']
    receiver_id=request.args['receiver_id']


    f="SELECT * FROM chat WHERE sender_id='%s' AND receiver_id=(select loginid from artist where artistid='%s') UNION SELECT * FROM chat WHERE sender_id=(select loginid from artist where artistid='%s') AND receiver_id='%s' ORDER BY date , time"%(sender_id,receiver_id,receiver_id,sender_id)
    rg=select(f)
    if rg:
        data['status']="success"
        data['data']=rg
    else:
        data['status']="failed"
    data['method']="chatdetail"
    return str(data)
