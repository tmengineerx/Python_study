FROM python:3.12-slim
RUN pip install qrcode pillow pandas
WORKDIR /app