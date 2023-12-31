'''
>> Modbus TCP:
- Utilizar a biblioteca pyModbusTCP (instalar via pip install)
- O código de exemplo trabalha com os registradores de entrada e saída 0
- Em python, os objetos "server" e "server.data_bank" possuem os métodos para escrever e ler os registradores/bobinas (utilizar print(dir(server)) e print(dir(server.data_bank)) para visualizar os comandos)
'''

from pyModbusTCP.server import ModbusServer
from time import sleep


#Create an instance of ModbusServer
SERVER_ADDRESS = '10.103.16.152'
SERVER_PORT = 502
server = ModbusServer(SERVER_ADDRESS, SERVER_PORT, no_block = True)


try:
    print('Starting server...')
    server.start()
    print('Server is online')

    while True:

        with open("dados.txt", "r") as arquivo:
            linhas = []
            for linha in arquivo:
                linhas.append(linha.strip())

        drink = linhas[0]
        alcool = linhas[1]
        sabor = linhas[2]


        DATA_SENT_1 = [drink]
        DATA_RECEIVED_1 = server.data_bank.get_holding_registers(180)
        DATA_SENT_2 = [alcool]
        DATA_RECEIVED_2 = server.data_bank.get_holding_registers(181)
        DATA_SENT_3 = [sabor]
        DATA_RECEIVED_3 = server.data_bank.get_holding_registers(182)
        server.data_bank.set_input_registers(180, DATA_SENT_1)
        server.data_bank.set_input_registers(181, DATA_SENT_2)
        server.data_bank.set_input_registers(182, DATA_SENT_3)
        print('Data sent 1:', DATA_SENT_1)
        print('Data received 1:', DATA_RECEIVED_1)
        print('-----------------------')
        print('Data sent 2:', DATA_SENT_2)
        print('Data received 2:', DATA_RECEIVED_2)
        print('-----------------------')
        print('Data sent 3:', DATA_SENT_3)
        print('Data received 3:', DATA_RECEIVED_3)


        #Leitura dos sensor capacitivo
        data_receive_1 = server.get_holding(183)

        with open("dados2.txt", "w") as arquivo:
            
            #Com liquido
            if data_receive_1 == 1:
                arquivo.write(f"{data_receive_1}\n")
                
            #Sem liquido
            else:
                arquivo.write(f"{data_receive_1}\n")   



        sleep(0.5)
                    


except:
    print('Shutting down server...')
    server.stop()
    print('Server is offline')