FROM python:3.11

WORKDIR /user/src/metrics

COPY . .
RUN pip install pip --upgrade
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -e .

WORKDIR /user/src/metrics/metrics

ENTRYPOINT [\
    "newrelic-admin",\
    "run-program",\
    "uvicorn",\
    "main:app",\
    "--host",\
    "0.0.0.0",\
    "--port=8005",\
    "--reload"\
]
