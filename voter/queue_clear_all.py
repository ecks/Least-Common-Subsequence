import optparse
import time

def dataInStreams(streams):
  return all(streams)

def numOfMessages(m, foq):
  n = 0
  for p in foq:
    if m[1] == p[1]:
      n = n+1
  return n

def removeFromFoq(m, foq):
  i = 0
  while i < len(foq):
    if m[1] == foq[i][1]:
      foq.remove(foq[i])  
    elif m[0] > foq[i]:
      foq.remove(foq[i][1])
    else:
      i = i + 1
  return foq

def vote(foq, numOfStreams, left_behind, fo):
#  print "intide vote " + str(foq)
#  print "inside vote " + str(left_behind)
  list_to_check = []
  if foq:
    list_to_check.extend(foq)
  if left_behind:
    list_to_check.extend(left_behind)
  for m in list_to_check:
    if float(numOfMessages(m, list_to_check))/float(numOfStreams) > float(1)/float(2):
#      print m
      fo.write(m[1] + ' ')
      list_to_check = removeFromFoq(m, list_to_check)
      foq = removeFromFoq(m, foq)
      left_behind = []
  if left_behind:
    foq.extend(left_behind)
  return foq

def make_stamp(msg):
  return (time.time(), msg)

parser = optparse.OptionParser()
parser.add_option("-i", "--input", action="store", type="string", dest="input",
                  help="input filename", metavar="INPUT")
parser.add_option("-o", "--output", action="store", type="string", dest="output",
                  help="output filename", metavar="OUTPUT")

(options, args) = parser.parse_args()

fi = open(options.input, 'r')
fo = open(options.output, 'w')

streams = []
numOfStreams = 0
for line in fi:
  streams.append(line.split())
  numOfStreams = numOfStreams + 1

left_behind = []
while dataInStreams(streams):
  foq = []
  for stream in streams:
    head = stream.pop(0)
    if head != 'x':
      foq.append(make_stamp(head))
  left_behind = vote(foq, numOfStreams, left_behind, fo)
#  print "outside vote " + str(left_behind)
