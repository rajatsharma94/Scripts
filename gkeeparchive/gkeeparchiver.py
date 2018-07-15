import sys
import gkeepapi
import time
from datetime import datetime

email1 = sys.argv[1]
pass1 = sys.argv[2]
email2 = sys.argv[3]
pass2 = sys.argv[4]

print("starting keep sync program")

keep1 = gkeepapi.Keep()
success = keep1.login(email1, pass1)

keep2 = gkeepapi.Keep()
success = keep2.login(email2, pass2)

while True:
    gnotes1 = keep1.all()
    gnotes2 = keep2.all()
    for gnote1 in gnotes1:
        for gnote2 in gnotes2:
            if (gnote1.id == gnote2.id and gnote1.archived != gnote2.archived):
                gnote2.archived = gnote1.archived
                print("modifying "+gnote1.id+", setting"+str(gnote1.archived))

    keep2.sync()
    time.sleep(300) # sleep for 5 minutes

print("exiting keep program")
