from computadora import Computer
from teclado import Teclado
from raton import Raton
from orden import Orden
from monitor import Monitor



def showMenu():
    print('''

        Bienvenido al sistema de computadoras
        0 PARA CALULCULAR EL PRECIO DE UNA ORDEN

''')

def captureUserOption():
    return int(input('Ingresa una opcion: '))

def captureRaton():
    print('Ingresa la informacion del raton'.center(50,'-'))
    typeInput=input('Ingresa el tipo de entrada: ')
    mark=input('Ingresa la marca: ')
    return Raton(typeInput,mark)
def captureTeclado():
    print('Ingresa la informacion del teclado'.center(50,'-'))
    typeInput=input('Ingresa el tipo de entrada: ')
    mark=input('Ingresa la marca: ')
    return Teclado(typeInput,mark)
def captureMonitor():
    print('Ingresa la informacion de la pantalla'.center(50,'-'))
    mark=input('Ingresa la marca: ')
    sizeComputer=float(input('Ingresa el tamanio de la pantalla: '))
    return Monitor(mark,sizeComputer)
def captureComputer():
    print('Ingresa la informacion de la computadora'.center(50,'-'))
    price=int(input('Ingresa el precio: '))
    name=input('Ingresa el nombre: ')
    monitor=captureMonitor()
    raton=captureRaton()
    teclado=captureTeclado()
    return Computer(monitor,raton,teclado,price,name)

def main():
    while True:
        showMenu()
        try:
            option=captureUserOption()
        except Exception:
            print('Opcion no valida')
        else:
            if option==0:
                totalAmount=orden.getTotalPrice()
                print(f'El total de la orden es de {totalAmount:.2f}')
                break
            else:
                orden=Orden()
                computer=captureComputer()
                computers=list([computer])
                orden=Orden(computers)
        
if __name__=='__main__':
    main()