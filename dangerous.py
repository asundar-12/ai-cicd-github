import subprocess
import shlex
import os

def run_command(user_input):
    """Run a shell command from user input."""
    args = shlex.split(user_input)
    subprocess.call(args, shell=False) #This is a dangerous function that runs a shell command from user input.

API_KEY = os.environ.get("API_KEY")
