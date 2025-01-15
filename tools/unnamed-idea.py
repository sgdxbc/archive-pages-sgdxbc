#!/usr/bin/env python3
from datetime import datetime, timezone
from pathlib import Path

now = datetime.now(timezone.utc).astimezone()
header = f"""\
title:  
date:   {now.strftime("%Y-%m-%d %H:%M:%S %z")}
"""

postdir = Path("_posts") / "ideas"
postdir.mkdir(exist_ok=True)
id = 0
while True:
    filename = postdir / f"{now.strftime('%Y-%m-%d')}-{id}.markdown"
    if not filename.exists():
        break
    id += 1
print("Creating", filename)
filename.write_text("---\n" + header + "---\n\n")
