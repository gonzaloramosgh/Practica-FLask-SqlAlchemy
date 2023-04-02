from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gonza.db'
app.config['SQLALCHEMY_DATA_TRACK'] = False

db = SQLAlchemy(app)
app.app_context().push()

class Socio(db.Model):

    __tablename__ = 'Socio'
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    apellido = db.Column(db.String(30),nullable=False)

    def __repr__(self):
        return f'Socio Nombre {self.name} , ID: {self.id}'


@app.route('/' , methods=['GET','POST'] )
def index():
    try:
        nom = request.form.get('nombre')
        apell=request.form.get('apellido')
        nuevo=Socio(name=nom ,apellido=apell)
        db.session.add(nuevo)
        db.session.commit()
        db.session.close()
    finally:
        return render_template('index.html')

#if __name__ == '__main__':
#    app.run(debug=True)
