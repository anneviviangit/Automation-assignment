import pytest
import subprocess
import os

def pytest_terminal_summary(terminalreporter, exitstatus):
    """
    Hook function that runs after pytest has finished to execute additional tasks,
    such as generating and sending a report via email.
    """
    try:
        # Define the absolute path to the sendmail script located in the utilities folder
        script_path = os.path.join(os.path.dirname(__file__), 'utilities', 'sendmail.py')

        # Run the sendmail script using Python, capturing the output for logging purposes
        result = subprocess.run(
            ["python", script_path],
            check=True,        # Raises an exception if the command fails
            capture_output=True, # Captures stdout and stderr
            text=True          # Returns the output as a string instead of bytes
        )
        
        # Print the captured stdout from the script execution
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        # Handle errors in subprocess execution
        print(f"Failed to execute sendmail script: {e}")
        print(f"Error output: {e.stderr}")
