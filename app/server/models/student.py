from typing import Optional
from pydantic import BaseModel,EmailStr,Field

class StudentSchema(BaseModel):
    full_name: str = Field(...)
    email : EmailStr  = Field(...)
    course_of_study : str = Field(...)
    year : int = Field(...,gt=0, lt=9)
    gpa : float = Field(...,le=4.0)

    class config:
        schema_extra = {
            "example": {
                "full_name": "Rupal Grover",
                "email" : "abc@gmail.com",
                "course_of_study" : "CSE", 
                "year": 2,
                "gpa" : "4.0", 
            }
        }

class updateStudentModel(BaseModel):
    full_name: Optional[str]
    email : Optional[EmailStr]
    course_of_study : Optional[str]
    year : Optional[int]
    gpa : Optional[float]

    class config:
        schema_extra = {
            "example": {
                "full_name": "Rupal Grover",
                "email" : "abc123@gmail.com",
                "course_of_study" : "CSE/IT", 
                "year": 1,
                "gpa" : "3.0", 
            }
        }

def ResponseModel(message,data):
    return{
        "data":[data],
        "code":200,
        "message":message,

    }


def ErrorResponseModel(error,code,message):
    return{
        "error":error,
        "code":code,
        "message":message

    }