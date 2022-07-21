from sqlalchemy import Column, String, Integer, ForeignKey, Enum
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
    specie = Column(Enum(AnimalType),nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    def __rep__(self):
        return f"Pet: [name={self.name}, specie={self.specie}, user_id={self.user_id}]"