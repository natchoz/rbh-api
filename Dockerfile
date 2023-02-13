FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

COPY assets /app/assets
COPY main.py /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]