#One-Liner with Math Trick (Digital Root Formula)
def digital_root(num):
    return 1 + (num - 1) % 9 if num > 0 else 0

print('Final digit sum  :', digital_root(2885)) 