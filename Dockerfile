FROM python:alpine3.16

WORKDIR /usr/src/app
ENTRYPOINT ["python"]

CMD ["-V"]
