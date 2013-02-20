import sys
import webbrowser

print "Script initialized"

try:
  print "Script arguments: ",sys.argv
except:
  print 

delays = []

def readBarcode(arg):
  if arg > 3:
    if arg < 50:
      delays.append(arg)
      if len(delays) == 4:
        print delays
        th = findGap(delays)
        bits = categorize(delays,th)
        print bits
        openSite(bits)
        del delays[:]
    else:
      del delays[:]

def findGap(dList):
  sortedList = sorted(dList)
  differences =  [x - sortedList[i - 1] for i, x in enumerate(sortedList)][1:]
  ind = differences.index(max(differences))
  threshold = sortedList[ind+1]
  print threshold
  return threshold

def categorize(dList,threshold):
  bitArr = []
  for delay in dList:
    if delay < threshold:
      bitArr.append(1)
    else:
      bitArr.append(0)
  return bitArr

def openSite(code):
  indexList = [
  [1,0,1,0],
  [0,1,0,1],
  [1,1,0,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,0]
  ]
  sites = ['http://www.youtube.com','http://www.google.com','http://www.twitter.com',
  'http://www.facebook.com','http://www.sparkfun.com','http://www.adafruit.com']
  for i,c in enumerate(indexList):
    if code == c:
      webbrowser.open(sites[i])
