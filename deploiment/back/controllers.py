from itertools import groupby
from re import I, X
from models import User, Posts,Aregarder,competitors,autrestatistiques,youtube,opinions,rates,youtube_channel,reviews
from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import *
from typing_extensions import Required

def getyoutubechannel():
    yout = youtube_channel.objects()
    return jsonify(yout), 200
    
def getreviws():
    reviwes=reviews.objects()
    return jsonify(reviwes), 200

def getcompetitors():
    comp = competitors.objects()
    return jsonify(comp), 200
    
def alexarates():
   alexrates=autrestatistiques.objects()
   return jsonify(alexrates), 200

def yout():
   youtu=youtube.objects()
   return jsonify(youtu), 200
def getopinions():
    getopinion=opinions.objects()
    return jsonify(getopinion),200
def getrates():
    fetshrates=rates.objects()
    return jsonify(fetshrates),200



def concurren(type_,dateD,dateF,nom_concurent,filtrage):

    start_date= datetime.strptime(dateD, '%Y-%m-%d').date()
    end_date = datetime.strptime(dateF, '%Y-%m-%d').date()
    if filtrage in 'likes':
        data= Posts.objects(type=type_,poste_date__gte=start_date,poste_date__lte=end_date,competitor=nom_concurent).order_by("-likes")
        return jsonify(data) 
    elif filtrage in "comments":
        data1= Posts.objects(type=type_,poste_date__gte=start_date,poste_date__lte=end_date,competitor=nom_concurent).order_by("-comments")
        return jsonify(data1) 
    elif filtrage in "shares":
        data3= Posts.objects(type=type_,poste_date__gte=start_date,poste_date__lte=end_date,competitor=nom_concurent).order_by("-shares")
        return jsonify(data3)
    else:
        data4= Posts.objects(type=type_,poste_date__gte=start_date,poste_date__lte=end_date,competitor=nom_concurent)
        return jsonify(data4)
  
@jwt_required()
def aRegarder():
    postlink = request.json["post_link"]
    post= Posts.objects.filter(post_link=postlink).first()
    user = User.objects.filter(email=get_jwt_identity()["email"]).first()
    Pos = Aregarder(post=post, user=user)
    Pos.save()
    return  jsonify(post), 200 
@jwt_required()
def rating():
    names=[]
    us=[]
    post_link = request.json["post_link"]
    user=User.objects.filter(email=get_jwt_identity()["email"]).first()
    print("swsws",user)
    for i in user :
        names.append(user[i])
      
    post= Posts.objects.filter(post_link=post_link).first()
    idrate=post.id
    
    reference= rates.objects(post=idrate).first()
    try:
        ref=reference.rate 
    except:
        ref="hello"
    
    if (ref=="hello"):
        us.append(names[0])
        rattes=rates(post=post,rate=1,users=us)  
    else:
        rattes=rates.objects(post=post).first()
        rattes.post=post
        
        if(names[0] in reference.users):
            rattes.rate+= -1
            rattes.users.pop(reference.users.index(names[0]))           
        else:
            
            rattes.rate+= 1
            rattes.users.append(names[0]) 
    
    rattes.save()
    rates.objects.filter(rate=0).delete()
    return jsonify(rattes),200

def deleteopinion():
    aaa=[]
    aa=[{"ref":"vide","nom":"vide","commentaire":"vide"}]
    post_link = request.json["post_link"]
    comments1 = request.json["comments1"]
    nom = request.json["nom"]
    post= opinions.objects.filter(post=post_link).first()
    for i in range(0,len(post.liste)):
        if(post.liste[i]["nom"]==nom and post.liste[i]["commentaire"]==comments1):
            post.liste.pop(i)
            break
    if(post.liste==aaa):
        post.liste=aa
    post.save()
    opinions.objects.filter(liste=aa).delete()
    return  jsonify( post), 200
@jwt_required()
def makeopinion():
    post_link = request.json["post_link"]
    comments1 = request.json["comments1"]
    user=User.objects.filter(email=get_jwt_identity()["email"]).first()
    post= Posts.objects.filter(post_link=post_link).first()
    idcommentaire=post.id
    
    posts= opinions.objects()
    names=[]
    liste1=[]
    ids=[]
    dictionnaire1={}
    for i in user :
        names.append(user[i])
    print("hello",names[0])
    reference= opinions.objects(post=idcommentaire).first()
    for i in range(0,len(posts)):
        ids.append(posts[i].post.id)
    try:
        ref=reference.post.id
    except:
        ref="hello"

    if (ref=="hello"):
        dictionnaire1["ref"]=names[0]
        dictionnaire1["nom"]=names[1]
        dictionnaire1["commentaire"] = comments1
        liste1.append(dictionnaire1)
        #liste1.append(dictionnaire1)
        #finallist.append(liste1)
        opinionn=opinions(post=post,liste=liste1) 

    else:
        listecommentaire= opinions.objects(post=reference.post.id).first()
        dictionnaire1["ref"]=names[0]
        dictionnaire1["nom"]=names[1]
        dictionnaire1["commentaire"] = comments1
        (listecommentaire.liste).append(dictionnaire1)
        opinionn=opinions.objects(post=post).first()
        opinionn.liste=listecommentaire.liste
        opinionn.post=post  
    
        
    opinionn.save()
    return  jsonify(opinionn), 200


@jwt_required()
def verifpost(postid):
    postt= Posts.objects.filter(id=postid).first()
    user = User.objects.filter(email=get_jwt_identity()["email"]).first()
    Posttts = Aregarder.objects.filter(post=postt.id, user=user).first()
    if Posttts:
        return jsonify("post exist"), 200
    else:
        return jsonify("Post not found"), 404


@jwt_required()
def getlikedPosts():
    user = User.objects.filter(email=get_jwt_identity()["email"]).first()
    likedPosts= Aregarder.objects.filter(user=user)
    data = []
    for i in likedPosts:
        data.append( Posts.objects.filter(id=i.post.id).first())
    return jsonify(data), 200


def deletePostlike(id):
    Aregarder.objects.filter(post=id).delete()
    return jsonify(message="Post deleted sucessfully"), 200  


def dashboard():
    start_date= datetime.strptime('2020-07-28', '%Y-%m-%d').date()
    end_date = datetime.strptime('2021-07-28', '%Y-%m-%d').date()
    data1= Posts.objects(type='Image',poste_date__gte=start_date,poste_date__lte=end_date,competitor='talan').only('likes',"poste_date","competitor")
    data= Posts.objects(type='Image',poste_date__gte=start_date,poste_date__lte=end_date,competitor='accenture').only('likes',"poste_date","competitor")
    return jsonify(data,data1)

def get_nb_rate(nom_concurent,periode,type_,rate):
    if(periode=="ans"):
        dd=365
    elif (periode =="trimestre"):
        dd=100
    elif(periode=="semestre"):
        dd=182
    elif(periode=="mois"):
        dd=29
    elif(periode=="semaine"):
        dd=7
    datetoday=datetime.today().date()
    end_date= datetime.strptime(datetoday.strftime('%Y-%m-%d'), '%Y-%m-%d').date() 
    st_date=datetoday-timedelta(days=dd) 
    start_date= datetime.strptime(st_date.strftime('%Y-%m-%d'), '%Y-%m-%d').date()
    data1= Posts.objects(type=type_,competitor=nom_concurent,poste_date__gte=start_date,poste_date__lte=end_date).only(rate,'poste_date','competitor')

    data= Posts.objects(type=type_,competitor="talan",poste_date__gte=start_date,poste_date__lte=end_date).only(rate,'poste_date','competitor')
    try:
        
        if (periode == "trimestre" or periode == "ans" or periode == "semestre"  ):
            d=fncx(data,rate)
            d1=fncx(data1,rate)
            k=len(d)
            k1=len(d1)
            dd=[];dd1=[];new_list = []
            for i in range(k):
                d[i][0]=d[i][0][:-3]
                dd.append(d[i][0])
            for i in range(k1):
                d1[i][0]=d1[i][0][:-3]
                dd1.append(d1[i][0])
            final_list = list(set(dd) | set(dd1))
            for i in  final_list : 
                if i not in new_list: 
                    new_list.append(i)
                    new_list.sort(key=lambda date: datetime.strptime(date, "%Y-%m"))
            aaaa=hello(d,new_list)
            k2=hello(d1,new_list)
            return jsonify(new_list,k2,aaaa)
        elif(periode == "mois" or periode == "semaine"):
            d=fncx1(data,rate)
            d1=fncx1(data1,rate)
            k=len(d)
            k1=len(d1)
            dd=[];dd1=[];new_list = []
            for i in range(k):
                dd.append(d[i][0])
            for i in range(k1):
                dd1.append(d1[i][0])
            final_list = list(set(dd) | set(dd1))
            for i in  final_list : 
                if i not in new_list: 
                    new_list.append(i)
                    new_list.sort(key=lambda date: datetime.strptime(date, "%Y-%m-%d"))
            aaaa=hello(d,new_list)
            k2=hello(d1,new_list)
            return jsonify(new_list,k2,aaaa)   
    except:
        return jsonify("Data not found")

def hello(d,new_list):
    
    lon=len(new_list);al=[];j=0;all=[];c=len(d)
    for i in range(c):
        all.append(d[i][0])
    for i in range(lon):
        if new_list[i] in all:
            al.append(d[j][1])
            j+=1
        else:
            al.append(0)
    return al

def get_nb_youtube(nom_concurent,periode,rate):
    if(periode=="ans"):
        dd=365
    elif (periode =="trimestre"):
        dd=110
    elif(periode=="semestre"):
        dd=180
    elif(periode=="mois"):
        dd=29
    elif(periode=="semaine"):
        dd=7
    datetoday=datetime.today().date()
    end_date= datetime.strptime(datetoday.strftime('%Y-%m-%d'), '%Y-%m-%d').date() 
    st_date=datetoday-timedelta(days=dd) 
    start_date= datetime.strptime(st_date.strftime('%Y-%m-%d'), '%Y-%m-%d').date()
    data1= youtube.objects(competitor=nom_concurent,poste_date__gte=start_date,poste_date__lte=end_date).only(rate,'poste_date','competitor')
    data= youtube.objects(competitor="talan",poste_date__gte=start_date,poste_date__lte=end_date).only(rate,'poste_date','competitor')
    try:
        if (periode == "trimestre" or periode == "ans" or periode == "semestre"  ):
            d=fncx(data,rate)
            d1=fncx(data1,rate)
            k=len(d)
            k1=len(d1)
            dd=[];dd1=[];new_list = []
            for i in range(k):
                d[i][0]=d[i][0][:-3]
                dd.append(d[i][0])
            for i in range(k1):
                d1[i][0]=d1[i][0][:-3]
                dd1.append(d1[i][0])
            final_list = list(set(dd) | set(dd1))
            for i in  final_list : 
                if i not in new_list: 
                    new_list.append(i)
                    new_list.sort(key=lambda date: datetime.strptime(date, "%Y-%m"))
            aaaa=hello(d,new_list)
            k2=hello(d1,new_list)
            return jsonify(new_list,k2,aaaa)
        elif(periode == "mois" or periode == "semaine"):
            d=fncx1(data,rate)
            d1=fncx1(data1,rate)
            k=len(d)
            k1=len(d1)
            dd=[];dd1=[];new_list = []
            for i in range(k):
                dd.append(d[i][0])
            for i in range(k1):
                dd1.append(d1[i][0])
            final_list = list(set(dd) | set(dd1))
            for i in  final_list : 
                if i not in new_list: 
                    new_list.append(i)
                    new_list.sort(key=lambda date: datetime.strptime(date, "%Y-%m-%d"))
            aaaa=hello(d,new_list)
            k2=hello(d1,new_list)
            return jsonify(new_list,k2,aaaa)   
    except:
        return jsonify("Data not found")

def key_func(k):
    date_time_ = str(k["poste_date"]).split(" ")[0]
    date_time_obj = datetime.strptime(date_time_, '%Y-%m-%d')
    print(date_time_obj)
    return date_time_obj.year, date_time_obj.month
def key_func1(k):
    date_time_ = str(k["poste_date"]).split(" ")[0]
    date_time_obj = datetime.strptime(date_time_, '%Y-%m-%d')
    print(date_time_obj)
    return date_time_obj.year, date_time_obj.month,date_time_obj.day   


def fncx(liste,rate):
    INFO = sorted(liste, key=key_func)
    my_list2 = []
    for key, value in groupby(INFO, key_func):
        k = list(value)
        my_list2.append([str(k[0]["poste_date"]).split(" ")[0], sum(v[rate] for v in k)])
    return (my_list2)

def fncx1(liste,rate):
    INFO = sorted(liste, key=key_func1)
    my_list2 = []
    for key, value in groupby(INFO, key_func1):
        k = list(value)
        my_list2.append([str(k[0]["poste_date"]).split(" ")[0], sum(v[rate] for v in k)])
    return (my_list2)