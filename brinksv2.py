import pyopencl as cl
import numpy as np

def encontrar_senha(key, alfa, length):
    ctx = cl.create_some_context()
    queue = cl.CommandQueue(ctx)

    combo = np.zeros(length, dtype=np.uint8)
    kernel = cl.Program(ctx, """
        __kernel void encontrar_senha(__global char* key, __global char* alfa, int length) {
            int i = get_global_id(0);
            for (int j = 0; j < length; j++) {
                combo[j] = alfa[i % length];
                i /= length;
            }
            if (combo == key) {
                return 1;
            }
            return 0;
        }
    """).build()

    evento = kernel.encontrar_senha(queue, (len(alfa) ** length,), None, key, alfa, length)
    resultado = evento.get()

    if resultado:
        print('Encontrei a senha')
    else:
        print('Palavra não encontrada')

def main():
    key = input('Digite uma palavra: ')
    alfa = (...)  # conjunto de caracteres
    length = len(key)

    encontrar_senha(key, alfa, length)

if __name__ == '__main__':
    main()
