'''
>> Modbus TCP:
- Utilizar a biblioteca pyModbusTCP (instalar via pip install)
- O código de exemplo trabalha com os registradores de entrada e saída 0
- Em python, os objetos "server" e "server.data_bank" possuem os métodos para escrever e ler os registradores/bobinas (utilizar print(dir(server)) e print(dir(server.data_bank)) para visualizar os comandos)
'''

from pyModbusTCP.server import ModbusServer
from time import sleep


#Create an instance of ModbusServer
SERVER_ADDRESS = '10.103.16.173'
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



        DATA_SENT_1 = [drink]
        DATA_SENT_2 = [alcool]


        DATA_RECEIVED_1 = server.data_bank.get_holding_registers(180)
        DATA_RECEIVED_2 = server.data_bank.get_holding_registers(181)
        #DATA_RECEIVED_3 = server.data_bank.get_holding_registers(182)
        DATA_RECEIVED_4 = server.data_bank.get_holding_registers(330)
    
    
        server.data_bank.set_input_registers(180, DATA_SENT_1)
        server.data_bank.set_input_registers(181, DATA_SENT_2)
        #server.data_bank.set_input_registers(182, DATA_SENT_3)
        
        print('Data sent 1:', DATA_SENT_1)
        print('Data received 1:', DATA_RECEIVED_1)
        print('-----------------------')
        print('Data sent 2:', DATA_SENT_2)
        print('Data received 2:', DATA_RECEIVED_2)
        print('-----------------------')
        print('-----------------------')
        print('Data received 4:', DATA_RECEIVED_4)


        with open("dados2.txt", "w") as arquivo2:
            if DATA_RECEIVED_4[0] == 1:
                arquivo2.write("1")
            else:
                arquivo2.write("0")   
        sleep(0.5)
                    
except:
    print('Shutting down server...')
    server.stop()
    print('Server is offline')