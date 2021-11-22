from fastapi import FastAPI
import uvicorn
import sqlite3
from starlette.requests import Request

app = FastAPI()

# Router
@app.get("/")
def root():
  return {"message": "It works !"}


@app.post("/register_student")
async def register_student(payload: Request):
  values_dict = await payload.json()
  # Open the DB
  dbase = sqlite3.connect('tp10.db', isolation_level=None, check_same_thread=False)
  # Step 1: retrieve the session id

  session = dbase.execute(''' 
                SELECT id FROM Sessions
                WHERE course_id = {}               
                '''.format(str(values_dict['course_id'])))
  # Step 2: create a new exam for the student and session:
  exam = dbase.execute('''
        INSERT INTO Exams(student_id, session_id) 
        VALUES ({student}, {session})             
        '''.format(student=str(values_dict['student_id']), session=str(session['id'])))
  # Close the DB
  dbase.close()
  return exam


@app.post("/confirm_attendance")
async def confirm_attendance():
  # We will put here the code to execute
  return True


@app.post("/grade_exam")
async def grade_exam():
  # We will put here the code to execute
  return True


@app.get("/session_grades")
async def session_grades():
  # We will put here the code to execute
  return True


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)