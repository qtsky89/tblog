#!/bin/sh
docker volume create tblog_mariadb_data
docker volume create tblog_mariadb_logs
docker run -v tblog_mariadb_data:/tmp busybox chown -R 27:27 /tmp
docker run -v tblog_mariadb_logs:/tmp busybox chown -R 27:27 /tmp
