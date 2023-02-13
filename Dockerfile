FROM python:3.11.2

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/crispy-umbrella/

COPY poetry.lock pyproject.toml /usr/crispy-umbrella/

RUN pip3 install poetry

RUN poetry install --no-root