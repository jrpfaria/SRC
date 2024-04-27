FROM alpine:latest
RUN apk add --no-cache iptables conntrack-tools
RUN apk add --no-cache nano
COPY ./scripts/restore.sh /restore
COPY ./scripts/save.sh /save
COPY ./scripts/conntrackd.sh /conntrackd
COPY ./scripts/entrypoint.sh /entrypoint
ENTRYPOINT [ "/entrypoint" ]
