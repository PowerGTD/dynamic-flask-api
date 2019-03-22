from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), unique=False, nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    
    def __repr__(self):
        return 'Item: %s (%s)' % (self.text, self.created_on)