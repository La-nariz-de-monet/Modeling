
rules = {}
rfile = open("Instructions.txt", "r")

for line in rfile:
    states = line.split(' ')
    if(states != ['\n']):
        read, write, move = states[1:4]
        next = states[4][:-1]
        print(states,read,write,move,next)
        if( states[0] in rules ):
            rules[states[0]][read] = { 'write' : write, 'move' : move, 'next': next }
        else:
            rules[states[0]] = { read : {} }
        rules[states[0]][read] = { 'write' : write, 'move' : move, 'next': next }

finish = false
tape = list('  1 1   ')
head = 3

while(!finish):
