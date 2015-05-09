# Set the base image to Ubuntu
FROM ubuntu:14.04

# File Author / Maintainer
MAINTAINER Emiliano Molina <emiliano.g.molina@gmail.com>

# Install system packages
RUN apt-get update && apt-get install -y build-essential wget

# Install Redis Server
WORKDIR /usr/local
RUN wget http://download.redis.io/redis-stable.tar.gz \
    && tar xvzf redis-stable.tar.gz \
    && rm -f redis-stable.tar.gz

WORKDIR redis-stable
RUN make
RUN mkdir -p /etc/redis /var/redis/6379 \
    && cp src/redis-server /usr/local/bin/ \
    && cp src/redis-cli /usr/local/bin/ \
    && cp utils/redis_init_script /etc/init.d/redis_6379 \
    && cp redis.conf /etc/redis/6379.conf

# Expose Redis port 6379
EXPOSE 6379

# Run Redis Server
ENTRYPOINT ["redis-server"]
