import psycopg2


conn = psycopg2.connect(
    dbname='AtividadesBD',
    user='FelipeSouza14',        
    password='felipebd1234',      
    host='localhost',          
    port='5432'
)

cursor = conn.cursor()


# Inserir uma atividade em um projeto
inserir_nova_atividade = """
INSERT INTO atividades (nome, descricao, data_inicio, data_fim, projeto_id) 
VALUES (%s, %s, %s, %s, %s);
"""
dados_nova_atividade = ('Atividade A', 'Descrição da Atividade A', '2024-08-06', '2024-08-07', 1)
cursor.execute(inserir_nova_atividade, dados_nova_atividade)

conn.commit()

# Atualizando o lider do projeto
atualizar_lider = """
    UPDATE projetos 
    SET lider = %s 
    WHERE id = %s;
    """
novo_lider = ('Benicio', 1)
cursor.execute(atualizar_lider, novo_lider)

conn.commit()

cursor.execute("SELECT * FROM projetos ORDER BY id")

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("SELECT * FROM atividades ORDER BY id")

rows = cursor.fetchall()
for row in rows:
    print(row)

# Fechar a conexão
cursor.close()
conn.commit()
conn.close()
print("Conexão fechada.")



