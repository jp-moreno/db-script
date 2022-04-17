# By J.P. Moreno

import random

arab_names = [("Abbas", "Salam"), ("Abdel", "Nour"), ("Abd", "Manaf"), ("Mohammed", "Ibn"), ("Zayneb", "Hossain"), ("Sarah", "Amin"), ("Aesha", "Saleh"), ("Asim", "IbnAbbas"), ("Ibrahim", "alUzza"), ("Khalil", "Mohammed")]

def arab_rest_namedesc_gen(user):
    option = random.randint(0,4)
    name, desc = "", ""
    if option == 0:
        name = f"{user.first_name}'s Oasis"
        desc = f"An Arab restaurant run by {user.last_name}. {name} is known for its sweet desserts."
    elif option == 1:
        name = f"{user.last_name} | Syrian Paradise"
        desc = f"One of the highest ranked restaurants where arab delicacy is served"
    elif option == 2:
        name = f"{user.last_name}’s Garden of kebab"
        desc = f"A family run Arab Place which is run by the {user.last_name} family. Known for its food from Damascus"
    elif option == 3:
        name = f"Babylon Fry"
        desc = f"A family run Arab restaurant by the {user.last_name} family. Known for its typical medieval arab dishes"
    elif option == 4:
        name = f"{user.last_name}'s Pita Delight"
        desc = f"A restaurant run by the {user.last_name} family. Best falafel in all Libya"
    return name, desc

arab_foods = [("Hummus","Server with special garlic from qatar", 9.99), ("Manakish","Arab pizza", 16.99), ("Halloumi","Mini-slabs of chewy goodness", 4.99), ("Foul meddamas ","Made of beans and special oil", 10.99), ("Tabbouleh","Aromatizedand vegetarian friendly", 19.99), ("Moutabal ghanoush"," Made with eggplant", 14.99), ("Fattoush","Arabic Salad", 10.50), ("Umm ali","Egyptian pudding", 12.99), ("Shanklish","Tasty cow or sheep milk cheese", 1.99), ("Shawarma","Tenderous meat", 23.99), ("Shish tawook","Served with pure garlic paste", 6.99), ("Dolma","Fresh with succulent lamb", 1.99), ("Kofta","Served with succulent meat", 4.99), ("Quwarmah Al Dajaj","Arab curry", 25.50 ), ("Mansaf","Looks like pizza covered with lamb carcass", 15.50), ("Kebab karaz","Delicious Syrian dish", 9.60), ("Kunefe"," Very tasty meat", 12), ("Baklava","Butterfly filo pastry", 10.30), ("Knafeh","Delicious cheesecake", 5.20), ("Iraqi masgouf","Slow cooked tasty carp", 4.30)]

chinese_names = [("Ah", "Kum"), ("Aiugo", "Ai"), ("Eric", "Lee"), ("Shun", "Li"), ("Jack", "Yang"), ("Jia", "Zhao"), ("Huiqing", "Chen"), ("Xiao", "Liu"), ("Yuan", "Huang"), ("Yihan", "Munchen")]


def chinese_rest_namedesc_gen(user):
    option = random.randint(0,4)
    name, desc = "", ""
    if option == 0:
        name = f"{user.first_name}'s Golden Rice House"
        desc = f"A Chinese restaurant run by {user.last_name}. {name} is known for its rice that can’t be tasted anywhere else."
    elif option == 1:
        name = f"Beijing Delicacies"
        desc = f"One of the highest ranked restaurants where Chinese delicacy is served"
    elif option == 2:
        name = f"{user.last_name}’s Dragon Egg Palace"
        desc = f"A family run Chinese Place which is run by the {user.last_name} family. Known for its food from Beijing"
    elif option == 3:
        name = f"Noodle Empire"
        desc = f"A family run Chinese restaurant by the {user.last_name} family. Known for its traditional dishes"
    elif option == 4:
        name = f"{user.last_name}'s Cousine"
        desc = f"A restaurant run by the {user.last_name} family. Best Chinese cuisine in Europe"
    return name, desc

chinese_foods = [("Fried Rice","Delicious and nutritious dish", 19.99), ("Peking Duck","Best way to eat duck", 19), ("Stinky Tofu","The stronger the smell the better it tastes", 14.99), ("Chow Mein","Delicious and tasty", 10.99), ("Congee","Nourishing and easy to digest", 7.99), ("Chinese Hamburger","A pita like bun filled with tender braised pork", 12.99), ("Scallion Pancakes","Savoury pancakes", 5.99), ("Kung Pao Chicken","Spicy stir-fried chicken dish", 32.99), ("Baozi","Bread like dumpling filled with meat and vegetables", 13.99), ("Mapo Tofu","Spicy but definitely worth it", 14.40), ("Char Siu","Succulent Barbecued meat", 31.50), ("Zhajiangmian","Tasty fried sauce noodles", 8.99), ("Wonton Soup","Most authentic Chinese dumplings", 8.99), ("Soup Dumplings","Delicious soup inside dumplings", 18.70 ), ("Hot Pot","Broths meat and veggies all together", 15.60), ("Chinese Sticky Rice","Cantonese dish of rice", 17.60), ("Hainanese Chicken Rice","Delicately flavoured poached chicken dish", 12), ("Seasoned Steamed Eggplant","Distinctive for its juiciness", 10.30), ("Jiaozi","Type of dumpling filled with meat and vegetables", 5), ("Spring Rolls","Rolls stuffed with vegetables or meat", 4.30)]

indian_names = [("Babu", "Anthony"), ("Pria", "Bakshi"), ("Raul", "Rajni"), ("Kamala", "Mital"), ("Vishnu", "Pandey"), ("Harish", "Dugal"), ("Anand", "Rish"), ("Joey", "Sibal"), ("Mitesh", "Deshpande"), ("Aditya", "Jaipur")]

def indian_rest_namedesc_gen(user):
    option = random.randint(0,4)
    name, desc = "", ""
    if option == 0:
        name = f"{user.first_name}'s Desi restaurant"
        desc = f"An Indian restaurant run by the {user.first_name}. {name} is known for it's Kerala Chicken Stew"
    elif option == 1:
        name = f"{user.last_name}’s Kitchen"
        desc = f"An Indian Restaurant run by two friends and by the {user.last_name} family. Known for its South-Indian food"
    elif option == 2:
        name = f"{user.last_name} Roti Bakery"
        desc = f"A family run Indian Roti Place which is run by the {user.last_name} family. Known for it's food from Delhi"
    elif option == 3:
        name = f"{user.last_name}’s Home of Biryani"
        desc = f"A family run Indian restaurant by the {user.last_name} family. Known for its food from Kolkata"
    elif option == 4:
        name = f"{user.last_name}'s Spice Factory"
        desc = f"A restaurant run by the {user.last_name} family. Known for its food from Mumbai"
    return name, desc

indian_foods = [("Aloo Gobi"," crispy and sweet", 6.99), ("Chana Masala"," A savoury Chana Masala with fresh spices all the way from India", 20.99), ("Chicken tikka masala"," Delicious Chicken with masala", 13.99), ("Dal Makhani"," A delicious stew made with black or yellow lentils", 10.99), ("Biryani"," A tasty dish mixed with meat and rice", 19.99), ("Laddu"," A delicious sweet from India", 4.99), ("Kheer"," A milk based sweet", 2.50), ("Kebab"," Freshly cooked meat with salad", 15.99), ("Gulab jamun"," Sugary milk based dessert", 5.99), ("Jalebi"," Orange sweet that melts in your mouth", 3.99), ("Tea"," Hot and sweet", 1.99), ("Masala dosa (pancake with stuffing"," Soft and delicious", 5.99), ("Appam (pancake steamed)"," Tasty bread", 4.99), ("Tali"," Spicy and with spices from Mumbai", 8.50 ), ("Uppuma"," Best breakfast dish", 15.50), ("Idli"," Locally farmed rice with delicious toppings", 19), ("Uttapam"," Very tasty meat", 5.99), ("Vegetarian rice Biryani"," Suitable for vegetarians", 8.99), ("Cakes Batura"," Served with tasty sauces", 7.20), ("Tortilla Paratha"," Freshly baked bread with sauce", 4.99)]

italian_names = [("Luca", "Rossi"), ("Marco", "DeLuca"), ("Julia", "Barbieri"), ("Matteo", "Bruno"), ("Enzo", "Colombo"), ("Isabella", "Rizzo"), ("Lucia", "Marino"), ("Dante", "Conti"), ("Alessio", "DiMarco"), ("Justin", "Maggio")]

def italian_rest_namedesc_gen(user):
    option = random.randint(0,4)
    name, desc = "", ""
    if option == 0:
        name = f"{user.first_name}'s Pizzeria"
        desc = f"An Italian Pizzeria run by the {user.first_name}. {name} is known for it's New York Style Pizza"
    elif option == 1:
        name = f"{user.last_name} Restaurante"
        desc = f"A family run Italian Restaurante by the {user.last_name} family. Known for its Sicillian food"
    elif option == 2:
        name = f"{user.last_name} Pasta"
        desc = f"A family run Italian Pasta Place which is run by the {user.last_name} family. Known for it's food from Napoli"
    elif option == 3:
        name = f"{user.last_name} Cucina"
        desc = f"A family run Italian Restaurante by the {user.last_name} family. Known for its food from Rome"
    elif option == 4:
        name = f"Papa {user.last_name}'s"
        desc = f"A family run Italian Restaurante by the {user.last_name} family. Known for its food from Turin"
    return name, desc

italian_foods = [("Cheese Pizza"," A savoury cheesey pizza with olive oil", 14.99), ("Pepperoni Pizza"," A savoury Pepperoni pizza with olive oil", 16.99), ("Ham Pizza"," A savoury ham pizza with fresh ham all the way from Italy", 17.99), ("Capellini Pasta"," Delicious Capellini Pasta with Alfredo Sauce", 14.99), ("Pene Pasta"," Delicious Pene Pasta with Alfredo Sauce", 14.99), ("Olives and Cheese"," Olives and Cheese all the way from Italy", 9.99), ("Red Wine"," A glass of red wine", 9.99), ("White Wine"," A glass of white wine", 9.99)]

spanish_names = [("Sofia", "Rodriguez"), ("Isabella", "Lopez"), ("Camila", "Morais"), ("Dario", "Garcia"), ("Izan", "Hernandez"), ("Matias", "Perez"), ("Alejandro", "Gonzalez"), ("Samuel", "Deleon"), ("Diego", "Morales"), ("Nicolas", "Cabrera")]


def spanish_rest_namedesc_gen(user):
    option = random.randint(0,4)
    name, desc = "", ""
    if option == 0:
        name = f"{user.first_name}'s Celler De Can Roca"
        desc = f"A Spanish restaurant run by {user.last_name}. The food is one of the best in the country."
    elif option == 1:
        name = f"Casa Lucio"
        desc = f"One of the highest ranked restaurants where Spanish delicacy is served"
    elif option == 2:
        name = f"{user.last_name}’s Casa"
        desc = f"A family run Spanish restaurant which is run by the {user.last_name} family. Known for its food from Madrid"
    elif option == 3:
        name = f"As De Copas"
        desc = f"A family run Spanish restaurant by the {user.last_name} family. Known for its traditional dishes and seafood"
    elif option == 4:
        name = f"{user.last_name}'s Abuelo"
        desc = f"A restaurant run by a Spanish couple living in France. The restaurant is based on spanish recipes from their grandparents."
    return name, desc

spanish_foods = [("Paella","Succulent and nutritious rice", 13.99), ("Puntillitas","Deep fried squids", 12), ("Gazpacho","Refreshing cold soup", 11.99), ("Churros con chocolate","Deep fried sticks of dough sprinkled with sugar and dipped in chocolate", 7.99), ("Patatas bravas","Fried potatoes with a heavenly garlic aioli", 17.99), ("Horchata con fartons","Refreshing milky drink", 3.45), ("Salmorejo","Thick and succulent cold soup", 15.99), ("Croquetas","Deep fried creaky rolls", 5.99), ("Migas","Spanish bakery bread", 6.99), ("Morcillia","Sausage made from pork blood", 11.50), ("Chorizo","Pork sausage spiced with paprika", 11.10), ("Potage","Soup or stew type dish made from beans, meat and veggies", 18.99), ("Gambas al Ajillo","Garlic shrimp", 8.35), ("Cocido","Boiling meats and veggies together", 21.70 ), ("Calamari a la Romana","Squid rings that are battered and deep-fried", 25.60), ("Flan","Custard dessert", 10.20), ("Fideua","Made with small thin pasta and it includes seafood", 20), ("Empanadas","Pastries that can be filled with many things", 10.90), ("Pulpo","Squid cooked with paprika and olive oil", 5.80), ("Tortilla de Patatas","Spanish omelette with potatoes", 16.30)]

turkish_names = [("Adem", "Agha"), ("Omer", "Avci"), ("Mehmet", "Ataturk"), ("Kemal", "Akber"), ("Aral", "Arsalan"), ("Aydem", "Balig"), ("Mehmet", "Hersi"), ("Mustofa", "Bulut"), ("Osman", "Demir"), ("Celaleddin", "Durmaz")]


def turkish_rest_namedesc_gen(user):
    option = random.randint(0,4)
    name, desc = "", ""
    if option == 0:
        name = f"{user.first_name}'s Hub"
        desc = f"A Turkish restaurant run by {user.first_name}. {name} is known for it's amazing service"
    elif option == 1:
        name = f"{user.last_name} Chefs"
        desc = f"One of the highest ranked restaurants where turkish delicacy is served"
    elif option == 2:
        name = f"{user.last_name} Turkish Charcoal Grill"
        desc = f"A family run Turkish Place which is run by the  {user.last_name} family. Known for it's food from Istanbul"
    elif option == 3:
        name = f"Ottoman Palace"
        desc = f"A family run Turkish restaurant by the {user.last_name} family. Known for its typical ottoman dishes"
    elif option == 4:
        name = f"{user.last_name}'s Turkish Kebab"
        desc = f"A restaurant run by the {user.last_name} family. Best kebab in all turkey"
    return name, desc

turkish_foods = [("Manti","Mini Ravioli", 4.99), ("Kofte","Delicious turkish meatballs", 6.99), ("Lahmacun","Turkish style pizza", 23.99), ("Doner","Tasty Turkish Sub", 10.99), ("Corba","Aromatized turkish soup", 19.99), ("Meze"," Delicious dish with fish ", 24.99), ("Pilav","Turkish pulao", 12.50), ("Dolma","Vegetarian delicacy", 12.99), ("Kumpir","Turkish snack", 1.99), ("Borek","Spinach or meat puffs", 23.99), ("Simit"," Turkish Pretzel", 13.99), ("Baklava"," crunchy and delicious", 1.99), ("Lokum","Yummy turkish jellies", 4.99), ("Halva","Unique Halwa", 5.50 ), ("Salep"," Best breakfast dish", 15.50), ("Islak Burgers"," Locally farmed rice with delicious toppings", 9.60), ("Kunefe"," Very tasty meat", 15), ("Mozzaik Pasta"," Suitable for vegetarians", 12.30), ("Turkish tea"," Served with tasty sauces", 7.20), ("Kazan Dibi"," Freshly baked bread with sauce", 4.30)]

drinks = [("Coke-a-Cola", "A Soda berverage", 1.99), ("Pepsi", "A Soda berverage", 1.99), ("Fanta", "A Soda berverage", 1.99), ("Iced Tea", "Tea with ice and lemon", 1.99), ("Tap Water", "Water from the tap", 0.99)]

lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Donec et odio pellentesque diam volutpat. Sed turpis tincidunt id aliquet risus feugiat in. Lacus laoreet non curabitur gravida arcu ac tortor dignissim. In cursus turpis massa tincidunt dui ut ornare lectus. Dignissim diam quis enim lobortis scelerisque fermentum. Nisi lacus sed viverra tellus in hac habitasse platea. Id donec ultrices tincidunt arcu non sodales neque. Ipsum dolor sit amet consectetur. Aenean et tortor at risus viverra adipiscing. Laoreet non curabitur gravida arcu ac tortor. Lacus vel facilisis volutpat est velit egestas. Ut diam quam nulla porttitor. Pretium nibh ipsum consequat nisl vel pretium."
