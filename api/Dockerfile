FROM python:3.8



COPY requirements.txt .
RUN pip install -r requirements.txt 
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

# Create working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy contents
COPY . /usr/src/app

# Set environment variables
ENV HOME=/usr/src/app

EXPOSE 2050

WORKDIR /usr/src/app
CMD ["gunicorn","app.main:app","-w","1","--threads", "1", "--timeout", "120", \
  "--worker-connections=300","-k","uvicorn.workers.UvicornWorker","--bind", "0.0.0.0:2050"]