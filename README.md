# Bike Factory Manufacturing Software
### Student ID: W22063136
### Charles Laverick

# How it works:

## Running the application
To run the application head to main.py and press run or use the command promt to run it using python3 main.py when in the correct directory

## Orders
Creating, viewing current order and viewing completed orders

### Creating Order:
1. Head to the top menu bar and go to the orders section clicking on it
2. Next click on the new orders button from the drop down sub menu
3. The order creation page should now be open
4. Enter in the details of the new order
5. Enter the details of the customer id
6. Press create order button
7. if no error message above the button then the order has gone through

### View Orders:
1. Head to the top menu bar and go to the orders section clicking on it
2. Next click on the View Orders button from the drop down sub menu
3. A table with the current orders should then be visible

### View Completed Orders:
1. Head to the top menu bar and go to the orders section clicking on it
2. Next click on the View Completed Orders button from the drop down sub menu
3. A table with the current orders should then be visible


## Inventory System
Viewing and updating inventory

### Inventory Page
1. Head to the top menu bar and go to the Inventory section clicking on it
2. Next click on the Dashboard button from the drop down sub menu
3. The inventory dashboard page should now be visible
4. Red means low stock, black means normal and green means too much stock

### Updating Inventory
1. Head to the top menu bar and go to the Inventory section clicking on it
2. Next click on the Dashboard button from the drop down sub menu
3. The inventory dashboard page should now be visible
4. To add to a specific item's inventory press the corresponding increase button to the items right
4. To remove from a specific item's inventory press the corresponding decrease button to the items right

## Bike Stations
Viewing each station and building a bike using the software

### Accessing Stations
1. Head to the top menu bar and go to the BikeFactory section clicking on it
2. Next click on the Stations button from the drop down sub menu
3. Then using the tab widget select which station you would like to use

### Understanding the Stations
The stations are fairly simple, they display the order information to the left, the middle contains the inventory and the right side contains the required information to assemble the bike at that station. Once ready the button can be pressed and the order will move to the next station whilst brining a new order to the current station if one exist. If a new order doesn't exist the information displayed will be default values and the button will not be able to be pressed. The button will not be able to be pressed under two conditions:
1. There is no current order to be completed at the station
2. The inventory required to make the bike at that station is too low to be completed and therefore the inventory needs to be updated.

### Completing the bike
1. Once the bike has gone to the last station (seat station) and the button has been pressed to state the bike has been assembled, the order will move from the current orders section to completed orders.

