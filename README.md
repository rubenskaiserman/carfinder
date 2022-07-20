# Carfinder
### O meu projeto final da Matéria de Web avançado
Em poucas palavras: 
"peguei emprestado" os dados de mais de 14k carros de uma empresa britânica que vende bases de dados desses veículos. 
Construí um banco de dados PostgreSQL com essas informações. 
Depois fiz uma integração com Flask para construir a interface de uma aplicação web que permitisse a qualquer um fazer acesso á esses dados.


## A Proposta
Bom, a ideia da disciplina é que os estudantes desenvolvam um sistema web completo, e ao final do período o entreguem. 
No caso de minha turma, não houve muita restrição, bastava entregar um documento descrevendo a ideia do site, e caso aprovada pelo professor, os alunos poderiam à construir.

### A proposta desse trabalho:
Bom, para o meu trabalho final de web, foi proposto um sistema similar a uma search engine, tal qual o google. Porém, claro, bem mais rudimentar. 
Ao invés de pesquisar por páginas web indexadas na base de dados, o sistema proposto pesquisaria modelos de carros a partir de palavras chaves inseridas pelo usuário. 
Mostrando como resultado uma série de carros que se adequem a pesquisa, permitindo ao usuário que selecione aquele que mais se adequa a sua procura. 
Uma vez selecionando, seria aberta uma página que mostra uma descrição completa do veículo requisitado.

## Bom, uma vez aprovado. Hora de construir

### Bom, quero requisitar os dados de uma base de dados de carros, onde eu consigo essa base?!
- Primeiramente, é feita a clássica pesquisa para ver se existe alguma base disponível e de fácil acesso no google. Bom, claro que não sería tão fácil.
- Bom tem aquele site de data science cheio de bases de dados doidas, será que alguém montou uma base de dados sobre carros lá? Claro que não tem no keggle.
- Bom, pode ter alguém que nem eu que tava tentando construir esse sistema e colocou ele no github. Claro que não teve ninguém doido igual eu.
- Ok, deu tudo errado, hora de apelar. Vamos ter que achar algum site que dê essas informações de carros internamente, do jeito que eu estou tentando fazer. <br>
Irônicamente, achei razoavelmente fácil. Mais irônicamente ainda, achei um site britânico que não só disponibilizava os dados dos carros como também vendia bases de dados personalizadas.
Mas acontece que as informações no site deles estão de graça né... <br>

#### O resumo da óbra:
Após uma breve análise do site da tal empresa, percebi alguns padrões nas informações da arquitetura do site: <br>
- Cada modificação de carro possuía um identificador único enumerado de 1 até 19997. 
- Cada informação sobre os carros estava registrada dentro de uma tag <span> dentro de uma tabela.

Com essas informações em mente, basta criar um script de automação web que percorra o endereço da página, modificando apenas o id do carro referênciado na URL da página.
Ou seja, criando um loop que percorra de 1 até 19997, você está garantido de passar por todas as páginas.

A partir disso, utilizei as bibliotecas Selenium e Psycopg do Python para realizar a utomatização do processo de requisições Web, e registrar os dados em uma base de dados PostgreSQL respectivamente.
O código desse script pode ser encontrado em [bot.py](https://github.com/rubskaiserman/car_search/blob/main/data_science_stuff/data_getharing/bot.py).

Com acesso aos dados, agora é importante fazer uma limpeza e uma análise do que foi obtido, o processo foi feito utilizando a biblioteca Pandas, do Python.

### Tenho a base, hora de trabalhar no site.
O processo foi bem standard. Utilizei a biblioteca Flask do Python para construir a infraestrutura do backend da aplicação.
O sistema em si se baseia na requisição direta dos dados de id, imagem, nome, modelo e modificação para o banco a partir da conexão feita com a biblioteca Psycopg. Uma vez entregues os dados da pesquisa, é construída uma lista com todos os resultados.
Selecionado o carro desejado, o usuário envia outra requisição para o banco de dados, dessa vez requisitando todas as informações de um unico carro, derivada do id entregue na requisição anterior. Desse modo se economiza processamento no banco de dados para o caso de requisição de muitos carros.

O front-end das páginas foi construído utilizando jinja syntax somado a HTML e CSS puros. 

Esse foi meu trabalho final de Web avançado
