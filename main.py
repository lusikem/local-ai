import os
import sys
import subprocess
import argparse

def pull_model(model_name="mistral"):
    """Pull a model from Ollama."""
    print(f"Pulling model: {model_name}")
    try:
        subprocess.run(["ollama", "pull", model_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error pulling model: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("Ollama not found. Please install Ollama first.")
        sys.exit(1)

def run_model(model_name="mistral"):
    """Run a model interactively."""
    print(f"Running model: {model_name}")
    try:
        subprocess.run(["ollama", "run", model_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running model: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("Ollama not found. Please install Ollama first.")
        sys.exit(1)

def list_models():
    """List all locally available models."""
    print("Listing local models...")
    try:
        subprocess.run(["ollama", "list"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error listing models: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("Ollama not found. Please install Ollama first.")
        sys.exit(1)

def train_model(base_model, modelfile_path, output_name):
    """
    Create a new model using a Modelfile.
    Note: 'modelfile_path' should point to a valid Modelfile.
    """
    print(f"Creating model '{output_name}' using Modelfile: {modelfile_path}")

    if not os.path.exists(modelfile_path):
        print(f"Error: Modelfile not found: {modelfile_path}")
        sys.exit(1)

    try:
        subprocess.run([
            "ollama", "create",
            output_name,
            "-f", modelfile_path
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error creating model: {e}")
        sys.exit(1)

def launch_gui():
    """Launch Open Web UI using Docker."""
    print("Attempting to launch Open Web UI...")

    try:
        subprocess.run(["docker", "version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Docker not running or not installed. Please start Docker first.")
        sys.exit(1)

    result = subprocess.run([
        "docker", "ps", "-a", "--filter", "name=open-webui", "--format", "{{.Names}}"
    ], capture_output=True, text=True)

    if "open-webui" in result.stdout:
        print("Open Web UI container already exists. Starting it...")
        subprocess.run(["docker", "start", "open-webui"], check=True)
    else:
        print("Creating new Open Web UI container...")
        try:
            subprocess.run([
                "docker", "run", "-d",
                "-p", "3000:8080",
                "--add-host=host.docker.internal:host-gateway",
                "-v", "open-webui:/app/backend/data",
                "--name", "open-webui",
                "--restart", "always",
                "ghcr.io/open-webui/open-webui:main"
            ], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error launching GUI: {e}")
            sys.exit(1)

    print("Open Web UI is (or will soon be) available at http://localhost:3000")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Local-AI CLI")
    parser.add_argument("command", choices=["pull", "run", "list", "train", "gui"], help="Command to run")
    parser.add_argument("--model", help="Model name (e.g. mistral)")
    parser.add_argument("--modelfile", help="Path to your Modelfile")
    parser.add_argument("--output", help="Name for the new model")

    args = parser.parse_args()

    if args.command == "pull":
        pull_model(args.model or "mistral")
    elif args.command == "run":
        run_model(args.model or "mistral")
    elif args.command == "list":
        list_models()
    elif args.command == "train":
        if not args.modelfile or not args.output:
            print("Error: For 'train', --modelfile and --output are required.")
            sys.exit(1)
        train_model(args.model or "mistral", args.modelfile, args.output)
    elif args.command == "gui":
        launch_gui()

# --------------------------------------------
# Local-AI CLI
# Author: L. Lusike Mukhongo
# License: MIT
# 
# Credits:
# - Ollama: https://github.com/ollama/ollama
# - Open Web UI: https://github.com/open-webui/open-webui
# - Docker: https://www.docker.com
# --------------------------------------------


