from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Teams(BaseModel):
    id: int
    name: str
    owner_id: int
    created_at: datetime.time


class ReadTeams(BaseModel):
    id: int
    name: str
    owner_id: int
    created_at: datetime.time
    class Config:
        from_attributes = True


class TeamMembers(BaseModel):
    id: int
    team_id: int
    user_id: int
    added_at: datetime.time


class ReadTeamMembers(BaseModel):
    id: int
    team_id: int
    user_id: int
    added_at: datetime.time
    class Config:
        from_attributes = True


class Tasks(BaseModel):
    id: int
    title: str
    description: str
    status: str
    priority: str
    visibility: str
    created_by: int
    assigned_to: int
    team_id: int
    created_at: datetime.time


class ReadTasks(BaseModel):
    id: int
    title: str
    description: str
    status: str
    priority: str
    visibility: str
    created_by: int
    assigned_to: int
    team_id: int
    created_at: datetime.time
    class Config:
        from_attributes = True


class TaskActivity(BaseModel):
    id: int
    task_id: int
    updated_by: int
    action: str
    timestamp: datetime.time


class ReadTaskActivity(BaseModel):
    id: int
    task_id: int
    updated_by: int
    action: str
    timestamp: datetime.time
    class Config:
        from_attributes = True


class BsUsers(BaseModel):
    id: int
    created_at: datetime.time
    email: str
    password: str
    name: str


class ReadBsUsers(BaseModel):
    id: int
    created_at: datetime.time
    email: str
    password: str
    name: str
    class Config:
        from_attributes = True




class PostTeams(BaseModel):
    id: str
    name: str
    owner_id: str
    created_at: str

    class Config:
        from_attributes = True



class PutTeamsId(BaseModel):
    id: str
    name: str
    owner_id: str
    created_at: str

    class Config:
        from_attributes = True



class PostTeamMembers(BaseModel):
    id: str
    team_id: str
    user_id: str
    added_at: str

    class Config:
        from_attributes = True



class PutTeamMembersId(BaseModel):
    id: str
    team_id: str
    user_id: str
    added_at: str

    class Config:
        from_attributes = True



class PostTasks(BaseModel):
    title: str
    description: str
    status: str
    priority: str
    visibility: str
    user_id: int

    class Config:
        from_attributes = True



class PutTasksId(BaseModel):
    id: str
    title: str
    description: str
    status: str
    priority: str
    visibility: str
    created_by: str
    assigned_to: str
    team_id: str
    created_at: str

    class Config:
        from_attributes = True



class PostTaskActivity(BaseModel):
    id: str
    task_id: str
    updated_by: str
    action: str
    timestamp: str

    class Config:
        from_attributes = True



class PutTaskActivityId(BaseModel):
    id: str
    task_id: str
    updated_by: str
    action: str
    timestamp: str

    class Config:
        from_attributes = True



class PostBsUsers(BaseModel):
    email: str
    password: str
    name: str

    class Config:
        from_attributes = True



class PutBsUsersId(BaseModel):
    id: str
    created_at: str
    email: str
    password: str
    name: str

    class Config:
        from_attributes = True



class PostSignin(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes = True

