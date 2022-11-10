from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import (LoginManager, login_manager, login_user
, logout_user, login_required, UserMixin)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = 'secretkey'


login_manager = LoginManager()

db = SQLAlchemy(app)
login_manager.init_app(app)

class User(UserMixin,db.Model):
    # __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique = True, nullable = False)
    password = db.Column(db.String(80), nullable = False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# route for sign-up
@app.route('/user/signup', methods = ['POST'])
def signUP():
    user = User(
        name=request.json.get('name'),
        email=request.json.get('email'),
        password=request.json.get('password')
    )

    db.session.add(user)
    db.session.commit()

    return {"message" : "user added sucessfully"}

# route for login
@app.route('/user/signin', methods = ['POST'])
def signin():
    if(request.method == 'POST'):
        req = request.get_json()
        email = req['email']
        password = req['password']
        check_user = User.query.filter_by(email = email).first()
        if(check_user is not None):
            if(check_user.password == password):
                login_user(check_user)
                return {"message" : "Logged In sucessfully"}
            else:
                return {"message" : "Incorrect password"}
        else:
            return {"message" : "No such user exists"}


@app.route('/user/signout', methods = ['GET'])
@login_required
def logout():
    logout_user()
    return {"message" : "Logged out successfully"}

@app.route('/seats/available', methods = ['GET'])
def get_all_seats():
    pass

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()