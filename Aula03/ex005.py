segundos_base = int(input('Digite uma quantidade de segundos: '))
resto_horas = segundos_base%3600
horas = segundos_base//3600

minutos = resto_horas/60
resto_minutos = resto_horas%60

segundos = resto_minutos/60

print(f'{segundos_base} segundos = {horas} horas, {minutos} minutos e {segundos} segundos')

