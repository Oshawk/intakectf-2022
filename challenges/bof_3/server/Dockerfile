# sudo docker build -t intake_ctf_2022_pwn_bof_3 .
# sudo docker run -d -p 42003:42003 intake_ctf_2022_pwn_bof_3

FROM ubuntu:22.04

RUN apt update && apt install -y socat && rm -rf /var/lib/apt/lists/*

RUN mkdir /srv/vuln
ADD . /srv/vuln
RUN chmod -R 755 /srv/vuln

RUN useradd -s /bin/bash intake
USER intake
WORKDIR /srv/vuln

CMD socat TCP-LISTEN:42003,fork,reuseaddr EXEC:/srv/vuln/bof_3,stderr