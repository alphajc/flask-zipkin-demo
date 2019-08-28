FROM alpine

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

RUN apk add --no-cache python3 gcc python3-dev libc-dev

ADD requirements.pip requirements.pip
RUN pip3 install -r requirements.pip

ADD src src

EXPOSE 5000

CMD ["python3", "/src/run.py"]
