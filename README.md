# ProjetoRedes

Alunos: Igor Hutson e Jhonnye Gabriel
Disciplina: Rede de Computadores
Professor: Leandro Sales
Curso: Engenharia de Computação

O projeto foi implementado em Python 3.7 numa implementação multi-thread em que podem ser abertas várias guias de terminal representando os clientes, desde que o servidor seja executado primeiro por meio do comando:

python server.py

Após isso, em outras abas do terminal, é possível executar o comando:

python client.py

Entres os comandos possíveis requisitados pelo cliente, deve ser usado no seguinte formato:

COMANDO:VALOR;VALOR;VALOR

Comandos: INCOME, REGISTRATION

Parâmetros:

- Income: Name, Value, Address 
- Registration: Name, Id, School

EX: INCOME:JHONNYE;1200.67;RUA NOVE

Em caso de erros ou sucesso no preenchimento dos parâmetros ou dos comandos, são exibidas mensagens de status com a possibilidade de um novo preenchimento.

Status registrados:

- 200: SUCESS
- 300: Command Error
- 301: Parameters Error
- 400: Disconnect

Para encerrar a comunicação com um dos clientes, basta escrever "exit" e uma mensagem de despedida será exibida. Mais detalhes podem ser encontrados no pdf em anexo.
