from typing_extensions import Required
import bcrypt
from enum import Enum, unique
import mongoengine
from flask import session
from mongoengine.errors import ValidationError

class RoleEnum(Enum):
    ADMIN = "a"
    USER = "u"

class User(mongoengine.Document):

    fullName = mongoengine.StringField(required=True)
    position = mongoengine.StringField(required=True)
    email = mongoengine.EmailField(required=True, unique=True)
    password = mongoengine.StringField(required=True)
    phoneNumber = mongoengine.StringField(required=True)
    role = mongoengine.EnumField(RoleEnum, default=RoleEnum.USER)

    def hashPassword(self):
        self.password = bcrypt.hashpw(
            self.password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")

    def passwordIsCorrect(self, password):
        print(self.password)
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))


class Posts(mongoengine.Document):
    poste_date= mongoengine.DateTimeField(required=True)
    post_text= mongoengine.StringField(required=True)
    likes= mongoengine.IntField(required=True)
    comments= mongoengine.IntField(required=True)
    shares= mongoengine.IntField(required=True)
    post_link= mongoengine.StringField(required=True)
    type= mongoengine.StringField(required=True)
    competitor=mongoengine.StringField(required=True)


class autrestatistiques(mongoengine.Document):
    competitor=mongoengine.StringField(required=True)
    daily_page_views_per_visitors=mongoengine.StringField(required=True)
    daily_time_on_sites=mongoengine.StringField(required=True)
    bounce_rates=mongoengine.StringField(required=True)
class youtube(mongoengine.Document):
    competitor=mongoengine.StringField(required=True)
    poste_date=mongoengine.DateTimeField(required=True)
    viewCount=mongoengine.IntField(required=True)
    likeCount=mongoengine.IntField(required=True)





class competitors(mongoengine.Document):
    link_Site_web= mongoengine.StringField(required=True)
    Sector= mongoengine.StringField(required=True)
    HeadOffice= mongoengine.StringField(required=True)
    foundingDate= mongoengine.StringField(required=True)
    Specializations= mongoengine.StringField(required=True)
    employees= mongoengine.IntField(required=True)
    subscribers= mongoengine.IntField(required=True)
    competitor=mongoengine.StringField(required=True, unique=True)
    link_logo=mongoengine.StringField(required=True)

class Aregarder(mongoengine.Document):
    user = mongoengine.ReferenceField(User)
    post = mongoengine.ReferenceField( Posts)

class opinions(mongoengine.Document):
    post = mongoengine.ReferenceField( Posts)
    liste=mongoengine.ListField(mongoengine.DictField(comments1=mongoengine.StringField(required=True),nom=mongoengine.StringField(required=True),ref = mongoengine.ReferenceField(User)))



class rates(mongoengine.Document):
    post = mongoengine.ReferenceField(Posts)
    rate=mongoengine.IntField(required=True)
    users=mongoengine.ListField()

class youtube_channel(mongoengine.Document):
    competitor=mongoengine.StringField(required=True)
    viewCount=mongoengine.IntField(required=True)
    subscriberCount=mongoengine.IntField(required=True)
    videoCount=mongoengine.IntField(required=True)

class reviews(mongoengine.Document):
    competitor=mongoengine.StringField(required=True)
    positive=mongoengine.FloatField(required=True)
    negative=mongoengine.FloatField(required=True)
