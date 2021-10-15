# Alpine base image v.3.10 that contains python 3.5.7
FROM python:3.5.7-alpine3.10

LABEL maintainer="GOCAS"

# Copy files
COPY . /Robot1ControllerMs
# Set working directory
WORKDIR /Robot1ControllerMs

# Remove cache,tmp files and update
RUN rm -rf /var/cache/apk/* && \
    rm -rf /tmp/* && \
    apk update
# Install necessary libs for rpi.gpio
RUN apk add --no-cache gcc musl-dev

# Install rpi.gpio  to have access to gpio pins from docker
RUN pip install --no-cache-dir rpi.gpio

# Install flask
RUN pip install flask

# Remove libs
RUN apk del gcc musl-dev

# Expose port
EXPOSE 8080

# Final command
CMD ["python","app.py"]
