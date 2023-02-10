FROM python
WORKDIR /app
COPY . .
RUN pip install scapy flask werkzeug Pillow
RUN apt update -y; apt install zip -y
RUN apt clean
CMD ["python", "server.py"]
