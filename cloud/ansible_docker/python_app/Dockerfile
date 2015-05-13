# Set the base image to Ubuntu
FROM ubuntu:14.04

# File Author / Maintainer
MAINTAINER Emiliano Molina <emiliano.g.molina@gmail.com>

# Install system packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libcurl4-openssl-dev \
    libev4 \
    libev-dev \
    python \
    python-dev \
    python-distribute \
    python-pip

# Deploy python application
COPY backend/dist/echo_service-1.0.0.tar.gz /tmp/echo_service.tar.gz
WORKDIR /tmp
RUN pip install echo_service.tar.gz

# Expose port
EXPOSE 8080

# Run app
CMD ["echo_service", "--port", "8080"]
