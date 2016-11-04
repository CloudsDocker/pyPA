import random
import traceback
import subprocess
import time
import os

from multiprocessing.pool import ThreadPool, Pool

FNULL = open(os.devnull, 'w')


    print "start"
    # pool = ThreadPool(processes=100)
    f = open('log.txt', 'w')

    def cb(result):
        print "cb"
        print result
        if result is None:
            return
        # ip, lat, lon, t = result
        ip, t = result
        print >>f, t


    ip = "111.13.100.91"

    try:
        # print ip, lat, lon, '?'
        t0 = time.time()
        print "start to ping"
        status = subprocess.call(['ping', '-c1', '-t2', ip], stdout=FNULL, stderr=FNULL)
        print status
        if status != 0:
            # return None
            print "status is Non zero"
        t =  time.time() - t0
        print >>f, ip, t
        # return ip,  time.time() - t0
    except:
        print "error"
        traceback.print_exc()

    print "enpooled"

    # pool.close()
    # pool.join()

    f.close()