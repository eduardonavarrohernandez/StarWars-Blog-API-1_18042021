from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Models):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    mail = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Personajes(db.Models):
    __tablename__ = 'personajes'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)

class Planetas(db.Models):
    __tablename__ = 'planetas'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)


class Favoritos(db.Models):
    __tablename__ = 'favoritos'

    id = Column(Integer, primary_key=True)

    User_id = Column(Integer, ForeignKey('user.id'))
    User = relationship(User)
    tipoFavorito = Column(String(250), nullable=False)
    favoritoId = Column(String(250), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }