import time

ind = 0
while True:
    if ind % 100 == 0:
        print(ind)
    time.sleep(1)
    ind += 1