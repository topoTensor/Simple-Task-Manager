FROM python:3.10-slim-bullseye

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

WORKDIR /TaskManager
ENTRYPOINT [ "python3" ,"manage.py" ,"runserver","0.0.0.0:8000" ]
