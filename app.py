# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
  return render_template("index.html")

@app.route("/questions")
def questions():
  return render_template("questions.html")

@app.route("/sendWaterInfo", methods = ["GET","POST"])
def handle_calculations():
  if request.method == "GET":
    return render_template("yourResultsRedirect.html")
  else:
    SHOWER_GALLONS_PER_MINUTE = 2.125
    LAUNDRY_GALLONS_PER_LOAD = 36.98
    DISHWASHER_GALLONS_PER_USE = 5
    FAUCET_GALLONS_PER_MINUTE = 2
    HANDWASH_GALLONS_PER_MINUTE = 2
    IRRIGATION_GALLONS_PER_MINUTE = 14
    HOSE_GALLONS_PER_MINUTE = 7
    POOL_GALLONS_PER_MINUTE = 7
    # US_PRICE_PER_GALLON = 0.00295
  
    form = request.form
    num_showers = form["num_showers"]
    shower_length = form["shower_length"]
    num_laundry = form["num_laundry"]
    num_dishwasher = form["num_dishwasher"]
    faucet_length = form["faucet_length"]
    handwash_length = form["handwash_length"]
    num_irrigation = form["num_irrigation"]
    irrigation_length = form["irrigation_length"]
    hose_length = form["hose_length"]
    pool_length = form["pool_length"]
    drinking_water = form["drinking_water"]

    num_showers = int(num_showers)
    shower_length = int(shower_length)
    num_laundry = int(num_laundry)
    num_dishwasher = int(num_dishwasher)
    faucet_length = int(faucet_length)
    handwash_length = int(handwash_length)
    num_irrigation = int(num_irrigation)
    irrigation_length = int(irrigation_length)
    hose_length = int(hose_length)
    pool_length = int(pool_length)
    drinking_water = int(drinking_water)
  
    gallons_shower = model.calculate_gallons_with_length(num_showers, shower_length, SHOWER_GALLONS_PER_MINUTE)
    gallons_laundry = model.calculate_gallons(num_laundry,LAUNDRY_GALLONS_PER_LOAD)
    gallons_dishwasher = model.calculate_gallons(num_dishwasher, DISHWASHER_GALLONS_PER_USE)
    gallons_faucet = model.calculate_gallons_with_length(7, FAUCET_GALLONS_PER_MINUTE, faucet_length) #the 7 is to convert daily to weekly
    gallons_handwash = model.calculate_gallons_with_length(7, HANDWASH_GALLONS_PER_MINUTE, handwash_length)
    gallons_irrigation = model.calculate_gallons_with_length(num_irrigation, irrigation_length, IRRIGATION_GALLONS_PER_MINUTE)
    gallons_hose = model.calculate_gallons(hose_length, HOSE_GALLONS_PER_MINUTE)
    gallons_pool = model.calculate_gallons(pool_length, POOL_GALLONS_PER_MINUTE)
    gallons_drinking = drinking_water/64

    total_gallons = gallons_shower + gallons_laundry + gallons_dishwasher + gallons_faucet + gallons_handwash + gallons_irrigation + gallons_hose + gallons_pool + gallons_drinking
  
    # cost_shower = model.monthly_cost(US_PRICE_PER_GALLON, gallons_shower)
    # cost_laundry = model.monthly_cost(US_PRICE_PER_GALLON, gallons_laundry)
    # cost_dishwasher = model.monthly_cost(US_PRICE_PER_GALLON, gallons_dishwasher)
    # cost_faucet = model.monthly_cost(US_PRICE_PER_GALLON, gallons_faucet)  
    # cost_handwash = model.monthly_cost(US_PRICE_PER_GALLON, gallons_handwash)
    # cost_irrigation = model.monthly_cost(US_PRICE_PER_GALLON, gallons_irrigation)
    # cost_hose = model.monthly_cost(US_PRICE_PER_GALLON, gallons_hose)
    # cost_pool = model.monthly_cost(US_PRICE_PER_GALLON, gallons_pool)
    # cost_drinking = model.monthly_cost(US_PRICE_PER_GALLON, gallons_drinking)

    #US National Average 
    #total_cost = cost_shower + cost_laundry + cost_dishwasher + cost_faucet + cost_handwash + cost_irrigation + cost_hose + cost_pool + cost_drinking

    #Prints out cost in all 6 cities
    results_NY = model.print_cities_cost(total_gallons, "NY")
    results_LA = model.print_cities_cost(total_gallons, "LA")
    results_DC = model.print_cities_cost(total_gallons, "DC")

    results_ottawa = model.print_cities_cost(total_gallons, "OTTAWA")
    results_london = model.print_cities_cost(total_gallons, "LONDON")
    results_canberra = model.print_cities_cost(total_gallons, "CANBERRA")

    
    #converts international currency to USD
    # cost_from_canada = total_cost * 0.78
    # cost_from_europe = total_cost * 1.21
    # cost_from_australia = total_cost * 0.70
    
    #results_str = f"This is the total cost: ${total_cost}"
    # can_results = f"This is how much the cost would be in CAD: {cost_from_canada}"
    # eur_results = f"This is how much the cost would be in Pounds: {cost_from_europe}"
    # aus_results = f"This is how much the cost would be in AUD: {cost_from_australia}"

    
    
    return render_template("/sendWaterInfo.html", results_NY = results_NY,results_LA = results_LA, results_DC = results_DC, results_ottawa = results_ottawa, results_london = results_london, results_canberra= results_canberra, total_gallons = total_gallons)

  
app.run(host='0.0.0.0', port=81, debug=True)
