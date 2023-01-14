FROM python:3.10-slim-bullseye
WORKDIR /usr/app
RUN pip install pdm
CMD [ "pdm", "run", "python", "./src/naming.py", "--help" ]
