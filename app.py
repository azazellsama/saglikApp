import sqlalchemy.exc
from flask import Flask, redirect, jsonify
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///digin.db'
db = SQLAlchemy(app)

class User(db.Model):
    userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userMail = db.Column(db.String(250), nullable=False)
    userPass = db.Column(db.String(250), nullable=False)


# class Restaurant(db.Model):
    # restId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # restName = db.Column(db.String(250), nullable=False)
    # restPhone = db.Column(db.Integer, unique=False, nullable=False)
    # restMail = db.Column(db.String(250), unique=True, nullable=False)
    # restPass = db.Column(db.String(250), nullable=False)
    # restAddress = db.Column(db.String(250), nullable=False)


# class Menu(db.Model):
    # menuId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # menuName = db.Column(db.String(250), nullable=False)
    # menuPhoto = db.Column(db.Text, nullable=True)
    # restOfMenu = db.Column(db.Integer, db.ForeignKey('restaurant.restId'), nullable=False)


# class Products(db.Model):
    # prodId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # prodName = db.Column(db.String(250), nullable=False)
    # prodPrice = db.Column(db.Integer, nullable=False)
    # prodPhoto = db.Column(db.Text, nullable=True)
    # restOfProd = db.Column(db.Integer, db.ForeignKey('menu.menuId'), nullable=False)


# class Ingredients(db.Model):
    # ingredId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # ingred01 = db.Column(db.String(50), nullable=True)
    # ingred02 = db.Column(db.String(50), nullable=True)
    # ingred03 = db.Column(db.String(50), nullable=True)
    # ingred04 = db.Column(db.String(50), nullable=True)
    # ingred05 = db.Column(db.String(50), nullable=True)
    # ingred06 = db.Column(db.String(50), nullable=True)
    # ingred07 = db.Column(db.String(50), nullable=True)
    # ingred08 = db.Column(db.String(50), nullable=True)
    # ingred09 = db.Column(db.String(50), nullable=True)
    # ingred10 = db.Column(db.String(50), nullable=True)
    # ingred11 = db.Column(db.String(50), nullable=True)
    # ingred12 = db.Column(db.String(50), nullable=True)
    # ingred13 = db.Column(db.String(50), nullable=True)
    # ingred14 = db.Column(db.String(50), nullable=True)
    # ingred15 = db.Column(db.String(50), nullable=True)
    # prodOfIng = db.Column(db.Integer, db.ForeignKey('products.prodId'), nullable=False)


# class Customer(db.Model):
    # custDesk = db.Column(db.Integer, primary_key=True, nullable=False)
    # custBasket = db.Column(db.String(250), unique=False, nullable=True)
    # custPOrders = db.Column(db.String(250), unique=False, nullable=True)
    # custCheck = db.Column(db.Integer, unique=False, nullable=True)
    # custRest = db.Column(db.Integer, db.ForeignKey('restaurant.restId'), nullable=False)


db.create_all()


@app.route('/login', methods=['GET', 'POST'])
def login():
    # items = Diginadmin(amail='anjul@ad.com', apassword='123456')
    admin = User(userMail="admin", userPass="123456")

    db.session.add(admin)
    db.session.commit()
    
    gelenData = request.get_json()
    
    userMail = gelenData.get("username", "")
    userPass = gelenData.get("password", "")
    
    validatePass = User.query.filter(User.userMail == userMail).first()
    

    if validatePass.userPass == userPass:
        return jsonify({"name":"Abdullah","surName":"Gökmen"}), 200
    return jsonify({"isSuccess":False}), 401
    
    # db.session.add(items)
    # db.session.commit()
    return render_template('index.html')


# @app.route('/login/', methods=['GET', 'POST'])
# def login():
    # if request.method == "GET":
        # restid = request.args.get("restid")
        # menuid = request.form['menuid']
        # custdesk = request.form['custdesk']
        # menuName = Menu.query.with_entities(Menu.menuName).filter(Menu.menuId == menuid).first()
        # menuProds = Products.query.filter(Products.restOfProd == menuid).all()
    # elif request.method == "POST":
        # restid = request.form['restid']
        # menuid = request.form['menuid']
        # custdesk = request.form['custdesk']
        # menuName = Menu.query.with_entities(Menu.menuName).filter(Menu.menuId == menuid).first()
        # menuProds = Products.query.filter(Products.restOfProd == menuid).all()

        # dictOfProdIng = {}
        # for i in menuProds:
            # listofins = []
            # prodsIns = Ingredients.query.filter(Ingredients.prodOfIng == i.prodId).all()
            # for in1 in prodsIns:
                # listofins.append(in1.ingred01)
            # dictOfProdIng[str(i.prodId)] = listofins

    # return render_template('indexmenu.html', menuName=menuName, menuProds=menuProds, dictOfIng=dictOfProdIng, restofcust=restid, deskofcust=custdesk)


# @app.route('/addBasket/', methods=['POST'])
# def addBasket():
    # keylist = []
    # for key, value in request.form.items():
        # if key.startswith("checkbox"):
            # keylist.append(key.replace("checkbox", ""))
    # customer = request.form["custdesk"]
    # restoran = request.form["restid"]
    # product = request.form["product"]
    # prodAndIng = [product]
    # try:
        # customer = Customer.query.filter(Customer.custDesk == customer).first()
        # for item in keylist:
            # prodAndIng.append(item)
        # customer.custBasket = customer.custBasket + str(prodAndIng)
        # db.session.commit()
    # except Exception as e:
        # db.session.rollback()
    # return "ok", 200


# @app.route('/about')
# def about():
    # return render_template('aboutus.html')


if __name__ == '__main__':
    app.secret_key = 'make this hard to guess!'
    app.run(host='0.0.0.0')
