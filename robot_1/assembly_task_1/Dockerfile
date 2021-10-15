# Alpine base image v.3.10 that contains python 3.5.7
FROM python:3.5.7-alpine3.10

LABEL maintainer="GOCAS"

# Set working directory
WORKDIR /WorkerTask1

# Copy files
COPY . /WorkerTask1

# Remove cache,tmp files and update
RUN rm -rf /var/cache/apk/* && \
    rm -rf /tmp/* && \
    apk update 

# Final command
CMD ["python3","main.py"]
