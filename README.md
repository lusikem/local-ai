# Local-AI. Offline Low-power AI for Everyone

> Run light-weight AI models entirely on your own device, without cloud, subscriptions, or internet access.

## Overview

**Local-AI** is an open-source project that empowers users to run light-weight language models (LLMs) on their local devices with limited computing power. Whether you're working with an older CPU-based laptop or deploying in remote or rural areas with unreliable connectivity, Local-AI gives you full control over your data and models.

This project uses the following stack:

[Ollama](https://ollama.com) — to run and customize LLMs on macOS, Linux, and Windows

[Open Web UI](https://github.com/open-webui/open-webui) — a browser-based chat interface, offline and open-source

[Docker](https://www.docker.com) — for simple and reproducible deployments

---

## Features

 **Run Offline** — Works without internet access or cloud services

 **100% Private** — Keeps all data on your device

 **Customizable** — Fine-tune and personalize your own AI models

 **Free and Open Source** — No subscriptions or vendor lock-in

 **Low Resource Compatible** — Works on CPUs, no GPU required

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

Use Docker to run Open Web UI locally:

Use Docker to run Open Web UI locally:

Once running, access the interface at: http://localhost:3000

 
### 4. Customize your model

You can fine-tune models like **Mistral** or **LLaMA** with your own datasets to adapt them to specific tasks, languages, or community knowledge.

####  Common Use Cases
- Chatbots trained on regional or cultural knowledge (e.g., Swahili, Dholuo)
- Domain-specific assistants (e.g., legal, medical, farming)
- Q&A over PDFs, spreadsheets, or transcribed audio
- Creative writing, translation, or grammar correction

---


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

This project is built for users/communities that have:
Limited access to reliable internet
Concerns over data privacy and AI surveillance
A need for localized, culturally-relevant AI tools

By supporting open-source LLMs on local devices, we reclaim control of our digital futures.



