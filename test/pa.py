import os
import  re
import  time
from multiprocessing import Process
XMAX=100
YMAX=1000
xlist = [int(XMAX*2/10),int(XMAX*5/10),int(XMAX*8/10)]
ylist = [int(YMAX*2/10),int(YMAX*4/10),int(YMAX*6/10)]
xylist = []
# for x in xlist:
#     for y in ylist:
#         xylist.append((x,y))
#
# print(xylist)

PATH = os.path.abspath(__file__)
print PATH
l = re.match(r'class (.*)\(', "class tansuoSigleTests_hwtest0001(tansuoSigleTests):")
print l.group(1)
def hahah(a):

    for i in range(0,10):
        time.sleep(5)
        print a



if __name__ == '__main__':
    screenshotParDir = ''.join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(16)))
    screenshotDir = os.path.join(os.path.dirname(__file__),"temScreenPic" ,screenshotParDir+".jpg")
    screenshotDir = r"d:\a.log"

    if os.path.exists(screenshotDir):
        os.remove(screenshotDir)


