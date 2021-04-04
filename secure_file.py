import sys

import pyAesCrypt

bufferSize = 64 * 1024


def encrypt(senha, arquivo):
    pyAesCrypt.encryptFile("{}.txt".format(arquivo), "{}.f1t4".format(arquivo), senha, bufferSize)
    print("Arquivo {}.txt Encriptado com Sucesso!".format(arquivo))


def decrypt(senha, arquivo):
    pyAesCrypt.decryptFile("{}.f1t4".format(arquivo), "{}.txt".format(arquivo), senha, bufferSize)
    print("Arquivo {}.f1t4 Desencriptado com Sucesso!".format(arquivo))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("*** Encryptador de Arquivos TXT ***")
        print("Para Encryptar: >>> python secure_file.py encrypt <senha> <filename_sem_extensão>")
        print("Para Desencryptar: >>> python secure_file.py decrypt <senha> <filename_sem_extensão>")
        print("EX: python secure_file.py encrypt senhafoda arquivodetexto")
    elif len(sys.argv) > 4:
        print("Passagem de argumentos inválida...")
    else:
        if sys.argv[1] == "encrypt":
            try:
                print("Encriptando {}.txt...".format(sys.argv[3]))
                encrypt(sys.argv[2], sys.argv[3])
            except ValueError:
                print("Arquivo {}.txt não encontrado".format(sys.argv[3]))
        elif sys.argv[1] == "decrypt":
            try:
                print("Desencryptando {}.f1t4...".format(sys.argv[3]))
                decrypt(sys.argv[2], sys.argv[3])
            except ValueError as erro:
                print("Erro:", erro)
        else:
            print("Erro: Primeiro argumento deve ser <encrypt> ou <decrypt>...")
            print("Ex: python secure_file.py encrypt senha arquivo")
