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
        ====="""
    ]

    SALVADO = [
        r"""
         +--+
            |
            |
        \O/ |
         |  |
        / \ |
        ====="""
    ]

    Clases = ['FRUTAS', 'ANIMALES', 'POKEMON']

    Frutas = 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE CEREZA CIRUELA FRESA GRANADA HIGO LIMA LIMON MANDARINA NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA '.split()
    Animales = 'PERRO GATO LEON TIGRE ELEFANTE JIRAFA CANGURO CEBRA OSO MONO '.split()
    Pokemon = 'PIKACHU CHARIZARD BULBASAUR SQUIRTLE MEWTWO EEVEE JIGGLYPUFF SNORLAX LUCARIO GENGAR '.split()

    def jugar(self):
        NombreJugador = input('Dame tu nombre: ')
        LetrasIncorrectas = []
        LetrasCorrectas = []

        categoria = random.choice(self.Clases)
        if categoria == 'FRUTAS':
            secreto = random.choice(self.Frutas)
        elif categoria == 'ANIMALES':
            secreto = random.choice(self.Animales)
        elif categoria == 'POKEMON':
            secreto = random.choice(self.Pokemon)

        while True:
            self.dibujar(LetrasIncorrectas, LetrasCorrectas, secreto)
            IntentosRestantes = self.IntentosRestantes(LetrasIncorrectas)
            print(f'Te quedan {IntentosRestantes} intentos.')

            Letra = self.DimeLetra(LetrasIncorrectas + LetrasCorrectas)

            if Letra == "TERMINAR":
                print(self.ESTADOS[-1])
                print('Has terminado el juego')
                print('La palabra era "{}"'.format(secreto))
                break

            if Letra in secreto:
                LetrasCorrectas.append(Letra)
                Ganador = True
                for Solucion in secreto:
                    if Solucion not in LetrasCorrectas:
                        Ganador = False
                        break
                if Ganador:
                    print(self.SALVADO[0])
                    print(f'¡Bien hecho! La palabra secreta es: {secreto}')
                    print(f'¡Has ganado, {NombreJugador}!')
                    break

            else:
                LetrasIncorrectas.append(Letra)

                if len(LetrasIncorrectas) == len(self.ESTADOS) - 1:
                    self.dibujar(LetrasIncorrectas, LetrasCorrectas, secreto)
                    print('Demasiados intentos!')
                    print(f'La palabra era "{secreto}"')
                    break

    def dibujar(self, LetrasIncorrectas, LetrasCorrectas, secreto):
        print(self.ESTADOS[len(LetrasIncorrectas)])
        print()

        print('Letras incorrectas:', end=' ')
        for Letra in LetrasIncorrectas:
            print(Letra, end=' ')
        if len(LetrasIncorrectas) == 0 and 0 == len(LetrasIncorrectas):
            print('No hay letras incorrectas.')
        if len(LetrasIncorrectas) == len(LetrasIncorrectas) + 1:
            print('Letras diferentes.')
        if len(LetrasIncorrectas) == len(LetrasIncorrectas) + 2:
            print('No coinciden.')

        print()

        Espacio = ['_'] * len(secreto)

        for i in range(len(secreto)):
            if secreto[i] in LetrasCorrectas:
                Espacio[i] = secreto[i]

        print(' '.join(Espacio))

    def DimeLetra(self, LetraAdivinada):
        while True:
            print('Adivina una letra, o escribe "TERMINAR" para finalizar el juego')
            adivina = input('> ').upper()
            if adivina == "TERMINAR":
                return adivina
            elif len(adivina) != 1:
                print('Introduce una única letra.')
            elif adivina in LetraAdivinada:
                print('Esa letra ya la sabías. Elige otra vez.')
            elif not adivina.isalpha():
                print('Introduce una LETRA.')
            else:
                return adivina

    def IntentosRestantes(self, LetrasIncorrectas):
        return len(self.ESTADOS) - 1 - len(LetrasIncorrectas)


if __name__ == '__main__':
    juego1 = juegoAhorcado()
    juego1.jugar()
