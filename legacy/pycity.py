import random as rn
import time
behaviour = [
          "happy",
          "angry",
          "creative",
          "very happy",
          "sad",
          "existential crysis",
          "mr.smile",
]
feeling_def = behaviour[0]
money = 10
health = 100
energy = 100
strength = 0
happiness = 50
inventory = {}
last_work_time = time.time() - 3600  # Initialize last work time to one hour ago
last_claim_time = time.time() -3600
creator_time = time.time() -3600
garden_time = time.time() -3600
eadableTime =time.time() - 10800
dirty_time = time.time() - 10
if money < 0:
    stress = rn.randint (1, 50)
    angry = rn.randint(0, 2)
    depression = rn. randint(0, 5)
    print("I'm sorry, but you seem to be in debt. You have to pay for it. Once everything is paid, you can continue your business. You only need your balance to be greater than or equal to zero. As long as you are in debt, you cannot buy or invest in anything. So I advise you to pay it as soon as possible.")
    happiness -= stress
    health -= angry
    energy -= depression
    print(f"Your level of happiness decreased by {stress}")
    print(f"Your health level decreased by {angry}")
    print(f"Your energy level decreased by {depression}")

# Dictionary mapping items to their prices
items_prices = {
    "apple": 3,
    "banana": 7,
    "cheese": 10,
    "tomato": 5,
    "meat": 12,
    "flour": 15,
    "sugar": 12,
    "milk": 10,
    "egg": 6,
    "potato": 7,
    "butter": 14,
    "cola": 14,
    "juice": 17,
    "chocolate": 15,
    "bread": 18,
    "beer": 21,
    "water": 5,
    "lemon": 7,
    "orange": 5,
    "lemonade": 16,
    "coffee": 10,
    "crisps": 18,
    "ice-cream": 14,
    "peach": 11,
    "strawberry": 9,
    "rawsberry": 12,
    "donut": 18,
    "pumpkin": 20,
    "carrot": 10,
    "ketchup": 16,
    "hamburger": 19,
    "wine": 24,
    "yeast": 7,
    "cocoa": 24,
    "barley": 11,
    "anchowy": 9,
    "onion": 5,
    "grapes": 8,
    "sunflower": 12,
    "olives": 15,
    "cabbage": 10,
    "lettuce": 8,
    "cucumber": 12,
    "eggplant": 9,
    "broccoli": 13,
    "zucchini": 10,
    "beets":7,
    "sunflower oil": 18,
    "corn": 12,
    "olive oil": 24,
    "garlic": 10,
    "vinegar": 16,
    "black pepper": 11,
    "pepper": 8,
    "cookies": 16,
    "pasta": 24,
    "salami": 19,
    "sausage": 28,
    "popcorn": 25,
    "mustard": 22,
    "pea": 4,
    "watermelon": 28,
    "apricot": 16,
    "blueberry": 13,
    "melon": 26,
    "lime": 14,
    "mango": 16,
    "mint": 9,
    "tea plant": 12,
    "coffee bean": 7,
    "rice": 15,
    "singlet": 24,
    
    "spoiled apple": 1.5,
    "spoiled banana" : 3.5,
    "spoiled cheese": 5,
    "spoiled tomato": 2.5,
    "spoiled meat": 6,
    "spoiled flour": 7.5,
    "spoiled milk": 5,
    "spoiled egg": 3,
    "spoiled potato": 3.5,
    "spoiled butter": 7,
    "spoiled cola": 7,
    "spoiled juice": 8.5,
    "spoiled chocolate": 7.5,
    "spoiled bread": 9, 
    "spoiled beer": 10.5,
    "spoiled lemon": 3.5,
    "spoiled orange": 2.5,
    "spoiled lemonade": 8,
    "spolied coffee":5,
    "spoiled crisps": 9,
    "spoiled ice-cream": 7,
    "spoiled peach": 5.5,
    "spoiled strawberry": 4.5,
    "spoiled rawsberry":6,
    "spoiled donut": 9,
    "spoiled pumpkin": 10,
    "spoiled  carrot": 5,
    "spoiled ketchup": 8,
    "spoiled hamburger": 9.5,
    "spoiled wine": 12,
    "spoiled yeast": 3.5,
    "spoiled cocoa": 12,
    "spoiled barley": 5.5,
    "spoiled anchowy": 4.5,
    "spoiled onion": 2.5,
    "spoiled grapes": 4,
    "spoiled sunflower": 6,
    "spoiled olives": 7.5,
    "spoiled cabbage": 5,
    "spoiled lettuce": 4,
    "spoiled cucumber": 6,
    "spoiled eggplant":4.5,
    "spoiled broccoli": 6.5,
    "spoiled zucchini": 5, 
    "spoiled beets": 3.5,
    'spoiled sunflower oil': 9,
    "spoiled corn": 6,
    "spoiled olive oil" : 12,
    "spoiled garlic": 5,
    "spoiled vinegar": 8,
    "spoiled black pepper": 5.5,
    "spoiled pepper": 4,
    "spoiled cookies": 8,
    "spoiled pasta": 12,
    "spoiled salami": 9.5,
    "spoiled sausage": 14,
    "spoiled popcorn": 12.5,
    "spoiled mustard": 11,
    "spoiled pea": 2,
    "spoiled watermelon": 14, 
    "spoiled apricot": 8,
    "spoiled blueberry": 6.5,
    "spoiled melon": 13,
    "spoiled lime": 7, 
    "spoiled mango": 8,
    "spoiled mint":4.5,
    "spoiled tea plant": 6,
    "spoiled coffee bean": 3.5,
    
    "jacket": 54,
    "blouse": 41,
    "overall": 58,
    "cap": 18,
    "t-shirt": 33,
    "jumper": 54,
    "sweater": 46,
    "ring": 73,
    "trainers": 44,
    "dress": 60,
    "glasses":20,
    "blazer": 48,
    "silk hat": 23,
    "shorts": 35,
    "tie": 17,
    "coat": 56,
    "bracelet": 19,
    "waistcoat": 43,
    "swimsuit": 32,
    "scarf": 24,
    "pans": 69,
    "socks": 17,
    "hat": 36,
    "boots": 45,
    "helmet": 26,
    "jeans": 44,
    "shirt": 34,
    "trousers": 56,
    "hoodie": 42,
    "pyjamas": 39,
    "slippers": 25,
    "necklace": 58,

    "fishing pole": 35,
    "carp": 32,
    "perch": 27,
    "trout": 30,
    "herring": 24,
    "pelengas": 28,
    "gudgeon": 32,
    "catfish": 45,
    "pike": 38,
    "mackerel": 25,
    "tuna": 34,
    "sardina": 8,
    "salmon": 30,
    "barracuda": 47,
    "fugu fish": 72,
    "shark": 84,
    "marlin": 66,
    "whale": 106,
    "lobster": 52,
    "crab": 37,
    "jellyfish": 63,
    "octopus": 74,
    "squid": 81,
    "turtle": 68,

    "hunting rifle": 40,
    "hare": 35,
    "fox": 76,
    "raccoon": 55,
    "badger": 62,
    "wolf": 86,
    "bear": 102,
    "beaver": 47,
    "duck": 38,
    "goose": 45,
    "coyote": 83,
    "eagle": 63,
    "lion": 90,
    "tiger": 104,
    "lynx": 75,
    "wild boar": 61,
    "deer": 54,
    "moose": 69,
    "wild goat": 80,
    "elephant": 130,
    "crocodile": 115,
    "cheetah": 97,
    "vulture": 50,
    "ostrich": 60,
    "hippopotamus": 70,
    "rhinoceros": 83,
    "puma": 78,
    "jaguar": 99,
    "armadillo": 70,
    "tortoise": 100,
    "ferret": 51,
    "parrot": 65,
    "peacock": 127,
    "monkey": 42,
    "mole": 39,
    "zebra": 84,
    "hedgehog": 49,
    "porcupine": 71,
    "squirrel": 42,
    "skunk": 56,
    "python": 78,
    "antilope": 38,
    "bizon": 113,
    "buffalo": 88,
    "ermine": 78,
    "cassowary": 52,
    "sable": 90,
    "chipmunk": 47,
    "hen": 30,
    "cow": 50,
    "sheep": 40,
    "pig":54,
    "hunting license": 30,

    "jackhammer": 75,
    "pickaxe": 50,
    "coal": 32,
    "silver": 75,
    "granite": 41,
    "uranium": 92,
    "diamond": 125,
    "clay": 26,
    "gold": 107,
    "amber": 111,
    "iron": 30,
    "oil bar": 43,
    "stone": 23,
    "rock salt": 32,
    "limestone": 27,
    "tungsten": 77,
    "platinum": 120,
    "tourmaline": 156,
    "rock crystal": 145,
    "agat":131,
    "sand": 21,
    "lean": 51,
    "zinc": 57,
    "emerald": 130,
    "ruby": 123,
    "aquamarine": 125,
    "tin": 65,
    "quartz": 96,
    "marble": 100,
    "aluminium": 66,
    "nickel": 66,
    "sapphire": 123,
    "natural gas": 34,
    "titan": 95,
    "topaz": 113,
    "cobblestone":32,
    "badrock": 86,
    "redstone":75,
    "copper": 48,
    "rubygite": 175,
    "sulfur": 87,
    "saltpeter": 54,

    "cinema ticket": 5,
    "theatre ticket": 7,
    "circus ticket": 6,
    "taxi ticket": 7,
    "bus ticket": 15,
    "train ticket": 50,
    "ship ticket": 75,
    "plane ticket": 120,
  
    "mystery box": 25,
    "giftbox": 50,
    "creator": 230,
    "washing machine": 92,
  
    "book": 20,
    "comics": 20,

    "car": 300,
    "limuzin": 170,
    "fuel": 25,
    "backpack": 77,
    
    "a bunch of flowers": 15,
    
    "film": 25,
    "laptop": 95,
    "TV": 112, 
    "game console": 82,
    "camera": 72,
    "generator of Ruby": 140,
    "computer": 104,
    "keyboard": 52,
    "system unit": 89,
    "mouse": 33,
    "monitor": 66,
    "processor": 71,
    "motherboard": 110,
    "video caed": 50,
    "hard disk": 46,
    "power supply": 68,
    "RAM":38,
    
    
    "water gun": 23,
    
    "crown": 150,
    "golden card": 200, 
    "golden medal": 102, 
    "trophy": 150,
  
    "fibreglass": 24,
    "house": 500,
    "table": 73,
    "chair": 52,
    "wardrobe": 95,
    "rubber": 42,
    "steel": 30,
    "plastic": 21,
    "glass": 43, 
    "leather": 38, 
    "wool":31,
    "bronze": 72,
    "ink": 18,
    "paper": 15,
    "brick": 17,
    "ceramic":24,
    "wood": 20,
    "octopus's ink": 30,
    "better leather": 60,
    "furnace": 112,
    "rope": 13,
    "hook": 10,
    "magnet":45,
    "fence":53,
    "compass":72,
    "light bulb": 14,
    "black powder": 21,
    "bullet" : 9,
    "bag": 36,
    "matches": 4,
    "mirror": 32,
    "carpet": 64,
    "plate": 17,
    "spoon": 14,
    "fork": 15,
    "cup": 22,
    "saucepan": 35,
    "showel": 30,
    "rake": 33,
    "water can":27,
    "flower pot": 24,

    "apple seeds": 5,
    "banana seeds": 9,
    "tomato seeds": 7,
    "lemon seeds" : 9,
    "orange seeds": 7,
    "pumpkin seeds": 22,
    "peach seeds": 13,
    "strawberry seeds": 11,
    "rawsberry seeds": 15,
    "carrot seeds": 12,
    "cocoa seeds": 26,
    "barley seeds": 13, 
    "grapes seeds": 10,
    
    "watermelon seeds": 30,
    "apricot seeds": 19,
    "blueberry seeds": 15,
    "melon seeds": 28,
    "sunflower seeds": 14,
    "olives seeds": 17,
    "cabbage seeds": 12,
    "lettuce seeds":10,
    "cucumber seeds": 14,
    "eggplant seeds": 11,
    "broccoli seeds": 15,
    "zucchini seeds": 12,
    "beets seeds": 9,
    "corn seeds": 14,
    "pepper seeds": 10,
    "black pepper seeds": 13, 
    "mustard seeds": 24,
    "pea seeds": 6,
    "potato seeds": 9,
    "onion seeds": 7,
    "garlic seeds" : 12,
    "mint seeds": 11,
    "lime seeds": 16,
    "mango seeds": 18,
    "tea plant seeds": 14,
    "coffee seeds": 9,\
  
    "treadmill": 74,
    "punching bag": 65,
    "exercise bike": 83,
    "horizontal bar": 62,
    "expander": 34,
    "dumbbell": 38,
    "weight": 42,
    "sweden ladder": 72,
    "barbell": 50,
  
    "aspirin": 16,
    "penicillin": 28,
    "zinnat": 24,
    "tetanus serum": 37,
    "iodine": 29,
    "antiflu": 41,
    "immoortin":93,
    "stimpak": 52,
    "poison":85,
    
    
}
while True:
    action = input("What do you want to do? Commands: balance, buy, claim,  cook, craft, eat, energy, garden, go, happiness, health, inventory, load, lounge, prices, recycle, save, sell, sleep, sport, travel, unwear, use-item, wear, work: ")
    
    if action.lower() == "health":
       print(f"Your health level is {health}")
       if health >= 100:
         print("In a healthy body healthy mind! Your health is very strong and adapted. With such health, you acquire various bonuses. One of them is boost work. The work will be done successfully. And if you have a good mood and everything is in order with energy, then you will get the biggest boost. And at the same time, the income will be corresponding.")
       elif health <= 75:
         print("Your health is slightly reduced. So far there is nothing serious, but still I advise you to do something with it. You can boost your health with unspoiled food and drink, as well as sleep and more.")
       elif health <= 50:
         print("Be careful. Your condition is much weaker than before. So I advise you to quickly take some action before it's too late. You can make a visit to the doctor by using the car or bus, or just get a good night's sleep to increase more health. Sleep restores 3/5 of all health.")
       elif health <= 25:
         print("Your health is practically in critical condition. You urgently need to go to the doctor. Or there are other ways. The store has medicines that can heal you, as well as products to treat wounds and repair injuries.")
       elif health == 0:
         print("Alas, death overtook you at the most inopportune moment. But there is one thing that will help you rise from the dead. It's a very expensive but interesting drug called Immortin. This medicine can give you a second chance at getting your health back. But keep in mind energy and happiness will also be greatly underestimated. Health will remain 10%. But woe to those who did not have time to buy such a drug. Then your life in this world will stop forever.")
         if "immortin" in inventory:
           del inventory["immortin"]
           health += 10
           energy += 10
           happiness += 10
         else:
           break

   
  

    if action.lower() == "energy":
     print(f"Your energy level equals {energy}")
     if energy >= 100:
        print("You are very energetic. Due to the maximum amount of energy, you will work perfectly. Enjoy these moments before it's too late. So they will fall sooner or later.")
     elif energy == 75:
        print("Your energy reserve has decreased slightly. This means that you need to make up for it somehow. This can be done in different ways. Eating food (not spoiled), sleeping, or exercising.")
     elif energy == 50:
        print("You have used up half of your energy. I recommend filling it up before it's too late. Remember, when the energy reaches zero, you will die of exhaustion. So I advise you to take action. If you can't sleep at home, and if you have a car, you can either sleep in it or go to a hotel. In extreme cases, you can sleep on the sidewalk.")
     elif energy == 25:
        print("Hurry, hurry! You urgently need to replenish your energy reserves. Use any method to boost your energy.")
     elif energy == 0:
        print("You died of exhaustion.")
        
    if action.lower() == "happiness":
        print(f"Your level of happiness equals {happiness}")
        if happiness >= 75:
            print("Well done. Happiness is the key to success. Continue in the same spirit.")
        elif happiness <= 25:
            print("Maybe you think about increasing your level of happiness? Because it is very low.")
        elif happiness >= 60:
            feeling = behaviour[3]
            print(f"Your behaviour is {feeling}. As long as you are in such a mood, you will have a nice bonus. Your work will be more successful, and the profit will be correspondingly greater.")
        elif happiness >= 80: 
            feeling1 = behaviour[2]
            print(f"Your behaviour is {feeling1}. Since you are in such a mood you have an even greater bonus. Due to the excellent work and creative approaches to its implementation, your salary will increase even higher. But keep in mind that if your level of happiness changes, you risk losing it.")
        elif happiness <= 40: 
            feeling2 = behaviour[1]
            print(f"Your behaviour is {feeling2}. Since the mood is quite angry, be careful not to get into trouble. Your level of happiness is less than normal, if you go to work, then the salary will be less than if you worked with normal behavior (50 - 59). But there is still a chance to fix everything by increasing your level of happiness before it's too late.")
        elif happiness <= 20: 
            feeling3 = behaviour[4]
            print(f"Your behaviour is {feeling3}. Since you are in a very sad mood, your work progress will be greatly reduced. The salary will be much less than usual. And the chances that you will return to the usual have become less.")
        elif happiness == 100:
            feeling4 = behaviour[6]
            print(f"Your behaviour is {feeling4}. Highest potential, highest success, highest salary, highest energy. Somebody said that happiness is the medicine so it also increase your health level")
        elif happiness == 0:
            feeling5 = behaviour[5]
            print(f"Your behaviour is {feeling5}. Lowest potential, high success, high salary, high energy. Somebody said that happiness is the medicine so it also increase your health level")

           
    if action.lower() == "prices":
      print("Prices of products:")
      for item, price in items_prices.items():
         print(f"{item}: {price} coins")
    if action.lower() == "claim":
        claim_happy = rn.randint(5, 12)
        current_time2 = time.time()

        if current_time2 - last_claim_time >= 3600:
            claim_money = rn.randint(35, 130)
            money += claim_money
            print(f"You claimed {claim_money} coins.")
            last_claim_time = current_time2
            happiness += claim_happy
            print(f"Your level of happiness increased by {claim_happy}")
        else:
            time_left = int((last_claim_time + 3600) - current_time2)
            
            seconds = time_left % 60
            print(f"You need to wait minutes and {seconds} seconds before claiming again.")
    if action.lower() == "buy":
        buy = input("What do you want to buy?. To see the prices use price command. Write only the name of the product: ")
        
        if buy.lower() in items_prices and money >= items_prices[buy.lower()]:
            quantity = int(input("How many do you want to buy? "))
            print(f"Here are your {quantity} {buy}(s)")
            money -= items_prices[buy.lower()] * quantity
            if buy.lower() in inventory:
                inventory[buy.lower()] += quantity
            else:
                inventory[buy.lower()] = quantity
        
        elif buy.lower() in items_prices and money < items_prices[buy.lower()]:
            print("You don't have enough money. Please come back when you have enough.")
        else:
            print("Sorry, we don't have this product.")
        buyNext = input("Wanna to buy something else? Y/N: ")
        if buyNext.lower() == "y":
          buy2 = input("To see the prices use price command. Write only the name of the product: ")
          if buy2.lower() in items_prices and money >= items_prices[buy2.lower()]:
            quantity = int(input("How many do you want to buy? "))
            print(f"Here are your {quantity} {buy2}(s)")
            money -= items_prices[buy2.lower()] * quantity
            if buy2.lower() in inventory:
                inventory[buy2.lower()] += quantity
            else:
                inventory[buy2.lower()] = quantity
        
          elif buy2.lower() in items_prices and money < items_prices[buy2.lower()]:
            print("You don't have enough money. Please come back when you have enough.")
        elif buyNext.lower() == "n":
          print("Well, that's your choice.")
        else:
            print("Sorry, we don't have this product.")

    

    if action.lower() == "work":
        work_happy = rn.randint (1, 9)
        current_time = time.time()

        if current_time - last_work_time >= 3600:
            earning = rn.randint(25, 150)
            print("You're going to work")
            print("Work has been completed 25%")
            print("Work has been completed 50%")
            print("Work has been completed 75%")
            print(f"Work has been completed 100%.\nYour earning is {earning} coins.")
            money += earning
            last_work_time = current_time
            happiness += work_happy
            print(f"Your level of happiness increased by {work_happy}")
        else:
            time_left = int((last_work_time + 3600) - current_time)
            minutes = time_left // 60
            seconds = time_left % 60
            print(f"You need to wait {minutes} minutes and {seconds} seconds before working again.")
    elif action.lower() == "work" and happiness >= 60:
        work_happy1 = rn.randint (4, 13)
        current_time = time.time()

        if current_time - last_work_time >= 3600:
            earning1 = rn.randint(50, 200)
            print("You're going to work")
            print("Work has been completed 25%")
            print("Work has been completed 50%")
            print("Work has been completed 75%")
            print(f"Work has been completed 100%.\nYour earning is {earning1} coins.")
            money += earning1
            last_work_time = current_time
            happiness += work_happy1
            print(f"Your level of happiness increased by {work_happy1}")
        else:
            time_left = int((last_work_time + 3600) - current_time)
            minutes = time_left // 60
            seconds = time_left % 60
            print(f"You need to wait {minutes} minutes and {seconds} seconds before working again.")
    elif action.lower() == "work" and happiness >= 80:
        work_happy2 = rn.randint (7, 17)
        current_time = time.time()

        if current_time - last_work_time >= 3600:
            earning2 = rn.randint(100, 250)
            print("You're going to work")
            print("Work has been completed 25%")
            print("Work has been completed 50%")
            print("Work has been completed 75%")
            print(f"Work has been completed 100%.\nYour earning is {earning2} coins.")
            money += earning2
            last_work_time = current_time
            happiness += work_happy2
        else:
            time_left = int((last_work_time + 3600) - current_time)
            minutes = time_left // 60
            seconds = time_left % 60
            print(f"Your level of happiness increased by {work_happy2}")
            print(f"You need to wait {minutes} minutes and {seconds} seconds before working again.")      
    elif action.lower() == "work" and happiness == 100:
        work_happy3 = rn.randint (13, 23)
        current_time = time.time()

        if current_time - last_work_time >= 3600:
            earning3 = rn.randint(200, 400)
            print("You're going to work")
            print("Work has been completed 25%")
            print("Work has been completed 50%")
            print("Work has been completed 75%")
            print(f"Work has been completed 100%.\nYour earning is {earning3} coins.")
            money += earning3
            last_work_time = current_time
            happiness += work_happy3
        else:
            time_left = int((last_work_time + 3600) - current_time)
            minutes = time_left // 60
            seconds = time_left % 60
            print(f"Your level of happiness increased by {work_happy3}")
            print(f"You need to wait {minutes} minutes and {seconds} seconds before working again.")      
    elif action.lower() == "work" and happiness <= 40:
        work_happy4 = rn.randint (-4, 5)
        current_time = time.time()

        if current_time - last_work_time >= 3600:
            earning4 = rn.randint(15, 75)
            print("You're going to work")
            print("Work has been completed 25%")
            print("Work has been completed 50%")
            print("Work has been completed 75%")
            print(f"Work has been completed 100%.\nYour earning is {earning4} coins.")
            money += earning4
            last_work_time = current_time
            if work_happy4 > 0:
              happiness += work_happy4
              print(f"Your level of happiness increased by {abs(work_happy4)}")
            elif work_happy4 < 0:
              happiness -= abs(work_happy4)
              print(f"Your level of happiness decreased by {abs(work_happy4)}")
            elif work_happy4 == 0:
              print("Your level of happiness will not be increased but also will not be decreased. So you will not lose something")
        else:
            time_left = int((last_work_time + 3600) - current_time)
            minutes = time_left // 60
            seconds = time_left % 60
           
            print(f"You need to wait {minutes} minutes and {seconds} seconds before working again.")  
    elif action.lower() == "work" and happiness <= 20:
        work_happy5 = rn.randint (-8, 5)
        current_time = time.time()

        if current_time - last_work_time >= 3600:
            earning5 = rn.randint(8, 50)
            print("You're going to work")
            print("Work has been completed 25%")
            print("Work has been completed 50%")
            print("Work has been completed 75%")
            print(f"Work has been completed 100%.\nYour earning is {earning5} coins.")
            money += earning5
            last_work_time = current_time
            if work_happy5 > 0:
              happiness += work_happy5
              print(f"Your level of happiness increased by {abs(work_happy5)}")
            elif work_happy5 < 0:
              happiness -= abs(work_happy5)
              print(f"Your level of happiness decreased by {abs(work_happy5)}")
            elif work_happy5 == 0:
              print("Your level of happiness will not be increased but also will not be decreased. So you will not lose something")  
            print(f"You need to wait {minutes} minutes and {seconds} seconds before working again.") 
        else:
            time_left = int((last_work_time + 3600) - current_time)
            minutes = time_left // 60
            seconds = time_left % 60
                 
    elif action.lower() == "work" and happiness == 0:
        work_happy6 = rn.randint (-15, 2)
        current_time = time.time()

        if current_time - last_work_time >= 3600:
            earning6 = rn.randint(1, 25)
            print("You're going to work")
            print("Work has been completed 25%")
            print("Work has been completed 50%")
            print("Work has been completed 75%")
            print(f"Work has been completed 100%.\nYour earning is {earning6} coins.")
            money += earning6
            last_work_time = current_time
            if work_happy6 > 0:
              happiness += work_happy6
              print(f"Your level of happiness increased by {abs(work_happy6)}")
            elif work_happy6 < 0:
              happiness -= abs(work_happy6)
              print(f"Your level of happiness decreased by {abs(work_happy6)}")
            elif work_happy6 == 0:
              print("Your level of happiness will not be increased but also will not be decreased. So you will not lose something") 
        else:
            time_left = int((last_work_time + 3600) - current_time)
            minutes = time_left // 60
            seconds = time_left % 60
            
            print(f"You need to wait {minutes} minutes and {seconds} seconds before working again.")      
    elif action.lower() == "balance":
        print(f"Your balance is {money} coins.")
 
      
    elif action.lower() == "sleep":
      if "house" in inventory:
        print("You're sleeping 25%")
        print("You're sleeping 50%")
        print("You're sleeping 75%")
        print("You're sleeping 100%")
        health += 60
        energy += 75
        happiness += 30
      else:
        print("You sleep in the quiet cave. You made bed from nig rock and big piece of wool. Feel like you are the ")
    elif action.lower() == "use-item":
     use = input("What thing do you want to use?: ")
    
     if use.lower() == "mystery box":
        fortuna = {
            "You found a couple of money. Lucky you!": 1,
            "You found some cheap items there.": 2,
            "There was another mystery box in the box.": 3,
            "You found some expensive things.": 4,
            "You found a magic artifact that doubled your money": 5,
            "There was a fireball that burned half of your money.": 6,
            "There was a snake that bit you and decreased your health level": 7,
            "Some money got wet. You lost some money.": 8,
            "There was nothing in the box.": 9,
            "There was money that you spent for this mystery box. At least you didn't lose anything": 10,
            "There was a bomb that explosed when you were opening this mystery box and decreased half of your health": 11,
            "There was a weakness potion that decreased your energy and strength levels":12,
            "There was a stimpak from Mint greenhouse that increased your health by 35 health": 13,
            "There was a MAX energy energetic that increased your energy level and strength level":14,
        }

        fortune_result = rn.choice(list(fortuna.keys()))
        print(fortune_result)

        if fortuna[fortune_result] == 1:
            jackpot = rn.randint(1, 5)
            prize_money = rn.randint(5, 50)
            money += prize_money
            happiness += jackpot
            print(f"Your level of happiness increased by {jackpot}")
        elif fortuna[fortune_result] == 2:
            jackpot2 = rn.randint(1, 5)
            prize_itemsCheap = rn.sample(list(items_prices.keys()), rn.randint(1, 5))
            for item in prize_itemsCheap:
                if item in inventory:
                    inventory[item] += 1
                else:
                    inventory[item] = 1
            happiness += jackpot2
            print(f"Your level of happiness increased by {jackpot2}")
        elif fortuna[fortune_result] == 4:
            prize_itemsExpensive = rn.choice(["diamond", "crown", "gold", "limuzin", "car", "house", "whale", "laptop", "golden card", "golden medal", "ruby", "trophy", "lion", "tiger", "wild goat", "elephant", "crocodile", "cheetah", "jaguar", "tortoise", "peacock", "bizon", "sable", "amber", "platinum", "tourmaline", "rock crystal", "uranium", "agat", "quartz", "sapphire", "titan", "marble", "topaz", "wardrobe", "furnace", "plane ticket", "rubygite", "generator of Ruby", "creator", "computer", "motherboard", "immortin", "washing machine"])
            jackpot3 = rn.randint(3, 7)
            if prize_itemsExpensive in inventory:
                inventory[prize_itemsExpensive] += jackpot3
            else:
                inventory[prize_itemsExpensive] = jackpot3
            happiness += jackpot3
            print(f"Your level of happiness increased by {jackpot3}")
        elif fortuna[fortune_result] == 3:
            if "mystery box" in inventory:
                inventory["mystery box"] += 1
            else:
                inventory["mystery box"] = 1
        elif fortuna[fortune_result] == 5:
            omg = rn.randint(5, 12)
            money *= 2
            happiness += omg
            print(f"Your level of happiness increased by {omg}")
        elif fortuna[fortune_result] == 6:
            loser = rn.randint(5, 12)
            money /= 2
            happiness -= loser
            print(f"Your level of happiness decreased by {loser}")
        elif fortuna[fortune_result] == 7:
            minusHP = rn.randint(5, 25)
            loser3 = rn.randint(3, 15)
            health -= minusHP
            happiness -= loser3
            print(f"Your level of happiness decreased by {loser3}")
        elif fortuna[fortune_result] == 8:
            loser2 = rn.randint(3, 8)
            lost_money = rn.randint(75, 200)
            money -= lost_money
            happiness -= loser2
            print(f"Your level of happiness decreased by {loser2}")
        elif fortuna[fortune_result] == 9:
            pass  # No action needed
        elif fortuna[fortune_result] == 10:
            tie = rn.randint(0, 3)
            money += 25
            happiness += tie
            print(f"Your level of happiness increased by {tie}")
        elif fortuna[fortune_result] == 11:
            totalLose = rn.randint(10, 50)
            health /= 2
            happiness -= totalLose
            print(f"Your level of happiness decreased by {totalLose}")
        elif fortuna[fortune_result] == 12:
            tired = rn.randint(25, 50)
            weak = rn.randint(1, 20)
            breath2 = rn.randint(1, 20)
            energy -= tired
            strength -= weak
            happiness -= breath2
            print(f"Your level of energy decreased by {tired}")
            print(f"Your level of strength decreased by {weak}")
            print(f"Your level of happiness increased by {breath2}")
        elif fortuna[fortune_result] == 13:
            adrenalin = rn.randint(10, 50)
            doctor = 35
            health += doctor
            happiness -= adrenalin
            print(f"Your level of happiness increased by {doctor}")
            print(f"Your level of happiness decreased by {adrenalin}")
        elif fortuna[fortune_result] == 14:
            MAXenergy = rn.randint(25, 50)
            MAXresult = rn.randint(1, 20)
            breath = rn.randint(1, 20)
            energy += MAXenergy
            strength += MAXresult
            happiness += breath
            print(f"Your level of energy increased by {MAXenergy}")
            print(f"Your level of strength increased by {MAXresult}")
            print(f"Your level of happiness increased by {breath}")

        # Remove the used mystery box from inventory
        if "mystery box" in inventory:
            del inventory["mystery box"]
        else:
            print("You don't have a mystery box in your inventory.")

     elif use.lower() == "giftbox":
        if "giftbox" in inventory:
            gifted_happiness = rn.randint(2, 10)
            inventory["giftbox"] -= 1
            if inventory["giftbox"] == 0:
                del inventory["giftbox"]
            gifted_item = rn.choice(list(items_prices.keys()))
            if gifted_item in inventory:
                inventory[gifted_item] += 1
            else:
                inventory[gifted_item] = 1
            happiness += gifted_happiness
            
            print(f"You used the giftbox and received a {gifted_item}!")
            print(f"Your level of happiness increased by {gifted_happiness}")
        else:
            print("You don't have a giftbox in your inventory.")
            # Remove the used giftbox from inventory
            if "giftbox" in inventory:
                del inventory["giftbox"]
            else:
                print("You don't have a giftbox in your inventory.")
     elif use.lower() == "creator":
      if "creator" in inventory:
        create_happy = rn.randint (1, 10)
        current_time3 = time.time()
        creation1 = rn.choice(list(items_prices.keys()))
        print("The process of creation has been begun")
        print("Item has been created 25%")
        print("Item has been created 50%")
        print("Item has been created 75%")
        print("Item has been created 100%")
        print(f"The process of creation has been finished. The item is {creation1}")
        if current_time3 - creator_time >= 3600:
            
            creator_time = current_time3
            happiness += create_happy
        else:
            time_left = int((creator_time + 3600) - current_time3)
            minutes = time_left // 60
            seconds = time_left % 60
            print(f"You need to wait {minutes} minutes and {seconds} seconds before claiming again.")
        if creation1 in inventory:
          inventory[creation1] += 1
        else:
          inventory[creation1] = 1
      else:
        print("To create a thing you need to have a creator. Buy or craft it.")
     elif use.lower() == "aspirin":
      health += 15
      strength += 2
      energy += 8
      happiness += 1
      print("Your health increased by 15")
      print("Your strength increased by 2")
      print("Your energy increased by 8")
      print("Your happiness increased by 1")
     elif use.lower() == "penicillin":
      health += 20
      strength += 1
      energy += 10
      happiness += 2
      print("Your health increased by 20")
      print("Your strength increased by 1")
      print("Your energy increased by 10")
      print("Your happiness increased by 2")
     elif use.lower() == "zinnat":
      health += 15
      strength += 3
      energy += 5
      happiness += 2
      print("Your health increased by 15")
      print("Your strength increased by 3")
      print("Your energy increased by 5")
      print("Your happiness increased by 2")
     elif use.lower() == "tetun serum":
      health += 25
      strength += 2
      energy += 12
      happiness += 2
      print("Your health increased by 25")
      print("Your strength increased by 2")
      print("Your energy increased by 12")
      print("Your happiness increased by 2")
     elif use.lower() == "iodine":
      health += 8
      energy += 2
      happiness += 1
      print("Your health increased by 8")
      print("Your energy increased by 2")
      print("Your happiness increased by 1")
     elif use.lower() == "antiflu":
      health += 15
      strength += 1
      energy += 6
      happiness += 2
      print("Your health increased by 15")
      print("Your strength increased by 1")
      print("Your energy increased by 6")
      print("Your happiness increased by 2")
     elif use.lower() == "":
      health += 15
      strength += 2
      energy += 8
      happiness += 1
      print("Your health increased by 15")
      print("Your strength increased by 3")
      print("Your energy increased by 8")
      print("Your happiness increased by 1")
     elif use.lower() == "stimpak":
      health += 25
      strength += 4
      energy += 14
      happiness += 3
      print("Your health increased by 25")
      print("Your strength increased by 4")
      print("Your energy increased by 14")
      print("Your happiness increased by 3")
     elif use.lower() == "poison":
      health -= 35
      strength -= 8
      energy -= 20
      happiness -= 10
      print("Your health decreased by 35")
      print("Your strength decreased by 8")
      print("Your energy decreased by 20")
      print("Your happiness decreased by 10")
     elif use.lower() == "fishing pole":
          if "fishing pole" in inventory:
            fish = {
                "carp": 1,
                "perch": 2,
                "trout": 3,
                "herring": 4,
                "pelengas": 5,
                "gudgeon": 6,
                "catfish": 7,
                "pike": 8,
                "mackerel": 9,
                "tuna": 10,
                "sardina": 11,
                "salmon": 12,
                "barracuda": 13,
                "fugu fish": 14,
                "shark": 15,
                "marlin": 16,
                "whale": 17,
                "lobster": 18,
                "crab": 19,
                "jellyfish": 20,
                "octopus": 21,
                "squid": 22,
                "turtle": 23,
                "anchovy": 24
            }
            caught_fish = rn.choice(list(fish.keys()))
            print(f"You used the fishing pole and caught a {caught_fish}!")
            if caught_fish in inventory:
                inventory[caught_fish] += 1
            else:
                inventory[caught_fish] = 1
        
          else:
             print("You don't have a fishing pole in your inventory.")
      
    
     elif use.lower() == "hunting rifle":
        if "hunting rifle" in inventory:
            animals = {
                "hare": 1,
                "fox": 2,
                "raccoon": 3,
                "badger": 4,
                "wolf": 5,
                "bear": 6,
                "beaver": 7,
                "duck": 8,
                "goose": 9,
                "coyote": 10,
                "eagle": 11,
                "lion": 12,
                "tiger": 13,
                "lynx": 14,
                "wild boar": 15,
                "deer": 16,
                "moose": 17,
                "wild goat": 18,
                "elephant": 19,
                "crocodile": 20,
                "cheetah": 21,
                "vulture": 22,
                "ostrich": 23,
                "hippopotamus": 24,
                "rhinoceros": 25,
                "puma": 26,
                "jaguar": 27,
                "armadillo": 28,
                "tortoise": 29,
                "ferret": 30,
                "parrot": 31,
                "peacock": 32,
                "monkey": 33,
                "mole": 34,
                "zebra": 35,
                "hedgehog": 36,
                "porcupine": 37,
                "squirrel": 38,
                "skunk": 39,
                "python": 40,
                "antelope": 41,
                "bison": 42,
                "buffalo": 43,
                "ermine": 44,
                "cassowary": 45,
                "sable": 46,
                "chipmunk": 47,
                "sheep": 48,
                "cow": 49,
                "hen": 50,
            }
            animalHunt = rn.choice(list(animals.keys()))
            print(f"You used the hunting rifle and killed the {animalHunt}!")
            if animalHunt in inventory:
                inventory[animalHunt] += 1
            else:
                inventory[animalHunt] = 1
        else:
            print("You don't have a hunting rifle in your inventory.")

     elif use.lower() == "pickaxe" or "jackhammer":
       if "pickaxe" or "jackhammer" in inventory: 
         rocksAndstones = {
         "coal": 1,
         "silver": 2,
         "granite": 3,
         "uranium": 4,
         "clay": 5,
         "gold": 6,
         "amber": 7,
         "iron": 8,
         "oil bar": 9,
         "stone": 10,
         "rock salt": 11,
         "limestone": 12,
         "tungsten": 13,
         "platinum": 14,
         "tourmaline": 15,
         "rock crystal": 16,
         "agat": 17,
         "sand": 18,
         "lean": 19,
         "zinc": 20,
         "tin": 21,
         "quartz": 22,
         "marble": 23,
         "aluminium": 24,
         "nickel": 25,
         "sapphire": 26,
         "natural gas": 27,
         "titan": 28,
         "topaz": 29,
         "cobblestone":30,
         "diamond": 31,
         "emerald": 32,
         "ruby": 33,
         "aquamarine": 41,
         "badrock": 34,
         "redstone":35,
         "copper": 36,
         "magnet": 37,
         "rubygite": 38,
         "sulfur": 39,
         "saltpeter": 40,
         
       }
         mineCraft = rn.choice(list(rocksAndstones.keys()))
         print(f"You used the pickaxe and mined the {mineCraft}.")
         if mineCraft in inventory:
           inventory[mineCraft]+= 1
         else:
           inventory[mineCraft] = 1
       else:
         print("You don't have an axe in your inventory.")
        
     else:
        print("Invalid item. Please try again.")
    
    
    if action.lower() == "sport":
      sporty= input("what do you want to use to do sport (treadmill, exercise bike, barbell, horizontal bar, punching bag, expander, weight, dumbbell, sweden ladder, gymnastic horse)? ")
      if sporty.lower() == "treadmill" and "treadmill" in inventory:
        print("Now you're legs are strong and full of power.")
        health += 5
        energy += 10
        strength += 2
        print("Your health increased by 5")
        print("Your energy increased by 10")
        print("You strengtj increased by 2")
      elif sporty.lower() == "treadmill" and "treadmill" not in inventory:
        print("You don't have treadmill. Please buy it. Or you can go to the gym")
      elif sporty.lower() == "exercise bike" and "exercise bike" in inventory:
        print("In healthy body, healthy mood.")
        health += 7
        energy += 13
        strength += 3
        print("Your health increased by 7")
        print("Your energy increased by 13")
        print("You strength increased by 3")
      elif sporty.lower() == "exercise bike" and "exercise bike" not in inventory:
        print("You don't have exercise bike. Please buy it. Or you can go to the gym")
      elif sporty.lower() == "barbell" and "barbell" in inventory:
        print("Now you are not afraid to lift a 80-kilogram load. And maybe even more. Keep exercising. And everything will be very good.")
        health += 6
        energy += 10
        strength += 5
        print("Your health increased by 6")
        print("Your energy increased by 10")
        print("You strength increased by 5")
      elif sporty.lower() == "barbell" and "barbell" not in inventory:
        print("You don't have barbell. Please buy it. Or you can go to the gym")
      elif sporty.lower() == "expander" and "expander" in inventory:
        print("Now you have a real crocodile grip..")
        health += 3
        energy += 4
        strength += 1
        print("Your health increased by 3")
        print("Your energy increased by 4")
        print("You strength increased by 1")
      elif sporty.lower() == "expander" and "expander" not in inventory:
        print("You don't have expander. Please buy it. Or you can go to the gym")
      elif sporty.lower() == "punching bag" and "punching bag" in inventory:
        print("Imagine that a bag is a sworn enemy. Your task is to win him. So give him the right answer. Let him see who he contacted.")
        health += 6
        energy += 9
        strength += 5
        print("Your health increased by 6")
        print("Your energy increased by 9")
        print("You strength increased by 5")
      elif sporty.lower() == "punching bag" and "punching bag" not in inventory:
        print("You don't have punching bag. Please buy it. Or you can go to the gym")
      elif sporty.lower() == "sweden ladder" and "sweden ladder" in inventory:
        print("This ladder is versatile. In addition to training climbing on it, you can also use it for other exercises like abs and parallel bars. In addition, you can fasten a horizontal bar to it and you can pull yourself up. The Swedes are great fellows.")
        health += 2
        energy += 7
        strength += 2
        print("Your health increased by 2")
        print("Your energy increased by 7")
        print("You strength increased by 2")
      elif sporty.lower() == "sweden ladder" and "sweden ladder" not in inventory:
        print("You don't have sweden ladder. Please buy it. Or you can go to the gym")
      elif sporty.lower() == "horizontal bar" and "horizontal bar" in inventory:
        print("Come on, who can pull up 1 time on the horizontal bar? And who is 5? Who is 10? Who is 20? Okay, I'll stop this torture. If you want to be able to pull up, then rather climb on the horizontal bar.")
        health += 4
        energy += 10
        strength += 5
        print("Your health increased by 4")
        print("Your energy increased by 10")
        print("You strength increased by 5")
      elif sporty.lower() == "horizontal bar" and "horizontal bar" not in inventory:
        print("You don't have horizontal bar. Please buy it. Or you can go to the gym")
      elif sporty.lower() == "weight" and "weight" in inventory:
        print("Prove that you are a strong person. Lift these 50 kg of pure cast iron in the form of a weight. Try another. If you can do that, then you are a fan of Schwarzenegger.")
        health += 2
        energy += 5
        strength += 10
        print("Your health increased by 2")
        print("Your energy increased by 5")
        print("You strength increased by 10")
      elif sporty.lower() == "weight" and "weight" not in inventory:
        print("You don't have weight. Please buy it. Or you can go to the gym")
      elif sporty.lower() == "dumbbell" and "dumbbell" in inventory:
        print("This simple exercise trains several pieces. First, your grip, second, your strength, third, your motor skills, and fourth, your punching power.")
        health += 3
        energy += 6
        strength += 5
        print("Your health increased by 3")
        print("Your energy increased by 6")
        print("You strength increased by 5")
      elif sporty.lower() == "dumbbell" and "dumbbell" not in inventory:
        print("You don't have dumbbell. Please buy it. Or you can go to the gym")
      elif sporty.lower() == "gymnastic horse" and "gymnastic horse" in inventory:
        print("Not every person is able to do this exercise. And you try. This is a very interesting trainer. You just try to climb over it or you will be cooler, do an interesting exercise. After all, you choose what to do.")
        health += 4
        energy += 12
        strength += 6
        print("Your health increased by 4")
        print("Your energy increased by 12")
        print("You strength increased by 6")
      elif sporty.lower() == "gymnastic horse" and "gymnastic horse" not in inventory:
        print("You don't have gymnastic horse. Please buy it. Or you can go to the gym")
    if action.lower() == "garden":
     grow_happiness = rn.randint(1, 15)
     seedsQuestion = input("What do you want to grow: ")
    
     if seedsQuestion.lower() == "apple":
        if "apple seeds" in inventory:
            del inventory ["apple seeds"] 
            print("You dug a small hole in the ground.")
            print("You put apple seeds in this hole.")
            print("You watered this place and started to wait.")
            apple = rn.randint(1, 6)
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "apple" in inventory:
                    inventory["apple"] += apple
                    print(f"Here is your {apple} apples")
            else:
                    inventory["apple"] = apple
                    print(f"Here is your {apple} apples")
        else: 
          print("You need apple seeds to grow apples. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "banana":
         if "banana seeds" in inventory:
            del inventory ["banana seeds"] 
            print("You dug a small hole in the ground.")
            print("You put banana seeds in this hole.")
            print("You watered this place and started to wait.")
            banana = rn.randint(1, 5)
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "banana" in inventory:
                    inventory["banana"] += banana
                    print(f"Here is your {banana} bananas")
            else:
                    inventory["banana"] = banana
                    print(f"Here is your {banana} bananas")
         else: 
          print("You need banana seeds to grow bananas. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "tomato":
        if "tomato seeds" in inventory:
            del inventory ["tomato seeds"] 
            print("You dug a small hole in the ground.")
            print("You put tomato seeds in this hole.")
            print("You watered this place and started to wait.")
            tomato = rn.randint(1, 4)
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "tomato" in inventory:
                    inventory["tomato"] += tomato
                    print(f"Here is your {tomato} tomatoes")
            else:
                    inventory["tomato"] = tomato
                    print(f"Here is your {tomato} tomatoes")
        else: 
          print("You need tomato seeds to grow tomatoes. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "lemon":
        if "lemon seeds" in inventory:
            del inventory ["lemon seeds"] 
            print("You dug a small hole in the ground.")
            print("You put lemon seeds in this hole.")
            print("You watered this place and started to wait.")
            lemon = rn.randint(1, 4),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "lemon" in inventory:
                    inventory["lemon"] += lemon
                    print(f"Here is your {lemon} lemons")
            else:
                    inventory["lemon"] = lemon
                    print(f"Here is your {lemon} lemons")
        else: 
          print("You need lemon seeds to grow lemons. Please buy them and come back if you'll ready.")
       
     elif seedsQuestion.lower() == "orange":
        if "orange seeds" in inventory:
            del inventory ["orange seeds"] 
            print("You dug a small hole in the ground.")
            print("You put orange seeds in this hole.")
            print("You watered this place and started to wait.")
            orange = rn.randint(1, 5),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "lemon" in inventory:
                    inventory["orange"] += orange
                    print(f"Here is your {orange} oranges")
            else:
                    inventory["orange"] = orange
                    print(f"Here is your {orange} oranges")
        else: 
          print("You need orange seeds to grow oranges. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "pumpkin":
        if "pumpkin seeds" in inventory:
            del inventory ["pumpkin seeds"] 
            print("You dug a small hole in the ground.")
            print("You put pumpkin seeds in this hole.")
            print("You watered this place and started to wait.")
            pumpkin = rn.randint(1, 3),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "pumpkin" in inventory:
                    inventory["pumpkin"] += pumpkin
                    print(f"Here is your {pumpkin} pumpkins")
            else:
                    inventory["pumpkin"] = pumpkin
                    print(f"Here is your {pumpkin} pumpkins")
     
        else: 
          print("You need pumpkin seeds to grow pumpkins. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "peach":
        if "peach seeds" in inventory:
            del inventory ["peach seeds"] 
            print("You dug a small hole in the ground.")
            print("You put peach seeds in this hole.")
            print("You watered this place and started to wait.")
            peach = rn.randint(1, 5),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "peach" in inventory:
                    inventory["peach"] += peach
                    print(f"Here is your {peach} peaches")
            else:
                    inventory["peach"] = peach
                    print(f"Here is your {peach} peaches")
     
        else: 
          print("You need peach seeds to grow peaches. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "strawberry":
        if "strawberry seeds" in inventory:
            del inventory ["strawberryseeds"] 
            print("You dug a small hole in the ground.")
            print("You put strawberry seeds in this hole.")
            print("You watered this place and started to wait.")
            strawberry = rn.randint(1, 3),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "strawberry" in inventory:
                    inventory["strawberry"] += strawberry
                    print(f"Here is your {strawberry} strawberries")
            else:
                    inventory["strawberry"] = strawberry
                    print(f"Here is your {strawberry} strawberries")
     
        else: 
          print("You need strawberry seeds to grow strawberries. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "rawsberry":
        if "rawsberry seeds" in inventory:
            del inventory ["rawsberry seeds"] 
            print("You dug a small hole in the ground.")
            print("You put rawsberry seeds in this hole.")
            print("You watered this place and started to wait.")
            rawsberry = rn.randint(1, 3),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "rawsberry" in inventory:
                    inventory["rawsberry"] += rawsberry
                    print(f"Here is your {rawsberry} rawsberries")
            else:
                    inventory["rawsberry"] = rawsberry
                    print(f"Here is your {rawsberry} rawsberries")
        else: 
          print("You need rawsberry seeds to grow rawsberries. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "carrot":
        if "carrot seeds" in inventory:
            del inventory ["carrot seeds"] 
            print("You dug a small hole in the ground.")
            print("You put carrot seeds in this hole.")
            print("You watered this place and started to wait.")
            carrot = rn.randint(1, 2),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "carrot" in inventory:
                    inventory["carrot"] +=carrot
                    print(f"Here is your {carrot} carrots")
            else:
                    inventory["carrot"] = carrot
                    print(f"Here is your {carrot} carrots")
        else: 
          print("You need carrot seeds to grow carrots. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "cocoa":
        if "cocoa seeds" in inventory:
            del inventory ["cocoa seeds"] 
            print("You dug a small hole in the ground.")
            print("You put cocoa seeds in this hole.")
            print("You watered this place and started to wait.")
            cocoa = rn.randint(1, 5),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "cocoa" in inventory:
                    inventory["cocoa"] += cocoa
                    print(f"Here is your {cocoa} cocoa")
            else:
                    inventory["cocoa"] = cocoa
                    print(f"Here is your {cocoa} cocoa")
        else: 
          print("You need cocoa seeds to grow cocoa. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "barley":
        if "barley seeds" in inventory:
            del inventory ["barley seeds"] 
            print("You dug a small hole in the ground.")
            print("You put barley seeds in this hole.")
            print("You watered this place and started to wait.")
            barley = rn.randint(1, 15),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "barley" in inventory:
                    inventory["barley"] += barley
                    print(f"Here is your {barley} barley")
            else:
                    inventory["barley"] = barley
                    print(f"Here is your {barley} barley")
        else: 
          print("You need barley seeds to grow barley. Please buy them and come back if you'll ready.")
     
     elif seedsQuestion.lower() == "grapes":
        if "grapes seeds" in inventory:
            del inventory ["grapes seeds"] 
            print("You dug a small hole in the ground.")
            print("You put grapes seeds in this hole.")
            print("You watered this place and started to wait.")
            grapes = rn.randint(1, 8),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "grapes" in inventory:
                    inventory["grapes"] += grapes
                    print(f"Here is your {grapes} grapes")
            else:
                    inventory["grapes"] = grapes
                    print(f"Here is your {grapes} grapes")
        else: 
          print("You need grapes seeds to grow grapes. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "watermelon":
        if "watermelon seeds" in inventory:
            del inventory ["watermelon seeds"] 
            print("You dug a small hole in the ground.")
            print("You put watermelon seeds in this hole.")
            print("You watered this place and started to wait.")
            watermelon = rn.randint(1, 2),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "watermelon" in inventory:
                    inventory["watermelon"] += watermelon
                    print(f"Here is your {watermelon} watermelons")
            else:
                    inventory["watermelon"] = watermelon
                    print(f"Here is your {watermelon} watermelons ")
        else: 
          print("You need watermelon seeds to grow watermelons. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "apricot":
        if "apricot seeds" in inventory:
            del inventory ["apricot seeds"] 
            print("You dug a small hole in the ground.")
            print("You put apricot seeds in this hole.")
            print("You watered this place and started to wait.")
            apricot = rn.randint(1, 6),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "apricot" in inventory:
                    inventory["apricot"] += apricot
                    print(f"Here is your {apricot} apricots")
            else:
                    inventory["apricot"] = apricot
                    print(f"Here is your {apricot} apricots ")
        else: 
          print("You need apricot seeds to grow apricots. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "blueberry":
        if "blueberryn seeds" in inventory:
            del inventory ["blueberry seeds"] 
            print("You dug a small hole in the ground.")
            print("You put blueberry seeds in this hole.")
            print("You watered this place and started to wait.")
            blueberry = rn.randint(1, 10),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "watermelon" in inventory:
                    inventory["blueberry"] += blueberry
                    print(f"Here is your {blueberry} blueberries")
            else:
                    inventory["blueberry"] = blueberry
                    print(f"Here is your {blueberry} blueberries ")
        else: 
          print("You need blueberry seeds to grow blueberries. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "melon":
        if "melon seeds" in inventory:
            del inventory ["melon seeds"] 
            print("You dug a small hole in the ground.")
            print("You put melon seeds in this hole.")
            print("You watered this place and started to wait.")
            melon = rn.randint(1, 2),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "watermelon" in inventory:
                    inventory["melon"] += melon
                    print(f"Here is your {melon} melons")
            else:
                    inventory["melon"] = melon
                    print(f"Here is your {melon} melons ")
        else: 
          print("You need melon seeds to grow melons. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "sunflower":
        if "sunflower seeds" in inventory:
            del inventory ["sunflower seeds"] 
            print("You dug a small hole in the ground.")
            print("You put sunflower seeds in this hole.")
            print("You watered this place and started to wait.")
            sunflower = 1,
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "watermelon" in inventory:
                    inventory["sunflower"] += sunflower
                    print(f"Here is your {sunflower} sunflowers")
            else:
                    inventory["sunflower"] = sunflower
                    print(f"Here is your {sunflower} sunflowers ")
        else: 
          print("You need sunflower seeds to grow sunflowers. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "olives":
        if "olives seeds" in inventory:
            del inventory ["olives seeds"] 
            print("You dug a small hole in the ground.")
            print("You put olives seeds in this hole.")
            print("You watered this place and started to wait.")
            olives = rn.randint(1, 12),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "olives" in inventory:
                    inventory["olives"] += olives
                    print(f"Here is your {olives} olives")
            else:
                    inventory["olives"] = olives
                    print(f"Here is your {olives} olives ")
        else: 
          print("You need olives seeds to grow olives. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "cabbage":
        if "cabbage seeds" in inventory:
            del inventory ["cabbage seeds"] 
            print("You dug a small hole in the ground.")
            print("You put cabbage seeds in this hole.")
            print("You watered this place and started to wait.")
            cabbage = 1,
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "cabbage" in inventory:
                    inventory["cabbage"] += cabbage
                    print(f"Here is your {cabbage} cabbages")
            else:
                    inventory["cabbage"] = cabbage
                    print(f"Here is your {cabbage} cabbages ")
        else: 
          print("You need cabbage seeds to grow cabbages. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "lettuce":
        if "lettuce seeds" in inventory:
            del inventory ["lettuce seeds"] 
            print("You dug a small hole in the ground.")
            print("You put lettuce seeds in this hole.")
            print("You watered this place and started to wait.")
            lettuce = rn.randint(1, 6),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "lettuce" in inventory:
                    inventory["lettuce"] += lettuce
                    print(f"Here is your {lettuce} lettuces")
            else:
                    inventory["lettuce"] = lettuce
                    print(f"Here is your {lettuce} lettuces ")
        else: 
          print("You need lettuce seeds to grow lettuces. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "cucumber":
        if "cucumber seeds" in inventory:
            del inventory ["cucumber seeds"] 
            print("You dug a small hole in the ground.")
            print("You put cucumber seeds in this hole.")
            print("You watered this place and started to wait.")
            cucumber = rn.randint(1, 4),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "cucumber" in inventory:
                    inventory["cucumber"] += cucumber
                    print(f"Here is your {cucumber} cucumbers")
            else:
                    inventory["cucumber"] = cucumber
                    print(f"Here is your {cucumber} cucumbers ")
        else: 
          print("You need cucumber seeds to grow cucumbers. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "eggplant":
        if "eggplant seeds" in inventory:
            del inventory ["eggplant seeds"] 
            print("You dug a small hole in the ground.")
            print("You put eggplant seeds in this hole.")
            print("You watered this place and started to wait.")
            eggplant = rn.randint(1, 3),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "eggplant" in inventory:
                    inventory["eggplant"] += eggplant
                    print(f"Here is your {eggplant} eggplants")
            else:
                    inventory["eggplant"] = eggplant
                    print(f"Here is your {eggplant} eggplants ")
        else: 
          print("You need eggplant seeds to grow eggplants. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "broccoli":
        if "broccoli seeds" in inventory:
            del inventory ["broccoli seeds"] 
            print("You dug a small hole in the ground.")
            print("You put broccoli seeds in this hole.")
            print("You watered this place and started to wait.")
            broccoli = 1,
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "broccoli" in inventory:
                    inventory["broccoli"] += broccoli
                    print(f"Here is your {broccoli} broccolies")
            else:
                    inventory["broccoli"] = broccoli
                    print(f"Here is your {broccoli} broccolies ")
        else: 
          print("You need broccoli seeds to grow broccolies. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "zucchini":
        if "zucchini seeds" in inventory:
            del inventory ["zucchini seeds"] 
            print("You dug a small hole in the ground.")
            print("You put zucchini seeds in this hole.")
            print("You watered this place and started to wait.")
            zucchini = rn.randint(1, 5),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "zucchini" in inventory:
                    inventory["zucchini"] += zucchini
                    print(f"Here is your {zucchini} zucchinies")
            else:
                    inventory["zucchini"] = zucchini
                    print(f"Here is your {zucchini} zucchinies ")
        else: 
          print("You need zucchini seeds to grow zucchinies. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "beets":
        if "beets seeds" in inventory:
            del inventory ["beets seeds"] 
            print("You dug a small hole in the ground.")
            print("You put beets seeds in this hole.")
            print("You watered this place and started to wait.")
            beets = rn.randint(1, 4),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "beets" in inventory:
                    inventory["beets"] += beets
                    print(f"Here is your {beets} beets")
            else:
                    inventory["beets"] = beets
                    print(f"Here is your {beets} beets ")
        else: 
          print("You need beets seeds to grow beets. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "corn":
        if "corn seeds" in inventory:
            del inventory ["corn seeds"] 
            print("You dug a small hole in the ground.")
            print("You put corn seeds in this hole.")
            print("You watered this place and started to wait.")
            corn = rn.randint(1, 4),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "corn" in inventory:
                    inventory["corn"] += corn
                    print(f"Here is your {corn} corns")
            else:
                    inventory["corn"] = corn
                    print(f"Here is your {corn} corns ")
        else: 
          print("You need corn seeds to grow corns. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "pepper":
        if "pepper seeds" in inventory:
            del inventory ["pepper seeds"] 
            print("You dug a small hole in the ground.")
            print("You put pepper seeds in this hole.")
            print("You watered this place and started to wait.")
            pepper = rn.randint(1, 6),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "pepper" in inventory:
                    inventory["pepper"] += pepper
                    print(f"Here is your {pepper} peppers")
            else:
                    inventory["pepper"] = pepper
                    print(f"Here is your {pepper} peppers ")
        else: 
          print("You need pepper seeds to grow peppers. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "black pepper":
        if "black pepper seeds" in inventory:
            del inventory ["black pepper seeds"] 
            print("You dug a small hole in the ground.")
            print("You put black pepper seeds in this hole.")
            print("You watered this place and started to wait.")
            black = rn.randint(1, 14),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "black pepper" in inventory:
                    inventory["black pepper"] += black
                    print(f"Here is your {black} black peppers")
            else:
                    inventory["black pepper"] = black
                    print(f"Here is your {black} black peppers ")
        else: 
          print("You need black pepper seeds to grow black peppers. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "mustard":
        if "mustard seeds" in inventory:
            del inventory ["mustard seeds"] 
            print("You dug a small hole in the ground.")
            print("You put mustard seeds in this hole.")
            print("You watered this place and started to wait.")
            mustard = rn.randint(1, 10),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "mustard" in inventory:
                    inventory["mustard"] += mustard
                    print(f"Here is your {mustard} mustard")
            else:
                    inventory["mustard"] = mustard
                    print(f"Here is your {mustard} mustard ")
        else: 
          print("You need mustard seeds to grow mustard. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "pea":
        if "pea seeds" in inventory:
            del inventory ["pea seeds"] 
            print("You dug a small hole in the ground.")
            print("You put pea seeds in this hole.")
            print("You watered this place and started to wait.")
            pea = rn.randint(1, 7),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "pea" in inventory:
                    inventory["pea"] += pea
                    print(f"Here is your {pea} peas")
            else:
                    inventory["pea"] = pea
                    print(f"Here is your {pea} peas ")
        else: 
          print("You need pea seeds to grow peas. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "potato":
        if "potato seeds" in inventory:
            del inventory ["potato seeds"] 
            print("You dug a small hole in the ground.")
            print("You put potato seeds in this hole.")
            print("You watered this place and started to wait.")
            potato = rn.randint(1, 5),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "potato" in inventory:
                    inventory["potato"] += potato
                    print(f"Here is your {potato} potatoes")
            else:
                    inventory["potato"] = potato
                    print(f"Here is your {potato} potatoes ")
        else: 
          print("You need potato seeds to grow potatoes. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "onion":
        if "onion seeds" in inventory:
            del inventory ["onion seeds"] 
            print("You dug a small hole in the ground.")
            print("You put onion seeds in this hole.")
            print("You watered this place and started to wait.")
            onion = rn.randint(1, 4),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "onion" in inventory:
                    inventory["onion"] += onion
                    print(f"Here is your {onion} onions")
            else:
                    inventory["onion"] = onion
                    print(f"Here is your {onion} onions ")
        else: 
          print("You need onion seeds to grow onions. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "garlic":
        if "garlic seeds" in inventory:
            del inventory ["garlic seeds"] 
            print("You dug a small hole in the ground.")
            print("You put garlic seeds in this hole.")
            print("You watered this place and started to wait.")
            garlic = rn.randint(1, 3),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "garlic" in inventory:
                    inventory["garlic"] += garlic
                    print(f"Here is your {garlic} garlics")
            else:
                    inventory["garlic"] = garlic
                    print(f"Here is your {garlic} garlivs ")
        else: 
          print("You need garlic seeds to grow garlics. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "mint":
        if "mint seeds" in inventory:
            del inventory ["mint seeds"] 
            print("You dug a small hole in the ground.")
            print("You put mint seeds in this hole.")
            print("You watered this place and started to wait.")
            mint = rn.randint(1, 6),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "mint" in inventory:
                    inventory["mint"] += mint
                    print(f"Here is your {mint} mints")
            else:
                    inventory["mint"] = mint
                    print(f"Here is your {mint} mints ")
        else: 
          print("You need mint seeds to grow mints. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "lime":
        if "lime seeds" in inventory:
            del inventory ["lime seeds"] 
            print("You dug a small hole in the ground.")
            print("You put lime seeds in this hole.")
            print("You watered this place and started to wait.")
            lime = rn.randint(1, 5),
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "lime" in inventory:
                    inventory["lime"] += lime
                    print(f"Here is your {lime} limes")
            else:
                    inventory["lime"] = lime
                    print(f"Here is your {lime} limes ")
        else: 
          print("You need lime seeds to grow limes. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "mango":
        if "mango seeds" in inventory:
            del inventory ["mango seeds"] 
            print("You dug a small hole in the ground.")
            print("You put mango seeds in this hole.")
            print("You watered this place and started to wait.")
            mango = rn.randint(1, 4)
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "mango" in inventory:
                    inventory["mango"] += mango
                    print(f"Here is your {mango} mangos")
            else:
                    inventory["mango"] = mango
                    print(f"Here is your {mango} mangos ")
        else: 
          print("You need mango seeds to grow mangos. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "tea plant":
        if "tea plant seeds" in inventory:
            del inventory ["tea plant seeds"] 
            print("You dug a small hole in the ground.")
            print("You put tea plant seeds in this hole.")
            print("You watered this place and started to wait.")
            tea = rn.randint(1, 5)
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "tea plant" in inventory:
                    inventory["tea plant"] += tea
                    print(f"Here is your {tea} tea plants")
            else:
                    inventory["tea plant"] = tea
                    print(f"Here is your {tea} tea plants ")
        else: 
          print("You need tea plant seeds to grow tea plants. Please buy them and come back if you'll ready.")
     elif seedsQuestion.lower() == "coffee bean":
        if "coffee seeds" in inventory:
            del inventory ["coffee seeds"] 
            print("You dug a small hole in the ground.")
            print("You put coffee seeds in this hole.")
            print("You watered this place and started to wait.")
            coffee = rn.randint(1, 9)
            happiness += grow_happiness
            print(f"Your happiness level increased by {grow_happiness}")
            if "coffee bean" in inventory:
                    inventory["coffee bean"] += coffee
                    print(f"Here is your {coffee} coffee beans")
            else:
                    inventory["coffee"] = coffee
                    print(f"Here is your {coffee} coffee beans")
        else: 
          print("You need coffee seeds to grow coffee beans. Please buy them and come back if you'll ready.")
    elif action.lower() == "cook":  
        recipe2 = {
          "dough": {"flour": 1, "egg": 3,"water":2, "sugar":2},
          "bread":{"yeast": 1, "dough": 1, "salt": 2},
          "cheese": {"milk": 2},
          "butter": {"milk": 2},
          "chocolate": {"cocoa": 2, "sugar":1, "milk":1},
          "beer": {"sugar":2, "flour": 1, "barley": 3},
          "lemonade": {"lemon": 2, "water": 3, "sugar":2},
          "crisps": {"potato": 2, "salt": 2},
          "ice-cream":{"milk": 2, "chocolate": 1, "strawberry":1, "dough":1},
          "wine":{"grapes": 4},
          "donut": {"dough": 1, "milk": 2, "sugar":1, "yeast": 1, "chocolate": 1},
          "ketchup": {"tomato": 3, "sugar": 1, "salt":1, "vinegar":1},
          "hamburger": {"bread":1, "tomato":1, "onion": 1, "ketchup":1, "cheese": 1, "meat": 1},
          "cookies": {"dough": 1, "chocolate": 2},
          "pasta": {"dough": 1},
          "salad": {"cucumber": 2, "tomato": 2, "onion": 2, "lettuce": 1, "sunflower oil":1},
          "popcorn": {"corn": 2},
          "pumpkin pie": {"pumpkin": 2, "egg": 3, "milk": 2, "sugar": 1},
          "salami": {"meat":1},
          "sausage": {"meat":2},
          "bbq": {"meat": 3},
          "pizza": {"dough": 1, "salami": 2, "ketchup":1, "cheese":2, "anchowy": 7, "tomato":3, "olives": 6},
          "sunflower oil": {"sunflower": 2},
          "olive oil": {"olives":2},
          "mayonnaise": {"olive oil":1, "egg": 3, "vinegar":1, "lemon":1, "mustard":2},
          "hot dog": {"sausage": 1, "dough": 1, "salt":2, "ketchup":1, "mustard": 2},
          "nachos": {"dough":1, "salt":2, "cheese": 1},
          "lasagna": {"cheese": 2, "flour": 3, "tomato": 3, "onion": 2, "egg": 2, "olive oil": 1, "butter":1},
          "olivier salad":{"potato": 5, "carrot": 3, "meat": 2, "pea": 14, "cucumber": 3, "onion": 1, "egg": 3},
          "potato soup": {"potato": 3, "carrot": 2, "water": 3, "onion": 2, "garlic": 1},
          "borsch": {"water": 2, "meat": 2, "onion":1, "beets": 3, "tomato": 1, "garlic": 2, "carrot": 2, "cabbage": 1},
          "harcho": {"cow": 1, "water": 2, "tomato": 1, "pepper": 2, "black pepper":1, "salt": 1},
          "chocolate cake": {"dough": 1, "milk": 1, "chocolate": 3, "sugar":3, "yeast":2},
          "fish pie": {"tuna": 2, "salmon": 2, "dough": 1, "salt": 2, "lemon": 1},
          "salt": {"rock salt":1},
          "rum":{"sugar": 7},
          "mojito": {"sugar": 3, "rum": 1, "mint": 2, "lime": 1},
          "pasta with cheese":  {"pasta": 1, "cheese": 1},
          "sushi": {"rice": 3, "salmon": 1, "tuna": 1, "lettuce": 1},
          "meat dumplings": {"dough": 1, "meat": 2, "salt": 1, "black pepper": 1, "vinegar":1},
          "stew": {"potato": 2, "cabbage":1, "carrot": 2, "meat": 2, "salt": 1, "tomato":2, "zucchini": 1, "onion": 1, "water": 1},
          "ramen": {"pasta": 1, "carrot": 1, "meat": 1," black pepper": 1, "water": 2},
          "apple pie":{"apple": 3, "dough": 1, "milk":1, "sugar": 1},
          "sauerkraut": {"cabbage": 1, "carrot": 2, "apple": 2, "lemon": 1, "water": 1, "sugar": 1},
        }
        print("Available recipes: ")
        for item, ingredients in recipe2.items():
            print(f"{item}: {ingredients}")
        item_to_cook = input("Which item do you want to cook? ")
        if item_to_cook.lower() in recipe2:
            ingredients = recipe2[item_to_cook.lower()]
            can_cook = True
            for ingredient, quantity in ingredients.items():
                if ingredient.lower() not in inventory or inventory[ingredient.lower()] < quantity:
                    can_cook = False
                    break
            if can_cook:
                for ingredient, quantity in ingredients.items():
                    inventory[ingredient.lower()] -= quantity
                if item_to_cook.lower() in inventory:
                    inventory[item_to_cook.lower()] += 1
                else:
                    inventory[item_to_cook.lower()] = 1
                print(f"You have cooked {item_to_cook}.")
            else:
                print("You don't have enough ingredients to cook that item.")
        else:
            print("That item cannot be cooked.")
     
  
    
    elif action.lower() == "inventory":
        Spoilable = ["apple", "banana", "cheese", "tomato", "meat", "flour", "milk", "egg", "potato", "butter", "cola", "juice", "chocolate", "bread", "beer", "lemon", "orange", "lemonade", "coffee", "crisps", "ice-cream", "peach", "strawberry", "rawsberry", "donut", "pumpkin", "carrot", 'ketchup', "hamburger", " wine", "yeast", "cocoa", "barley", "anchowy", "onion", "grapes", "sunflower", "grapes", "olives", "cabage", "lettuce", "cucumber", "eggplant", "zucchini", "broccoli", "beets", "sunflower oil", "corn", "olive oil", "garlic", "vinegar", "black pepper", "pepper", "cookies", "pasta", " salami", "sausage", "popcorn", "mustard", "pea", "watermelon", "melon", "blueberry", "apricot", "mint", "coffee bean", "tea plant", "lime", "pizza", "harcho", "salad", "lasagna", "hot-dog", "nachos", "bbq", "potato soup", "rum", "olivier salad", "pumpkin pie", "borsch", "dough", "mojito", "chocolate cake", "fish pie", "mayonnaise"]
        timeBeforeSpoil = time.time()
        print("Your inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
        
        if item in inventory and item in Spoilable: 
         if timeBeforeSpoil - eadableTime > 10800:
            del inventory[item]
            spoiled_item = f"spoiled {item}"
            inventory[spoiled_item] = inventory.get(spoiled_item, 0) + 1
            edibleTime = timeBeforeSpoil
         else:
            time_left = int((timeBeforeSpoil + 10800) - eadableTime)
            seconds = time_left % 10800
            print(f"Hurry! This food will be spoiled after {seconds} seconds")
    elif action.lower() == "sell":
        productSell = input("What product do you want to sell: ")
        if productSell.lower() in inventory:
            quantitySell = int(input(f"How many {productSell}(s) do you want to sell? "))
            if inventory[productSell.lower()] >= quantitySell:
                moneySell = rn.randint(items_prices[productSell.lower()] - 3, items_prices[productSell.lower()] + 3) * quantitySell
                money += moneySell
                inventory[productSell.lower()] -= quantitySell
                print(f"You earned {moneySell} coins.")
                if inventory[productSell.lower()] == 0:
                    del inventory[productSell.lower()]
            else:
                print("You don't have enough of that item in your inventory.")
        else:
            print("You don't have that item in your inventory.") 
    elif action.lower() == "eat":
     food = input("What do you want to eat. Hurry, hurry! You need to eat it before 15 mins. Otherwise, you will have spoiled food ")
     if food.lower() in inventory:
       inventory[food.lower()] -= 1
       
       if food.lower() == "watermelon":
         health += 2
         energy += 7
         happiness += 3
         print("Your health level increased by 2")
         print("Your energy level increased by 7")
         print("Your happiness level increased by 3")
       if food.lower() == "spoiled watermelon":
         health -= 3
         energy -= 5
         happiness -= 2
         print("Your health level decreased by 3")
         print("Your energy level decreased by 5")
         print("Your happiness level decreased by 2")
       if food.lower() == "apricot":
         health += 1
         energy += 3
         print("Your health level increased by 1")
         print("Your energy level increased by 3")
       if food.lower() == "spoiled apricot":
         health -= 2
         energy -= 3
         happiness -= 2
         print("Your health level decreased by 2")
         print("Your energy level decreased by 3")
         print("Your happiness level decreased by 2")
       if food.lower() == "blueberry":
         health += 2
         energy += 5
         print("Your health level increased by 2")
         print("Your energy level increased by 5")
       if food.lower() == "spoiled blueberry":
         health -= 4
         energy -= 6
         happiness -= 3
         print("Your health level decreased by 3")
         print("Your energy level decreased by 5")
         print("Your happiness level decreased by 2")
       if food.lower() == "melon":
         health += 2
         energy += 6
         happiness += 3
         print("Your health level increased by 2")
         print("Your energy level increased by 6")
         print("Your happiness level increased by 3")
       if food.lower() == "spoiled melon":
         health -= 6
         energy -= 8
         happiness -= 5
         print("Your health level decreased by 6")
         print("Your energy level decreased by 8")
         print("Your happiness level decreased by 5")
       if food.lower() == "fish pie":
         health += 4
         energy += 10
         happiness += 2
         print("Your health level increased by 1")
         print("Your energy level increased by 2")
       if food.lower() == "spoiled fish pie":
         health -= 12
         energy -= 13
         happiness -= 2
         print("Your health level decreased by 3")
         print("Your energy level decreased by 5")
         print("Your happiness level decreased by 2")
       if food.lower() == "apple":
         health += 1
         energy += 2
         print("Your health level increased by 1")
         print("Your energy level increased by 2")
       if food.lower() == "spoiled apple":
         health -= 3
         energy -= 5
         happiness -= 2
         print("Your health level decreased by 3")
         print("Your energy level decreased by 5")
         print("Your happiness level decreased by 2")
       elif food.lower() == "banana":
         health += 1
         energy += 4
         happiness += 1
         print("Your health level increased by 1")
         print("Your energy level increased by 4")
         print("Your happiness level increased by 1")
       elif food.lower() == "spoiled banana":
         health -= 3
         energy -= 7
         happiness -= 3
         print("Your health level decreased by 3")
         print("Your energy level decreased by 7")
         print("Your happiness level decreased by 3")
       elif food.lower() == "cheese":
          health += 2
          energy += 5
          happiness += 2
          print("Your health level increased by 2")
          print("Your energy level increased by 5")
          print("Your happiness level increased by 2")
       elif food.lower() == "spoiled cheese":
         health -= 6
         energy -= 8
         happiness -= 24
         print("Your health level decreased by 3")
         print("Your energy level decreased by 5")
         print("Your happiness level decreased by 2")
       elif food.lower() == "tomato":
          health += 1
          energy += 3
          print("Your health level increased by 1")
          print("Your energy level increased by 3")
       if food.lower() == "spoiled tomato":
         health -= 3
         energy -= 5
         happiness -= 2
         print("Your health level decreased by 3")
         print("Your energy level decreased by 5")
         print("Your happiness level decreased by 2")
       elif food.lower() == "potato":
          health += 1
          energy += 6
          print("Your health level increased by 1")
          print("Your energy level increased by 6")
       elif food.lower() == "spoiled potato":
         health -= 3
         energy -= 9
         happiness -= 2
         print("Your health level decreased by 3")
         print("Your energy level decreased by 9")
         print("Your happiness level decreased by 2") # <:_(
       elif food.lower() == "meat":
          health += 4
          energy += 10
          happiness += 4
          print("Your health level increased by 4")
          print("Your energy level increased by 10")
          print("Your happiness level increased by 4")
       elif food.lower() == "spoiled meat":
         health -= 6
         energy -= 13
         happiness -= 6
         print("Your health level decreased by 6")
         print("Your energy level decreased by 13")
         print("Your happiness level decreased by 6")
       elif food.lower() == "milk":
          health += 3
          energy += 8
          happiness += 2
          print("Your health level increased by 3")
          print("Your energy level increased by 8")
          print ("Your happiness level increased by 2")
       elif food.lower() == "spoiled milk":
         health -= 5
         energy -= 11
         happiness -= 4
         print("Your health level decreased by 5")
         print("Your energy level decreased by 11")
         print("Your happiness level decreased by 4")
       elif food.lower() == "egg":
          health += 2
          energy += 7
          print("Your health level increased by 2")
          print("Your energy level increased by 7")
       if food.lower() == "spoiled egg":
         health -= 5
         energy -= 9
         happiness -= 2
         print("Your health level decreased by 5")
         print("Your energy level decreased by 9")
         print("Your happiness level decreased by 2")
       elif food.lower() == "cola":
          health += 1
          energy += 9
          happiness += 4
          print("Your health level increased by 1")
          print("Your energy level increased by 9")
          print("Your happiness level increased by 4")
       if food.lower() == "spoiled cola":
         health -= 3
         energy -= 12
         happiness -= 6
         print("Your health level decreased by 4")
         print("Your energy level decreased by 12")
         print("Your happiness level decreased by 6")
       elif food.lower() == "juice":
          health += 3
          energy += 7
          happiness += 2
          print("Your health level increased by 3")
          print("Your energy level increased by 7")
          print("Your happiness level increased by 2")
       if food.lower() == "spoiled juice":
         health -= 6
         energy -= 10
         happiness -= 4
         print("Your health level decreased by 6")
         print("Your energy level decreased by 10")
         print("Your happiness level decreased by 42")
       elif food.lower() == "chocolate":
          health += 2
          energy += 8
          happiness += 2
          print("Your health level increased by 2")
          print("Your energy level increased by 8")
          print("Your happiness level increased by 2")
       if food.lower() == "spoiled chocolate":
         health -= 5
         energy -= 11
         happiness -= 4
         print("Your health level decreased by 5")
         print("Your energy level decreased by 11")
         print("Your happiness level decreased by 4")
       elif food.lower() == "bread":
          health += 4
          energy += 5
          happiness += 1
          print("Your health level increased by 4")
          print("Your energy level increased by 5")
          print("Your happiness level increased by 1")
       if food.lower() == "spoiled bread":
         health -= 7
         energy -= 8
         happiness -= 3
         print("Your health level decreased by7")
         print("Your energy level decreased by 8")
         print("Your happiness level decreased by 3")
       elif food.lower() == "beer":
          health -= 3
          energy -= 5
          print("Your health level decreased by 3")
          print("Your energy level decreased by 5")
       if food.lower() == "spoiled beer":
         health -= 6
         energy -= 8
         happiness -= 2
         print("Your health level decreased by 6")
         print("Your energy level decreased by 8")
         print("Your happiness level decreased by 2")
       elif food.lower() == "orange":
          health += 2
          energy += 4
          print("Your health level increased by 2")
          print("Your energy level increased by 4")
       if food.lower() == "spoiled orange":
         health -= 4
         energy -= 7
         happiness -= 2
         print("Your health level decreased by 43")
         print("Your energy level decreased by 7")
         print("Your happiness level decreased by 2")
       elif food.lower() == "lemon":
          health += 2
          energy += 5
          happiness -= 1
          print("Your health level increased by 2")
          print("Your energy level increased by 5")
          print("Your happiness level decreased by 1")
       if food.lower() == "spoiled lemon":
         health -= 4
         energy -= 8
         happiness -= 3
         print("Your health level decreased by 4")
         print("Your energy level decreased by 8")
         print("Your happiness level decreased by 3")
       elif food.lower() == "lemonade":
          health += 1
          energy += 10
          happiness += 3
          print("Your health level increased by 1")
          print("Your energy level increased by 10")
          print("Your happiness level increased by 3")
       if food.lower() == "spoiled lemonade":
         health -= 4
         energy -= 13
         happiness -= 5
         print("Your health level decreased by 4")
         print("Your energy level decreased by 13")
         print("Your happiness level decreased by 5")
       elif food.lower() == "coffee":
          health += 2
          energy += 15
          happiness += 3
          print("Your health level increased by 2")
          print("Your energy level increased by 15")
          print("Your happiness level increased by 3")
       if food.lower() == "spoiled coffee":
         health -= 5
         energy -= 18
         happiness -= 5
         print("Your health level decreased by 5")
         print("Your energy level decreased by 18")
         print("Your happiness level decreased by 5")
       elif food.lower() == "crisps":
          health += 1
          energy += 8
          happiness += 3
          print("Your health level increased by 1")
          print("Your energy level increased by 8")
          print("Your happiness level increased by 3")
       if food.lower() == "spoiled crisps":
         health -= 3
         energy -= 5
         happiness -= 2
         print("Your health level decreased by 3")
         print("Your energy level decreased by 5")
         print("Your happiness level decreased by 2") # B-(
       elif food.lower() == "ice-cream":
          health += 2
          energy += 6
          happiness += 2
          print("Your health level increased by 2")
          print("Your energy level increased by 6")
          print("Your happiness level increased by 2")
       if food.lower() == "spoiled ice-cream":
         health -= 5
         energy -= 9
         happiness -= 4
         print("Your health level decreased by 3")
         print("Your energy level decreased by 5")
         print("Your happiness level decreased by 2")
       elif food.lower() == "peach":
          health += 1
          energy += 4
          happiness += 1
          print("Your health level increased by 1")
          print("Your energy level increased by 4")
          print("Your happiness level increased by 1")
       elif food.lower() == "spoiled peach":
         health -= 4
         energy -= 7
         happiness -= 3
         print("Your health level decreased by 4")
         print("Your energy level decreased by 7")
         print("Your happiness level decreased by 3")
       elif food.lower() == "strawberry":
          health += 1
          energy += 3
          print("Your health level increased by 1")
          print("Your energy level increased by 3")
       if food.lower() == "spoiled strawberry":
         health -= 4
         energy -= 6
         happiness -= 2
         print("Your health level decreased by 4")
         print("Your energy level decreased by 6")
         print("Your happiness level decreased by 2")
       elif food.lower() == "rawsberry":
          health += 1
          energy += 4
          print("Your health level increased by 1")
          print("Your energy level increased by 4")
       if food.lower() == "spoiled rawsberry":
         health -= 4
         energy -= 7
         happiness -= 2
         print("Your health level decreased by 4")
         print("Your energy level decreased by 7")
         print("Your happiness level decreased by 2")
       elif food.lower() == "donut":
          health += 3
          energy += 7
          happiness += 3
          print ("Your health level increased by 3")
          print ("Your energy level increased by 7")
          print ("Your happiness level increased by 3")
       if food.lower() == "spoiled donut":
         health -= 6
         energy -= 10
         happiness -= 5
         print("Your health level decreased by 6")
         print("Your energy level decreased by 10")
         print("Your happiness level decreased by 5")
       elif food.lower() == "carrot":
          health += 2
          energy += 4
          print ("Your health level increased by 2")
          print ("Your energy level increased by 4")
       if food.lower() == "spoiled carrot":
         health -= 5
         energy -= 7
         happiness -= 2
         print("Your health level decreased by 5")
         print("Your energy level decreased by 7")
         print("Your happiness level decreased by 2")
       elif food.lower() == "pumpkin":
          health += 2
          energy += 6
          happiness += 1
          print("Your health level increased by 2")
          print ("Your energy level increased by 6")
          print("Your happiness level increased by 1")
       if food.lower() == "sppiled pumpkin":
         health -= 5
         energy -= 9
         happiness -= 3
         print("Your health level decreased by 5")
         print("Your energy level decreased by 9")
         print("Your happiness level decreased by 3")
       elif food.lower() == "ketchup":
          health += 2
          energy += 5
          happiness += 2
          print ("Your health level increased by 2")
          print ("Your energy level increased by 5")
          print ("Your happiness level increased by 2")
       if food.lower() == "sppiled ketchup":
         health -= 5
         energy -= 8
         happiness -= 4
         print("Your health level decreased by 5")
         print("Your energy level decreased by 8")
         print("Your happiness level decreased by 4")
       elif food.lower() == "hamburger":
          health += 3
          energy += 12
          happiness += 3
          print("Your health level increased by 3")
          print("Your energy level increased by 12")
          print("Your happiness level increased by 3")
       if food.lower() == "spoiled hamburger":
         health -= 6
         energy -= 15
         happiness -= 5
         print("Your health level decreased by 6")
         print("Your energy level decreased by 15")
         print("Your happiness level decreased by 5")
       elif food.lower() == "wine":
          health -= 2
          energy -= 3
          happiness += 2
          print("Your health level decreased by 2")
          print("Your energy level decreased by 3")
          print ("Your happiness level increased by 2")
       if food.lower() == "spoiled wine":
         health -= 5
         energy -= 6
         happiness -= 4
         print("Your health level decreased by 5")
         print("Your energy level decreased by 6")
         print("Your happiness level decreased by 4")
       elif food.lower() == "cocoa":
          health += 2
          energy += 6
          happiness -= 3
          print ("Your health level increased by 2")
          print ("Your energy level increased by 6")
          print("Your happiness level decreased by 3")
       if food.lower() == "spoiled cocoa":
         health -= 5
         energy -= 9
         happiness -= 4
         print("Your health level decreased by 5")
         print("Your energy level decreased by 9")
         print("Your happiness level decreased by 4")
       elif food.lower() == "onion":
          health += 2
          energy += 6
          print("Your health level increased by 2")
          print("Your energy level increased by 6")
       if food.lower() == "spoiled onion":
         health -= 5
         energy -= 9
         happiness -= 2
         print("Your health level decreased by 5")
         print("Your energy level decreased by 9")
         print("Your happiness level decreased by 2")
       elif food.lower() == "grapes":
          health += 2
          energy += 4
          happiness += 1
          print("Your health level increased by 2")
          print("Your energy level increased by 4")
          print ("Your happiness level increased by 1")
       if food.lower() == "spoiled grapes":
         health -= 5
         energy -= 7
         happiness -= 3
         print("Your health level decreased by 5")
         print("Your energy level decreased by 7")
         print("Your happiness level decreased by 3")
       elif food.lower() == "olives":
          health += 2
          energy += 6
          happiness += 2
          print ("Your health level increased by 2")
          print ("Your energy level increaased by 6")
          print ("Your happiness level increased by 2")
       if food.lower() == "spoiled olives":
         health -= 5
         energy -= 9
         happiness -= 4
         print("Your health level decreased by 5")
         print("Your energy level decreased by 9")
         print("Your happiness level decreased by 4")
       elif food.lower() == "cabbage":
          health += 2
          energy += 2
          print("Your health level increased by 2")
          print("Your energy level increased by 2")
       if food.lower() == "spoiled cabbage":
         health -= 5
         energy -= 5
         happiness -= 2
         print("Your health level decreased by 5")
         print("Your energy level decreased by 5")
         print("Your happiness level decreased by 2")
       elif food.lower() == "lettuce":
          health += 2
          energy += 3
          print ("Your health level increased by 2")
          print("Your energy level increased by 3")
       if food.lower() == "spoiled lettuce":
         health -= 5
         energy -= 6
         happiness -= 2
         print("Your health level decreased by 5")
         print("Your energy level decreased by 6")
         print("Your happiness level decreased by 2")
       elif food.lower() == "cucumber":
          health += 2
          energy += 4
          print ("Your health level increased by 2")
          print("Your energy level increased by 4")
       if food.lower() == "spoiled cucumber":
         health -= 5
         energy -= 7
         happiness -= 2
         print("Your health level decreased by 5")
         print("Your energy level decreased by 7")
         print("Your happiness level decreased by 2")
       elif food.lower() == "eggplant":
          health += 2
          energy += 4
          print("Your health level increased by 2")
          print("Your energy level increased by 4")
       if food.lower() == "spoiled eggplant":
         health -= 5
         energy -= 7
         happiness -= 2
         print("Your health level decreased by 5")
         print("Your energy level decreased by 7")
         print("Your happiness level decreased by 2")
       elif food.lower() == "broccoli":
          health += 2
          energy += 4
          print("Your health level increased by 2")
          print ("Your energy level increased by 4")
       if food.lower() == "spoiled broccoli":
         health -= 5
         energy -= 7
         happiness -= 2
         print("Your health level decreased by 5")
         print("Your energy level decreased by 7")
         print("Your happiness level decreased by 2")
       elif food.lower() == "zucchini":
          health += 2
          energy += 5
          print("Your health level increased by 2")
          print ("Your energy level increased by 5")
       if food.lower() == "spoiled zucchini":
         health -= 5
         energy -= 8
         happiness -= 2
         print("Your health level decreased by 5")
         print("Your energy level decreased by 8")
         print("Your happiness level decreased by 2")
       elif food.lower() == "beets":
          health += 2
          energy += 6
          happiness += 1
          print("Your health level increased by 2")
          print("Your energy level increased by 6")
          print("Your happiness level incresed by 1")
       if food.lower() == "spoiled beets":
         health -= 5
         energy -= 9
         happiness -= 3
         print("Your health level decreased by 5")
         print("Your energy level decreased by 9")
         print("Your happiness level decreased by 3")
       elif food.lower() == "sunflower oil":
          health -= 1
          energy -= 2
          print ("Your health level decreased by 1")
          print("Your energy level decreased by 2")
       if food.lower() == "spoiled sunflower oil":
         health -= 4
         energy -= 5
         happiness -= 2
         print("Your health level decreased by 4")
         print("Your energy level decreased by 5")
         print("Your happiness level decreased by 2")
       elif food.lower() == "corn":
          health += 2
          energy += 6
          happiness += 2
          print("Your health level increased by 2")
          print("Your energy level increased by 6")
          print ("Your happiness level increased by 2")
       if food.lower() == "spoiled corn":
         health -= 5
         energy -= 9
         happiness -= 4
         print("Your health level decreased by 5")
         print("Your energy level decreased by 9")
         print("Your happiness level decreased by 4")
       elif food.lower() == "olive oil":
          health -= 1
          energy -= 3
          print("Your health level decreased by 1")
          print ("Your energy level decreased by 3")
       if food.lower() == "spoiled olive oil":
         health -= 4
         energy -= 6
         happiness -= 2
         print("Your health level decreased by 4")
         print("Your energy level decreased by 6")
         print("Your happiness level decreased by 2")
       elif food.lower() == "garlic":
          health += 2
          energy += 8
          print("Your health level increased by 1")
          print ("Your energy level increased by 2")
       if food.lower() == "spoiled garlic":
         health -= 5
         energy -= 11
         happiness -= 2
         print("Your health level decreased by 5")
         print("Your energy level decreased by 11")
         print("Your happiness level decreased by 2")
       elif food.lower() == "vinegar":
          health -= 4
          energy -= 10
          happiness -= 6
          print ("Your health level decreased by 4")
          print ("Your energy level decreased by 10")
          print("Your happiness level decreased by 6")
       if food.lower() == "spoiled vinegar":
         health -= 7
         energy -= 13
         happiness -= 8
         print("Your health level decreased by 7")
         print("Your energy level decreased by 13")
         print("Your happiness level decreased by 8")
       elif food.lower() == "black pepper":
          health -= 2
          energy += 5
          happiness += 1
          print("Your health level decreased by 2")
          print ("Your energy level increased by 5")
          print("Your happiness level increased by 1")
       if food.lower() == "spoiled black pepper":
         health -= 5
         energy -= 8
         happiness -= 3
         print("Your health level decreased by 5")
         print("Your energy level decreased by 8")
         print("Your happiness level decreased by 3")
       elif food.lower() == "pepper":
          health += 2
          energy += 4
          print ("Your health level increased by 2")
          print ("Your energy level increased by 4")
       if food.lower() == "spoiled pepper":
         health -= 5
         energy -= 7
         happiness -= 2
         print("Your health level decreased by 5")
         print("Your energy level decreased by 7")
         print("Your happiness level decreased by 2")
       elif food.lower() == "cookies":
          health += 1
          energy += 6
          happiness += 2
          print("Your health level increased by 1")
          print ("Your energy level increased by 6")
          print("Your happiness level increased by 2")
       if food.lower() == "spoiled cookies":
         health -= 4
         energy -= 9
         happiness -= 4
         print("Your health level decreased by 4")
         print("Your energy level decreased by 9")
         print("Your happiness level decreased by 4")      
       elif food.lower() == "pasta":
          health += 2
          energy += 7
          happiness += 1
          print ("Your health level increased by 2")
          print("Your energy level increased by 7")
          print ("Your happiness level increased by 1")
       if food.lower() == "spoiled pasta":
         health -= 5
         energy -= 10
         happiness -= 3
         print("Your health level decreased by 5")
         print("Your energy level decreased by 10")
         print("Your happiness level decreased by 3")
       elif food.lower() == "salami":
          health += 2
          energy += 6
          happiness += 2
          print ("Your health level increased by 2")
          print("Your energy level increased by 6")
          print ("your happiness level increased by 2")
       if food.lower() == "spoiled salami":
         health -= 5
         energy -= 9
         happiness -= 4
         print("Your health level decreased by 5")
         print("Your energy level decreased by 9")
         print("Your happiness level decreased by 4")
       elif food.lower() == "sausage":
          health += 2
          energy += 8
          happiness += 1
          print("Your health level increased by 2")
          print ("Your energy level increased by 8")
          print ("Your happiness level increased by 1")
       if food.lower() == "spoiled sausage":
         health -= 5
         energy -= 11
         happiness -= 3
         print("Your health level decreased by 5")
         print("Your energy level decreased by11")
         print("Your happiness level decreased by 3")
       elif food.lower() == "popcorn":
          health += 1
          energy += 7
          happiness += 3
          print("Your health level increased by 1")
          print ("Your energy level increased by 7")
          print("Your happiness level increased by 3")
       if food.lower() == "spoiled popcorn":
         health -= 4
         energy -= 10
         happiness -= 5
         print("Your health level decreased by 4")
         print("Your energy level decreased by 10")
         print("Your happiness level decreased by 5")
       elif food.lower() == "mustard":
          health += 3
          energy += 10
          print("Your health level increased by 3")
          print ("Your energy level increased by 10")
       if food.lower() == "spoiled mustard":
         health -= 6
         energy -= 13
         happiness -= 2
         print("Your health level decreased by 6")
         print("Your energy level decreased by 13")
         print("Your happiness level decreased by 2")
       elif food.lower() == "pea":
          health += 1
          energy += 4
          print("Your health level increased by 1")
          print("Your energy level increased by 4")
       if food.lower() == "spoiled pea":
         health -= 4
         energy -= 7
         happiness -= 2
         print("Your health level decreased by 4")
         print("Your energy level decreased by 7")
         print("Your happiness level decreased by 2")
       elif food.lower() == "salad":
          health += 3
          energy += 9
          happiness += 2
          print("Your health level increased by 3")
          print("Your energy level increased by 9")
          print("your happiness level increased by 2")
       if food.lower() == "spoiled salad":
         health -= 6
         energy -= 12
         happiness -= 4
         print("Your health level decreased by 6")
         print("Your energy level decreased by 12")
         print("Your happiness level decreased by 4")
       elif food.lower() == "pumpkin pie":
          health += 3
          energy += 6
          happiness += 1
          print("Your health level increased by 3")
          print ("Your energy level increased by 6")
          print ("your happiness level increased by 1")
       if food.lower() == "spoiled pumpkin pie":
         health -= 6
         energy -= 9
         happiness -= 3
         print("Your health level decreased by 6")
         print("Your energy level decreased by 9")
         print("Your happiness level decreased by 3")
       elif food.lower() == "bbq":
          health += 2
          energy += 12
          happiness += 3
          print ("Your health level increased by 2")
          print ("Your energy level increased by 12")
          print ("your happiness level increased by 3")
       if food.lower() == "spoiled bbq":
         health -= 5
         energy -= 15
         happiness -= 5
         print("Your health level decreased by 5")
         print("Your energy level decreased by 15")
         print("Your happiness level decreased by 5")
       elif food.lower() == "pizza":
          health += 4
          energy += 14
          happiness += 4
          print("Your health level increased by 4")
          print("Your energy level increased by 14")
          print("your happiness level increased by 4")
       if food.lower() == "spoiled pizza":
         health -= 7
         energy -= 17
         happiness -= 6
         print("Your health level decreased by 7")
         print("Your energy level decreased by 17")
         print("Your happiness level decreased by 6")
       elif food.lower() == "mayonnaise":
          health += 1
          energy += 5
          happiness += 1
          print("Your health level increased by 1")
          print("Your energy level increased by 5")
          print("your happiness level increased by 1")
       if food.lower() == "spoiled salad":
         health -= 4
         energy -= 8
         happiness -= 3
         print("Your health level decreased by 4")
         print("Your energy level decreased by 8")
         print("Your happiness level decreased by 3")
       elif food.lower() == "hot dog":
          health += 2
          energy += 9
          happiness += 3
          print("Your health level increased by 2")
          print("Your energy level increased by 9")
          print("your happiness level increased by 3")
       if food.lower() == "spoiled hot dog":
         health -= 5
         energy -= 12
         happiness -= 5
         print("Your health level decreased by 5")
         print("Your energy level decreased by 12")
         print("Your happiness level decreased by 5")
       elif food.lower() == "nachos":
          health += 1
          energy += 7
          happiness += 2
          print("Your health level increased by 1")
          print("Your energy level increased by 7")
          print("your happiness level increased by 2")
       if food.lower() == "spoiled nachos":
         health -= 4
         energy -= 10
         happiness -= 4
         print("Your health level decreased by 4")
         print("Your energy level decreased by 10")
         print("Your happiness level decreased by 4")
       elif food.lower() == "lasagna":
          health += 3
          energy += 8
          happiness += 2
          print ("Your health level increased by 3")
          print ("Your energy level increased by 8")
          print("your happiness level increased by 2") 
       if food.lower() == "spoiled lasagna":
         health -= 6
         energy -= 11
         happiness -= 4
         print("Your health level decreased by 6")
         print("Your energy level decreased by 11")
         print("Your happiness level decreased by 4")
       elif food.lower() == "olivier salad":
          health += 3
          energy += 7
          happiness += 3
          print("Your health level increased by 3")
          print ("Your energy level increased by 7")
          print ("your happiness level increased by 3")
       if food.lower() == "spoiled olivier salad":
         health -= 6
         energy -= 10
         happiness -= 5
         print("Your health level decreased by 6")
         print("Your energy level decreased by 10")
         print("Your happiness level decreased by 5")
       elif food.lower() == "potato soup":
          health += 3
          energy += 6
          happiness += 3
          print ("Your health level increased by 3")
          print ("Your energy level increased by 6")
          print("your happiness level increased by 1")
       if food.lower() == "spoiled potato soup":
         health -= 6
         energy -= 9
         happiness -= 5
         print("Your health level decreased by 6")
         print("Your energy level decreased by 9")
         print("Your happiness level decreased by 5") # <X_(
       elif food.lower() == "borsch":
          health += 3
          energy += 10
          happiness += 3
          print("Your health level increased by 3")
          print ("Your energy level increased by 10")
          print("your happiness level increased by 3")
       if food.lower() == "spoiled borsch":
         health -= 6
         energy -= 13
         happiness -= 5
         print("Your health level decreased by 6")
         print("Your energy level decreased by 13")
         print("Your happiness level decreased by 5")
       elif food.lower() == "harcho":
          health += 3
          energy += 12
          happiness += 4
          print("Your health level increased by 3")
          print("Your energy level increased by 12")
          print("your happiness level increased by 4")
       if food.lower() == "spoiled borsch":
         health -= 6
         energy -= 15
         happiness -= 6
         print("Your health level decreased by 6")
         print("Your energy level decreased by 15")
         print("Your happiness level decreased by 6")
       elif food.lower() == "chocolate cake":
          health += 2
          energy += 7
          happiness += 3
          print("Your health level increased by 2")
          print("Your energy level increased by 7")
          print("your happiness level increased by 3")
       if food.lower() == "spoiled chocolate cake":
         health -= 5
         energy -= 10
         happiness -= 5
         print("Your health level decreased by 5")
         print("Your energy level decreased by 10")
         print("Your happiness level decreased by 5")
     else:
            print(f"You don't have {food.lower()} in inventory.")
    elif action.lower() == "wear":
      time_before_lounge =time.time()
      clothes = [ "jacket", "hat", "boots", "pans", "trousers", "t-shirt", "shirt", "cap", "waistcoat", "sweater", "blouse", "trainers", "shoes", "shorts", "coat", "scarf", "blazer", "jumper", "glasses", "singlet", "tie", "ring", "necklace", "bracelet", "silk hat", "swimsuit", "socks", "overall", "helmet", "dress", "jeans", "pyjamas", "hoodie", "slippers"]
      wear = input(f"What do you want to wear?. Here is the list of clothes: {clothes} :")

      if wear in clothes:
        if wear in inventory and inventory[wear] > 0:
          del inventory[wear]
          wearing = f"(wearing) {wear}"
          inventory[wearing] = inventory.get(wearing, 0) + 1
          print(f"You put on a(n)/the {wear}. Now you can look in the mirror.")
          if time_before_lounge - dirty_time > 10:
            del inventory [wearing]
            dirty = f"(dirty) {wear}"
            inventory[dirty] = inventory.get(dirty, 0) + 1
            
            dirty_time = time_before_lounge
          else:
            time_left = int((time_before_lounge + 10) - dirty_time)
        else:
            print("You don't have that item in your inventory.")
      else:
        print("Sorry, but you can't wear this item.")
    elif action.lower() == "unwear":
     time_before_lounge =time.time()
     unwear = input("What clothes do you want to take off?: ")
     clothes = [ "jacket", "hat", "boots", "pans", "trousers", "t-shirt", "shirt", "cap", "waistcoat", "sweater", "blouse", "trainers", "shoes", "shorts", "coat", "scarf", "blazer", "jumper", "glasses", "singlet", "tie", "ring", "necklace", "bracelet", "silk hat", "swimsuit", "socks", "overall", "helmet", "dress", "jeans", "pyjamas", "hoodie", "slippers"]
     if unwear in clothes:
        if wearing in inventory and inventory[wearing] > 0:
            del inventory[wearing]
            inventory[unwear] += 1
            print(f"You took off a(n)/the {unwear}. Now you can look in the mirror.")
            if time_before_lounge - dirty_time > 1800:
             del inventory[unwear]
             dirty = f"(dirty) {unwear}"
             inventory[dirty] = inventory.get(dirty, 0) + 1
             dirty_time = time_before_lounge
            else:
              time_left = int((time_before_lounge + 1800) - dirty_time)
        else:
            print("You don't have any more of that item to take off.")
     else:
        print("You don't have that item in your inventory.")
    elif action.lower() == "lounge":
     if "washing machine" in inventory:
        lounge = input("What clothes do you want to lounge?: ")
        if lounge in inventory:
            print("Clothes has been lounged - 25%")
            print("Clothes has been lounged - 50%")
            print("Clothes has been lounged - 75%")
            print("Clothes has been lounged - 100%")
            del inventory[dirty]  # Remove the lounged clothes from inventory
            inventory[wear] = inventory.get(wear, 0) + 1  # Increment the count of lounged clothes
        else:
            print("You don't have that item in your inventory.")
     else:
        print("Please buy a washing machine to lounge your clothes.")


      
    elif action.lower() == "craft":
        recipe = {
            "steel": {"iron": 1},
            "ceramic": {"clay": 2},
            "glass": {"sand":  3},
            "brick": {"clay":1},
            "paper": {"wood":3},
            "bronze": {"cooper": 1, "tin" : 1},
            "plastic": {"oil bar" :2},
            "axe": {"wood" :2, "steel": 3},
            "pickaxe":{"wood" :2, "steel": 3},
            "ink":{"octopus's ink" :1} or {"oil bar": 1},
            "octopus's ink": {"octopus": 1},
            "book":{"paper":3, "ink":2},
            "leather": {"cow": 1},
            "better leather":{"buffalo":1},
            "jacket":{"leather": 3, "steel": 1},
            "wool":{"sheep":1},
            "table": {"wood":3, "steel":1},
            "chair": {"wood":2},
            "furnace": {"coal":1, "cobblestone":4, "stone":4, "steel":2},
            "crown": {"gold": 3, "ruby": 2, "emerald": 2},
            "rope": {"wood": 2},
            "hook": {"steel": 1},
            "trophy":{"gold": 3},
            "fence": {"wood": 3},
            "compass":{"magnet": 1, "steel":2, "nickel": 1, "tungsten":1},
            "light bulb":{"glass": 1, "steel":1, "tungsten":1},
            "black powder": {"saltpeter": 1, "sulfur": 1, "coal": 1},
            "bullet": {"black powder": 1, "lead": 1},
            "hunting rifle":{"wood": 2, "steel": 3, "nickel": 1, "bullet": 5, "black powder": 3},
            "wardrobe" :{"wood": 4, "steel":1},
            "matches":{"wood": 2, "sulfur": 1},
            "bag": {"leather": 3},
            "generator of Ruby": {"rubygite": 3, "steel": 10, "titan": 3, "diamond": 2, "silver": 2, "uranium": 3},
            "creator":{"rubygite": 2, "steel": 15, "titan": 5, "silver": 3, "quartz": 2, "computer": 1},
            "computer": {"monitor":1, "system unit":1, "keyboard":1, "mouse":1},
            "motherboard": {"fibreglass": 4, "copper": 3},
            "fibreglass": {"glass": 2}, 
            "hard disk": {"steel": 1, "magnet":2 , "plastic":1},
            "video card": {"rubber": 3, "steel": 1, "copper": 1, "aluminium":1},
            "power supply":{"copper": 3, "aluminium":1, "steel": 3}, 
            "RAM":{"sand": 3, "aluminium":2, "steel": 1},
            "processor":{"copper": 2, "plastic": 3, "sand": 1, "gold":1, "silver":1, "aluminium":2},
            "system unit": {"processor":1, "motherboard":1, "video card": 1, "RAM":2, "power supply": 1, "rubber":3, "hard disk": 2, "steel": 5, "sand":2},
            "liquid crystals": {"pig": 2},
            "monitor":{"steel": 2, "liquid crystals": 2},
            "keyboard":{"steel":2, "iron": 1, "aluminium": 2},
            "mouse":{"plastic": 2, "rubber": 1, "steel":1},
            "mirror": {"bronze":2, "glass": 3},
            "carpet": {"wool": 3},
            "fuel": {"oil bar": 2},
            "plate": {"ceramic":1},
            "spoon": {"steel" :1},
            "fork": {"steel": 1},
            "cup": {"ceramic":1},
            "saucepan":{"steel":2, "plastic": 1},
            "showel": {"steel": 1, "wood": 2},
            "rake": {"steel":2, "plastic":1, "wood": 3},
            "water can": {"plastic": 2},
            "greenhouse": {"glass": 8},
            "flower pot": {"clay":2},
            "treadmill": {"wood":2, "steel": 2, "copper": 1, "aluminium": 2, "rubber":1}, 
            "punching bag":{"better leather": 2, "steel":1},
            "exercise bike": {"steel": 3, "aluminium":2, "titan":1, "rubber": 1},
            "horizontal bar": {"steel":2, "plastic":1, "nickel": 1},
            "expander": {"titan":1, "steel":1, "leather":1},
            "dumbbell":{"iron":2},
            "weight": {"iron":2},
            "sweden ladder": {"wood": 4,"steel":1},
            "barbell":{"nickel":1, "steel":2},
            "ball": {"rubber": 2},
            "toilet": {"ceramic":3},
            "sink": {"ceramic": 2},
            "bath": {"ceramic": 4}
          # Add more recipes here
        }

        print("Available recipes:")
        for item, components in recipe.items():
            print(f"{item}: {components}")

        item_to_craft = input("Which item do you want to craft? ")
        if item_to_craft.lower() in recipe:
            components = recipe[item_to_craft.lower()]
            can_craft = True
            for component, quantity in components.items():
                if component.lower() not in inventory or inventory[component.lower()] < quantity:
                    can_craft = False
                    break
            if can_craft:
                for component, quantity in components.items():
                    inventory[component.lower()] -= quantity
                if item_to_craft.lower() in inventory:
                    inventory[item_to_craft.lower()] += 1
                else:
                    inventory[item_to_craft.lower()] = 1
                print(f"You have crafted {item_to_craft}.")
            else:
                print("You don't have enough components to craft that item.")
        else:
            print("That item cannot be crafted.")

    elif action == "recycle":
      item_list = {
            "steel": {"iron": 1},
            "ceramic": {"clay": 2},
            "glass": {"sand":  3},
            "brick": {"clay":1},
            "paper": {"wood":3},
            "bronze": {"cooper": 1, "tin" : 1},
            "plastic": {"oil bar" :2},
            "axe": {"wood" :2, "steel": 3},
            "pickaxe":{"wood" :2, "steel": 3},
            "ink":{"octopus's ink" :1} or {"oil bar": 1},
            "octopus's ink": {"octopus": 1},
            "book":{"paper":3, "ink":2},
            "leather": {"cow": 1},
            "better leather":{"buffalo":1},
            "jacket":{"leather": 3, "steel": 1},
            "wool":{"sheep":1},
            "table": {"wood":3, "steel":1},
            "chair": {"wood":2},
            "furnace": {"coal":1, "cobblestone":4, "stone":4, "steel":2},
            "crown": {"gold": 3, "ruby": 2, "emerald": 2},
            "rope": {"wood": 2},
            "hook": {"steel": 1},
            "trophy":{"gold": 3},
            "fence": {"wood": 3},
            "compass":{"magnet": 1, "steel":2, "nickel": 1, "tungsten":1},
            "light bulb":{"glass": 1, "steel":1, "tungsten":1},
            "black powder": {"saltpeter": 1, "sulfur": 1, "coal": 1},
            "bullet": {"black powder": 1, "lead": 1},
            "hunting rifle":{"wood": 2, "steel": 3, "nickel": 1, "bullet": 5, "black powder": 3},
            "matches":{"wood": 2, "sulfur": 1},
            "bag": {"leather": 3},
            "generator of Ruby": {"rubygite": 3, "steel": 10, "titan": 3, "diamond": 2, "silver": 2, "uranium": 3},
            "creator":{"rubygite": 2, "steel": 15, "titan": 5, "silver": 3, "quartz": 2, "computer": 1},
            "wardrobe" :{"wood": 4, "steel":1},
            "computer": {"monitor":1, "system unit":1, "keyboard":1, "mouse":1},
            "motherboard": {"fibreglass": 4, "copper": 3},
            "fibreglass": {"glass": 2}, 
            "hard disk": {"steel": 1, "magnet":2 , "plastic":1},
            "video card": {"rubber": 3, "steel": 1, "copper": 1, "aluminium":1},
            "power supply":{"copper": 3, "aluminium":1, "steel": 3}, 
            "RAM":{"sand": 3, "aluminium":2, "steel": 1},
            "processor":{"copper": 2, "plastic": 3, "sand": 1, "gold":1, "silver":1, "aluminium":2},
            "system unit": {"processor":1, "motherboard":1, "video card": 1, "RAM":2, "power supply": 1, "rubber":3, "hard disk": 2, "steel": 5, "sand":2},
            "liquid crystals": {"pig": 2},
            "monitor":{"steel": 2, "liquid crystals": 2},
            "keyboard":{"steel":2, "iron": 1, "aluminium": 2},
            "mouse":{"plastic": 2, "rubber": 1, "steel":1},
            "mirror": {"bronze":2, "glass": 3},
            "carpet": {"wool": 3},
            "fuel": {"oil bar": 2},
            "plate": {"ceramic":1},
            "spoon": {"steel" :1},
            "fork": {"steel": 1},
            "cup": {"ceramic":1},
            "saucepan":{"steel":2, "plastic": 1},
            "showel": {"steel": 1, "wood": 2},
            "rake": {"steel":2, "plastic":1, "wood": 3},
            "water can": {"plastic": 2},
            "greenhouse": {"glass": 8},
            "flower pot": {"clay":2},
            "treadmill": {"wood":2, "steel": 2, "copper": 1, "aluminium": 2, "rubber":1}, 
            "punching bag":{"better leather": 2, "steel":1},
            "exercise bike": {"steel": 3, "aluminium":2, "titan":1, "rubber": 1},
            "horizontal bar": {"steel":2, "plastic":1, "nickel": 1},
            "expander": {"titan":1, "steel":1, "leather":1},
            "dumbbell":{"iron":2},
            "weight": {"iron":2},
            "sweden ladder": {"wood": 4,"steel":1},
            "barbell":{"nickel":1, "steel":2},
            "ball": {"rubber": 2},
            "toilet": {"ceramic":3},
            "sink": {"ceramic": 2},
            "bath": {"ceramic": 4}
      }
      print("Available items:")
      for item, components in item_list.items():
        print(f"{item}: {', '.join(components.keys())}")

      item_to_parts = input("What item do you want to dismantle for parts? ").lower()

      if item_to_parts in item_list and item_to_parts in inventory:
        components = item_list[item_to_parts]
        can_recycle = True

        for component, quantity in components.items():
         if component.lower() not in inventory or inventory[component.lower()] < quantity:
            can_recycle = False
            break
        
        if can_recycle:
         for component, quantity in components.items():
            inventory[component.lower()] -= quantity
        
            print(f"You have recycled {item_to_parts}.")
        else:
         print("You don't have the required components to recycle this item.")
      else:
       print("That item cannot be dismantled.")


    elif action == "go":
      goTo = input("Where do you want to go (Tkinter theatre, PyGame's circus, Pycinema) Just write(cinema, theatre, circus): ")
      if goTo.lower() == "theatre":
        if "theatre ticket" in inventory:
          print("Wait before third ring rings")
          print("First ring rang")
          print("Second ring rang")
          print("Third ring rang")
          print("The perfomance has begun")
          print("25%")
          print("50%")
          print("75%")
          print("The show is over. You applauded the actors. And then they left in a good mood.")
        elif "theatre ticket" not in inventory:
          print("Please, buy theatre ticket and come back if you'll have it.")
      if goTo.lower() == "cinema":
        if "cinema ticket" in inventory:
          taste = rn.choice(list(items_prices.keys()))
          print(f"You got a popcorn with {taste} taste")
          print("Film has begun")
          print("25%")
          print("50%")
          print("75%")
          print("Film was interesting")
        elif "cinema ticket" not in inventory:
          print("Please, buy cinema ticket and come back if you'll have it ")
      if goTo.lower() == "circus":
        if "circus ticket" in inventory:
          print("Perfomance has begun")
          print("25%")
          print("50%")
          print("75%")
          print("Perfomance was really funny. Clowns also. You really liked the acrobatics and animal perfomances. You apploed to people, who work in circus.")
        elif "circus ticket" not in inventory:
          print("Please, buy circus ticket and come back if you'll have it ")
    elif action.lower() == "travel":
      transport = input("What kind of transport do you want to use? (car, bus, train, plane, ship): ")

      if transport.lower() == "car":
        if "car" in inventory:
            places = input("Where do you want to travel? (digital park, 'Blender' beach, museum of computer history, gas station, doctor Kaspersky's clinic, Firefox hotel): ")
            if places.lower() == "digital park":
                creation = rn.choice(list(items_prices.keys()))
                print(f"This park is very beautiful, and most importantly, everything here is made of numbers and words. That is literally from nothing. Every leaf, every blade of grass has been designed and modeled. The large area and beautiful scenery attract many. There is also Lake Zero, a 2D playground, a fountain, and the very place where you can create something yourself. Anything. After visiting, you will never forget this place. You arrived there, explored all places in this park, and even tried to make {creation}.")
                if creation in inventory:
                    inventory[creation] += 1
                else:
                    inventory[creation] = 1
            elif places.lower() == "blender beach":
                print("This beach is the best beach in this city. Its highlight is the excellent high-quality graphics made in Blender. To do this, all possible tools were used. It has everything you need for a normal resort. You arrived there, swam in the Tyuring's sea, ate an ice-cream, and played volleyball.")
            elif places.lower() == "museum of computer history":
                print("This museum houses ancient artifacts that tell the ancient history of computers and all kinds of gadgets. In the showcases, there are copies of old computers, telephones, processors, and so on. There are also portraits of great scientists. And also a huge canvas telling about the bots revolution in 4096.")
            elif places.lower() == "gas station":
                print("You stopped at the gas station to refuel your car. It's always a good idea to have a full tank before going on a long journey.")
            elif places.lower() == "doctor Kaspersky's clinic":
              print("Doctor Kaspersky is the best doctor in our country. In addition to ordinary diseases, he also treats computer diseases, and also fixes bugs and errors. His clinic is located in the heart of Pi City. So if you feel bad, contact him. You went there and the doctor personally cured you of all the ailments you had.")
            elif places.lower() == "hotel Millenium":
              print("Welcome to the Millennium Hotel, a luxurious four-star accommodation perfect for your next getaway. Nestled in the heart of a bustling city, this hotel offers a haven of comfort and convenience. With its elegant decor and top-notch amenities, the Millennium Hotel promises a memorable stay for both business and leisure travelers. As you step into the stylish lobby, you'll be greeted by friendly and attentive staff who are dedicated to ensuring your every need is met. The tastefully appointed rooms and suites provide a tranquil retreat, featuring modern furnishings, plush bedding, and all the amenities required for a restful night's sleep. Indulge in a delectable culinary experience at the hotel's exquisite restaurant, where talented chefs prepare a diverse array of international cuisines using the finest ingredients. Whether you crave a hearty breakfast to kick-start your day or an intimate dinner to wind down, the restaurant offers an extensive menu that caters to all tastes. For those seeking relaxation and rejuvenation, the Millennium Hotel boasts a state-of-the-art fitness center and a luxurious spa. Unwind with a soothing massage, take a dip in the sparkling pool, or work up a sweat in the well-equipped gym. Whatever your preference, the hotel ensures that your well-being and wellness are at the forefront of your stay. With its prime location, the Millennium Hotel places you in close proximity to the city's major attractions, shopping districts, and vibrant nightlife. Whether you're here for business meetings or exploring the city's cultural gems, the hotel's concierge service is readily available to assist you in planning your itinerary and making the most of your visit. Experience the epitome of comfort, elegance, and exceptional service at the Millennium Hotel. From its luxurious accommodations to its convenient amenities, this four-star establishment invites you to relax, unwind, and enjoy a truly memorable stay.")
            else:
                print("Invalid destination. Please choose a valid destination.")
        else:
            print("You need to buy a car to travel.")
    
      elif transport.lower() == "bus":
        if "bus ticket" in inventory:
            places2 = input("Where do you want to travel: greenhouse Mint, Google Dino's park, Microsoft office zoo, Unreal village, ruins of Pascal, Rossum's river. Write(greenhouse, dinopark, zoo, village, ruins, river): ")
            if places2.lower() == "greenhouse":
                honey = rn.choice(list(items_prices.keys()))
                print(f"Welcome to the Mint Greenhouse. This is an interesting greenhouse where amazing plants grow, some of which were brought from a very distant land of Linux. Here you can really feel the abundance of life. There is also a laboratory where scientists test and invent new types of plants. Because of the clearly written commands, everything here works harmoniously, without any error. Most importantly, do not tear or trample the plants. You entered here, a guide named Arch, told what and where it grows. You especially liked Mint Distribution brought from Linux. For good behavior, you were allowed to taste honey from {honey}.")
            elif places2.lower() == "dinopark":
                print("And now you are crossing the gates of an unusual park. This park was created by Google. It contains real, three-dimensional Google dinosaurs. There is also the famous genus of T-rexes, which were once famous for huge jumps over cacti, as well as pterodactyls. In total, there are more than 150 species of Google dinosaurs in this park. Feel like you are in Jurassic Park. Have a nice trip and beware of cacti and teeth.")
            elif places2.lower() == "zoo":
                print("The Microsoft Office Zoo is another amazing place. This zoo, which was built by Microsoft, was funded by Todd Howard and Bill Gates. Its area is incredibly large. When you look at the map, it is very reminiscent of the icons of Microsoft, Bethesda Softwareworks and many other famous things. This zoo has over 5,000 species of animals. All of them are either in the real world, or have been resurrected, such as the saber-toothed tiger or mammoth, or were created from well-known projects, such as Fallout. Here you can really meet the death claw, mole rat, radroach, etc. There is also a Nuka Cola production site, a mini-town where there are some people who have been taken and all kinds of games that were either sponsored by Microsoft or were made by companies that Microsoft bought. There is even a small prototype of the Institute. Curie and Dr. Lee work in veterinary medicine.")
            elif places2.lower() == "village":
                print("This village was called Unreal Village because it was created on the Unreal Engine 10. Everything that was needed for creation was met here. Graphics taken from Blender. So look around here, enjoy the beauty of this place and even try to help the residents.")
            elif places2.lower() == "ruins":
                artefact = rn.choice(list(items_prices.keys()))
                print(f"If you love history, then you will be very interested in these ruins of the ancient city of Pascal. These ruins tell how people lived in the same place for more than 2000 years. There are perfectly preserved three residential buildings, an almost collapsed stone wall, and also one place where there were four prototype codegraphers. These are devices with which we can write code outside the house. We all have a pocket one. And at that time, they were large and well-hammered in the ground. There they coded in Assembly, Fortran, C, Java, and the main thing is Pascal. They had one OS, namely PascalOS. You came there and found a strange button on one statue, pressed it, and the statue moved aside, and there was a passage that led to a door with a riddle. You guessed the riddle and found an ancient {artefact}.")
            elif places2.lower() == "river":
                caught_fish = rn.choice(list(items_prices.keys()))
                print(f"The Rossum River was named after the creator of Python. And therefore, if you look at this river from above, it resembles a python snake. There is excellent clear water, good fish, and even turtles and anacondas are found. A lot of modules were spent on its creation, including Pygame, time, num.pie, and even the new Pyworld. You came there, rested, swam in the river, and even caught {caught_fish}.")
            else:
                print("Invalid destination. Please choose a valid destination.")
        else:
            print("You should buy a bus ticket to travel on this kind of transport.")
    
      elif transport == "train":
       if "train ticket" in inventory:
         places3 = input("Cavetown Ruby, Kingdom of bots, City of C: ")
         if places3.lower() == "cavetown":
            print("This city is incredibly beautiful. Since it is located in Ruby's cave, people had to adapt to such conditions. But they did it, and now it is a real paradise underground. They have very strong code-block walls that can withstand nuclear bombs and thermonuclear explosions. They also discovered an unusual crystal that they use almost everywhere, from fire and building materials to inexhaustible energy fuel and high-quality innovative technologies. These crystals are created from atoms in the same place where they were mined because deep in the cave there is a tank with atomic liquid. People have also learned to create crystals themselves, even more powerful than natural ones. You arrived there, surprised by the beauty of the city. Guides Yukihiro and Hamatsu gave you a tour, and you even managed to help three residents. As a reward, you received a giftbox, a pickaxe, and three Rubygite crystals.")
            if "giftbox" in inventory:
                inventory["giftbox"] += 1
            else:
                inventory["giftbox"] = 1
            if "rubygite" in inventory:
                inventory["rubygite"] += 3
            else:
                inventory["rubygite"] = 3
            if "pickaxe" in inventory:
                inventory["pickaxe"] += 1
            else:
                inventory["pickaxe"] = 1
         elif places3.lower() == "kingdom of bots":
            print("Welcome to the Kingdom of Bots. This realm is ruled by advanced artificial intelligence. The kingdom showcases a blend of past and future, with some houses built in the spirit of the Middle Ages and others in a futuristic style. You can visit the Blue Willow Art Workshop, the Earth Music Club, and interact with various bots and AI. It's a unique experience in the world of bots.")
         elif places3.lower() == "city of c":
            print("Welcome to City C. Everything in this city is built using the three languages C, C++, and C#. The city's structure resembles a giant computer board. The main building houses a device that allows you to connect with machines. The city's main ally is the New Assembly, with both having access to the car. City C is home to over 13 million inhabitants, more than 20 million buildings and businesses. It's a city of the future.")
           
         else:
            print("Invalid destination. Please choose a valid destination.")
    
       else:
         print("You should buy a train ticket to travel on this kind of transport.")

  
    
      elif transport.lower() == "ship":
       places4 = input("Java island, Linux country, Gatesburg: ")
       if "ship ticket" in inventory:
         if places4.lower() == "java island":
            print("Whether you're on vacation or just want to spend some time in paradise, you've come to the right place. Java Island is the perfect destination to relax and unwind. Enjoy palm trees, beaches, crystal-clear sea, and coconuts.")
         elif places4.lower() == "linux country":
            print("Linux Country is known for its diverse flora and fauna. It played a significant role during the bot war and continues to support our country. Explore the Mint Greenhouse, Arch Temple, Debian Caves, Ubuntu Metro, and other attractions. Just make sure to familiarize yourself with the local laws.")
         elif places4.lower() == "gatesburg":
            print("Welcome to Gatesburg, the largest IT port on the planet. Built back in 3579, it remains a hub for scientific discoveries and inventions. Explore the city's skyscrapers of science, visit the prestigious university, and learn about groundbreaking innovations.")
         else:
            print("Invalid destination. Please choose a valid destination.")
      else:
         print("You should buy a ship ticket to travel on this kind of transport.")

      if transport.lower() == "plane":
        places5 = input("Places: Discordland, Amazonia, Googlia, Gamesland, Mackintosh-city, New-Assembly, Mozillia: ")
        if "plane ticket" in inventory:
          if places5.lower() == "discordland":
            print("Welcome to Discordland, the country known for its beauty and unique structure. As a resident, you can meet everyone's favorite Wumpus and other Discord monsters. Explore the various cities (servers) and channels (houses) while enjoying the presence of bots such as Dank Memer, Arcane, and Disboard.")
          elif places5.lower() == "amazonia":
            print("Amazonia is a prestigious country with beautiful jungles that occupy 84% of the territory. The country values alternative energy sources and has abundant medicinal plants. Visit the jungles, experience the diverse wildlife, and explore the largest market in the world.")
          elif places5.lower() == "googlia":
            print("Welcome to Googlia, the country known for its technological advancements and partnerships. It is home to the 3D Google Dinosaur Park and has strong alliances with New Assembly, Discordland, Amazonia, Bot Kingdom, CaveCity Ruby, Gatesburg, Linux, and Macintosh City.")
          elif places5.lower() == "gamesland":
            print("Gamesland is a haven for gamers, where you can immerse yourself in the world of video games. Experience the latest gaming technologies, attend gaming conventions, and explore gaming-themed attractions.")
          elif places5.lower() == "mackintosh-city":
            print("Mackintosh City is dedicated to the legacy of Steve Jobs and Apple. It showcases the company's innovations, houses the renowned Mac University, and offers a glimpse into the world of Macintosh.")
          elif places5.lower() == "new-assembly":
            print("Welcome to New Assembly, a city dedicated to code and software development. It offers a thriving ecosystem for programmers, with coding academies, tech startups, and innovation centers. Immerse yourself in the coding culture and collaborate with fellow developers.")
          elif places5.lower() == "mozillia":
            print("Mozillia is a country driven by open-source principles and focuses on internet privacy and security. Explore their advancements in web technologies, learn about their browser development, and witness their dedication to a free and open internet.")
          else:
            print("Invalid destination. Please choose a valid destination.")
        else:
         print("You should buy a plane ticket to travel on this kind of transport.")

    if action.lower() == "save":
      save_balance = money
      save_inventory = inventory
      save_health = health
      save_energy = energy
      save_happiness = happiness
      save_strength = strength
      save_question = input("Do you want to save your progress? (Y/n): ")
      if save_question.lower() == "y":
        
        save_data = {
          "balance":save_balance, 
          "inventory":save_inventory,
          "health":save_health, 
          "energy":save_energy,
          "happiness":save_happiness, 
          "strength":save_strength}
        with open("save_data.txt", "w") as save_file:
            for key, value in save_data.items():
                save_file.write(f"{key}={value}\n")
        print("Game progress saved.")
      elif save_question.lower() == "n":
        print("Well, that's your own choice.")
      else:
        print("Invalid input. Please enter 'Y' or 'n'.")
    if action.lower() == "load":
      try:
        with open("save_data.txt", "r") as save_file:
            save_data = {}
            for line in save_file:
                key, value = line.strip().split('=')
                if key == 'inventory':
                    inventory_data = value.strip('{}').split(', ')
                    inventory = {}
                    for item in inventory_data:
                        item_name, item_count = item.split(': ')
                        inventory[item_name.strip("'")] = int(item_count)
                    save_data[key] = inventory
                else:
                    save_data[key] = int(value)

        # Update game variables with loaded data
        money = save_data.get('balance', 0)
        inventory = save_data.get('inventory', {})
        health = save_data.get('health', 100)
        energy = save_data.get('energy', 100)
        happiness = save_data.get('happiness', 50)
        strength = save_data.get('strength', 0)
        print("Game progress loaded.")
      except FileNotFoundError:
        print("No saved game progress found.")
      except Exception as e:
        print("Error loading game progress:", str(e))

      

    else:
        print("Invalid command. Please try again.")