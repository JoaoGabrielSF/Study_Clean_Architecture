from sqlalchemy import Column, String, Integer, ForeignKey
from src.infra.config import Base
import enum

class AnimalType(enum.Enum):
    """ Defining AnimalType """
    
    dog = 'dog',
    cat = 'cat',
    fish = 'fish',
    turtle = 'turtle'
    
    
class Pets(Base):
    """ Pets Entity """
   
    __tablename__ = "pets"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)