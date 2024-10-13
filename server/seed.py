#!/usr/bin/env python3
from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    
    restaurants = [
        Restaurant(name="Karen's Pizza Shack", address='address1'),
        Restaurant(name="Sanjay's Pizza", address='address2'),
        Restaurant(name="Kiki's Pizza", address='address3')
    ]
    db.session.add_all(restaurants)
    db.session.commit()

    
    pizzas = [
        Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese"),
        Pizza(name="Geri", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni"),
        Pizza(name="Melanie", ingredients="Dough, Sauce, Ricotta, Red peppers, Mustard")
    ]
    db.session.add_all(pizzas)
    db.session.commit()

    
    restaurant_pizzas = [
        RestaurantPizza(restaurant=restaurants[0], pizza=pizzas[0], price=1),
        RestaurantPizza(restaurant=restaurants[1], pizza=pizzas[1], price=4),
        RestaurantPizza(restaurant=restaurants[2], pizza=pizzas[2], price=5)
    ]
    db.session.add_all(restaurant_pizzas)
    db.session.commit()

    print("Seeding done!")