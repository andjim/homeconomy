from src.server import  db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True,  nullable=False)
    password = db.Column(db.String(30), unique=True,  nullable=False)

    def __repr__(self):
        return '<User id=%d >' % self.id
