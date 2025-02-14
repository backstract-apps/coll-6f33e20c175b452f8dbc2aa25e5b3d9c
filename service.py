from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_teams(db: Session):

    teams_all = db.query(models.Teams).all()
    teams_all = [new_data.to_dict() for new_data in teams_all] if teams_all else teams_all

    res = {
        'teams_all': teams_all,
    }
    return res

async def get_teams_id(db: Session, id: int):

    teams_one = db.query(models.Teams).filter(models.Teams.id == id).first() 
    teams_one = teams_one.to_dict() if teams_one else teams_one

    res = {
        'teams_one': teams_one,
    }
    return res

async def post_teams(db: Session, raw_data: schemas.PostTeams):
    id:str = raw_data.id
    name:str = raw_data.name
    owner_id:str = raw_data.owner_id
    created_at:str = raw_data.created_at


    record_to_be_added = {'id': id, 'name': name, 'owner_id': owner_id, 'created_at': created_at}
    new_teams = models.Teams(**record_to_be_added)
    db.add(new_teams)
    db.commit()
    db.refresh(new_teams)
    teams_inserted_record = new_teams.to_dict()

    res = {
        'teams_inserted_record': teams_inserted_record,
    }
    return res

async def put_teams_id(db: Session, raw_data: schemas.PutTeamsId):
    id:str = raw_data.id
    name:str = raw_data.name
    owner_id:str = raw_data.owner_id
    created_at:str = raw_data.created_at


    teams_edited_record = db.query(models.Teams).filter(models.Teams.id == id).first()
    for key, value in {'id': id, 'name': name, 'owner_id': owner_id, 'created_at': created_at}.items():
          setattr(teams_edited_record, key, value)
    db.commit()
    db.refresh(teams_edited_record)
    teams_edited_record = teams_edited_record.to_dict() 

    res = {
        'teams_edited_record': teams_edited_record,
    }
    return res

async def delete_teams_id(db: Session, id: int):

    teams_deleted = None
    record_to_delete = db.query(models.Teams).filter(models.Teams.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        teams_deleted = record_to_delete.to_dict() 

    res = {
        'teams_deleted': teams_deleted,
    }
    return res

async def get_team_members(db: Session):

    team_members_all = db.query(models.TeamMembers).all()
    team_members_all = [new_data.to_dict() for new_data in team_members_all] if team_members_all else team_members_all

    res = {
        'team_members_all': team_members_all,
    }
    return res

async def get_team_members_id(db: Session, id: int):

    team_members_one = db.query(models.TeamMembers).filter(models.TeamMembers.id == id).first() 
    team_members_one = team_members_one.to_dict() if team_members_one else team_members_one

    res = {
        'team_members_one': team_members_one,
    }
    return res

async def post_team_members(db: Session, raw_data: schemas.PostTeamMembers):
    id:str = raw_data.id
    team_id:str = raw_data.team_id
    user_id:str = raw_data.user_id
    added_at:str = raw_data.added_at


    record_to_be_added = {'id': id, 'team_id': team_id, 'user_id': user_id, 'added_at': added_at}
    new_team_members = models.TeamMembers(**record_to_be_added)
    db.add(new_team_members)
    db.commit()
    db.refresh(new_team_members)
    team_members_inserted_record = new_team_members.to_dict()

    res = {
        'team_members_inserted_record': team_members_inserted_record,
    }
    return res

async def put_team_members_id(db: Session, raw_data: schemas.PutTeamMembersId):
    id:str = raw_data.id
    team_id:str = raw_data.team_id
    user_id:str = raw_data.user_id
    added_at:str = raw_data.added_at


    team_members_edited_record = db.query(models.TeamMembers).filter(models.TeamMembers.id == id).first()
    for key, value in {'id': id, 'team_id': team_id, 'user_id': user_id, 'added_at': added_at}.items():
          setattr(team_members_edited_record, key, value)
    db.commit()
    db.refresh(team_members_edited_record)
    team_members_edited_record = team_members_edited_record.to_dict() 

    res = {
        'team_members_edited_record': team_members_edited_record,
    }
    return res

async def delete_team_members_id(db: Session, id: int):

    team_members_deleted = None
    record_to_delete = db.query(models.TeamMembers).filter(models.TeamMembers.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        team_members_deleted = record_to_delete.to_dict() 

    res = {
        'team_members_deleted': team_members_deleted,
    }
    return res

async def get_tasks(db: Session):

    tasks_all = db.query(models.Tasks).all()
    tasks_all = [new_data.to_dict() for new_data in tasks_all] if tasks_all else tasks_all

    res = {
        'tasks_all': tasks_all,
    }
    return res

async def get_tasks_id(db: Session, id: int):

    tasks_one = db.query(models.Tasks).filter(models.Tasks.id == id).first() 
    tasks_one = tasks_one.to_dict() if tasks_one else tasks_one

    res = {
        'tasks_one': tasks_one,
    }
    return res

async def post_tasks(db: Session, raw_data: schemas.PostTasks):
    title:str = raw_data.title
    description:str = raw_data.description
    status:str = raw_data.status
    priority:str = raw_data.priority
    visibility:str = raw_data.visibility
    user_id:int = raw_data.user_id


    import uuid
    from datetime import datetime

    try:
        created_at:datetime = datetime.now()
        id = int(uuid.uuid4().int % 1000000)
    except Exception as e:
        raise HTTPException(500, str(e))



    record_to_be_added = {'created_by': user_id, 'visibility': visibility, 'priority': priority, 'status': status, 'description': description, 'title': title, 'id': id, 'created_at': created_at}
    new_tasks = models.Tasks(**record_to_be_added)
    db.add(new_tasks)
    db.commit()
    db.refresh(new_tasks)
    taskAdded = new_tasks.to_dict()

    res = {
        'tasks_inserted_record': created_at,
    }
    return res

async def put_tasks_id(db: Session, raw_data: schemas.PutTasksId):
    id:str = raw_data.id
    title:str = raw_data.title
    description:str = raw_data.description
    status:str = raw_data.status
    priority:str = raw_data.priority
    visibility:str = raw_data.visibility
    created_by:str = raw_data.created_by
    assigned_to:str = raw_data.assigned_to
    team_id:str = raw_data.team_id
    created_at:str = raw_data.created_at


    tasks_edited_record = db.query(models.Tasks).filter(models.Tasks.id == id).first()
    for key, value in {'id': id, 'title': title, 'description': description, 'status': status, 'priority': priority, 'visibility': visibility, 'created_by': created_by, 'assigned_to': assigned_to, 'team_id': team_id, 'created_at': created_at}.items():
          setattr(tasks_edited_record, key, value)
    db.commit()
    db.refresh(tasks_edited_record)
    tasks_edited_record = tasks_edited_record.to_dict() 

    res = {
        'tasks_edited_record': tasks_edited_record,
    }
    return res

async def delete_tasks_id(db: Session, id: int):

    tasks_deleted = None
    record_to_delete = db.query(models.Tasks).filter(models.Tasks.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        tasks_deleted = record_to_delete.to_dict() 

    res = {
        'tasks_deleted': tasks_deleted,
    }
    return res

async def get_task_activity(db: Session):

    task_activity_all = db.query(models.TaskActivity).all()
    task_activity_all = [new_data.to_dict() for new_data in task_activity_all] if task_activity_all else task_activity_all

    res = {
        'task_activity_all': task_activity_all,
    }
    return res

async def get_task_activity_id(db: Session, id: int):

    task_activity_one = db.query(models.TaskActivity).filter(models.TaskActivity.id == id).first() 
    task_activity_one = task_activity_one.to_dict() if task_activity_one else task_activity_one

    res = {
        'task_activity_one': task_activity_one,
    }
    return res

async def post_task_activity(db: Session, raw_data: schemas.PostTaskActivity):
    id:str = raw_data.id
    task_id:str = raw_data.task_id
    updated_by:str = raw_data.updated_by
    action:str = raw_data.action
    timestamp:str = raw_data.timestamp


    record_to_be_added = {'id': id, 'task_id': task_id, 'updated_by': updated_by, 'action': action, 'timestamp': timestamp}
    new_task_activity = models.TaskActivity(**record_to_be_added)
    db.add(new_task_activity)
    db.commit()
    db.refresh(new_task_activity)
    task_activity_inserted_record = new_task_activity.to_dict()

    res = {
        'task_activity_inserted_record': task_activity_inserted_record,
    }
    return res

async def put_task_activity_id(db: Session, raw_data: schemas.PutTaskActivityId):
    id:str = raw_data.id
    task_id:str = raw_data.task_id
    updated_by:str = raw_data.updated_by
    action:str = raw_data.action
    timestamp:str = raw_data.timestamp


    task_activity_edited_record = db.query(models.TaskActivity).filter(models.TaskActivity.id == id).first()
    for key, value in {'id': id, 'task_id': task_id, 'updated_by': updated_by, 'action': action, 'timestamp': timestamp}.items():
          setattr(task_activity_edited_record, key, value)
    db.commit()
    db.refresh(task_activity_edited_record)
    task_activity_edited_record = task_activity_edited_record.to_dict() 

    res = {
        'task_activity_edited_record': task_activity_edited_record,
    }
    return res

async def delete_task_activity_id(db: Session, id: int):

    task_activity_deleted = None
    record_to_delete = db.query(models.TaskActivity).filter(models.TaskActivity.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        task_activity_deleted = record_to_delete.to_dict() 

    res = {
        'task_activity_deleted': task_activity_deleted,
    }
    return res

async def get_bs_users(db: Session):

    bs_users_all = db.query(models.BsUsers).all()
    bs_users_all = [new_data.to_dict() for new_data in bs_users_all] if bs_users_all else bs_users_all

    res = {
        'bs_users_all': bs_users_all,
    }
    return res

async def get_bs_users_id(db: Session, id: int, email: str, password: str):

    bs_users_one = db.query(models.BsUsers).filter(models.BsUsers.id == id).first() 
    bs_users_one = bs_users_one.to_dict() if bs_users_one else bs_users_one

    res = {
        'bs_users_one': bs_users_one,
    }
    return res

async def post_bs_users(db: Session, raw_data: schemas.PostBsUsers):
    email:str = raw_data.email
    password:str = raw_data.password
    name:str = raw_data.name


    import uuid
    from datetime import datetime

    try:
        id = int(uuid.uuid4().int % (10**10))
        created_at:datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    record_to_be_added = {'id': id, 'created_at': created_at, 'email': email, 'password': password, 'name': name}
    new_bs_users = models.BsUsers(**record_to_be_added)
    db.add(new_bs_users)
    db.commit()
    db.refresh(new_bs_users)
    userdata = new_bs_users.to_dict()

    res = {
        'bs_users_inserted_record': email,
    }
    return res

async def put_bs_users_id(db: Session, raw_data: schemas.PutBsUsersId):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    email:str = raw_data.email
    password:str = raw_data.password
    name:str = raw_data.name


    bs_users_edited_record = db.query(models.BsUsers).filter(models.BsUsers.id == id).first()
    for key, value in {'id': id, 'created_at': created_at, 'email': email, 'password': password, 'name': name}.items():
          setattr(bs_users_edited_record, key, value)
    db.commit()
    db.refresh(bs_users_edited_record)
    bs_users_edited_record = bs_users_edited_record.to_dict() 

    res = {
        'bs_users_edited_record': bs_users_edited_record,
    }
    return res

async def delete_bs_users_id(db: Session, id: int):

    bs_users_deleted = None
    record_to_delete = db.query(models.BsUsers).filter(models.BsUsers.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        bs_users_deleted = record_to_delete.to_dict() 

    res = {
        'bs_users_deleted': bs_users_deleted,
    }
    return res

async def post_signin(db: Session, raw_data: schemas.PostSignin):
    email:str = raw_data.email
    password:str = raw_data.password



    query = db.query(models.BsUsers)
    query = query.filter(
        
        and_(
            models.BsUsers.email == email,
            models.BsUsers.password == password
        )
    )


    userdata = query.all()
    userdata = [new_data.to_dict() for new_data in userdata] if userdata else userdata


    
    from fastapi import HTTPException

    try:
        user_info = next((user for user in userdata if user["email"] == email and user["password"] == password), None)
        
        if not user_info:
            raise HTTPException(status_code=400, detail="You entered invalid credentials.")  # Raises HTTP 400 Bad Request
    except Exception as e:
        raise HTTPException(500, str(e))


    res = {
        'output': userdata,
    }
    return res

