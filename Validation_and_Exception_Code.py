from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel , EmailStr
class Students(BaseModel):
    id:int
    name:str
    age:int
    email:EmailStr
app= FastAPI() 
students =[ {"id":1 ,"name":"abc","age":22,"email":"abc@gmail.com"},
            {"id":2,"name":"xyz","age":21,"email":"xyz@gmail.com"},
            {"id":3,"name":"pqr","age":20,"email":"pqr@gmail.com"}
           ]
@app.put("/student/{id}")
def update_students(id:int, student:Students): 
    students[id] = student
    return student

@app.get("/students") 
def get_all_students(): 
    return {"student" : students} 

@app.get("/students/{id}")
def get_student(id: int):
    if id>len(students):
        raise HTTPException(status_code=404,detail="not found")
    for student in students:
        if student["id"] == id:
            return student


@app.post("/students/")
def create_students(student:Students): 
    return {"student" : student} 


@app.delete("/students/{id}")
def delete_students(id:int): 
    students.pop(id)
    return {"message" : "Deleted successfully"} 

