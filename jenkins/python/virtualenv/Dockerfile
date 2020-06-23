ARG pythonVersion
FROM python:${pythonVersion}

RUN pip install --upgrade pip

COPY src /app
WORKDIR /app
RUN pip install -e .

ENTRYPOINT ["sample"]
CMD []
