FROM python
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN apt update -y; apt install zip -y
RUN apt clean
CMD ["python", "server.py"]
