ålder = int(input('hur gammal är du?'))

if ålder == 17:
    print('du är lika gammal som de flesta i EE25')

if ålder != 43:
    print('du är inte lika gammal som per')
else:
    print('du är lika gammal som per')
    
if ålder <= 13:
    print('du är väldigt ung')
elif ålder < 18:
    print('du får inte ta körkort')
elif ålder < 20:
    print('du får ta körkort')
else:
    print('du får handla på systembolaget')
    
if ålder == -1:
    print('du finns inte ens')
    
namn = input('vad är ditt namn')

if namn == 'Ebbe':
    print('kung')
elif namn == 'eEbb':
    print('så stavas det inte')
else:
    print('varför heter du inte Ebbe')

if ålder == 17 and namn =='Ebbe':
    print('du måste vara Ebbe')