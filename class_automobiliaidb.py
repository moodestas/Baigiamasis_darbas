from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///automobiliaidb.db')
Base = declarative_base()

class AutomobiliaiDb(Base):
    __tablename__ = 'Automobiliai'
    id = Column(Integer, primary_key=True)
    marke = Column("Markė", String)
    modelis = Column("Modelis", String)
    kebulas = Column("Kėbulas", String)
    rida = Column("Rida", Integer)
    variklio_turis = Column("Variklio tūris", Integer)
    gamybos_metai = Column("Gamybos metai", Integer)
    kuro_tipas = Column("Kuro tipas", String)
    pavaru_deze = Column("Pavarų dėžė", String)
    trukumai = Column("Trūkumai", String)
    kaina = Column("Kaina", Integer)
    rinkos_verte = Column("Rinkos vertė: ", Integer)

    def __init__(self, marke, modelis, kebulas, rida, variklio_turis, gamybos_metai, kuro_tipas, pavaru_deze, trukumai,
                 kaina, rinkos_verte):
        self.marke = marke
        self.modelis = modelis
        self.kebulas = kebulas
        self.rida = rida
        self.variklio_turis = variklio_turis
        self.gamybos_metai = gamybos_metai
        self.kuro_tipas = kuro_tipas
        self.pavaru_deze = pavaru_deze
        self.trukumai = trukumai
        self.kaina = kaina
        self.rinkos_verte = rinkos_verte

    def __repr__(self):
        return f"{self.id} {self.marke} {self.modelis}, {self.kebulas}, {self.rida} km, {self.variklio_turis} l, " \
               f"{self.gamybos_metai} m, {self.kuro_tipas}, {self.pavaru_deze}, {self.trukumai}, {self.kaina} €, " \
               f"rinkos vertė {self.rinkos_verte} €"


Base.metadata.create_all(engine)
