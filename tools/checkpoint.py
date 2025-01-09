#!/usr/bin/env python3
from sys import argv
from datetime import datetime, timezone
from pathlib import Path

now = datetime.now(timezone.utc).astimezone()
header = f"""\
layout: post
date:   {now.strftime("%Y-%m-%d %H:%M:%S %z")}
categories: [检查点]
permalink: /checkpoint/:year:month:day:output_ext
"""

postdir = Path("_posts")
filename = postdir / "checkpoints" / f"{now.strftime('%Y-%m-%d')}-.markdown"
assert not filename.exists()
print("Creating", filename)
filename.write_text("---\n" + header + "---\n\n")
