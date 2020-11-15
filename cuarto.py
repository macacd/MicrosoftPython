#Estrcuturas condicionales

canada = input('Eres de canada (Y/N)')

if canada.lower() == 'y' :
    provincia = input ('de que provincia?')
    if provincia.lower() in('alberta', 'nunavut','yukon'):
        tax = 0.5
    elif provincia.lower() == 'ontario' :
        tax = 0
else :
    tax = 0.15

print (f'La tasa de impuestos es {str(tax)}')


