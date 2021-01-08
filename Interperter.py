
rules = {}
rfile = open("Instructions.txt", "r")

for line in rfile:
    states = line.split(' ')
    if(states != ['\n']):
        read, write, move = states[1:4]
        if(write == '_'):
            write = ' '
        if(read == '_'):
            read = ' '
        next = states[4][:-1]
        if( states[0] in rules ):
            rules[states[0]][read] = { 'write' : write, 'move' : move, 'next': next }
        else:
            rules[states[0]] = { read : {} }
        rules[states[0]][read] = { 'write' : write, 'move' : move, 'next': next }

finish = False
head = 2
state = '0'
print("Write two binary numbers separated by a space")
line = input()
tape = list('  '+str(line)+'  ')

while(not(finish)):
    print('State:',state,', head:', head-2, ', tape:', ''.join(tape[:head])+'|'+''.join(tape[head])+'|'+''.join(tape[head+1:]))
    read = tape[head]
    write = rules[state][read]['write']
    move = rules[state][read]['move']
    next = rules[state][read]['next']
    tape[head] = write
    if(move == 'r'):
        head += 1
    elif(move == 'l'):
        head -=1
    state = next
    if state == 'halt-accept':
        finish = True

print('\nFinish head:', head-2, ', tape:', ''.join(tape[:head])+'|'+''.join(tape[head])+'|'+''.join(tape[head+1:]))
