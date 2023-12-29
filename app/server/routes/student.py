from fastapi import APIRouter,Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_student,
    rtrieve_student,
    retrieve_students,
    update_student,
    delete_student,
)

from app.server.models.student import (
    ErrorResponseModel,
    ResponseModel,
    StudentSchema,
    updateStudentModel,
) 

router = APIRouter()

@router.post("/",response_description="Student data added into database")
async def add_student_data(student:StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student,"Student Added successfully")