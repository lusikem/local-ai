import subprocess
import sys

def pull_model(model_name="mistral"):
    print(f"Pulling model: {model_name}")
    subprocess.run(["ollama", "pull", model_name], check=True)

def run_model(model_name="mistral"):
    print(f"Running model: {model_name}")
    subprocess.run(["ollama", "run", model_name], check=True)

def list_models():
    print("Available models:")
    subprocess.run(["ollama", "list"], check=True)

def launch_gui():
    print("Launching Open Web UI...")
    subprocess.run([
        "docker", "run", "-d",
        "-p", "3000:8080",
        "-v", "open-webui:/app/backend/data",
        "--name", "open-webui",
        "--restart", "always",
        "ghcr.io/open-webui/open-webui:main"
    ], check=True)
    print("Visit http://localhost:3000")

if __name__ == "__main__":
    print("Choose a command:")
    print("1 - Pull Model")
    print("2 - Run Model")
    print("3 - List Models")
    print("4 - Launch GUI")
    choice = input("Enter number: ")

    try:
        if choice == "1":
            pull_model()
        elif choice == "2":
            run_model()
        elif choice == "3":
            list_models()
        elif choice == "4":
            launch_gui()
        else:
            print("Invalid choice.")
    except subprocess.CalledProcessError:
        print("Command failed to execute.")
        print("Please check the following:")
        print("- Is Ollama installed? https://ollama.com/download")
        print("- Is Docker installed and running? https://docs.docker.com/get-docker/")
        print("- Are you connected to the internet (if pulling models)?")
        print("- Try running the command manually in your terminal to see the full error.")
        sys.exit(1)



# --------------------------------------------
# Credits:
# - Ollama: https://github.com/ollama/ollama
# - Open Web UI: https://github.com/open-webui/open-webui
# - Docker: https://www.docker.com
# --------------------------------------------


