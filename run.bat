
docker rm --force pcap-to-images
docker build -t pcap-to-images . 
docker run --name="pcap-to-images" -d -p 5555:5555 pcap-to-images 
