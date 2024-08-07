# Resumo sobre ODBC
ODBC (Open Database Connectivity) em Python oferece uma maneira padronizada de se conectar e interagir com vários bancos de dados, independentemente do sistema de gerenciamento utilizado. Utilizando bibliotecas como psycopg2, é possível acessar bancos de dados como SQL Server, PostgreSQL e MySQL através de drivers ODBC apropriados. Essa API fornece uma abordagem consistente para executar comandos SQL e gerenciar dados, o que simplifica a integração e a migração de dados entre diferentes sistemas e aplicativos. ODBC é particularmente útil quando se trabalha com diversos tipos de bancos de dados, oferecendo um método uniforme para comunicação e manipulação de dados.

# Resumo sobre ORM
ORM (Object-Relational Mapping) em Python é uma técnica que permite interagir com bancos de dados relacionais usando uma abordagem orientada a objetos. Em vez de escrever diretamente consultas SQL para manipular dados, o ORM mapeia as tabelas do banco de dados para classes Python e as linhas das tabelas para instâncias dessas classes. Isso simplifica a manipulação dos dados e melhora a legibilidade e manutenção do código, permitindo que os desenvolvedores trabalhem com objetos e atributos em vez de lidar com SQL cru.

O SQLAlchemy é um dos frameworks ORM mais populares em Python. Ele oferece uma API poderosa para a criação e manipulação de objetos relacionados a bancos de dados. O SQLAlchemy suporta tanto a abordagem de mapeamento declarativo, onde você define classes Python que correspondem às tabelas do banco de dados, quanto a abordagem de mapeamento programático, oferecendo flexibilidade para diferentes estilos de desenvolvimento.

Além do ORM, o SQLAlchemy inclui um conjunto de ferramentas para construção de consultas SQL e gerenciamento de transações, proporcionando uma interface robusta para acessar e manipular dados. Ele é amplamente adotado por sua capacidade de suportar uma ampla variedade de bancos de dados e sua integração com outras bibliotecas Python, tornando-o uma escolha versátil e eficaz para projetos de banco de dados em Python.

# Scripts
[ODBC](https://github.com/FelipeSouza14/BD2-PROJECT/blob/main/tarefas/orm/script-odbc.py)
</br>

[ORM](https://github.com/FelipeSouza14/BD2-PROJECT/blob/main/tarefas/orm/script-orm.py)