FROM ubuntu:18.04

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    ca-certificates 

WORKDIR /var/cloudyali

ADD ./bin/linux_amd64/snapshotservice /var/cloudyali
RUN chmod +x /var/cloudyali/snapshotservice

# Run Binary
CMD ["/var/cloudyali/snapshotservice"]