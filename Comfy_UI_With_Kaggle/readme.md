# ComfyUI Setup and Usage in Kaggle or Colab

This repository automates the setup and running of [ComfyUI](https://github.com/comfyanonymous/ComfyUI) within an environment like Kaggle or any other cloud-based Jupyter notebook environment.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Custom Nodes and Tools](#custom-nodes-and-tools)
- [Ngrok Setup for Remote Access](#ngrok-setup-for-remote-access)
- [Notes on LoRa Models](#notes-on-lora-models)
- [License](#license)

## Prerequisites
Ensure that the environment has the following installed:
- Python 3.x
- Git
- `pip` (Python package manager)

Optional but recommended:
- [Ngrok](https://ngrok.com/) for exposing your local server to the internet.

## Setup Instructions

### 1. Clone ComfyUI and Install Dependencies
The first cell in the notebook handles cloning the `ComfyUI` repository and installing the necessary dependencies.

```bash
git clone https://github.com/comfyanonymous/ComfyUI
cd ComfyUI
pip install xformers!=0.0.18 -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu121 --extra-index-url https://download.pytorch.org/whl/cu118 --extra-index-url https://download.pytorch.org/whl/cu117
```

### 2. Install Custom Nodes
In the second cell, a custom node manager (`ComfyUI-Manager`) is installed to extend the UI functionality.

```bash
cd custom_nodes
git clone https://github.com/ltdrdata/ComfyUI-Manager.git
pip install pyngrok simpleeval
```

### 3. Download Pre-trained Models
The third cell downloads specific models and saves them to their respective folders within the `ComfyUI` directory. If the LoRa model is downloaded from Civit AI, it will be renamed to ensure compatibility with the `.safetensor` extension.

```bash
wget -c https://huggingface.co/city96/FLUX.1-dev-gguf/resolve/main/flux1-dev-Q6_K.gguf -P ./models/unet/
wget -c https://huggingface.co/openai/clip-vit-large-patch14/resolve/main/model.safetensors -P ./models/clip/
wget -c https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn.safetensors -P ./models/clip/
wget -c https://huggingface.co/StableDiffusionVN/Flux/resolve/main/Vae/flux_vae.safetensors -P ./models/vae/

# Boreal LoRa
wget -c https://civitai.com/api/download/models/810340?type=Model&format=SafeTensor -P ./models/loras/
mv ./models/loras/810340?type=Model&format=SafeTensor ./models/loras/boreal.safetensors
```

### 4. Ngrok Setup for Remote Access
The fourth cell sets up Ngrok to allow remote access to the ComfyUI interface.

Make sure to replace the `NGROK_AUTHTOKEN` and `YOUR_NGROK_DOMAIN` with your Ngrok credentials.

```python
from pyngrok import ngrok

ngrok.set_auth_token('NGROK_AUTHTOKEN')  # Replace with your Ngrok auth token
ngrok_tunnel = ngrok.connect(addr=str(port), proto="http", hostname="YOUR_NGROK_DOMAIN.ngrok-free.app")
```

Once the UI is fully loaded, Ngrok will create a public URL that can be used to access the ComfyUI interface remotely.

## Usage
After setting up the repository and installing the required dependencies, use the following command to launch the ComfyUI interface:

```bash
python main.py --dont-print-server
```

The Ngrok tunnel will provide a public URL that allows you to access the ComfyUI from your browser.

## Custom Nodes and Tools
The repository uses the `ComfyUI-Manager` for installing and managing custom nodes. More nodes can be added by cloning their respective repositories into the `custom_nodes` directory.

### Installing Custom Nodes
You can add more custom nodes by cloning the required repositories into the `custom_nodes` folder, and then restarting ComfyUI.

```bash
cd custom_nodes
git clone <url_of_custom_node_repository>
```

## Notes on LoRa Models
If you download LoRa models from Civit AI, you must rename the files with the `.safetensor` extension. This is mandatory for the models to be usable by ComfyUI.

```bash
mv ./models/loras/filename ./models/loras/filename.safetensors
```

## License
This project follows the license provided by the original ComfyUI repository and all respective tools used.
