# Bicycle Factory

## Brief

Create a Python application that streamlines the production process of bicycles, incorporating various assembly stations, inventory management, and customer order management. You will need to fill in any details not explicitly stated in this specification, using your creativity and programming skills to enhance the functionality of the app.

## Requirements

#### Screens:

A menu bar with at least the standard menu items is a requirement

1. Main Dashboard
    - Overview of production stages
    - Inventory Status
    - Buttons for each assembly station to record completed tasks

2. Inventory Screen
    - Display current quantities of all components
    - Highlight components with low stock ( items <= 3>)
    - Functionality to replenish stock

3. Order Entry Screen
    - Fields for customer information and bike specifications
    - Drop down menus for selecting bike size, colour, and component options
    - Submit button to record the order and initiate production

4. Report Screen (higher marks)
    - Visual representations (graphs/charts) of inventory levels and production rates
    - History of completed orders
    - Customer information history


#### Stations:
1. Frame Welding Station:
    - Button to record completion of each frame assembly
    - Deduct a specific amount of tubular steel from the stock based on the frame size and type

2. Fork Welding Station:
    - Button to record completion of each fork assembly
    - Deduct steel accordingly from the stock

3. Assembly Stations:
    - Button for front fork assembly
    - Button to record painting
    - Button to record pedal addition
    - Button to record wheel addition
    - Button to record chain / gear installation
    - Button to record brake addition
    - Button to record light addition
    - Button to record seat installation
    - Visible indication of numbers of components (input and outputs)
    - When one station is complete it should remove one item from that station
        - e.g. when painting is complete it should remove one item of the frame and one item of the fork from the welding stations
        - The input zone of the pedal addition should then be marked
    - If one or more of the storage bins gets more than 3 items it should be marked
        - Bought in components such as steel does not need to be indicated


#### Systems:

1. Inventory Management
    a. Stock Tracking:
        - Maintain a full inventory of all components
            - Tubular steel
            - Wheels
            - Seats
            - Gears
            - Brakes
            - Lights
        - Each component will have an associated quantity
    
    b. Updating Stock
        - Provide functionality to update stock levels as components are added or replenished

    c. Low Stock Alerts
        - Signal when stock is down to 3 remianing items in stock, promting a reorder of stock

2. Order Management
    - Bike cusstomization
    - Allow users to specify the:
        - Bike model
        - Size
        - Colour
        - Wheel size
        - Component Quality
            - Premium Gears
            - Different types of brakes
                - Disc
                - Rim
            - Light options
                - LED
                - Standard
    - Customer Information Entry
        - Name
        - Address
        - Contact information
            - Phone
            - Email

3. Display Information
    - Show current inventory levels for each part type
    - Provide a summary of current production status of each bike in the assembly line
    - Enable reporting features to track production rates and inventory ussage over time


#### Not Required:

- Anything to do with saving or loading the current state
    - But menus providing this should be on the interface to do this just not the functionality
- Documentation
    - Comments should be enough

#### Extension:

- Having different types of bikes
    - e.g. Sport, Tour, Commute, Compact...


## Classes:
- Type of bike (Standard, Sport, kids...)
#### Bike:
- 


#### Customer:
- Name
- Address (Possible classs of its own)
    - Address line 1
    - Address line 2
    - City
    - Postcode
    - Country
- Phone Number
- Orders