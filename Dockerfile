FROM python:3.9

# set working directory
WORKDIR /api

RUN python -m pip install  --no-cache-dir --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /api

CMD ["bash", "./start_server.sh"]
