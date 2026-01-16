FROM python:3.11-slim

WORKDIR /app

COPY app/ app/

RUN pip install fastapi uvicorn requests

ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["uvicorn", "app.genai.main:app", "--host", "0.0.0.0", "--port", "8000"]