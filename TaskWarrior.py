#!/usr/bin/python3
import openai
import subprocess
import sys


openai.api_key = "API_KEY"


if len(sys.argv) > 1:
    # Use the provided arguments as the TaskWarrior command
    prompt = " ".join(sys.argv[1:])
else:
    print("No TaskWarrior command provided.")
    sys.exit(1)

completion = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"{prompt}, turn this into a valid TaskWarrior command.",
  max_tokens=2048,
  temperature=0
)

response = completion.choices[0].text
taskwarrior_cmd = f"task {response}"
print(taskwarrior_cmd)

# Execute the TaskWarrior command using subprocess
try:
    completed = subprocess.run(taskwarrior_cmd, shell=True, check=True)
    output = completed.stdout
    print(output)

except subprocess.CalledProcessError as e:
    print(f"Error executing TaskWarrior command: {e}")