from fastapi import FastAPI 
from pydantic import BaseModel 
class Students(BaseModel):
    name:str
    id:int
app= FastAPI() 
students =[ {"id":1 ,"name":"abc"},
            {"id":2,"name":"xyz"},
            {"id":3,"name":"pqr"}
           ]
@app.get("/students") 
def get_all_students(): 
    return {"student" : students} 

@app.get("/students/{id}") 
def get_students(id:int): 
    for student in students:
        if student["id"]==id:
            return student
    return "Student not found"

@app.post("/student")
def create_students(student:Students): 
    return {"student" : student} 

@app.put("/putstudent")
def put_students(student:Students): 
    return {"student" : student} 

@app.delete("/deletestudent")
def delete_students(student:Students): 
    return {"student" : student} 

