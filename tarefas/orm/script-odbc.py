import psycopg2


conn = psycopg2.connect(
    dbname='AtividadesBD',
    user='FelipeSouza14',        # substitua pelo seu usuário
    password='sua_senha',      # substitua pela sua senha
    host='localhost',          # ou o IP do contêiner, se for diferente
    port='5432'
)

cur = conn.cursor()


