listMenu = {

'Wings' :0,
'Cookies':0,
'Spring Rolls':0,
'Salmon':0,
'Steak':0,
'Meat Tornado':0,
'A Literal Garden':0,
'Ice Cream':0,
'Cake':0,
'Pie':0,
'Coffee':0,
'Tea':0,
'Unicorn Tears':0
}

welcom = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""

print (welcom)


def resturent():


 while 1:
  iput_fromuser = input('> ')
  if iput_fromuser == 'quit':
    break
  elif iput_fromuser in listMenu:
    listMenu[iput_fromuser] += 1 
  else:
    print('\n** Please enter item from menu  ** \n ')
  for key, val in listMenu.items():
    if val == 1:
      print ( ' ** 1 order of'+key +' added **')
    elif val > 1:
      print('** ' + str(val) + ' orders of ' + key + ' added to your meal **')
    else:
      continue

resturent()