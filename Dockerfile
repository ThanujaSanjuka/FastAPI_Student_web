FROM python:3.9-slim
WORKDIR /app
RUN pip install fastapi uvicorn
COPY main.py .
EXPOSE 8000
CMD ["uvicorn", "main.py:app", "--host", "0.0.0.0", "--port", "8000"]
