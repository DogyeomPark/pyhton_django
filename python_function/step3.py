price = 10000
vat_rate = 0.1
print(price*vat_rate)

print('----------')

def get_vat():
    price = 10000
    vat_rate = 0.1
    print(price * vat_rate)
get_vat()

print('----------')

def get_vat(price):
    vat_rate = 0.1
    print(price * vat_rate)
get_vat(10000)
get_vat(20000)

print('----------')

def get_vat(price, vat_rate):
    print(price * vat_rate)
get_vat(10000, 0.2)
get_vat(20000, 0.3)

print('----------')

def get_vat(price, vat_rate=0.1):
    print(price * vat_rate)
get_vat(10000)
get_vat(20000,0.3)

print('----------')

def get_vat(price, vat_rate=0.1):
    return price * vat_rate
print(get_vat(10000))
get_vat(20000, 0.3)