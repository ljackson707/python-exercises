
#1)
# You have rented some movies for your kids: 
# The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), 
# and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

rented_movie1 = {
        "name": "little Mermaid",
        "rent_day": 3
}
print(rented_movie1)

rented_movie2 = {
        "name": "Borther Bear",
        "rent_day": 5,
        "like": True
}
print(rented_movie2)

rented_movie3 = {
        "name": "Hercules",
        "rent_day": 1,
        "like": "?"
}
print(rented_movie3)

rented_movies = [rented_movie1, rented_movie2, rented_movie3]
print(rented_movies)

(rented_movie1["rent_day"]) * 3
(rented_movie2["rent_day"]) * 3
(rented_movie3["rent_day"]) * 3

#This is the final Answer
total_rent = ((rented_movie1["rent_day"]) * 3) + ((rented_movie2["rent_day"]) * 3) + ((rented_movie3["rent_day"]) * 3)
total_rent
#27 dollars to rent all the movies


#2) 
# Suppose you're working as a contractor for 3 companies: Google, 
# Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, 
# Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 
# 6 hours for Google and 4 hours for Amazon.

#3)
# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

#4)
# A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. Premium members do not need to buy a specific amount of products.
