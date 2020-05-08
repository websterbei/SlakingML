# @Author: Webster Bei Yijie, Joey Junyu Liang
# @Date: 5/8/2020, 3:13:32 PM
# @Email: yijie.bei@duke.edu, junyu.liang@duke.edu

# For testing on kubernetes only
import time

ind = 0
while True:
    if ind % 100 == 0:
        print(ind)
    time.sleep(1)
    ind += 1