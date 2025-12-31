# Local-AI. Offline Low-power AI for Everyone

> Run AI models entirely on your own device, without cloud, subscriptions, or internet access.

## Overview

**Local-AI** is an open-source project that empowers users to run powerful language models (LLMs) on their local devices — even with limited computing power. Whether you're working on a feature phone, an older CPU-based laptop, or deploying to rural areas with unreliable connectivity, Local-AI gives you full control over your data and models.

This project uses the following stack:

- [Ollama](https://ollama.com) — to run and customize LLMs on macOS, Linux, and Windows
- [Open Web UI](https://github.com/open-webui/open-webui) — a browser-based chat interface, offline and open-source
- [Docker](https://www.docker.com) — for simple and reproducible deployments

---

## Features

- ✅ **Run Offline** — Works without internet access or cloud services
- 🔐 **100% Private** — Keeps all data on your device
- 🧩 **Customizable** — Fine-tune and personalize your own AI models
- 💸 **Free and Open Source** — No subscriptions or vendor lock-in
- 💻 **Low Resource Compatible** — Works on CPUs, no GPU required

---

## 🚀 Getting Started
### 1. Install Ollama

Download Ollama from: https://ollama.com/download  
Or use terminal

Ollama supports:
Mac (M1/M2/M3 optimized)
Linux
Windows (via WSL)


### 2. Run a Model

ollama pull mistral
ollama run mistral

This starts a local REPL (interactive terminal). Here, you can type your prompts and interact with the model.

### 3. Launch Open Web UI (Optional GUI)

docker run --detach \
  --publish 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  --volume open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main

Access the UI at: http://localhost:3000

### 4. Customize your model

You can fine-tune models like Mistral with your own data (e.g., Swahili Q&A) using JSONL files

ollama train \
  --model mistral \
  --dataset ./dataset.jsonl \
  --output ./fine-tuned-model

## Optional SMS Integration
Integrate with SMS tools like:

Africa's Talking
Twilio
TextMagic
You can use Gammu to send/receive SMS from a modem or Android phone. This enables interaction with your LLM without internet access.

## Requirements

macOS/Linux/Windows
Docker (optional for GUI)
CPU with at least 8GB RAM is recommended
Terminal access

## License

This project is released under the MIT License.

## Contributing

Pull requests, forks, and improvements are welcome!
Fork the repo
Add your Swahili/other-language dataset
Train and test locally
Submit a PR from your fork to the original repo

## Community & Purpose

This project was built with communities in mind who have:
Limited access to reliable internet
Concerns over data privacy and AI surveillance
A need for localized, culturally-relevant AI tools

By supporting open-source LLMs on local devices, we reclaim control of our digital futures.



