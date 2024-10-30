#!/usr/bin/env python3
from sys import argv
from datetime import datetime, timezone
from pathlib import Path

name = argv[1]

now = datetime.now(timezone.utc).astimezone()
header = f"""\
layout: post
title:  
date:   {now.strftime("%Y-%m-%d %H:%M:%S %z")}
"""

if name == "checkpoint":
    header += """\
categories: [检查点]
permalink: /:title-:year:month:day:output_ext
"""
else:
    header += "categories: \n"

postdir = Path("_posts")
filename = postdir / f"{now.strftime('%Y-%m-%d')}-{name}.markdown"
print("Creating", filename)
filename.write_text("---\n" + header + "---\n\n")