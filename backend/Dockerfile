FROM python:alpine3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app/backend

# Install system dependencies required by grpcio and other packages
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev linux-headers g++ make

COPY requirements.txt /app/backend/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/backend/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]