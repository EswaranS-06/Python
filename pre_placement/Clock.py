import time
def clock():
    try:
        h, m, s = 11, 59, 50
        while True:
            print(f"\r {h:02d}:{m:02d}:{s:02d}", end='', flush= True)
            time.sleep(1)
            s+=1
            if s == 60:
                s = 0
                m += 1
            elif m == 60:
                s = 0
                m = 0
                h += 1
            elif h == 12 :
                s = 0
                m = 0
                h = 0
    except KeyboardInterrupt:
        print("\rWait....",end='',flush=True)
        time.sleep(3)
        clock()
        
clock()