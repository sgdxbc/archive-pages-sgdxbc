#!/usr/bin/env python3
from datetime import datetime, timezone
from pathlib import Path

now = datetime.now(timezone.utc).astimezone()
header = f"""\
date:   {now.strftime("%Y-%m-%d %H:%M:%S %z")}
"""

postdir = Path("_posts") / "checkpoints"
filename = postdir / f"{now.strftime('%Y-%m-%d')}-.markdown"
assert not filename.exists()
print("Creating", filename)
filename.write_text("---\n" + header + "---\n\n")
