def to_seconds(h, m, s):
    return h*3600+m*60+s

def read_hour():
    x = int(input('Enter hour: '))
    return x

def read_minute():
    x = int(input('Enter minute: '))
    return x

def read_second():
    x = int(input('Enter second: '))
    return x

def time_elapsed(start, finish):
    time_dis  = finish-start
    hr = time_dis//3600
    left = time_dis-3600*hr
    min = left//60
    left = left-min*60
    return f'{hr} hours {min} minutes {left} seconds.'

def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))
