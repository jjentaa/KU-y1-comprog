def caltime(t_n):
    t = t_n
    hr = t//3600
    t = t%3600
    m = t//60
    t = t%60
    return (hr, m, t)

s = int(input('s: '))
ans = caltime(s)
print(f'{s} seconds equals {ans[0]} hour(s) {ans[1]} minute(s) and {ans[2]} second(s)')