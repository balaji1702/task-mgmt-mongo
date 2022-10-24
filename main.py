from http.client import HTTPException
from enum_ import Status,Priority
from schema import Task
from typing import Optional
from db_config import task_collection
from fastapi import FastAPI, HTTPException,status
#some comment for testing git
app = FastAPI()
@app.post("/create-task")
def create_task(new_task:Task):
    task=new_task.dict()
    task["priority"]=task["priority"].value
    task["status"]=task["status"].value
    
    try:
        task_collection.insert_one(task)
        return {"msg":"task done sucessfully"}
    except Exception as error:
          print(type(error))
          
          raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED, detail= {"msg":"cannot perform the task debug it",
          "error":str(error)})


@app.get("/task")
def get_task():
    try:
         all_task=list(task_collection.find({}, {"_id":0}))
         return all_task
    except Exception as error:
          print(type(error))
          
          raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED, detail= {"msg":"cannot perform the task debug it",
          "error":str(error)})


@app.get("/filter-task-by-PRIORITY")
def filter_by_priority(q: Priority):
     try:
          priority_task=list(task_collection.find({"priority":q.value},{"_id":0}))
          return priority_task
     except Exception as error:
          print(type(error))
          
          
          raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED, detail= {"msg":"cannot perform the task debug it",
          "error":str(error)})
     
     
     
            
        
    

@app.get("/filter-task-by-status")
def filter_by_status(q:Status):
    try:
        status_task=list(task_collection.find({"status":q.value},{"_id":0}))
        return status_task
        
        
        
    except Exception as error:
          
          
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= {"msg":"cannot perform the task debug it",
          "error":str(error)})


@app.put("/task_update_status/{taskname}")
def update_status(taskname:str,q:Status):
    try:
        task_collection.update_one({"task_name":taskname},{"$set":{ "status":q .value}})
        return {"msg":"task updated sucessfully"}
    except Exception as error:
        
          
          raise HTTPException( status_code=status.HTTP_417_EXPECTATION_FAILED,detail= {"msg":"cannot perform the task debug it",
          "error":str(error)})

@app.put("/task_update_priority/{taskname}")
def update_priority(taskname:str,q:Priority):
    try:
        task_collection.update_one({"task_name":taskname},{"$set":{ "priority":q .value}})
        return {"msg":"task updated sucessfully"}
    except Exception as error:
        
          
          raise HTTPException( status_code=status.HTTP_417_EXPECTATION_FAILED,detail= {"msg":"cannot perform the task debug it",
          "error":str(error)})

@app.delete("/delete-task")
def delete_task(task_name:str):
    try:
        task_collection.delete_one({"task_name":task_name})
        return  {"msg":"task deleted sucessfully"}
    except Exception as error:
          print(type(error))
          
          raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED, detail= {"msg":"cannot perform the task debug it",
          "error":str(error)})
@app.delete("/delet-all-task")
def delete_all():
    try:
        task_collection.delete_many({})
        return {"msg":"deleted all values in table"}
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED, detail= {"msg":"cannot perform the task debug it",
          "error":str(error)})

    








