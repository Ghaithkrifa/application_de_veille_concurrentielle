import email
from flask_mail import Mail, Message
from models import User,RoleEnum,Aregarder,opinions,rates
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, get_jwt, verify_jwt_in_request
from flask import Flask
import random
import string
from functools import wraps
from datetime import *

app = Flask(__name__, template_folder="templates", static_folder="assets")
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'innovationtalan356@gmail.com'
app.config['MAIL_PASSWORD'] = 'pqsknkvilxvcscht'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
  

def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["sub"]["isAdmin"]:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Admins only!"), 403
        return decorator

    return wrapper

def login():
    email = request.json["email"]
    password = request.json["password"]
    user = User.objects.filter(email=email).only("fullName", "position","email","phoneNumber", "role", "password").first()
    if user and user.passwordIsCorrect(password):
        access_token = create_access_token(identity={"email":email, "isAdmin": user.role  == RoleEnum.ADMIN})
        return jsonify(user=user, access_token=access_token), 201
    else:
        return jsonify(message="Email or Password error"), 401

def sentMail(email,password,fullName):
 
   msg = Message(sender="innovationtalan356@gmail.com", recipients = [email], subject=F"Welcome to Talan madame/monsieur {fullName}")

   msg.body = F"Paramètre d’accès de votre compte :  votre email= {email},  Votre password={password}"
   print(msg)
   mail.send(msg)
   
   return jsonify(message="Message sent successfully"), 200

def createUser():
    try:
        fullName = request.json["fullName"]
        position = request.json["position"]
        email = request.json["email"]   
        password="".join(random.choices(string.ascii_lowercase, k=10))
        pass1=password
        print("aaaa",pass1)
        phoneNumber = request.json["phoneNumber"] 
        user = User(fullName=fullName, position=position, email=email, password=password, phoneNumber=phoneNumber,role=RoleEnum.USER)
        user.hashPassword()
        user.save()
        return jsonify(message="User created sucessfully"), 201
    except Exception:  
        return jsonify(message="User creation error"), 400


def getUsers():
    users = User.objects.filter(role=RoleEnum.USER).only('fullName', 'position',"email","phoneNumber")
    return jsonify(users), 200


def deleteUser(email):
    user=User.objects.filter(email=email).first()
    User.objects.filter(email=email).delete()
    Aregarder.objects.filter(user=user).delete()
    p=opinions.objects()
    aaa=[]
    aa=[{"ref":"vide","nom":"vide","commentaire":"vide"}]
    for i in p:
        res = [i for i in i.liste  if not (i["ref"]==user.id)]
        i.liste=res
        if(i.liste==aaa):
            i.liste=aa
        i.save()
    opinions.objects.filter(liste=aa).delete()
    pp=rates.objects()
    for i in pp :
        for j in i.users:
            if(j==user.id):
                i.users.remove(j)
                i.rate+=-1
        i.save()
        rates.objects.filter(rate=0).delete()
    return jsonify(message="User deleted sucessfully"), 200





def getUser(email):
    user = User.objects.filter(email=email).first()
    if user:
        return jsonify(user), 200
    else:
        return jsonify(message="user not found"), 404


def updateUser(oldEmail):
    try:
        fullName = request.json["fullName"]
        position = request.json["position"]
        email = request.json["email"]
        password = request.json.get("password", None)
        password1=password
        phoneNumber = request.json["phoneNumber"]
        datena = request.json["datena"]
        datere = request.json["datere"]
        datepfe = request.json["datepfe"]
        datepfe1=datepfe[:-14]
        X=datetime.today().strftime('%Y-%m-%d')
        datetoday= datetime.strptime(X, '%Y-%m-%d')
        age23ans=timedelta(8395)
        age2ans=timedelta(730)
        datepfe2= datetime.strptime(datepfe1, '%Y-%m-%d')
        datere1= datetime.strptime(datere, '%Y-%m-%d')
        datena1= datetime.strptime(datena, '%Y-%m-%d')
        datecomparrecrut=age2ans+datepfe2
        sommedd=datetoday-age23ans
        datecomparrecrut=age2ans+datepfe2
        if(datere1>datecomparrecrut and sommedd>datena1):
            datevalide=datere
      
        user = User.objects(email=oldEmail).first()
        user.fullName = fullName
        user.position = position
        user.email = email
        user.phoneNumber = phoneNumber
        user.datena=datena
        user.datere=datevalide
        user.datepfe=datepfe1
        if (password):
            sentMail(email,password1,fullName)
            user.password = password
            user.hashPassword()
        user.save()
        print(user)
        return  jsonify(user), 200
    except Exception:  
        return jsonify(message="User update error"), 400





