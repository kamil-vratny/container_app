FROM amazonlinux:2023
EXPOSE 80
ARG FUNCTION_DIR="/opt/backend/"
RUN yum -y update && yum -y install python3-pip
RUN pip3 install fastapi uvicorn
WORKDIR ${FUNCTION_DIR}
COPY backend_main.py ${FUNCTION_DIR}
CMD uvicorn backend_main:app --host 0.0.0.0 --port 80
