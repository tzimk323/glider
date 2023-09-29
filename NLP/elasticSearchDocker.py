# docker network create elastic
#
# docker pull docker.elastic.co/elasticsearch/elasticsearch:8.10.2
#
# wget https://artifacts.elastic.co/cosign.pub
# cosign verify --key cosign.pub docker.elastic.co/elasticsearch/elasticsearch:8.10.2
#
# docker run --name es03 --net elastic -p 9200:9200 -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.10.2


# Password
# for the elastic user (reset with `bin / elasticsearch-reset-password -u elastic`):
#     MVS6OE = *JfQr + xo1X75x


# HTTP CA certificate SHA-256 fingerprint:
#   d03ab9be98d3c39ec498a66be7284ab6144df67cb525adfb746338b4ad91960f


#  Configure Kibana to use this cluster:
# • Run Kibana and click the configuration link in the terminal when Kibana starts.
# • Copy the following enrollment token and paste it into Kibana in your browser (valid for the next 30 minutes):
#   eyJ2ZXIiOiI4LjEwLjIiLCJhZHIiOlsiMTcyLjE4LjAuMjo5MjAwIl0sImZnciI6ImQwM2FiOWJlOThkM2MzOWVjNDk4YTY2YmU3Mjg0YWI2MTQ0ZGY2N2NiNTI1YWRmYjc0NjMzOGI0YWQ5MTk2MGYiLCJrZXkiOiJRRGZIeklvQnVCQ185d2VvNTdvMzphUFlHTUpvZFNqLWNKRndITEh1a0hBIn0=


#  Configure other nodes to join this cluster:
# • Copy the following enrollment token and start new Elasticsearch nodes with `bin/elasticsearch --enrollment-token <token>` (valid for the next 30 minutes):
#   eyJ2ZXIiOiI4LjEwLjIiLCJhZHIiOlsiMTcyLjE4LjAuMjo5MjAwIl0sImZnciI6ImQwM2FiOWJlOThkM2MzOWVjNDk4YTY2YmU3Mjg0YWI2MTQ0ZGY2N2NiNTI1YWRmYjc0NjMzOGI0YWQ5MTk2MGYiLCJrZXkiOiJRVGZIeklvQnVCQ185d2VvNTdvMzpjeFg1akdSYlRtS0J1VHpLb1BNaXJnIn0=
#
#   If you're running in Docker, copy the enrollment token and run:
#   `docker run -e "ENROLLMENT_TOKEN=<token>" docker.elastic.co/elasticsearch/elasticsearch:8.10.2`