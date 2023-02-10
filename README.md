# PCAP to Images
A simple server to generate images from pcap files

## Usage

```
git clone https://github.com/evanwb/pcap-to-images.git && cd pcap-to-images
```

Start docker container

Mac/Linux
```
sh run.sh
```

Windows
```
run.bat
```
To run outside of docker
  
```
pip3 install -r requirements.txt
python3 server.py
```

The server runs on [http://localhost:5555](http://localhost:5555)

upload your pcap file and click generate to download a zip file with the images

Images can also be generated from the cli

```
curl -X POST -F file='@<input filename>'  http://localhost:5555/generate -o <output filename>.zip
```
