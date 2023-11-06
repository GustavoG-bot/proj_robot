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

        with open("valor_var_1.txt", "r") as file:
            conteudo = file.read()
            valor_lido = int(conteudo)

        DATA_SENT_1 = [conteudo]
        DATA_RECEIVED_1 = server.data_bank.get_holding_registers(180)
        server.data_bank.set_input_registers(180, DATA_SENT_1)
        print('Data sent:', DATA_SENT_1)
        print('Data received:', DATA_RECEIVED_1)
        sleep(0.5)

except:
    print('Shutting down server...')
    server.stop()
    print('Server is offline')