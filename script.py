#classes
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return "{} menu available from {} to {}".format(self.name, self.start_time, self.end_time)
  
  def calculate_bill(self, purchased_items):
    total= 0
    for item in purchased_items:
      if item in self.items:
        total += self.items[item]
    round_total = "{:.2f}".format(total)
    print("Total cost: $" + str(round_total))


class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return "This Franchise's address is {}".format(self.address)
  
  def available_menu(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return print(available_menus)

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchise = franchises



#menus
brunch = Menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 1100, 1600)

early_bird = Menu("Early Bird", {  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}, 1500, 1800)

dinner = Menu("Dinner", {  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}, 1700, 2300 )

kids = Menu("Kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 1100, 2100)

arepas_menu = Menu("Arepas", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, 1000, 2000)

print(brunch)

brunch.calculate_bill(["pancakes", "home fries", "coffee"])

early_bird.calculate_bill(["salumeria plate", "vegan mushroom ravioli"])

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids] )
new_installment = Franchise("12 East Mulberry Street",  [brunch, early_bird, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])


Basta_Fazoolin = Business("Basta Faxoolin' with my Heart", [flagship_store, new_installment])
Arepas = Business("Take a' Arepa", [arepas_place])

print(flagship_store)

flagship_store.available_menu(1200)
flagship_store.available_menu(1700)

print(Arepas.name)
print(Arepas.franchise)
print(arepas_place.address)
print(arepas_place.available_menu(1400))
