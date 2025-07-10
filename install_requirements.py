import subprocess
import sys

def install():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("\n✓ Done")
    except:
        print("\n✗ Failed")

if __name__ == "__main__":
    install()
