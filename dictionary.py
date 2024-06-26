menu={'appam':40,
      'puttu':35,
      'dosa':50,
      'idiyappam':40
      }
#adding new element into dictionary
menu['idli']=10
#delete item
del menu['puttu']
#get print None best for error handling
test=menu.get('pattiri')
print("Test:",test)
print(menu.items())
for item in menu.items():
    print(item)
for item in menu.items():
    food,price=item #contents item assigned to food <-key,price<-value.unpack item 2 elements into food,price
    print("item:",food,"Price:",price)    
    