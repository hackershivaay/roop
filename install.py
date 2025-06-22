
import os
import subprocess

def run(cmd):
    print(f"🔧 Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def main():
    # Clone the repo
    if not os.path.exists("roop"):
        run("git clone https://github.com/hackershivaay/roop")

    os.chdir("roop")

    # Install system packages (only works in Colab or Linux)
   # run("apt-get update --yes")
   # run("apt-get install -y nvidia-cuda-toolkit")

    # Install Python dependencies
    run("pip install -r /content/roop/requirements.txt")

    print("✅ System setup completed!")

if __name__ == "__main__":
    main()
