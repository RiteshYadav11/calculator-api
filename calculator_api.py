from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/calculate")
def calculate(a: float = Query(...), b: float = Query(...), operation: str = Query("+")):
    try:
        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            if b == 0:
                return JSONResponse(status_code=400, content={"error": "Cannot divide by zero"})
            result = a / b
        else:
            return JSONResponse(status_code=400, content={"error": "Unsupported operation"})
        return {"result": result}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
