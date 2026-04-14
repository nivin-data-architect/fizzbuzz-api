from fastapi import FastAPI, Query, HTTPException
from typing import List

app = FastAPI(title="FizzBuzz API")


def generate_fizzbuzz(int1: int, int2: int, limit: int, str1: str, str2: str) -> List[str]:
    result = []

    for i in range(1, limit + 1):
        output = ""

        if i % int1 == 0:
            output += str1
        if i % int2 == 0:
            output += str2

        if not output:
            output = str(i)

        result.append(output)

    return result


@app.get("/fizzbuzz")
def fizzbuzz(
    int1: int = Query(...),
    int2: int = Query(...),
    limit: int = Query(...),
    str1: str = Query(...),
    str2: str = Query(...)
):
    if int1 <= 0 or int2 <= 0 or limit <= 0:
        raise HTTPException(status_code=400, detail="All integers must be > 0")

    return {
        "result": generate_fizzbuzz(int1, int2, limit, str1, str2)
    }