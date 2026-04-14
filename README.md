# FizzBuzz API 🚀

## Overview

A REST API built with FastAPI that generates a customizable FizzBuzz sequence based on user-defined inputs.

---

## API Endpoint

**GET** `/fizzbuzz`

### Parameters

* `int1`: First divisor
* `int2`: Second divisor
* `limit`: Upper bound (inclusive)
* `str1`: Replacement for multiples of `int1`
* `str2`: Replacement for multiples of `int2`

---

## Example Request

```
http://127.0.0.1:8000/fizzbuzz?int1=3&int2=5&limit=15&str1=Fizz&str2=Buzz
```

## Example Response

```
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
```

---

## Setup & Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Access API docs:

```
http://127.0.0.1:8000/docs
```

---

## Validation

* All numeric inputs must be > 0
* Returns HTTP 400 for invalid inputs

---

## Tech Stack

* Python
* FastAPI
* Uvicorn

---

## Author

Nivin Eapen
