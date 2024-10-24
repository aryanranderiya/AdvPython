
import subprocess
import os
from pathlib import Path

# 1. Running a Subprocess
result = subprocess.run(["python", "-c", "print('This is a subprocess')"], capture_output=True, text=True)
print(result.stdout)  # Output: This is a subprocess

# 2. Running a Subprocess with Error Handling
result = subprocess.run(["python", "-c", "print('Hello from subprocess')"], capture_output=True, text=True, check=True)
print('Output:', result.stdout)
print('Error:', result.stderr)

# 3. Using Timeout for Subprocess
try:
    # This will succeed
    subprocess.run(["python", "-c", "import time; time.sleep(5)"], capture_output=True, text=True)

    # This will raise a TimeoutExpired exception
    subprocess.run(["python", "-c", "import time; time.sleep(5)"], capture_output=True, text=True, timeout=2)
except subprocess.TimeoutExpired as e:
    print(f"Process exceeded the timeout: {e}")

# 4. Input to Subprocess
result = subprocess.run(
    ["python", "-c", "import sys; my_input=sys.stdin.read(); print(my_input)"],
    capture_output=True, text=True, input='my_text'
)
print(result.stdout)  # Output: my_text

# 5. Running a Backup Process in Parallel Using Subprocess
def backup_files(source_folder, dest_folders):
    # Ensure the source folder exists
    if not os.path.exists(source_folder):
        raise FileNotFoundError(f"Source folder '{source_folder}' does not exist.")
    
    # Ensure all destination folders exist, create them if they don't
    for folder in dest_folders:
        Path(folder).mkdir(parents=True, exist_ok=True)

    # Create a list to hold subprocesses
    processes = []

    # Loop through each destination and start the copy process in parallel
    for dest_folder in dest_folders:
        command = ["cp", "-r", source_folder, dest_folder]
        print(f"Starting backup to {dest_folder}")
        process = subprocess.Popen(command)
        processes.append(process)

    # Wait for all processes to finish
    for process in processes:
        process.wait()
        print(f"Backup to {process.args[-1]} completed")

if __name__ == "__main__":
    source_folder = "/path/to/source/folder"
    dest_folders = ["/path/to/destination1", "/path/to/destination2", "/path/to/destination3"]
    
    backup_files(source_folder, dest_folders)
