import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.students
student_collection = database.get_collection("students_collection")

#helpers

def student_helper(student) -> dict:
    return {
        "id" : str(student["_id"]),
        "full_name" : student["full_name"],
        "email" : student["email"],
        "course_of_study" : student["course_of_study"],
        "year" : student["year"],
        "GPA" : student["gpa"],
    }


#Retrieve all students present in the database
async def retrieve_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students

# Add a new student to the database
async def add_student(student_data:dict) -> dict:
    student = student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id":student.inserted_id})
    if student:
        return student_helper(new_student)
    


#Retrieve a student with a matching id
async def rtrieve_student(id:str) -> dict:
    student = await student_collection.find_one({"_id":ObjectId(id)})
    if student:
        return student_helper(student)
    

#Update a student with a matching id
async def update_student(id:str,data:dict):
    if len(data) < 1:
        return False
    student = await student_collection.find_one({"_id":ObjectId(id)})
    if student:
        updated_student = student_collection.update_one(
            {"_id":ObjectId(id)}, {"$set":data}
        )
        if updated_student:
            return True
        return False
    

#Delete a student from the database
async def delete_student(id:str):
    student = await student_collection.find_one({"_id":ObjectId(id)})
    if student:
        await student_collection.delete_one({"_id":ObjectId(id)})
        return True















