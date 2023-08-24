from flask import Blueprint
from controllers import getcompetitors,aRegarder,getlikedPosts,getreviws,deletePostlike,verifpost,dashboard,concurren,get_nb_rate,alexarates,yout,get_nb_youtube,makeopinion,getopinions,rating,getrates,deleteopinion,getyoutubechannel#,deleteuserrates,
from flask_jwt_extended import jwt_required
user_bp = Blueprint("home_bp", __name__)
user_bp.route("/youtubchannel", methods=["GET"])(getyoutubechannel)
user_bp.route("/competit", methods=["GET"])(getcompetitors)
user_bp.route("/getopinion", methods=["GET"])(getopinions)
user_bp.route("/getrates", methods=["GET"])(getrates)
user_bp.route("/alxa", methods=["GET"])(alexarates)
user_bp.route("/al", methods=["GET"])(yout)
user_bp.route("/reviws", methods=["GET"])(getreviws)
user_bp.route("/compt/<type_>/<dateD>/<dateF>/<nom_concurent>/<filtrage>", methods=["GET"])(concurren)
user_bp.route("/nb/<nom_concurent>/<periode>/<type_>/<rate>", methods=["GET"])(get_nb_rate)
user_bp.route("/nn/<nom_concurent>/<periode>/<rate>", methods=["GET"])(get_nb_youtube)
user_bp.route("/dashboard", methods=["GET"])(dashboard)
# user_bp.route("/deluserrat", methods=["put"])(deleteuserrates)
user_bp.route("/regarder",methods=["POST"])(aRegarder)
user_bp.route("/deleteopinion",methods=["put"])(deleteopinion)
user_bp.route("/opinion",methods=["put"])(makeopinion)
user_bp.route("/rate",methods=["put"])(rating)
user_bp.route("/verif/<postid>",methods=["GET"])(verifpost)
user_bp.route("/likeposts",methods=["GET"])(getlikedPosts)
user_bp.route("/deletePostlike/<id>", methods=["DELETE"])(deletePostlike) 







