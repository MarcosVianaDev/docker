FROM python:latest
WORKDIR /api

COPY . .

RUN rm -rf venv
RUN python -m pip install -r req.txt

VOLUME /var/www/html

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]

EXPOSE 8002