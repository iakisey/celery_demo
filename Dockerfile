FROM python:2.7

ADD requirements.txt /app/requirements.txt
WORKDIR /app
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime
RUN pip install -r requirements.txt