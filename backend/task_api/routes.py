
# from models import db, Task, Category
import datetime
from xmlrpc.client import DateTime
from flask import jsonify,request
from backend.models import Task, db ,task_schema,tasks_schema
from . import task_api_blueprint


@task_api_blueprint.route('/api/tasks', methods=['GET'])
def get_tasks():
    all_tasks = Task.query.all()
    results = tasks_schema.dump(all_tasks)
    return jsonify(results)

@task_api_blueprint.route('/api/category_tasks/<cat_id>/', methods=['GET'])
def get_category_tasks(cat_id):
    category_tasks = Task.query.filter(Task.category_id == cat_id)
    results = tasks_schema.dump(category_tasks)
    return jsonify(results)

@task_api_blueprint.route('/api/addtask', methods=['POST'])
def add_task():
    title = request.json['title']
    desc = request.json['desc']
    status = request.json['status']
    dateAdded = datetime.datetime.now()
    priority = request.json['priority']
    category_id = request.json['category_id']
    

    task = Task(title,desc,dateAdded,status,priority,category_id)
    db.session.add(task)
    db.session.commit() 
    return task_schema.jsonify(task)

@task_api_blueprint.route('/api/updatetask/<id>/', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)

    title = request.json['title']
    desc = request.json['desc']
    # status = request.json['status']
    # notificationDone = request.json['notificationDone']
    # notificationDate = request.json['notificationDate']
    # isDone = request.json['isDone']
    # marked = request.json['marked']
    category_id = request.json['category_id']
    
    task.title = title
    task.desc = desc
    # task.status = status
    # task.notificationDone = notificationDone
    # task.notifDate = notificationDate
    # task.isDone = isDone
    # task.marked = marked
    task.category_id = category_id
    
    db.session.commit() 
    return task_schema.jsonify(task)

@task_api_blueprint.route('/api/deletetask/<id>/', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)

    db.session.delete(task)
    db.session.commit()

    all_tasks = Task.query.all()
    results = tasks_schema.dump(all_tasks)
    return jsonify(results)

@task_api_blueprint.route('/api/insertnotif/<id>/', methods=['PUT'])
def insert_notif(id):
    task = Task.query.get(id)
    if(not task.notificationDone):
        notificationDone = request.json['notificationDone']
    
    notificationDate = request.json['notificationDate']

    task.notificationDone = notificationDone
    task.notifDate = notificationDate

    db.session.commit()
    return task_schema.jsonify(task)

@task_api_blueprint.route('/api/checknotif/<id>/', methods=['PUT'])
def check_notif(id):
    task = Task.query.get(id)

    if(task.notificationDate == datetime.datetime.now()):
        task.notificationDone = False

    db.session.commit()
    return task_schema.jsonify(task)

@task_api_blueprint.route('/api/completetask/<id>/', methods=['PUT'])
def complete_task(id):
    task = Task.query.get(id)

    isDone = request.json['isDone']
    task.isDone = isDone

    db.session.commit()
    return task_schema.jsonify(task) 

@task_api_blueprint.route('/api/archivetask/<id>/', methods=['PUT'])
def archive_task(id):
    task = Task.query.get(id)

    status = request.json['status']
    task.status = status

    db.session.commit()
    return task_schema.jsonify(task)


@task_api_blueprint.route('/api/marktask/<id>/', methods=['PUT'])
def mark_task(id):
    task = Task.query.get(id)

    mark = request.json['mark']
    task.mark = mark

    db.session.commit()
    return task_schema.jsonify(task)
    