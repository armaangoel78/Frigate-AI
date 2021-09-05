"""Frigate AI
Deploy your tensorflow models as web apps in just a few steps.

Usage:
  frigate ship <filename>
"""

import os

from docopt import docopt
from rich.console import Console

console = Console()

def shell(command: str): 
  response = os.system(command)
  if response != 0:
    exit()

def dockerize(filename: str):
  console.print("Creating container folder...", style="bold yellow")
  if not '.container' in os.listdir():
    shell('mkdir .container')

  console.print("Copying over your model...", style="bold yellow")
  shell(f'cp {filename} .container/main.py')

  console.print("Copying over requirements.txt...", style="bold yellow")
  if (not 'requirements.txt' in os.listdir()):
    console.print("Copying over requirements.txt...", style="bold red")

  shell(f'cp requirements.txt .container/requirements.txt')

  console.print("Stitching Dockerfile...", style="bold yellow")
  with open('.container/Dockerfile', 'w') as f:
      f.write('FROM python:3.8-slim-buster\n')
      f.write('WORKDIR /root\n')

      f.write('RUN mkdir /root/src\n')
      f.write('COPY . /root/src\n')

      f.write('RUN pip install -r src/requirements.txt\n')
      
      # f.write('RUN mkdir /root/frigate\n')
      # f.write('COPY frigate /root/frigate\n')

  console.print("Building Docker container...", style="bold yellow")
  response = shell('docker build .container')
  print(response)

  console.print("Model Dockerized!", style="bold green")

def cdkDeploy():
  console.print("Provisioning AWS Resources...", style="bold yellow")
  # from .cdk import app
  cdk_path = os.path.dirname(os.path.realpath(__file__)) + '/cdk'
  os.chdir(cdk_path)
  shell('cdk deploy')

  console.print("Resources Provisioned!", style="bold green")

def generateFrontend():
  pass

def main():
  arguments = docopt(__doc__, version='Naval Fate 2.0')
  filename = arguments['<filename>']

  dockerize(filename=filename)
  generateFrontend()
  cdkDeploy()  

if __name__ == '__main__':
  main()
