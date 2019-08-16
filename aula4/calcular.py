import datetime

dia = input('Digite o dia que vocẽ nasceu')
mes = input('Digite o mes que voce nasceu')
ano = input('Digite o ano em que você nasceu')

total = datetime.date(year=ano,day=dia,month=mes)

def calcular_dias(data):
    if data in None:
        error='ops'
        return error

    hoje = datetime.date.today()
    dias_de_vida = hoje - data
    return dias_de_vida

retorno = calcular_dias(total)
print(retorno)
