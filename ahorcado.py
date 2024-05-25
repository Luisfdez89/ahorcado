import random

class juegoAhorcado:
    ESTADOS = [
    r"""
     +--+
     |  |
        |
        |
        |
        |
    =====""",
    r"""
     +--+
     |  |
     O  |
        |
        |
        |
    =====""",
    r"""
     +--+
     |  |
     O  |
     |  |
        |
        |
    =====""",
    r"""
     +--+
     |  |
     O  |
    /|  |
        |
        |
    =====""",
    r"""
     +--+
     |  |
     O  |
    /|\ |
        |
        |
    =====""",
    r"""
     +--+
     |  |
     O  |
    /|\ |
    /   |
        |
    =====""",
    r"""
     +--+
     |  |
     O  |
    /|\ |
    / \ |
        |
    ====="""]

    SALVADO = [
    r"""
     +--+
        |
        |
    \O/ |
     |  |
    / \ |
    ====="""]

    Clase = 'FRUTAS'
    Palabra = 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE CEREZA CIRUELA FRESA GRANADA HIGO LIMA LIMON MANDARINA NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA '.split()


    def jugar(self):

        LetrasIncorrectas = []
        LetrasCorrectas = []
        secreto = random.choice(self.Palabra)

        while True:
            self.dibujar(LetrasIncorrectas,LetrasCorrectas,secreto)

            Letra = self.DimeLetra(LetrasIncorrectas + LetrasCorrectas)

            if Letra in secreto:

                LetrasCorrectas.append(Letra)


                Ganador = True
                for Solucion in secreto:
                    if Solucion not in LetrasCorrectas:
                        Ganador = False
                        break
                if Ganador:
                    print(self.SALVADO[0])
                    print('¡Bien hecho! la palabra secreta es :', secreto)
                    print('Has ganado!')
                    break
                    break
            else:
                LetrasIncorrectas.append(Letra)

                if len(LetrasIncorrectas) == len(self.ESTADOS)-1:
                    self.dibujar(LetrasIncorrectas,LetrasCorrectas,secreto)
                    print('Demasiados intentos!')
                    print('La palabra era "{}"'.format(secreto))
                    break


    def dibujar(self, LetrasIncorrectas, LetrasCorrectas, secreto):
        print(self.ESTADOS[len(LetrasIncorrectas)])
        print('La categoría es: ', self.Clase)
        print()

        print('Letras incorrectas: ', end='')
        for Letra in LetrasIncorrectas:
            print(Letra, end=' ')
        if len(LetrasIncorrectas) == 0 and 0 == len(LetrasIncorrectas):
            print('No hay letras incorrectas.')
        if len(LetrasIncorrectas) == len(LetrasIncorrectas)+1:
            print('Letras diferentes.')
        if len(LetrasIncorrectas) == len(LetrasIncorrectas) + 2:
            print('No coinciden.')



        print()

        Espacio = ['_']*len(secreto)

        for i in range(len(secreto)):
            if secreto[i] in LetrasCorrectas:
                Espacio[i] = secreto[i]

        print(' '.join(Espacio))


    def DimeLetra(self, LetraAdivinada):
        while True:
            print('Adivina una letra.')
            adivina = input('> ').upper()
            if len(adivina) != 1:
                print('Introduce una única letra.')
            elif adivina  in LetraAdivinada:
                print('Esa letra ya la sabías. Elige otra vez.')
            elif not  adivina.isalpha():
                print('Introduce una LETRA.')

            else:
                return adivina


if __name__ == '__main__':
    juego1=juegoAhorcado()
    juego1.jugar()

