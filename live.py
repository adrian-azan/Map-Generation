import time
from rich.live import Live
from rich.table import Table
from generator import *
import random

table = Table()

table.add_column("Row ID")
table.add_column("Description")
table.add_column("Level")

diff = generator(80,30,400)

with Live(diff, refresh_per_second=4) as live:
    while diff.finished() == False:
        diff.diffusion()
        live.update(diff.update())
        time.sleep(.08)

    diff.Tom.reset(80,30)

