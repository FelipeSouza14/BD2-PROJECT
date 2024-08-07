from sqlalchemy import create_engine, Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Configuração do banco de dados
DATABASE_URL = 'postgresql://FelipeSouza14:felipebd1234@localhost:5432/AtividadesBD'

# Criar engine e base
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Definir as classes para as tabelas
class Projeto(Base):
    __tablename__ = 'projetos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(Text)
    lider = Column(String(100))
    atividades = relationship("Atividade", back_populates="projeto")

class Atividade(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(Text)
    data_inicio = Column(Date)
    data_fim = Column(Date)
    projeto_id = Column(Integer, ForeignKey('projetos.id'))
    projeto = relationship("Projeto", back_populates="atividades")

# Criar a sessão
Session = sessionmaker(bind=engine)
session = Session()

# # Inserir uma atividade em um projeto
# nova_atividade = Atividade(
#     nome='Atividade B',
#     descricao='Descrição da Atividade B',
#     data_inicio='2024-08-06',
#     data_fim='2024-08-07',
#     projeto_id=1
# )
# session.add(nova_atividade)
# session.commit()

projeto = session.query(Projeto).filter_by(id=1).first()
if projeto:
    projeto.lider = 'Felipe'
    session.commit()
    print("Líder atualizado com sucesso!")
else:
    print("Projeto não encontrado.")

