import subprocess

def run_command(user_input):
    """Run a shell command from user input."""
    subprocess.call(user_input, shell=True) #This is a dangerous function that runs a shell command from user input.

API_KEY = "sk-live-abc123def456"
