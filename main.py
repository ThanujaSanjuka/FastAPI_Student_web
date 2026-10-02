from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Database Web Service</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f9; margin: 0; padding: 20px; display: flex; justify-content: center; }
        .container { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); width: 400px; }
        h2 { color: #333; text-align: center; }
        label { display: block; margin-top: 10px; font-weight: bold; }
        input { width: 100%; padding: 8px; margin-top: 5px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        button { width: 100%; background-color: #28a745; color: white; padding: 10px; border: none; border-radius: 4px; margin-top: 15px; cursor: pointer; font-size: 16px; }
        button:hover { background-color: #218838; }
        .records { margin-top: 20px; background: #e9ecef; padding: 10px; border-radius: 4px; max-height: 150px; overflow-y: auto; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Student Database</h2>
        <form action="/add" method="post">
            <label>Student ID:</label>
            <input type="number" name="id" required>
            <label>Name:</label>
            <input type="text" name="name" required>
            <label>GPA:</label>
            <input type="number" step="0.01" name="gpa" required>
            <button type="submit">Add Student</button>
        </form>
        
        <h3>Saved Records:</h3>
        <div class="records">
            <pre>{{ records }}</pre>
        </div>
    </div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def read_root():
    records = "No records yet."
    if os.path.exists("student_database.txt"):
        with open("student_database.txt", "r") as f:
            records = f.read()
    return HTML_TEMPLATE.replace("{{ records }}", records)

@app.post("/add", response_class=HTMLResponse)
def add_student(id: int = Form(...), name: str = Form(...), gpa: float = Form(...)):
    with open("student_database.txt", "a") as f:
        f.write(f"ID: {id} | Name: {name} | GPA: {gpa}\n")
    
    with open("student_database.txt", "r") as f:
        records = f.read()
        
    return HTML_TEMPLATE.replace("{{ records }}", records)
