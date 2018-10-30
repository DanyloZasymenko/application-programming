import enum
from datetime import datetime

from flask_login import UserMixin

from lab_3.internet_store import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class UsersGoods(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    good_id = db.Column(db.Integer, db.ForeignKey('good.id'), primary_key=True)
    number = db.Column(db.Integer, default=1)

    def __repr__(self):
        return f"UsersGoods('{self.user_id}', '{self.good_id}', '{self.number}')"


class Roles(enum.Enum):
    USER = 'User'
    ADMIN = 'Admin'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    role = db.Column(db.Enum(Roles), default=Roles.USER)
    stock = db.relationship('UsersGoods', backref='user',
                            primaryjoin=id == UsersGoods.user_id, cascade='all, delete')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Good(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    producer = db.Column(db.String(30), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default-product.jpg')
    number_available = db.Column(db.Integer, nullable=False, default=0)
    stock = db.relationship('UsersGoods', backref='good',
                            primaryjoin=id == UsersGoods.good_id, cascade='all, delete')

    def __repr__(self):
        return f"Good('{self.name}', '{self.producer}', '{self.date_posted}', '{self.number_available}')"
