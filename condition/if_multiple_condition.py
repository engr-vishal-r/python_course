ordered_amount =10000
days='friday'
has_membership=False


if(ordered_amount >=10000 and days in ['sat', 'sun']) or has_membership == True:
    print('20% discount')
else:
    print('discounts not applicable')