FROM python:3.7.0-slim
WORKDIR /backend
COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5000
#CMD ["gunicorn", "-c", "/gunicorn.conf", "app:app"]
CMD ["python3", "/backend/app.py"]

# docker build -t indicator-backend
# docker run -d -p 5000:5000 indicator-backend