# #constants
# SHOWER_GALLONS_PER_MINUTE = 2.125
# LAUNDRY_GALLONS_PER_LOAD = 36.98
# DISHWASHER_GALLONS_PER_USE = 5
# FAUCET_GALLONS_PER_MINUTE = 2
# HANDWASH_GALLONS_PER_MINUTE = 2
# US_PRICE_PER_GALLON = 0.00295

# gallons_shower = num_showers * shower_length * SHOWER_GALLONS_PER_MINUTE
# gallons_laundry = num_laundry * LAUNDRY_GALLONS_PER_LOAD
# gallons_dishwasher = num_dishwaher * DISHWASHER_GALLONS_PER_USE
# gallons_faucet = faucet_length * 7 * FAUCET_GALLONS_PER_MINUTE

# cost_shower = monthly_cost(US_PRICE_PER_GALLON, gallons_shower)
# cost_laundry = monthly_cost(US_PRICE_PER_GALLON, gallons_laundry)
# cost_dishwasher = monthly_cost(US_PRICE_PER_GALLON, gallons_dishwasher)
# cost_faucet = monthly_cost(US_PRICE_PER_GALLON, gallons__faucet)

# total_cost = cost_shower + cost_laundry + cost_dishwasher + cost_faucet

def monthly_cost(price_per_gal, gallons):
  cost = price_per_gal * gallons * 4.33 #4.33 converts weekly to monthly 
  return cost


def calculate_gallons(num, const):
  return num * const
  
def calculate_gallons_with_length(num, const, length):
  return num * const * length

# def choose_city(city, gal):
#   if city == 'NY':
#     monthly_cost_NY(gal)
#     print_international_cities_cost(gal)
#   elif city == 'DC':
#     monthly_cost_DC(gal)
#     print_international_cities_cost(gal)
#   elif city == 'LA':
#     monthly_cost_LA(gal)
#     print_international_cities_cost(gal)

def print_cities_cost(gal, city): 
  if(city == "NY"):
    string = "The monthly cost in New York City would be $" + str(monthly_cost_NY(gal)) 
  elif(city == "DC"):
    string = "The monthly cost in Washington D.C. would be $" + str(monthly_cost_DC(gal)) 
  elif(city == "LA"):
    string = "\nThe monthly cost in Los Angeles would be $" + str(monthly_cost_LA(gal))
  elif(city == "LONDON"):
    string = "The monthly cost in London, England would be " + str(monthly_cost_london(gal)) + " pounds."
  elif(city == "OTTAWA"):
    string =  "The monthly cost in Ottawa, Canada would be " + str(monthly_cost_ottawa(gal)) + " CAD." 
  elif(city == "CANBERRA"):
    string = "The monthly cost in Canberra, Australia would be " + str(monthly_cost_canberra(gal)) + " AUD."
  return string

def monthly_cost_NY(gal):
  WATER_RATE = 0.005748
  SEWER_RATE = 0.014184492
  water_cost = WATER_RATE * gal
  sewer_cost = SEWER_RATE * gal
  total_cost = water_cost + sewer_cost
  return round(total_cost,2)

def monthly_cost_DC(gal):
  WATER_RATE = 0.00572
  SEWER_RATE = 0.01505
  METER_FEE = 7.75
  CRIAC_FEE = 18.14
  WATER_REPLACEMENT_FEE = 6.30
  water_cost = WATER_RATE * gal
  sewer_cost = SEWER_RATE * gal
  total_cost = water_cost + sewer_cost + METER_FEE + CRIAC_FEE + WATER_REPLACEMENT_FEE
  return round(total_cost,2)

def monthly_cost_LA(gal):
  WATER_RATE = 0.0119766043
  SEWER_RATE =  .0077540107
  BASE_FEE = 13.69
  water_cost = WATER_RATE * gal
  sewer_cost = SEWER_RATE * gal
  total_cost = water_cost + sewer_cost + BASE_FEE
  return round(total_cost,2)

def monthly_cost_london(gal):
  WATER_FEE = 1.75416667
  SEWER_FEE = 5.29833333
  WATER_RATE = 0.00583521342
  SEWER_RATE =  0.00359159941 
  water_cost = WATER_RATE * gal
  sewer_cost = SEWER_RATE * gal
  total_cost = water_cost + sewer_cost + WATER_FEE + SEWER_FEE
  return round(total_cost,2)

def monthly_cost_ottawa(gal):
  WATER_FEE = 10.84
  SEWER_FEE = 9.40166667
  FIRE_HYDRANT_FEE = 4.21583333
  WATER_RATE = 0.00333116303
  water_cost = WATER_RATE * gal
  total_cost = water_cost + WATER_FEE + SEWER_FEE + FIRE_HYDRANT_FEE
  return round(total_cost,2)

def monthly_cost_canberra(gal):
  WATER_FEE = 15
  SEWER_FEE = 42.1916667
  WATER_RATE = 0.000225485958
  water_cost = WATER_RATE * gal
  total_cost = water_cost + WATER_FEE + SEWER_FEE 
  return round(total_cost,2)
