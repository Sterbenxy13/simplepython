

from numpy import inf
from time import sleep

def check(input, classe , inicial , final = inf) :
    """\n
    - input   = um input do usário.
    - classe  = classe que o input vai receber ao ser retornado.
    (1 = int() ; 2 = float() ; 3 = str() ; 4 = True)
    - inicial = menor item dentre as opções válidas.
    - final   = maior item dentre as opções válidas. (padrão = infinito)

    Função que checa se um input faz parte das
    opções válidas, e se fazer parte, retorna o input
    com a classe escolhida no segundo parâmetro.
    """

    if input >= inicial :
        if input <= final :
            if classe == 1 :
                return int(input)
            if classe == 2 :
                return float(input)
            if classe == 3 :
                return str(input)
            if classe == 4 :
                return True
        else :
            input('Escolha uma opção válida.')
            return False
    else :
        input('Escolha uma opção válida.')
        return False

def reset(cont) :
    for c in range(cont) :
        print('Recomeçando')
        sleep(1)
        print('Recomeçando.')
        sleep(1)
        print('Recomeçando..')
        sleep(1)
        print('Recomeçando...')
        sleep(1)

def exit(cont) :
    for c in range (cont) :
        print('encerrando')
        sleep(1)
        print('encerrando.')
        sleep(1)
        print('encerrando..')
        sleep(1)
        print('encerrando...')
        sleep(1)

def cor(str = '' , t = 'none' , b = 'none') :
    corest = {'none':'' , 'black':30 , 'red':31 , 'green':32 , 'yellow':33 , 'blue':34 , 'magenta':35 , 'cyan':36 , 'white':37}
    coresb = {'none':'' , 'black':';40' , 'red':';41' , 'green':';42' , 'yellow':';43' , 'blue':';44' , 'magenta':';45' , 'cyan':';46' , 'white':';47'}



    return (f'\033[{corest[t]}{coresb[b]}m{str}\033[m')







print(cor('erro:' , 'red') , cor('tente inserir valores válidos'))
