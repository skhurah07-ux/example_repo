def hotel_cost(num_nights):
    price_per_night = 120
    return num_nights * price_per_night


def plane_cost(city_flight):
    # Flight costs based on the destination.
    if city_flight.lower() == "Durban":
        return 1500
    elif city_flight.lower() == "newcastle":
        return 1500
    elif city_flight.lower() == "capetown":
        return 2000
    else:
        city_flight.lower() == "Bloemfontein"
        return 1000


def car_rental(rental_days):
    daily_rental_rate = 60
    return rental_days * daily_rental_rate



# Gets user inputs of the parameters.
city_flight = input("Which city are you visiting? ")
num_nights = int(input("How many nights? "))
rental_days = int(input("For how many days? "))

def holiday_cost(num_nights, city_flight, rental_days):
    total = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total


# Calculates all the costs.
hotel_total = hotel_cost(num_nights)
plane_total = plane_cost(city_flight)
car_total = car_rental(rental_days)
holiday_total = holiday_cost(num_nights, city_flight, rental_days)

# Prints out the holiday calculation results.
print(f"Destination: {city_flight}")
print(f"Hotel stay  for {num_nights} nights is R{hotel_total}")
print(f"The flight cost: R{plane_total}")
print(f"Car rental for {rental_days} days is R{car_total}")
print(f"The total holiday cost will be R{holiday_total}")