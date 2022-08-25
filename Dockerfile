FROM 420811272222.dkr.ecr.ap-southeast-1.amazonaws.com/vb-staging-ecr:pythonbase_v1

RUN apk add --no-cache tzdata git

RUN apk upgrade -U \
    && apk add --no-cache -u ca-certificates libffi-dev libva-intel-driver supervisor python3-dev build-base linux-headers pcre-dev curl busybox-extras

COPY requirements.txt /
RUN pip --no-cache-dir install --upgrade pip setuptools
RUN pip --no-cache-dir install -r requirements.txt
RUN pip --no-cache-dir install "Flask[async]"

COPY conf/supervisor/ /etc/supervisor.d/
COPY . /webapps

WORKDIR /webapps