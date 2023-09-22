import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STACK_CONFIG = os.path.join(BASE_DIR,"stack_config.json")

stack_config = {}

with open(STACK_CONFIG, 'r') as file:
  stack_config = json.load(file)
  


