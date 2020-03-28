FROM python:3
ADD . .
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app
EXPOSE 5000
CMD ["python", "./app.py"]