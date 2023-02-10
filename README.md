# PCAP to Images
A simple server to generate images from pcap files

## Usage

```
git clone https://github.com/evanwb/pcap-to-images.git && cd pcap-to-images
```

to start docker container
```
sh run.sh
```
to run outside of docker
  
```
pip install -r requirements.txt
python server.py
```

the server runs on [http://localhost:5555](http://localhost:5555)

upload your pcap file and click generate to download a zip file with the images
