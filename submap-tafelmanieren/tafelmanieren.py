import time

print('tafels')
nummer = int(input('kies van welk getal je de tafel wil weten '))
for i in range(1,11):
    time.sleep(0.2)
    print(i*nummer)

print('')

print('countdown')
for i in range(30,0,-1):
    time.sleep(1)
    print(i)
    if i == 1:
        print('lift off!')

print('')


print('hours of the day')
am = ':00 am'
pm = ':00 pm'
for i in range(0,25):
    time.sleep(0.2)
    if i < 13:
       print(str(i) + am)
    else:
        print(str(i) + pm)

print('')

print('20 tot 50 alleen even getallen')
for i in range(20,51,2):
    time.sleep(0.2)
    print(i)




