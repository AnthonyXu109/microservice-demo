from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    greeting = "Hello, welcome to the simple caculator! Here are what you can do: summation (add), subtraction (minus), multiplication (multi), division (div), power (pow), square root (sqrt), modulo (mod), factorization (fac)"
    return greeting

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """summation"""

    total = num1 + num2
    return {"summation": total}

@app.get("/minus/{num1}/{num2}")
async def minus(num1: int, num2: int):
    """subtraction"""

    total = num1 - num2
    return {"subtraction": total}

@app.get("/multi/{num1}/{num2}")
def multi(num1: int, num2: int):
    """multiplication"""

    total = num1 * num2
    return {"multiplication": total}

@app.get("/div/{num1}/{num2}")
async def div(num1: int, num2: int):
    """division"""

    total = num1 / float(num2)
    return {"division": total}

@app.get("/power/{num1}/{num2}")
async def power(num1: int, num2: int):
    """power"""

    total = num1 ** num2
    return {"power": total}

@app.get("/sqrt/{num1}")
async def sqrt(num1: int):
    """square root"""
    
    import math
    total = math.sqrt(num1)
    return {"square root": total}

@app.get("/mod/{num1}/{num2}")
async def mod(num1: int, num2: int):
    """modulo"""

    total = num1 % num2
    return {"modulo": total}
    
@app.get("/fac/{num1}")
async def fac(num1: int):
    """factorization"""
    
    i = 2
    total = ''
    while i * i <= num1:
        while num1 % i == 0:
            total += str(i) + ' '
            num1 //= i
        i += 1
    if num1 > 1:
        total += str(num1)
    return {"factorization": total}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
