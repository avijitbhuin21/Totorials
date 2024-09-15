#THE ORIGINAL FILE SHOULD BE IN IPYNB FORMAT.

##FIRST CELL

# Environment Setup
from IPython.display import clear_output
from pathlib import Path
import os
import subprocess

OPTIONS = {}

WORKSPACE = 'ComfyUI'

# Initial setup: Clone the repository if it doesn't exist
if not Path(WORKSPACE).exists():
    print("-= Initial setup ComfyUI =-")
    subprocess.run(['git', 'clone', 'https://github.com/comfyanonymous/ComfyUI'])

# Change directory to the workspace
os.chdir(WORKSPACE)

# Update ComfyUI

print("-= Updating ComfyUI =-")
subprocess.run(['git', 'pull'])

# Install dependencies
print("-= Install dependencies =-")
subprocess.run([
    'pip', 'install', 'xformers!=0.0.18', '-r', 'requirements.txt',
    '--extra-index-url', 'https://download.pytorch.org/whl/cu121',
    '--extra-index-url', 'https://download.pytorch.org/whl/cu118',
    '--extra-index-url', 'https://download.pytorch.org/whl/cu117'
])

# Clear the output (this function works in Kaggle)
clear_output()
print('Installation finished.')

## SECOND CELL

current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")
os.chdir('custom_nodes')
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

!git clone https://github.com/ltdrdata/ComfyUI-Manager.git
os.chdir("/kaggle/working/ComfyUI")
!pip install pyngrok
!pip install simpleeval
current_directory = os.getcwd()
clear_output()
print(f"Current Directory: {current_directory}")


## THIRD CELL

#Quick Note : if the lora is loaded from civit ai you have to rename them with .safetensor extension in order to use them.
import os
!wget -c https://huggingface.co/city96/FLUX.1-dev-gguf/resolve/main/flux1-dev-Q6_K.gguf -P./models/unet/
!wget -c https://huggingface.co/openai/clip-vit-large-patch14/resolve/main/model.safetensors -P./models/clip/
!wget -c https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn.safetensors -P./models/clip/
!wget -c https://huggingface.co/StableDiffusionVN/Flux/resolve/main/Vae/flux_vae.safetensors -P./models/vae/
    
#Boreal
!wget -c  https://civitai.com/api/download/models/810340?type=Model&format=SafeTensor -P./models/loras/
os.rename('/kaggle/working/ComfyUI/models/loras/810340?type=Model&format=SafeTensor','/kaggle/working/ComfyUI/models/loras/boreal.safetensors') 

!wget -c https://huggingface.co/alvdansen/flux-koda/resolve/main/araminta_k_flux_koda.safetensors -P./models/loras/
!wget -c https://huggingface.co/camenduru/FLUX.1-dev/resolve/main/flux_realism_lora.safetensors -P./models/loras/
clear_output()


##FOURTH CELL
from pyngrok import ngrok
import subprocess
import threading
import time
import socket
import urllib.request

def iframe_thread(port):
  ngrok.set_auth_token('NGROK_AUTHTOKEN')  # Replace with your Ngrok auth token
  ngrok_tunnel = ngrok.connect(addr=str(port), proto="http", hostname="YOUR_NGROK_DOMAIN.ngrok-free.app")
  print("This is the URL to access ComfyUI:", ngrok_tunnel.public_url)

  while True:
      time.sleep(0.5)
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      result = sock.connect_ex(('127.0.0.1', port))
      if result == 0:
        break
      sock.close()
  print("\nComfyUI finished loading, trying to launch ngrok (if it gets stuck here ngrok is having issues)\n")

  


threading.Thread(target=iframe_thread, daemon=True, args=(8188,)).start()

!python main.py --dont-print-server

#after this you should be good to go.
