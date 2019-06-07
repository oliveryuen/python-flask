FROM python:3.7-alpine

# not caching the index locally to keep container small
RUN apk --no-cache add curl

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "myflaskapp:create_app()"]

