FROM python:3

WORKDIR /usr/src

RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv install --system --deploy --ignore-pipfile

COPY . .

CMD [ "python", "./src/main.py" ]
