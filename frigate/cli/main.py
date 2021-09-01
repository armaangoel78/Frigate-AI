"""Frigate AI
Deploy your tensorflow models as web apps in just a few steps.

Usage:
  frigate ship <filename>
"""

import os

from docopt import docopt
from rich.console import Console

console = Console()

def main():
  arguments = docopt(__doc__, version='Naval Fate 2.0')
  filename = arguments['<filename>']

  console.print("Creating container folder...", style="bold yellow")
  os.system('mkdir .container')

  console.print("Copying over your model...", style="bold yellow")
  os.system(f'cp {filename} .container/main.py')

  console.print("Stitching Dockerfile...", style="bold yellow")
  with open('.container/Dockerfile', 'w') as f:
      f.write('Hello\n')

  console.print("Building Docker container...", style="bold yellow")
  console.print("Model Dockerized!", style="bold green")

  # os.system('cdk --app "python3 cdk.py" deploy')

if __name__ == '__main__':
  main()
