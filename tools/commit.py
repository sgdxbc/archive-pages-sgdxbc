#!/usr/bin/env python3
from subprocess import run

run("./tools/test.sh", shell=True, check=True)
run("git add .", shell=True, check=True)
run("git status", shell=True, check=True)
message = input('message: ')
if not message:
    message = 'Post'
run(f"git commit -m \"{message}\"", shell=True, check=True)
run(f"git push", shell=True, check=True)
