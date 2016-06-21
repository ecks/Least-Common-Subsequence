import subprocess
import sys

f1 = open('run_1', 'w')
f2 = open('run_2', 'w')

process = subprocess.Popen(['python', 'input_generator.py', '-n', '5', '-w', '20', '-o', 'input'], stdin=subprocess.PIPE)
for p in range(4):
  for e in range(4):
    for l in range(4):
      for d in range(4):
        process.stdin.write('c')
        pProb = str(p*0.20)
        eProb = str(e*0.20)
        lProb = str(l*0.20)
        dProb = str(d*0.20)
        subprocess.call(['python', 'randomize.py', '-i', 'input', '-o', 'input_1', '-p', pProb, '-P', pProb, '-e', eProb, '-E', eProb, '-l', lProb, '-L', lProb, '-d', dProb, '-D', dProb])
        subprocess.call(['python', 'queue_clear_stream.py', '-i', 'input_1', '-o', 'vote_1'])
        subprocess.call(['python', 'queue_clear_all.py', '-i', 'input_1', '-o', 'vote_2'])
        p1 = subprocess.Popen(['python', 'metric.py', '-i', 'input', '-I', 'vote_1'], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['python', 'metric.py', '-i', 'input', '-I', 'vote_2'], stdout=subprocess.PIPE)
        p1_output = p1.stdout.read()
        p2_output = p2.stdout.read()
        if p1_output != p2_output:
          sys.stdout.write('clear stream with p ' + pProb + ' e ' + eProb + ' l ' + lProb + ' d ' + dProb + ' : ' + p1_output)
          sys.stdout.write('clear all with p ' + pProb + ' e ' + eProb + ' l ' + lProb + ' d ' + dProb +  ' : ' + p2_output)
        f1.write(p1_output)
        f2.write(p2_output)
#        subprocess.call(['cp', 'input', 'perf_inp_'+pProb+'_'+eProb+'_'+lProb+'_'+dProb])
#        subprocess.call(['cp', 'input_1', 'input_'+pProb+'_'+eProb+'_'+lProb+'_'+dProb])
process.stdin.write('x')
