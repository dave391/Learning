
#linea di codice per creare la lista di esecuzione, così da poter essere richiamata.

def somma (a:float,b:float):
    som=a+b
    print(som)
    return som

def sottrazione (a:float,b:float):
    sot=a-b
    print(sot)
    return sot

def main():
    a=5
    b=6
    somma(a,b)
    sottrazione(a,b)


if __name__=="__main__":
    main()