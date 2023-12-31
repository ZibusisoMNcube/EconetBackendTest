import os

from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shopname = db.Column(db.String(100), nullable=False)
    areaname = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    areacode = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    desc = db.Column(db.Text)

     def __repr__(self):
            return f'<Shop {self.shopname}>'

#displaying shops
@app.route('/')
def index():
    areas = Shop.query.all()
    return render_template('index.html', areas=areas)


#inputing shops    
@app.route('/create/', methods=('GET', 'POST'))
def create():
    def create():
        if request.method == 'POST':
            shopname = request.form['shopname']
            areaname = request.form['areaname']
            city = request.form['city']
            areacode = request.form['areacode']
            desc = request.form['desc']
            shop = Shop(shopname=shopname,
                              areaname=areaname,
                              city=city,
                              areacode=areacode,
                              desc=desc)
            db.session.add(shop)
            db.session.commit()
    
            return redirect(url_for('index'))

    return render_template('create.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)