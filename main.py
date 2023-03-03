a=int(input('введите номер места в вагоне'))
print()
if a>36 and a%2:
    print('боковое место сверху')
elif a>36 and a!=a%2:
    print('боковое место сверху')
elif a<36 and a%2:
    print('купе сверху')
else:
    print('купе сверху')