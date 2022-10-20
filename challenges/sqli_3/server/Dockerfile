# sudo docker build -t intake_ctf_2022_sqli_3 .
# sudo docker run -d -p 42008:42008 intake_ctf_2022_sqli_3

FROM ubuntu:22.04

RUN apt update && apt install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*
RUN pip3 install flask

RUN mkdir /srv/vuln
ADD . /srv/vuln
RUN chmod -R 755 /srv/vuln

RUN useradd -s /bin/bash intake
USER intake
WORKDIR /srv/vuln

CMD python3 /srv/vuln/sqli_3.py