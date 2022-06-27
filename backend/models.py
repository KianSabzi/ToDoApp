import datetime
import enum
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_enum import EnumField


db = SQLAlchemy()

ma = Marshmallow()


def init_app(app):
    db.app = app
    db.init_app(app)
    return db


def create_tables(app):
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    db.metadata.create_all(engine)
    return engine


class priorityType(str,enum.Enum):
    Urgent: str = 'Urgent'
    Normal: str = 'Normal'
    Smooth: str = 'Smooth'


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(250), nullable=False)
    desc = db.Column(db.UnicodeText(450))
    dateAdded = db.Column(db.DateTime, nullable=False,
                          default=datetime.datetime.now)
    status = db.Column(db.Boolean)
    notificationDone = db.Column(db.Boolean)
    notifDate = db.Column(db.DateTime)
    priority = db.Column(db.Enum(priorityType,values_callable=lambda x: [str(member.name) for member in priorityType]))
    isDone = db.Column(db.Boolean)
    marked = db.Column(db.Boolean)
    category_id = db.Column(db.Integer, db.ForeignKey(
        'category.id'), nullable=False)
    category = db.relationship(
        'Category', backref=db.backref('task', lazy=True))

    def __repr__(self):
        return '<Task %r>' % (self.title)

    def __init__(self, title, desc,dateAdded,status,priority,category_id):
        self.title = title
        self.desc = desc
        self.dateAdded = dateAdded
        self.status = status
        self.priority = priority
        self.category_id = category_id

        # self.notifDate = notifDate
        # self.notificationDone = notificationDone
        # self.isDone = isDone
        # self.marked = marked


class TaskSchema(ma.Schema):
    class Meta:
        # model = Task
        # id = ma.auto_field(data_key='id', required=True)
        # title = ma.auto_field(data_key='title', required=True)
        # desc = ma.auto_field(data_key='desc')
        # dateAdded = ma.auto_field(data_key='dateAdded', required=True)
        # status = ma.auto_field(data_key='status')
        # notification = ma.auto_field(data_key='notification')
        # notifDate = ma.auto_field(data_key='notifDate')
        # isDone = ma.auto_field(data_key='isDone')
        # category_id = ma.auto_field(data_key = 'category_id' , required=True)

        fields = ("id", "title", "desc", "dateAdded", "status",
                  "notification" , "notifDate", "isDone", "priority","category_id")
        # priority = EnumField(priorityType,values_callable=lambda x: [str(member.value) for member in priorityType])


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
   

    def __repr__(self):
        return '<Category %r>' % (self.name)

    def __init__(self, name):
        self.name = name


class CategorySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)