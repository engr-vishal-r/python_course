name='vIShal r'

print(f'LowerCase  : {name.lower()}')
print(f'UpperCase  : {name.upper()}')
print(f'UpperCase  : {name.capitalize()}')


mobile_num='8899990000'
masked_num=mobile_num[:2] #showing only first 2 digits
masked_newNum=mobile_num[:2] + '******' + mobile_num[-2:] #show first and last 2 digits


print(f'Printing only first 2 digits : {masked_num}')
print(f'Printing masked number : {masked_newNum}')


song='shape of you'
artist='vishal r'
formatted=f'{song.title()}  - {artist.title()}'

print('formatted string  : ' ,formatted)

destination='chennai'
default_location=destination.replace('chennai', 'vellore')
print('default location  : ' , default_location)


message='your booking ID: BK12345. Please keep it safe'
booking_id=message.split(":")[1].split(".")[0].strip() #split the string based on index and remove backspace using strip
print('booking id  : ', booking_id)


promo_message='use swiggy100 to get 100 off on your first order'

if 'swiggy100' in promo_message:
    print('Promo message found')
else:
    print('Promo message not found')

feedback="ride was good and car is in good condition"
print('position is  ', feedback.find('good'))

name_to_find_only_initials='vishal ramesh babu'
initialize=' '.join([word[0].upper() for word in name_to_find_only_initials.split( )])
print(initialize)