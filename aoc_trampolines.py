''' Implementation of trampoline processing for AoC 2017 Day 5 '''
def trampolines(input_data):
    ''' Take a list of jumps as input, then process until it's out of the list. '''
    count = 0
    curr = 0
    nxt = 0
    end = len(input_data)

    while nxt < end:
        count += 1
        nxt = input_data[curr] + curr
        input_data[curr] += 1
        curr = nxt
    return count

def trampolines_2(input_data):
    ''' Take a list of jumps as input, then process until it's out of the list. '''
    count = 0
    curr = 0
    nxt = 0
    end = len(input_data)
    max = -1
    while nxt < end:
        count += 1
        if max < curr:
            max = curr
            print('highest idx has been [{}]'.format(max))
        nxt = input_data[curr] + curr
        if input_data[curr] > 2:
            input_data[curr] -= 1
        else:
            input_data[curr] += 1
        curr = nxt

    return count



if __name__ == '__main__':
    print('Hello world again!')

    with open('./input_data', 'r') as f:
        _data = f.read()
        _data = list(map(int, _data.split()))
    t1 = trampolines(_data)
    print('T1 is {}'.format(t1))

    with open('./input_data', 'r') as f:
        _data = f.read()
        _data = list(map(int, _data.split()))
    t2 = trampolines_2(_data)
    print('T2 is {}'.format(t2))

