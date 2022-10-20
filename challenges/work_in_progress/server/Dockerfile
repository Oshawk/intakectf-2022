# sudo docker build -t intake_ctf_2022_work_in_progress .
# sudo docker run -d -p 42005:42005 intake_ctf_2022_work_in_progress

FROM ubuntu:22.04

RUN apt update && apt install -y curl python3 python3-pip && rm -rf /var/lib/apt/lists/*
RUN pip3 install flask

RUN mkdir /srv/vuln
ADD . /srv/vuln
RUN chmod -R 755 /srv/vuln

RUN useradd -s /bin/bash intake
USER intake
WORKDIR /srv/vuln

CMD python3 /srv/vuln/work_in_progress.py