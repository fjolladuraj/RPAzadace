IgracPrvi = input ('Unesi skare,papir,stijena,guster ili spock ')
IgracDrugi = input ('Unesi skare,papir,stijena,gusterili spock ')


if IgracPrvi =='skare' and IgracDrugi =='papir':
    print ('Skare režu papir. \nIgrač prvi je pobjedio!')
elif IgracPrvi == 'papir' and IgracDrugi == 'skare':
    print ('Skare rezu papir. \nIgrač drugi je pobjedio!')
elif IgracPrvi == 'papir' and IgracDrugi == 'stijena':
    print ('Papir prekriva stijenu. \nIgrač prvi je pobjedio!')
elif IgracPrvi == 'stijena' and IgracDrugi == 'papir':
    print ('Papir prekriva stijenu. \nIgrač drugi je pobjedio!')
elif IgracPrvi == 'stijena' and IgracDrugi == 'guster':
    print ('Stijena drobi gustera. \nIgrač prvi je pobjedio!')
elif IgracPrvi == 'guster' and IgracDrugi == 'stijena':
    print ('Stijena drobi guštera. \nIgrač drugi je pobjedio!')
elif IgracPrvi == 'papir' and IgracDrugi == 'stijena':
    print ('Papir prekriva stijenu. \nIgrač prvi je pobjedio!')
elif IgracPrvi == 'stijena' and IgracDrugi == 'papir':
    print ('Papir prekriva stijenu. \nIgrač drugi je pobjedio!')
elif IgracPrvi == 'guster' and IgracDrugi == 'spock':
    print ('Guster truje Spock. \nIgrač prvi je pobjedio!')
elif IgracPrvi == 'spock' and IgracDrugi == 'guster':
    print ('Guster truje Spock. \nIgrač drugi je pobjedio!')
elif IgracPrvi =='spock' and IgracDrugi == 'skare':
    print ('Spock razbija skare. \nIgrač prvi je pobjedio!')
elif IgracPrvi == 'skare' and IgracDrugi == 'spock':
    print ('Spock razbija skare. \nIgrač drugi je pobjedio!')
elif IgracPrvi == 'skare' and IgracDrugi == 'guster':
    print ('Skare obrubljuju guštera. \nIgrač prvi je pobjedio!')
elif IgracPrvi == 'guster' and IgracDrugi == 'skare':
    print ('Skare obrubljuju guštera. \nIgrač drugi je pobjedio!')
elif IgracPrvi == 'guster' and IgracDrugi == 'papir':
    print ('Guster jede papir. \nIgrač prvi je pobjedio!')
elif IgracPrvi == 'papir' and IgracDrugi == 'guster':
    print ('Guster jede papir. \nIgrač drugi je pobjedio!')
elif IgracPrvi == 'papir' and IgracDrugi == 'spock':
    print ('Papir opovrgava Spock. \nIgrač prvi je pobjedio!')
elif IgracPrvi == 'spock' and IgracDrugi == 'papir':
    print ('Papir opovrgava Spock. \nIgrač drugi je pobjedio!')
elif IgracPrvi == 'spock' and IgracDrugi == 'stijena':
    print ('Spock isparava stijenu. \nIgrač prvi je pobjedio!')
elif IgracPrvi == 'stijena' and IgracDrugi == 'spock':
    print ('Spock isparava stijenu. \nIgrač drugi je pobjedio!')
elif IgracPrvi == 'stijena' and IgracDrugi == 'skare':
    print ('Stijena drobi škare. \nIgrač prvi je pobjedio!')
elif IgracPrvi == 'skare' and IgracDrugi == 'stijena':
    print ('Stijena drobi škare. \nIgrač drugi je pobjedio!')
elif IgracPrvi == 'papir' and IgracDrugi == 'papir':
    print ('Neriješeno!')
elif IgracPrvi == 'stijena' and IgracDrugi == 'stijena':
    print ('Neriješeno!')
elif IgracPrvi == 'guster' and IgracDrugi == 'guster':
    print ('Neriješeno!')
elif IgracPrvi == 'skare' and IgracDrugi == 'skare':
    print ('Neriješeno!')
elif IgracPrvi == 'spock' and IgracDrugi == 'spock':
    print ('Neriješeno!')
else: 
    print ('Neispravne vrijednosti')