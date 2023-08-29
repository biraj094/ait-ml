from a1_app import application
from flask import render_template,request,redirect,url_for
from a1_app.helper import get_predicted_values


@application.route('/', methods=['GET', 'POST'])
def home():  
    contents = {
      'title':"🚗💨 Car Price Prediction Model 🚗💨"
    }
    return render_template('home.html', **contents)


@application.route('/predict', methods=['POST'])
def predict():
    # get all values from the form
    name = request.form.get('name','')
    year = request.form.get('year','')
    km_driven = request.form.get('km_driven','')
    fuel = request.form.get('fuel','')
    seller_type = request.form.get('seller_type','')
    transmission = request.form.get('transmission','')
    owner = request.form.get('owner','')
    mileage = request.form.get('mileage')
    engine = request.form.get('engine')
    power = request.form.get('power')
    seat = request.form.get('seat')

    if mileage.strip() == '' and engine.strip() == '' and power.strip() == '' :
        warning_message = '🚨 Hold up! 🚨 Looks like your form is dancing to the "Missing Values" beat! 🎶 Our prediction model is all about grooving with your data to serve up the freshest results. But uh-oh, it seems some values do not RSVP to the party! 😲 Do not worry, we have got your back – We will fill some of them for you! ⚡ Keep the data vibes flowing for the best prediction dance-off in town! 💃🕺'
    else:
        warning_message = '🎉 Hey there, trendsetter! 🌟 You have just taken the coolest ride on the prediction express! 🚀 Thanks for dropping by and letting our prediction model do its funky thing. 🕺💃'

    default_mileage = float(19.266374680306907)
    mileage = float(mileage) if mileage else default_mileage
    default_engine = float(1248.0)
    engine = float(engine) if engine else default_engine
    default_power = float(82.85)
    power = float(power) if power else default_power

    # Get prediction
    model_values = [[engine,power,mileage]]
    predicted_price = get_predicted_values(model_values)

    contents = {
        
        'title':"🚗💨 Car Price Prediction Model Result 🚗💨",
        #Model
        'predicted_price':predicted_price,
        #Form elements
        'name':name,
        'year':year,
        'km_driven':km_driven,
        'fuel':fuel,
        'seller_type':seller_type,
        'transmission':transmission,
        'owner':owner,
        'mileage':mileage,
        'engine':engine,
        'power':power,
        'seat':seat,
        
        #additional
        'warning_message':warning_message
    }



    return render_template('predict.html',**contents)

