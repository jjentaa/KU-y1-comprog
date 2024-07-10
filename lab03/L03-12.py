def eat(S=197,P=70,G=11):
    pp = S//P
    leftt = S%P
    gg = leftt//G
    leftt = leftt%G
    return (pp, gg, leftt)

s = int(input('Input starting food (S): '))
p = int(input("Input Paun's eating rate (P): "))
g = int(input("Input Gane's eating rate (G): "))
ans = eat(s, p, g)
print(f'Paun eats {ans[0]} time(s)\nGane eats {ans[1]} time(s)\nRemaining {ans[2]} for dog')