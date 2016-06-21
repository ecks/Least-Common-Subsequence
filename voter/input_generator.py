import random
import optparse
import sys

parser = optparse.OptionParser()
parser.add_option("-n", "--number", action="store", type="int", dest="numOfStreams",
                  help="number of streams", metavar="NUMSTREAMS")
parser.add_option("-w", "--window", action="store", type="int", dest="window",
                  help="window of messages printed", metavar="WINDOW")
parser.add_option("-o", "--output", action="store", type="string", dest="output",
                  help="output filename", metavar="OUTPUT")

(options, args) = parser.parse_args()

seqNum = 0
checksumSeqNums = []
while True:
  c = sys.stdin.read(1)
  if c == 'c':
    alphabet = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    checksumSeqNums = []
    seqNum = 0
    f = open(options.output, 'w')
    while seqNum < options.window:
      checksum = random.choice(alphabet)
      alphabet.remove(checksum)
      checksumSeqNums.append(checksum + "," + str(seqNum))
      seqNum = seqNum + 1

    for stream in range(options.numOfStreams):
      for checksumSeqNum in checksumSeqNums:
        f.write(checksumSeqNum + " ")
      f.write("\n")
    f.close()
  elif c == 'x':
    break
