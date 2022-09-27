#!/usr/bin/env python3
import os
import json

# create empty dict
env = {}

# iterate through environment variables and add them to env
for env_key, env_value in os.environ.items():
    env[env_key] = env_value
    # print('{} -> {}'.format(env_key, env_value))


print("Content-Type: application/json") # HTML is following
print()                                 # blank line for end of headers

# print env dictionary in json format
print(json.dumps(env))