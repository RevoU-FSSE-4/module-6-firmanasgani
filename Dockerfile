FROM  python:3.12-slim
RUN mkdir -p /app

COPY ./src /app
WORKDIR /app
RUN pip install -U pipenv
RUN pipenv install --deploy
EXPOSE 4300
CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:4300", "app:app"]