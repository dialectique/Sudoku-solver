FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY .api /api
COPY .sudokupackage /sudokupackage
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
