from flask import *
from public import public
from admin import admin
from artist import artist
from user import user




app=Flask(__name__)


app.secret_key='sderftghyujihgfds'

app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(artist)
app.register_blueprint(user)


app.run(debug=True,port=5045,host="0.0.0.0")


    