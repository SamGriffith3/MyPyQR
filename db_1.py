from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
import getpass
import DateTime as Datetime
from sqlalchemy.ext.declarative import declarative_base

eng_local = ('sqlite:///C\\Users\\{}\\Documents\\Database\\db1.db').format(getpass.getuser())
engine = create_engine(eng_local)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    password = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', password='%s')>" % (self.name, self.password)

class Soaps(Base):
    __tablename__ = 'soaps'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(500))
    season = Column(String(50))
    date_created = Column(Datetime)
    wholesale = Column(Float)
    retail = Column(Float)
    batch_size = Column(Integer)
    recipe_link = Column(String(100))
    table_kids = relationship("Recipes", back_populates='soaps')

    def __repr__(self):
        return "<Soaps(name='%s', description='%s', season='%s', date_created='%s', wholesale='%s', retail='%s', " \
               "batch_size='%s', recipe_link='%s'>" %(self.name, self.description, self.season, self.date_created,
                                                      self.wholesale, self.retail, self.batch_size, self.recipe_link)

class Recipes(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    ingredients = Column(String(60))
    amounts = Column()
    soap_id = Column(Integer, ForeignKey('soaps.id'))
    cost_per = Column(Integer, ForeignKey('amounts.cost_per'))
    table_kids = relationship("Ingredients", "Amounts")

    def __repr__(self):
        return "<Recipes(soap_id='%s', ingredients='%s', amounts='%s')>" % (self.soap_id, self.ingredients,
                                                                             self.amounts)


class Ingredients(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    cost_per = Column(Float)

    def __repr__(self):
        return "<Ingredients(id='%s', name='%s', cost_per='%s')>" % (self.id, self.name, self.cost_per)

class Amounts(Base):
    __tablename__ = 'amounts'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))
    amount = Column(String(40))

    def __repr__(self):
        return "<Amounts(id='%s', recipe_id='%s', ingredient_id='%s', amount='%s')>" % (self.id, self.recipe_id,
               self.ingredient_id, self.amount)








