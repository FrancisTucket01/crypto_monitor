from flask import render_template, url_for, request, flash, session, redirect, jsonify
from ltwallet import app, mysql
import time
from datetime import date
from ltwallet.forms import RegisterForm
import subprocess

quotes_forex = ["news","GBP-USD", "GBP-EUR","GBP-CAD","GBP-AUD","GBP-CHF","BTC-GBP", "EUR-USD","EUR-JPY","EUR-CHF","EUR-AUD", "BTC-EUR","USD-CAD","USD-CHF", "USD-AUD","USD-JPY", "BTC-USD", ".INX:INDEXSP", ".DJI:INDEXDJX"]
database_forex = []
quotes_crypto = ["BTC-KSH","ETH-KSH","XRP-KSH","DOGE-KSH","MATIC-KSH", "SOL-KSH"]
database_crypto =[]

for quote in quotes_forex:
            if "-" in quote:
                quote = quote.replace("-", "")
            elif "." in quote:
                quote = quote.strip(".").replace(":", "")
            else:
                quote = quote
            database_forex.append(quote)

for quote in quotes_crypto:
            if "-" in quote:
                quote = quote.replace("-", "")
            elif "." in quote:
                quote = quote.strip(".").replace(":", "")
            else:
                quote = quote
            database_crypto.append(quote)

# Home page route
@app.route('/')
def home():
    db = "news"
    latest = False
    try:
        db = request.args['db']
        latest = request.args['latest']
    except:
        pass
    cursor = mysql.connection.cursor()
    smt = f"SELECT * FROM news"
    cursor.execute(smt)
    data = cursor.fetchall()
    return render_template("/home1.html", data=data, tables=database_crypto, db=db, latest=latest)

# Forecast page Route
@app.route('/forecast')
def forecast():
    
    return render_template("/forecast.html", tables=database_crypto)

#sentiment page Just more tweet analysys
@app.route('/sentiment')
def sentiment():

    cursor = mysql.connection.cursor()
    smt = f"SELECT time, tweet, sentiment, user FROM tweets"
    cursor.execute(smt)
    data = cursor.fetchall()
    # pos = 0
    # neg = 0
    # neu = 0
    # for row in data:
    #     x=row[2]
    #     if x < 0:
    #         neg += 1
    #     elif x > 0:
    #         pos += 1
    #     else:
    #         neu += 1
    # sentiment = [(pos*100/4987), (neg*100/4987), (neu*100/4987)]
    sentiment = [40.80609584920794, 16.30238620413074, 42.89151794666132]
    # print(sentiment)
    return render_template("/sentiment.html", sentiment=sentiment, tweets=data, tables=database_crypto)
  
# singin content
@app.route('/signin')
def signin():
    return render_template('signin.html')
 
# signup content
@app.route('/signup')
def signup():
    return render_template("/signup.html")

 
# About Content
@app.route('/about')
def about():
    return render_template("about.html")

# Content for contact page
@app.route('/contact')
def contact():
    return render_template("contact.html")

# Signing out route
@app.route('/signout')
def signout():
    session['loggedin'] = ""
    session['id'] = ""
    session['username'] = ""
    return redirect(url_for("home"))

# Charts routes
@app.route("/news")
def news():
    years = [2012,2013,2014,2015,2016,2017,2018]
    cursor = mysql.connection.cursor()
    year = request.args.get('year', 0, type=int)
    if year == 0:
        year = 2012
    smt = f"SELECT * FROM sentiment WHERE year = {year};"
    cursor.execute(smt)
    data = cursor.fetchall()
    return render_template("/news.html", data=data, years=years)


# Login Endpoint
@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM users WHERE name = %s', (username,))
    # Fetch one record and return result
    account = cursor.fetchone()
    if account:
        # Create session data, we can access this data in other routes
        if account[2] == password:
            session['loggedin'] = True
            session['id'] = password
            session['username'] = username
            # Redirect to home page
            flash(f"Login Successful... Welcome Back: { request.form['username']}")
            return redirect(url_for("home"))
        else:
            message = "Incorect Password!!!"
            flash(message)
        return render_template("/signin.html", error = message)
    else:
        message = "Incorect Username and Password"
        return render_template("/signin.html", error = message)


# Registration Endpoint
@app.route("/registration", methods=['GET', 'POST'])
def registration():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    password2 = request.form['password2']
    smt = f"INSERT INTO users(name, password, email_address) VALUES('{username}', '{password}', '{email}')"

    if password == password2:
        curs = mysql.connection.cursor()
        curs.execute(smt)
        mysql.connection.commit()
        message = "Account created successfully"
        print(username, email, password)
        return render_template("/signin.html", infor = message)
    else:
        message = "Passwords Dont Match!!! Try again"
        return render_template("/signup.html", error = message)


# Api for accessing chart candlestic data
@app.route("/chartdata/<ctype>/<table>/<col_a>/<col_b>", methods=['GET', 'POST'])
def chart_data(ctype="null", table="null",col_a="null",col_b="null"):
    if ctype == "candlestic":
        # if "BTC" in db:
        #     db = 'EURUSD'
        if 'news' in table:
            table = 'EURUSD'
        elif 'NDEX' in table:
            table = 'EURUSD'
        elif table == "null":
            table = 'BTCUSD'
        cursor = mysql.connection.cursor()

        smt = f"select  date , open, high, low, close from {table} ORDER BY id DESC;"
        cursor.execute(smt)
        chart_data = cursor.fetchall()
        epoch_time = date(1970, 1, 1)
        new_data = []
        for i in chart_data:
            delta = (i[0] - epoch_time).total_seconds()
            new_data.append({'date': int(delta), 'price': [i[1], i[2], i[3],i[4]]})
        return jsonify(new_data)
    elif ctype == "line":
        # if "BTC" in db:
        #     db = 'EURUSD'
        if 'news' in table:
            table = 'EURUSD'
        elif 'NDEX' in table:
            table = 'EURUSD'
        elif table == "null":
            table = 'BTCUSD'
        cursor = mysql.connection.cursor()
        
        if col_a != "null":
            smt = f"select  date, {col_a}, {col_b} from {table} ORDER BY id DESC;"
            cursor.execute(smt)
            chart_data = cursor.fetchall()
            epoch_time = date(1970, 1, 1)
            new_data = []
            for i in chart_data:
                delta = (i[0] - epoch_time).total_seconds()
                new_data.append({'date': int(delta), 'price': [i[1],i[2]]})
            # flash("Hello there I see you from somewhere else.... carefull")
            return jsonify(new_data)
        else:
            smt = f"select  date, volume from {table} ORDER BY id DESC;"
            cursor.execute(smt)
            chart_data = cursor.fetchall()
            epoch_time = date(1970, 1, 1)
            new_data = []
            for i in chart_data:
                delta = (i[0] - epoch_time).total_seconds()
                new_data.append({'date': int(delta), 'price': [i[1]]})
            return jsonify(new_data)
    else:
        err = "Supplied value for Table not recognised"
        return jsonify(err)
    

@app.route("/barchart/<menu>/<quote>/<date>")
def barchart(menu="", quote="", date=""):
    return jsonify(menu)