from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/teams/')
async def get_teams(db: Session = Depends(get_db)):
    try:
        return await service.get_teams(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/teams/id')
async def get_teams_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_teams_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/teams/')
async def post_teams(raw_data: schemas.PostTeams, db: Session = Depends(get_db)):
    try:
        return await service.post_teams(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/teams/id/')
async def put_teams_id(raw_data: schemas.PutTeamsId, db: Session = Depends(get_db)):
    try:
        return await service.put_teams_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/teams/id')
async def delete_teams_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_teams_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/team_members/')
async def get_team_members(db: Session = Depends(get_db)):
    try:
        return await service.get_team_members(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/team_members/id')
async def get_team_members_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_team_members_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/team_members/')
async def post_team_members(raw_data: schemas.PostTeamMembers, db: Session = Depends(get_db)):
    try:
        return await service.post_team_members(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/team_members/id/')
async def put_team_members_id(raw_data: schemas.PutTeamMembersId, db: Session = Depends(get_db)):
    try:
        return await service.put_team_members_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/team_members/id')
async def delete_team_members_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_team_members_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tasks/')
async def get_tasks(db: Session = Depends(get_db)):
    try:
        return await service.get_tasks(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tasks/id')
async def get_tasks_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_tasks_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/tasks/')
async def post_tasks(raw_data: schemas.PostTasks, db: Session = Depends(get_db)):
    try:
        return await service.post_tasks(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/tasks/id/')
async def put_tasks_id(raw_data: schemas.PutTasksId, db: Session = Depends(get_db)):
    try:
        return await service.put_tasks_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/tasks/id')
async def delete_tasks_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_tasks_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/task_activity/')
async def get_task_activity(db: Session = Depends(get_db)):
    try:
        return await service.get_task_activity(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/task_activity/id')
async def get_task_activity_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_task_activity_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/task_activity/')
async def post_task_activity(raw_data: schemas.PostTaskActivity, db: Session = Depends(get_db)):
    try:
        return await service.post_task_activity(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/task_activity/id/')
async def put_task_activity_id(raw_data: schemas.PutTaskActivityId, db: Session = Depends(get_db)):
    try:
        return await service.put_task_activity_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/task_activity/id')
async def delete_task_activity_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_task_activity_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/bs_users/')
async def get_bs_users(db: Session = Depends(get_db)):
    try:
        return await service.get_bs_users(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/bs_users/id')
async def get_bs_users_id(id: int, email: str, password: str, db: Session = Depends(get_db)):
    try:
        return await service.get_bs_users_id(db, id, email, password)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/bs_users/')
async def post_bs_users(raw_data: schemas.PostBsUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_bs_users(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/bs_users/id/')
async def put_bs_users_id(raw_data: schemas.PutBsUsersId, db: Session = Depends(get_db)):
    try:
        return await service.put_bs_users_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/bs_users/id')
async def delete_bs_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_bs_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/signin')
async def post_signin(raw_data: schemas.PostSignin, db: Session = Depends(get_db)):
    try:
        return await service.post_signin(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

