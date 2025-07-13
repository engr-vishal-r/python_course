amount=1200
tax=amount * 0.18
total=amount+tax
print(f'total amount without discount : {total} ')

if total > 1000:
    discount = total * 0.10
    total -=discount

print(f'total amount discount incl : {total} ')