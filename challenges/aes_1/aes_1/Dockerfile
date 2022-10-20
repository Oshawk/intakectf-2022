# sudo docker build -t intake_ctf_2022_crypto_aes_1 .
# sudo docker run -d -p 42004:42004 intake_ctf_2022_crypto_aes_1

FROM ubuntu:22.04

RUN apt update && apt install -y python3 python3-pip socat && rm -rf /var/lib/apt/lists/*
RUN pip3 install pycryptodome

RUN mkdir /srv/vuln
ADD . /srv/vuln
RUN chmod -R 755 /srv/vuln

RUN useradd -s /bin/bash intake
USER intake
WORKDIR /srv/vuln

CMD socat TCP-LISTEN:42004,fork,reuseaddr EXEC:'python3 /srv/vuln/aes_1.py',stderr