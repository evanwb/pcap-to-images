FROM python
WORKDIR /app
COPY . .
RUN pip install scapy flask werkzeug Pillow
CMD ["python", "server.py"]
