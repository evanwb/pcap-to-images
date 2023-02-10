from scapy.all import *
from PIL import Image, ImageDraw


#pcap_filename = input('please enter file name like Muiref without extension: \n')


def my_bin(k, b):
  r = [0]*b
  i = b - 1
  while k > 0:
    if k % 2 == 1:
      r[i]= 1
    else:
      r[i] = 0
    i-=1
    k= k //2
  return r

def gen_imgs(filepath: str):
  packets = rdpcap(filepath)
  pcap_filename = filepath.split('.')[0]
  temp = Image.new("RGB", (50, 50))
  draw = ImageDraw.Draw(temp)
  sessions = packets.sessions()
  print(len(sessions))


  c = 0
  n = 0
  max_session = 0

  os.system(f'mkdir {pcap_filename}')
  
  for k,v in sessions.items():
    #if not ("UDP" in k or "TCP" in k):
    if not ( "TCP" in k):
      continue
    if len(v) < 8:
      continue

    protocol = k[:3]
    print(protocol)
    print(len(v))
    j=0
    max_session = max(max_session, len(v))
    os.system(f"mkdir {pcap_filename}/{protocol}")
    
    for p in v:
      data = (raw(p[IP]))
      print(my_bin(p[IP].tos, 8) )
      tos = my_bin(p[IP].tos, 8)
      for x in range(8):
        draw.point((x,j), fill = (255*tos[x],0 ,0))
      print(my_bin(p[IP].len, 16) )
      ip_len = my_bin(p[IP].len, 16)
      for x in range(16):
        draw.point((x+8,j), fill = (0, 255*ip_len[x], 0))
      print(my_bin(data[6]>>5, 3))
      ip_flag = my_bin(data[6]>>5, 3)
      for x in range(3):
        draw.point((x+24, j), fill = (0, 0, 255*ip_flag[x]))
      ip_ttl = my_bin(p[IP].ttl, 8)
      for x in range(8):
        draw.point((x+27, j), fill = (255*ip_ttl[x], 0, 0 ))

      print(my_bin(p[IP].ttl, 8))
      ip_proto = my_bin(p[IP].proto, 8)
      for x in range(8):
        draw.point((x+35, j), fill = (0, 255*ip_proto[x], 0 ))
      print(my_bin(p[IP].proto, 8))
      j +=1
      if j >= 50:
        break    

    temp.save(f'{pcap_filename}/{protocol}/{k[4:]}.png')
    n+=1
    
  os.system(f"mv {pcap_filename}.pcap {pcap_filename}/")
  os.system(f"zip -r !{pcap_filename}.zip {pcap_filename}")  
  os.system(f"rm -rf {pcap_filename}*") 
  os.system(f"mv !{pcap_filename}.zip {pcap_filename}.zip")
  return f"{pcap_filename}.zip"