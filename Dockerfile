FROM python:alpine3.16
WORKDIR /usr/src/app
RUN pip install diagrams  
RUN apk add --update --no-cache \
    graphviz \
    ttf-freefont
CMD ["python","-V"]
