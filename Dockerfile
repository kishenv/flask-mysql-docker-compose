from alpine:latest

RUN apk add --no-cache build-base
RUN apk add --no-cache gcc
RUN apk add --no-cache mariadb-dev

RUN apk add --no-cache python3-dev py3-pip \
    && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["mydb.py"]


