from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Router
@app.get("/")
def root():
  return {"message": "It works !"}


@app.post("/register_student")
async def register_student():
  # We will put here the code to execute
  return True


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