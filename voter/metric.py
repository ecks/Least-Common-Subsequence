import random
import optparse

def levenshtein(A, B):
  D = []

  for i in range(len(A)+1):
    D.append([])
    for j in range(len(B)+1):
      D[i].append(0)

  for i in range(len(A)+1):
    D[i][0] = i

  for j in range(len(B)+1):
    D[0][j] = j

  for j in range(len(B)):
    for i in range(len(A)):
      if A[i] == B[j]:
        D[i+1][j+1] = D[i][j]
      else:
        D[i+1][j+1] = min(
                        D[i][j+1] + 1,
                        D[i+1][j] + 1,
                        D[i][j] + 1)
  return D[len(A)][len(B)]


parser = optparse.OptionParser()
parser.add_option("-i", "--perf_input", action="store", type="string", dest="perf_input",
                  help="perfect input filename", metavar="PERFECT INPUT")
parser.add_option("-I", "--ans_input", action="store", type="string", dest="ans_input",
                  help="answer input filename", metavar="ANSWER INPUT")
parser.add_option("-o", "--output", action="store", type="string", dest="output",
                  help="output filename", metavar="OUTPUT")

(options, args) = parser.parse_args()

fp = open(options.perf_input, 'r')
fa = open(options.ans_input, 'r')

voted_ans = fa.read().split()

s = []

for line in fp:
  s.append(line)

perf_ans = random.sample(s, 1)[0].split()

print str(levenshtein(voted_ans, perf_ans))
