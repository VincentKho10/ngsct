import subprocess
import json

with open("config.json") as cfg:
  config = json.load(cfg)
  print(config['tunnelsettings']['exepath'])
subprocess.run('ls')