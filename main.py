import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QTableWidgetItem
from PySide6.QtCore import QFile, QIODevice

from classes import Bike, BMXBike, KidsBike, RoadBike, TrackBike, MountainBike, Address, Customer, Order

#StudentID: W22063136
if __name__ == "__main__":

    APP = QApplication(sys.argv)
    UI_FILE_NAME = "BicycleFactory/BikeFactoryDesign/form.ui"
    UI_FILE = QFile(UI_FILE_NAME)

    if not UI_FILE.open(QIODevice.ReadOnly):
        print(f"Cannot open {UI_FILE_NAME}: {UI_FILE.errorString()}")
        sys.exit(-1)
    
    loader = QUiLoader()
    window = loader.load(UI_FILE)

    customers = dict()
    orders = dict() # OrderID: Order
    fork_Station_Order = []
    frame_Station_Order = []
    chassis_Station_Order = []
    paint_Station_Order = []
    pedal_Station_Order = []
    drive_chain_Station_Order = []
    wheel_Station_Order = []
    brakes_Station_Order = []
    lights_Station_Order = []
    seat_Station_Order = []
    completed_Orders = []
    inventory = dict()

    def InventoryChange(keyword: str, amount: float):
        item = inventory[keyword]
        if type(item) == str:
            if item.value() + amount < 0:
                item.display(0)
            else:
                item.display(item.value()+amount)
            if item.value() <= 3:
                # Low stock update qlcd to display red
                item.setStyleSheet("""QLCDNumber {
                                   background-color: red; 
                                   }""")

        elif type(item) == list:
            for display in item:
                if display.value() + amount < 0:
                    display.display(0)
                else:
                    display.display(display.value()+amount)

                if display.value() < 3:
                    # Low stock update qlcd to display red
                    display.setStyleSheet("""QLCDNumber {
                                    background-color: red;
                                    }""")
                    
                elif display.value() > 3:
                    display.setStyleSheet("""QLCDNumber {
                                   background-color: Green; 
                                   }""")
                else:
                    display.setStyleSheet("""QLCDNumber {
                                   background-color: None; 
                                   }""")
        else:
            TypeError("This should not be possible. The type from the inventory dict is wrong")

        if keyword in ["Steel", "Aluminium", "Carbon Fibre"]:
            # Check if fork and frames have orders
            if len(fork_Station_Order) > 0:
                # Check if they now have required amount
                if fork_Station_Order[0].bike_order.fork == "Tubular Steel" and window.ForkStationTubularSteelRequiredCount.value() <= inventory["Steel"][0].value():
                    # Enable station button
                    window.ForkWeldedButton.setEnabled(True)
                elif fork_Station_Order[0].bike_order.fork == "Tubular Aluminium" and window.ForkStationTubularAluminiumRequiredCount.value() <= inventory["Aluminium"][0].value():
                    # Enable station button
                    window.ForkWeldedButton.setEnabled(True)

                elif fork_Station_Order[0].bike_order.fork == "Carbon Fibre" and window.ForkStationCarbonRequiredCount.value() <= inventory["Carbon Fibre"][0].value():
                    # Enable station button
                    window.ForkWeldedButton.setEnabled(True)
                else:
                    # Disable station button
                    window.ForkWeldedButton.setEnabled(False)

            elif len(frame_Station_Order) > 0:
                # Check if they now have required amount
                if frame_Station_Order[0].bike_order.fork == "Tubular Steel" and window.FrameStationTubularSteelRequiredCount.value() <= inventory["Steel"][0].value():
                    # Enable station button
                    window.FrameWeldedButton.setEnabled(True)
                elif frame_Station_Order[0].bike_order.fork == "Tubular Aluminium" and window.FrameStationTubularAluminiumRequiredCount.value() <= inventory["Aluminium"][0].value():
                    # Enable station button
                    window.FrameWeldedButton.setEnabled(True)

                elif frame_Station_Order[0].bike_order.fork == "Carbon Fibre" and window.FrameStationCarbonRequiredCount.value() <= inventory["Carbon Fibre"][0].value():
                    # Enable station button
                    window.FrameWeldedButton.setEnabled(True)
                else:
                    # Disable station button
                    window.FrameWeldedButton.setEnabled(False)
            else:
                pass
        elif "Fork" in keyword or "Frame" in keyword:
            # Check if Chassis Station has orders
            if len(chassis_Station_Order) > 0:
                # Check if they now have required amount
                if chassis_Station_Order[0].bike_order.fork == "Tubular Steel" and chassis_Station_Order[0].bike_order.frame == "Tubular Steel":
                    if type(chassis_Station_Order[0].bike_order) == Bike:
                        if window.ChassisStationInventoryStandardForksCount.value() > 0 and window.ChassisStationInventoryStandardFrameCount.value() > 0:
                            window.ChassisAssemblyButton.setEnabled(True)
                        else:
                            window.ChassisAssemblyButton.setEnabled(False)
                    elif type(chassis_Station_Order[0].bike_order) == MountainBike:
                        if window.ChassisStationInventoryMountainForksCount.value() > 0 and window.ChassisStationInventoryMountainFrameCount.value() > 0:
                            window.ChassisAssemblyButton.setEnabled(True)
                        else:
                            window.ChassisAssemblyButton.setEnabled(False)
                    elif type(chassis_Station_Order[0].bike_order) == BMXBike:
                        if window.ChassisStationInventoryBMXForksCount.value() > 0 and window.ChassisStationInventoryBMXFrameCount.value() > 0:
                            window.ChassisAssemblyButton.setEnabled(True)
                        else:
                            window.ChassisAssemblyButton.setEnabled(False)
                    elif type(chassis_Station_Order[0].bike_order) == KidsBike:
                        if window.ChassisStationInventoryKidsForksCount.value() > 0 and window.ChassisStationInventoryKidsFrameCount.value() > 0:
                            window.ChassisAssemblyButton.setEnabled(True)
                        else:
                            window.ChassisAssemblyButton.setEnabled(False)
                    else:
                        TypeError("Bike type is not recognised for chassis_Station_Order[0].bike_order")

                elif chassis_Station_Order[0].bike_order.fork == "Tubular Aluminium" and window.ChassisStationInventoryAluminiumForksCount.value() > 0 and chassis_Station_Order[0].bike_order.frame == "Tubular Aluminium" and window.ChassisStationInventoryAluminiumFrameCount.value() > 0:
                    # Enable station button
                    window.ChassisAssemblyButton.setEnabled(True)

                elif chassis_Station_Order[0].bike_order.fork == "Carbon Fibre" and window.ChassisStationInventoryCarbonForksCount.value() > 0 and chassis_Station_Order[0].bike_order.frame == "Carbon Fibre" and window.ChassisStationInventoryCarbonFrameCount.value() > 0:
                    # Enable station button
                    window.ChassisAssemblyButton.setEnabled(True)

                else:
                    # Disable station button
                    window.ChassisAssemblyButton.setEnabled(False)

        elif "Chassis" in keyword:
            # Check if Paint Station has orders
            if len(paint_Station_Order) > 0:
                # Check if they now have required amount
                if PaintStationHasRequiredAmount():
                    # Enable station button
                    window.PaintedButton.setEnabled(True)
                else:
                    # Disable station button
                    window.PaintedButton.setEnabled(False)
        
        elif "Paint" in keyword:
            # Check if Paint Station has orders
            if len(paint_Station_Order) > 0:
                # Check if they now have required amount
                if PaintStationHasRequiredAmount():
                    # Enable station button
                    window.PaintedButton.setEnabled(True)
                else:
                    # Disable station button
                    window.PaintedButton.setEnabled(False)
        elif "Pedals" in keyword:
             # Check if Paint Station has orders
            if len(pedal_Station_Order) > 0:
                # Check if they now have required amount
                if PedalStationHasRequiredAmount():
                    # Enable station button
                    window.PedalAssembly_AssembledButton.setEnabled(True)
                else:
                    # Disable station button
                    window.PedalAssembly_AssembledButton.setEnabled(False)

        elif "Gears" in keyword or "Chain" in keyword:
             # Check if DC Station has orders
            if len(drive_chain_Station_Order) > 0:
                # Check if they now have required amount
                if DCStationHasRequiredAmount():
                    # Enable station button
                    window.DCAssembledButton.setEnabled(True)
                else:
                    # Disable station button
                    window.DCAssembledButton.setEnabled(False)

        elif "Wheel" in keyword:
            # Check if Wheel Station has orders
            if len(wheel_Station_Order) > 0:
                # Check if they now have required amount
                if WheelHasRequiredAmount():
                    # Enable station button
                    window.WheelAssembly_AssembledButton.setEnabled(True)
                else:
                    # Disable station button
                    window.WheelAssembly_AssembledButton.setEnabled(False)

        elif "Brakes" in keyword:
            # Check if Wheel Station has orders
            if len(brakes_Station_Order) > 0:
                # Check if they now have required amount
                if BrakeHasRequiredAmount():
                    # Enable station button
                    window.BrakeAssemblyAssembledButton.setEnabled(True)
                else:
                    # Disable station button
                    window.BrakeAssemblyAssembledButton.setEnabled(False)

        elif "Light" in keyword:
            # Check if Wheel Station has orders
            if len(lights_Station_Order) > 0:
                # Check if they now have required amount
                if LightHasRequiredAmount():
                    # Enable station button
                    window.LightStation_Assembly_AssembledButton.setEnabled(True)
                else:
                    # Disable station button
                    window.LightStation_Assembly_AssembledButton.setEnabled(False)

        elif "Seat" in keyword:
            # Check if Wheel Station has orders
            if len(seat_Station_Order) > 0:
                # Check if they now have required amount
                if SeatHasRequiredAmount():
                    # Enable station button
                    window.SeatStation_Seat_Assembled_Button.setEnabled(True)
                else:
                    # Disable station button
                    window.SeatStation_Seat_Assembled_Button.setEnabled(False)
        else:
            return

    def TableChassisInventory(table, display) -> None:
        display.display(table.rowCount())
        if table.rowCount() < 3:
            display.setStyleSheet("""QLCDNumber {
                                   background-color: red; 
                                   }""")

        elif table.rowCount() > 3:
            display.setStyleSheet("""QLCDNumber {
                                   background-color: Green; 
                                   }""")
        else:
            display.setStyleSheet("""QLCDNumber {
                                   background-color: None; 
                                   }""")


            

    def setupInventory():
        #Raw Materials
        inventory["Steel"] = [window.Inventory_RawMaterial_Steel_Count, window.ForkStationTubularSteelInventoryCount, window.FrameStationInventoryTubularSteelCount]
        inventory["Aluminium"] = [window.Inventory_RawMaterial_Aluminium_Count, window.ForkStationTubularAluminiumInventoryCount, window.FrameStationInventoryTubularAluminiumCount]
        inventory["Carbon Fibre"] = [window.Inventory_RawMaterial_Carbon_Count, window.ForkStationTubularCarbonInventoryCount, window.FrameStationInventoryCarbonCount]

        #Paint
        inventory["Black Paint"] = [window.Inventory_RawMaterial_BlackPaintCount, window.PaintStationBlackPaintCount]
        inventory["Blue Paint"] = [window.Inventory_RawMaterial_BluePaintCount, window.PaintStationBluePaintCount]
        inventory["Green Paint"] = [window.Inventory_RawMaterial_GreenPaintCount, window.PaintStationGreenPaintCount]
        inventory["Grey Paint"] = [window.Inventory_RawMaterial_GreyPaintCount, window.PaintStationGreyPaintCount]
        inventory["Orange Paint"] = [window.Inventory_RawMaterial_OrangePaintCount, window.PaintStationOrangePaintCount]
        inventory["Pink Paint"] = [window.Inventory_RawMaterial_PinkPaintCount, window.PaintStationPinkPaintCount]
        inventory["Purple Paint"] = [window.Inventory_RawMaterial_PurplePaintCount, window.PaintStationPurplePaintCount]
        inventory["Red Paint"] = [window.Inventory_RawMaterial_RedPaintCount, window.PaintStationRedPaintCount]
        inventory["Yellow Paint"] = [window.Inventory_RawMaterial_YellowPaintCount, window.PaintStationYellowPaintCount]
        inventory["White Paint"] = [window.Inventory_RawMaterial_WhitePaintCount, window.PaintStationWhitePaintCount]

        #Parts

        #Pedals
        inventory["Normal Pedals"] = [window.Inventory_Parts_Pedals_Normal_Count, window.PedalStationInventoryTotalPedalsCount, window.PedalStationInventoryNormalPedalsCount]
        inventory["Premium Pedals"] = [window.Inventory_Parts_Pedals_Premium_Count, window.PedalStationInventoryTotalPedalsCount, window.PedalStationInventoryPremiumPedalsCount]
        inventory["Carbon Fibre Pedals"] = [window.Inventory_Parts_Pedals_Carbon_Count, window.PedalStationInventoryTotalPedalsCount, window.PedalStationInventoryCarbonPedalsCount]
        inventory["Kids Pedals"] = [window.Inventory_Parts_Pedals_Kids_Count, window.PedalStationInventoryTotalPedalsCount, window.PedalStationInventoryKidsPedalsCount]

        #Gears
        inventory["Standard Gears"] = [window.Inventory_Parts_Gears_Normal_Count, window.DCStationInventoryTotalGearCounter, window.DCStationInventoryNormalGearCounter]
        inventory["Low Speed Gears"] = [window.Inventory_Parts_Gears_LowSpeed_Count, window.DCStationInventoryTotalGearCounter, window.DCStationInventoryLowSpeedGearCounter]
        inventory["High Speed Gears"] = [window.Inventory_Parts_Gears_HighSpeed_Count, window.DCStationInventoryTotalGearCounter, window.DCStationInventoryHighSpeedGearCounter]
        inventory["Kids Gears"] = [window.Inventory_Parts_Gears_Kids_Count, window.DCStationInventoryTotalGearCounter, window.DCStationInventoryKidsGearCounter]

        #Chains
        inventory["Standard Chain"] = [window.Inventory_Parts_Chain_Normal_Count, window.DCStationInventoryTotalChainCounter, window.DCStationInventoryNormalChainCounter]
        inventory["Premium Chain"] =[window.Inventory_Parts_Chain_Premium_Count, window.DCStationInventoryTotalChainCounter, window.DCStationInventoryPremiumChainCounter]
        inventory["Track Chain"] = [window.Inventory_Parts_Chain_Track_Count, window.DCStationInventoryTotalChainCounter, window.DCStationInventoryTrackChainCounter]

        #Wheels
        inventory["Standard Wheels"] = [window.Inventory_Parts_Wheels_Normal_Count, window.WheelStationInventory_TotalCount, window.WheelStationInventory_NormalCount]
        inventory["Offroad Wheels"] = [window.Inventory_Parts_Wheels_Offroad_Count, window.WheelStationInventory_TotalCount, window.WheelStationInventory_OffroadCount]
        inventory["Road Wheels"] = [window.Inventory_Parts_Wheels_Road_Count, window.WheelStationInventory_TotalCount, window.WheelStationInventory_RoadCount]
        inventory["Carbon Fibre Wheels"] = [window.Inventory_Parts_Wheels_Carbon_Count, window.WheelStationInventory_TotalCount, window.WheelStationInventory_CarbonCount]
        inventory["Kids Wheels"] = [window.Inventory_Parts_Wheels_Kids_Count, window.WheelStationInventory_TotalCount, window.WheelStationInventory_KidsCount]

        #Brakes
        inventory["Normal Brakes"] = [window.Inventory_Parts_Brakes_Normal_Count, window.BrakeStationTotalBrakeCounter, window.BrakeStationNormalBrakeCounter]
        inventory["Premium Brakes"] = [window.Inventory_Parts_Brakes_Premium_Count, window.BrakeStationTotalBrakeCounter, window.BrakeStationPremiumBrakeCounter]

        #Seats
        inventory["Normal Seat"] = [window.Inventory_Parts_Seats_Normal_Count, window.SeatStationInventoryTotalSeatCount, window.SeatStationInventoryNormalSeatCount]
        inventory["Premium Seat"] = [window.Inventory_Parts_Seats_Premium_Count, window.SeatStationInventoryTotalSeatCount, window.SeatStationInventoryPremiumSeatCount]
        inventory["Carbon Fibre Seat"] = [window.Inventory_Parts_Seats_Carbon_Count, window.SeatStationInventoryTotalSeatCount, window.SeatStationInventoryCarbonSeatCount]

        #Lights
        inventory["Normal Lights"] = [window.Inventory_Parts_Lights_Normal_Count, window.LightStation_TotalLightCount, window.LightStation_NormalLightCount]
        inventory["Premium Lights"] = [window.Inventory_Parts_Lights_Premium_Count, window.LightStation_TotalLightCount, window.LightStation_PremiumLightCount]

        # Forks

        inventory["Total Forks"] = window.ForkStationInventoryTotalForksCount
        inventory["Standard Forks"] = [window.ForkStationInventoryStandardForksCount, window.ForkStationInventoryTotalForksCount, window.ChassisStationInventoryTotalForksCount, window.ChassisStationInventoryStandardForksCount]
        inventory["Mountain Forks"] = [window.ForkStationInventoryMountainForksCount, window.ForkStationInventoryTotalForksCount, window.ChassisStationInventoryTotalForksCount, window.ChassisStationInventoryMountainForksCount]
        inventory["BMX Forks"] = [window.ForkStationInventoryBMXForksCount, window.ForkStationInventoryTotalForksCount, window.ChassisStationInventoryTotalForksCount, window.ChassisStationInventoryBMXForksCount]
        inventory["Road Forks"] = [window.ForkStationInventoryTubularAluminiumForksCount, window.ForkStationInventoryTotalForksCount, window.ChassisStationInventoryTotalForksCount, window.ChassisStationInventoryAluminiumForksCount]
        inventory["Track Forks"] = [window.ForkStationInventoryCarbonForksCount, window.ForkStationInventoryTotalForksCount,  window.ChassisStationInventoryTotalForksCount, window.ChassisStationInventoryCarbonForksCount]
        inventory["Kids Forks"] = [window.ForkStationInventoryKidsForksCount, window.ForkStationInventoryTotalForksCount, window.ChassisStationInventoryTotalForksCount, window.ChassisStationInventoryKidsForksCount]

        # Frames

        inventory["Total Frames"] = window.FrameStationInventoryTotalFramesCount
        inventory["Standard Frames"] = [window.FrameStationInventoryStandardFrameCount, window.FrameStationInventoryTotalFramesCount, window.ChassisStationInventoryTotalFrameCount, window.ChassisStationInventoryStandardFrameCount]
        inventory["Mountain Frames"] = [window.FrameStationInventoryMountainFrameCount, window.FrameStationInventoryTotalFramesCount, window.ChassisStationInventoryTotalFrameCount, window.ChassisStationInventoryMountainFrameCount]
        inventory["BMX Frames"] = [window.FrameStationInventoryBMXFrameCount, window.FrameStationInventoryTotalFramesCount, window.ChassisStationInventoryTotalFrameCount, window.ChassisStationInventoryBMXFrameCount]
        inventory["Road Frames"] = [window.FrameStationInventoryAluminiumFrameCount, window.FrameStationInventoryTotalFramesCount, window.ChassisStationInventoryTotalFrameCount, window.ChassisStationInventoryAluminiumFrameCount]
        inventory["Track Frames"] = [window.FrameStationInventoryCarbonFrameCount, window.FrameStationInventoryTotalFramesCount, window.ChassisStationInventoryTotalFrameCount, window.ChassisStationInventoryCarbonFrameCount]
        inventory["Kids Frames"] = [window.FrameStationInventoryKidsFrameCount, window.FrameStationInventoryTotalFramesCount, window.ChassisStationInventoryTotalFrameCount, window.ChassisStationInventoryKidsFrameCount]

        # Chassis

        inventory["Total Chassis"] = window.ChassisInventoryTotalChassisCount
        inventory["Standard Chassis"] = [window.ChassisInventoryNormalChassisCount, window.ChassisInventoryTotalChassisCount, window.PaintStationTotalChassisCount, window.PaintStationNormalChassisCount]
        inventory["Mountain Chassis"] = [window.ChassisInventoryMountainChassisCount, window.ChassisInventoryTotalChassisCount, window.PaintStationTotalChassisCount, window.PaintStationMountainChassisCount]
        inventory["Road Chassis"] = [window.ChassisInventoryRoadChassisCount, window.ChassisInventoryTotalChassisCount, window.PaintStationTotalChassisCount, window.PaintStationRoadChassisCount]
        inventory["Track Chassis"] = [window.ChassisInventoryTrackChassisCount, window.ChassisInventoryTotalChassisCount, window.PaintStationTotalChassisCount, window.PaintStationTrackChassisCount]
        inventory["BMX Chassis"] = [window.ChassisInventoryBMXChassisCount, window.ChassisInventoryTotalChassisCount, window.PaintStationTotalChassisCount, window.PaintStationBMXChassisCount]
        inventory["Kids Chassis"] = [window.ChassisInventoryKidsChassisCount, window.ChassisInventoryTotalChassisCount, window.PaintStationTotalChassisCount, window.PaintStationKidsChassisCount]

        #Connecting Buttons

        # Raw Material
        window.Inventory_RawMaterial_Steel_Increase.clicked.connect(lambda: InventoryChange("Steel", 1.0))
        window.Inventory_RawMaterial_Aluminium_Increase.clicked.connect(lambda: InventoryChange("Aluminium", 1.0))
        window.Inventory_RawMaterial_Carbon_Increase.clicked.connect(lambda: InventoryChange("Carbon Fibre", 1.0))

        window.Inventory_RawMaterial_Steel_Decrease.clicked.connect(lambda: InventoryChange("Steel", -1.0))
        window.Inventory_RawMaterial_Aluminium_Decrease.clicked.connect(lambda: InventoryChange("Aluminium", -1.0))
        window.Inventory_RawMaterial_Carbon_Decrease.clicked.connect(lambda: InventoryChange("Carbon Fibre", -1.0))

        # Paint
        window.Inventory_RawMaterial_BlackPaintIncrease.clicked.connect(lambda: InventoryChange("Black Paint", 1.0))
        window.Inventory_RawMaterial_BluePaintIncrease.clicked.connect(lambda: InventoryChange("Blue Paint", 1.0))
        window.Inventory_RawMaterial_GreenPaintIncrease.clicked.connect(lambda: InventoryChange("Green Paint", 1.0))
        window.Inventory_RawMaterial_GreyPaintIncrease.clicked.connect(lambda: InventoryChange("Grey Paint", 1.0))
        window.Inventory_RawMaterial_OrangePaintIncrease.clicked.connect(lambda: InventoryChange("Orange Paint", 1.0))
        window.Inventory_RawMaterial_PinkPaintIncrease.clicked.connect(lambda: InventoryChange("Pink Paint", 1.0))
        window.Inventory_RawMaterial_PurplePaintIncrease.clicked.connect(lambda: InventoryChange("Purple Paint", 1.0))
        window.Inventory_RawMaterial_RedPaintIncrease.clicked.connect(lambda: InventoryChange("Red Paint", 1.0))
        window.Inventory_RawMaterial_YellowPaintIncrease.clicked.connect(lambda: InventoryChange("Yellow Paint", 1.0))
        window.Inventory_RawMaterial_WhitePaintIncrease.clicked.connect(lambda: InventoryChange("White Paint", 1.0))

        window.Inventory_RawMaterial_BlackPaintDecrease.clicked.connect(lambda: InventoryChange("Black Paint", -1.0))
        window.Inventory_RawMaterial_BluePaintDecrease.clicked.connect(lambda: InventoryChange("Blue Paint", -1.0))
        window.Inventory_RawMaterial_GreenPaintDecrease.clicked.connect(lambda: InventoryChange("Green Paint", -1.0))
        window.Inventory_RawMaterial_GreyPaintDecrease.clicked.connect(lambda: InventoryChange("Grey Paint", -1.0))
        window.Inventory_RawMaterial_OrangePaintDecrease.clicked.connect(lambda: InventoryChange("Orange Paint", -1.0))
        window.Inventory_RawMaterial_PinkPaintDecrease.clicked.connect(lambda: InventoryChange("Pink Paint", -1.0))
        window.Inventory_RawMaterial_PurplePaintDecrease.clicked.connect(lambda: InventoryChange("Purple Paint", -1.0))
        window.Inventory_RawMaterial_RedPaintDecrease.clicked.connect(lambda: InventoryChange("Red Paint", -1.0))
        window.Inventory_RawMaterial_YellowPaintDecrease.clicked.connect(lambda: InventoryChange("Yellow Paint", -1.0))
        window.Inventory_RawMaterial_WhitePaintDecrease.clicked.connect(lambda: InventoryChange("White Paint", -1.0))

        # Pedals

        window.Inventory_Parts_Pedals_Normal_Increase.clicked.connect(lambda: InventoryChange("Normal Pedals", 1.0))
        window.Inventory_Parts_Pedals_Premium_Increase.clicked.connect(lambda: InventoryChange("Premium Pedals", 1.0))
        window.Inventory_Parts_Pedals_Carbon_Increase.clicked.connect(lambda: InventoryChange("Carbon Fibre Pedals", 1.0))
        window.Inventory_Parts_Pedals_Kids_Increase.clicked.connect(lambda: InventoryChange("Kids Pedals", 1.0))

        window.Inventory_Parts_Pedals_Normal_Decrease.clicked.connect(lambda: InventoryChange("Normal Pedals", -1.0))
        window.Inventory_Parts_Pedals_Premium_Decrease.clicked.connect(lambda: InventoryChange("Premium Pedals", -1.0))
        window.Inventory_Parts_Pedals_Carbon_Decrease.clicked.connect(lambda: InventoryChange("Carbon Fibre Pedals", -1.0))
        window.Inventory_Parts_Pedals_Kids_Decrease.clicked.connect(lambda: InventoryChange("Kids Pedals", -1.0))

        # Gears
        
        window.Inventory_Parts_Gears_Normal_Increase.clicked.connect(lambda: InventoryChange("Standard Gears", 1.0))
        window.Inventory_Parts_Gears_LowSpeed_Increase.clicked.connect(lambda: InventoryChange("Low Speed Gears", 1.0))
        window.Inventory_Parts_Gears_HighSpeed_Increase.clicked.connect(lambda: InventoryChange("High Speed Gears", 1.0))
        window.Inventory_Parts_Gears_Kids_Increase.clicked.connect(lambda: InventoryChange("Kids Gears", 1.0))

        window.Inventory_Parts_Gears_Normal_Decrease.clicked.connect(lambda: InventoryChange("Standard Gears", -1.0))
        window.Inventory_Parts_Gears_LowSpeed_Decrease.clicked.connect(lambda: InventoryChange("Low Speed Gears", -1.0))
        window.Inventory_Parts_Gears_HighSpeed_Decrease.clicked.connect(lambda: InventoryChange("High Speed Gears", -1.0))
        window.Inventory_Parts_Gears_Kids_Decrease.clicked.connect(lambda: InventoryChange("Kids Gears", -1.0))

        # Chains

        window.Inventory_Parts_Chain_Normal_Increase.clicked.connect(lambda: InventoryChange("Standard Chain", 1.0))
        window.Inventory_Parts_Chain_Premium_Increase.clicked.connect(lambda: InventoryChange("Premium Chain", 1.0))
        window.Inventory_Parts_Chain_Track_Increase.clicked.connect(lambda: InventoryChange("Track Chain", 1.0))

        window.Inventory_Parts_Chain_Normal_Decrease.clicked.connect(lambda: InventoryChange("Standard Chain", -1.0))
        window.Inventory_Parts_Chain_Premium_Decrease.clicked.connect(lambda: InventoryChange("Premium Chain", -1.0))
        window.Inventory_Parts_Chain_Track_Decrease.clicked.connect(lambda: InventoryChange("Track Chain", -1.0))

        # Wheels

        window.Inventory_Parts_Wheels_Normal_Increase.clicked.connect(lambda: InventoryChange("Standard Wheels", 1.0))
        window.Inventory_Parts_Wheels_Offroad_Increase.clicked.connect(lambda: InventoryChange("Offroad Wheels", 1.0))
        window.Inventory_Parts_Wheels_Road_Increase.clicked.connect(lambda: InventoryChange("Road Wheels", 1.0))
        window.Inventory_Parts_Wheels_Carbon_Increase.clicked.connect(lambda: InventoryChange("Carbon Fibre Wheels", 1.0))
        window.Inventory_Parts_Wheels_Kids_Increase.clicked.connect(lambda: InventoryChange("Kids Wheels", 1.0))

        window.Inventory_Parts_Wheels_Normal_Decrease.clicked.connect(lambda: InventoryChange("Standard Wheels", -1.0))
        window.Inventory_Parts_Wheels_Offroad_Decrease.clicked.connect(lambda: InventoryChange("Offroad Wheels", -1.0))
        window.Inventory_Parts_Wheels_Road_Decrease.clicked.connect(lambda: InventoryChange("Road Wheels", -1.0))
        window.Inventory_Parts_Wheels_Carbon_Decrease.clicked.connect(lambda: InventoryChange("Carbon Fibre Wheels", -1.0))
        window.Inventory_Parts_Wheels_Kids_Decrease.clicked.connect(lambda: InventoryChange("Kids Wheels", -1.0))

        # Brakes

        window.Inventory_Parts_Brakes_Normal_Increase.clicked.connect(lambda: InventoryChange("Normal Brakes", 1.0))
        window.Inventory_Parts_Brakes_Premium_Increase.clicked.connect(lambda: InventoryChange("Premium Brakes", 1.0))

        window.Inventory_Parts_Brakes_Normal_Decrease.clicked.connect(lambda: InventoryChange("Normal Brakes", -1.0))
        window.Inventory_Parts_Brakes_Premium_Decrease.clicked.connect(lambda: InventoryChange("Premium Brakes", -1.0))

        # Seats

        window.Inventory_Parts_Seats_Normal_Increase.clicked.connect(lambda: InventoryChange("Normal Seat", 1.0))
        window.Inventory_Parts_Seats_Premium_Increase.clicked.connect(lambda: InventoryChange("Premium Seat", 1.0))
        window.Inventory_Parts_Seats_Carbon_Increase.clicked.connect(lambda: InventoryChange("Carbon Fibre Seat", 1.0))

        window.Inventory_Parts_Seats_Normal_Decrease.clicked.connect(lambda: InventoryChange("Normal Seat", -1.0))
        window.Inventory_Parts_Seats_Premium_Decrease.clicked.connect(lambda: InventoryChange("Premium Seat", -1.0))
        window.Inventory_Parts_Seats_Carbon_Decrease.clicked.connect(lambda: InventoryChange("Carbon Fibre Seat", -1.0))

        # Lights

        window.Inventory_Parts_Lights_Normal_Increase.clicked.connect(lambda: InventoryChange("Normal Lights", 1.0))
        window.Inventory_Parts_Lights_Premium_Increase.clicked.connect(lambda: InventoryChange("Premium Lights", 1.0))

        window.Inventory_Parts_Lights_Normal_Decrease.clicked.connect(lambda: InventoryChange("Normal Lights", -1.0))
        window.Inventory_Parts_Lights_Premium_Decrease.clicked.connect(lambda: InventoryChange("Premium Lights", -1.0))

    # 6 tables for inventory + possible customer table

    # Stacked Widget and Menu Bar Logic:
    def changePage(stacked_widget, index):
        """
        Function to change the current indedx (page) of the stacked widget

        # Parameters:
        stacked_widget: QStackedWidget
        index: int
        """
        stacked_widget.setCurrentIndex(index)

    def updatedOrderTable(order):
        order_table = window.Orders_Table
        row_count = window.Orders_Table.rowCount()
        order_table.insertRow(row_count)
        order_table.setItem(row_count, 0, QTableWidgetItem(str(order.id)))
        order_table.setItem(row_count, 1, QTableWidgetItem(str(order.customer.id)))
        order_table.setItem(row_count, 2, QTableWidgetItem(order.bike_order.bike_type))
        order_table.setItem(row_count, 3, QTableWidgetItem(order.bike_order.fork))
        order_table.setItem(row_count, 4, QTableWidgetItem(order.bike_order.frame))
        order_table.setItem(row_count, 5, QTableWidgetItem(order.bike_order.colour))
        order_table.setItem(row_count, 6, QTableWidgetItem(order.bike_order.pedals))
        order_table.setItem(row_count, 7, QTableWidgetItem(order.bike_order.gears))
        order_table.setItem(row_count, 8, QTableWidgetItem(order.bike_order.chain))
        order_table.setItem(row_count, 9, QTableWidgetItem(order.bike_order.wheels))
        order_table.setItem(row_count, 10, QTableWidgetItem(order.bike_order.brakes))
        order_table.setItem(row_count, 11, QTableWidgetItem(order.bike_order.lights))
        order_table.setItem(row_count, 12, QTableWidgetItem(order.bike_order.seat))

    def updatePedalsTable():
        table = window.PedalStationChassisInventoryTable
        table.setRowCount(0)
        for order in pedal_Station_Order:
            row_count = table.rowCount()
            table.insertRow(row_count)
            if type(order.bike_order) == Bike:
                table.setItem(row_count, 0, QTableWidgetItem("Standard"))
            elif type(order.bike_order) == MountainBike:
                table.setItem(row_count, 0, QTableWidgetItem("Mountain"))
            elif type(order.bike_order) == RoadBike:
                table.setItem(row_count, 0, QTableWidgetItem("Road"))
            elif type(order.bike_order) == TrackBike:
                table.setItem(row_count, 0, QTableWidgetItem("Track"))
            elif type(order.bike_order) == BMXBike:
                table.setItem(row_count, 0, QTableWidgetItem("BMX"))
            elif type(order.bike_order) == KidsBike:
                table.setItem(row_count, 0, QTableWidgetItem("Kids"))
            table.setItem(row_count, 1, QTableWidgetItem(str(order.bike_order.colour)))
        TableChassisInventory(table, window.PedalStationInventoryTotalChassis)

    def updateDriveChainTable():
        table = window.DCStationChassisInventoryTable
        table.setRowCount(0)
        for order in drive_chain_Station_Order:
            row_count = table.rowCount()
            table.insertRow(row_count)
            if type(order.bike_order) == Bike:
                table.setItem(row_count, 0, QTableWidgetItem("Standard"))
            elif type(order.bike_order) == MountainBike:
                table.setItem(row_count, 0, QTableWidgetItem("Mountain"))
            elif type(order.bike_order) == RoadBike:
                table.setItem(row_count, 0, QTableWidgetItem("Road"))
            elif type(order.bike_order) == TrackBike:
                table.setItem(row_count, 0, QTableWidgetItem("Track"))
            elif type(order.bike_order) == BMXBike:
                table.setItem(row_count, 0, QTableWidgetItem("BMX"))
            elif type(order.bike_order) == KidsBike:
                table.setItem(row_count, 0, QTableWidgetItem("Kids"))
            table.setItem(row_count, 1, QTableWidgetItem(str(order.bike_order.colour)))
            table.setItem(row_count, 2, QTableWidgetItem(str(order.bike_order.pedals)))
        TableChassisInventory(table, window.DCStationInventoryTotalChassis)

    def updateWheelTable():
        table = window.WheelStationChassisInventory
        table.setRowCount(0)
        for order in wheel_Station_Order:
            row_count = table.rowCount()
            table.insertRow(row_count)
            if type(order.bike_order) == Bike:
                table.setItem(row_count, 0, QTableWidgetItem("Standard"))
            elif type(order.bike_order) == MountainBike:
                table.setItem(row_count, 0, QTableWidgetItem("Mountain"))
            elif type(order.bike_order) == RoadBike:
                table.setItem(row_count, 0, QTableWidgetItem("Road"))
            elif type(order.bike_order) == TrackBike:
                table.setItem(row_count, 0, QTableWidgetItem("Track"))
            elif type(order.bike_order) == BMXBike:
                table.setItem(row_count, 0, QTableWidgetItem("BMX"))
            elif type(order.bike_order) == KidsBike:
                table.setItem(row_count, 0, QTableWidgetItem("Kids"))
            table.setItem(row_count, 1, QTableWidgetItem(str(order.bike_order.colour)))
            table.setItem(row_count, 2, QTableWidgetItem(str(order.bike_order.pedals)))
            table.setItem(row_count, 3, QTableWidgetItem(str(order.bike_order.gears)))
            table.setItem(row_count, 4, QTableWidgetItem(str(order.bike_order.chain)))
        TableChassisInventory(table, window.WheelStationInventoryTotalChassis)


            
    def updateBrakeTable():
        table = window.BrakeStationChassisInventoryTable
        table.setRowCount(0)
        for order in brakes_Station_Order:
            row_count = table.rowCount()
            table.insertRow(row_count)
            if type(order.bike_order) == Bike:
                table.setItem(row_count, 0, QTableWidgetItem("Standard"))
            elif type(order.bike_order) == MountainBike:
                table.setItem(row_count, 0, QTableWidgetItem("Mountain"))
            elif type(order.bike_order) == RoadBike:
                table.setItem(row_count, 0, QTableWidgetItem("Road"))
            elif type(order.bike_order) == TrackBike:
                table.setItem(row_count, 0, QTableWidgetItem("Track"))
            elif type(order.bike_order) == BMXBike:
                table.setItem(row_count, 0, QTableWidgetItem("BMX"))
            elif type(order.bike_order) == KidsBike:
                table.setItem(row_count, 0, QTableWidgetItem("Kids"))
            table.setItem(row_count, 1, QTableWidgetItem(str(order.bike_order.colour)))
            table.setItem(row_count, 2, QTableWidgetItem(str(order.bike_order.pedals)))
            table.setItem(row_count, 3, QTableWidgetItem(str(order.bike_order.gears)))
            table.setItem(row_count, 4, QTableWidgetItem(str(order.bike_order.chain)))        
            table.setItem(row_count, 5, QTableWidgetItem(str(order.bike_order.wheels)))    
        TableChassisInventory(table, window.BrakeStationInventoryTotalChassis)

    def updateLightTable():
        table = window.LightStation_ChassisInventory_Table
        table.setRowCount(0)
        for order in lights_Station_Order:
            row_count = table.rowCount()
            table.insertRow(row_count)
            if type(order.bike_order) == Bike:
                table.setItem(row_count, 0, QTableWidgetItem("Standard"))
            elif type(order.bike_order) == MountainBike:
                table.setItem(row_count, 0, QTableWidgetItem("Mountain"))
            elif type(order.bike_order) == RoadBike:
                table.setItem(row_count, 0, QTableWidgetItem("Road"))
            elif type(order.bike_order) == TrackBike:
                table.setItem(row_count, 0, QTableWidgetItem("Track"))
            elif type(order.bike_order) == BMXBike:
                table.setItem(row_count, 0, QTableWidgetItem("BMX"))
            elif type(order.bike_order) == KidsBike:
                table.setItem(row_count, 0, QTableWidgetItem("Kids"))
            table.setItem(row_count, 1, QTableWidgetItem(str(order.bike_order.colour)))
            table.setItem(row_count, 2, QTableWidgetItem(str(order.bike_order.pedals)))
            table.setItem(row_count, 3, QTableWidgetItem(str(order.bike_order.gears)))
            table.setItem(row_count, 4, QTableWidgetItem(str(order.bike_order.chain)))        
            table.setItem(row_count, 5, QTableWidgetItem(str(order.bike_order.wheels)))       
            table.setItem(row_count, 6, QTableWidgetItem(str(order.bike_order.brakes)))             
        TableChassisInventory(table, window.LightStation_InventoryTotalChassisCount)

    def updateSeatTable():
        table = window.SeatStationChassisInventoryTable
        table.setRowCount(0)
        for order in seat_Station_Order:
            row_count = table.rowCount()
            table.insertRow(row_count)
            if type(order.bike_order) == Bike:
                table.setItem(row_count, 0, QTableWidgetItem("Standard"))
            elif type(order.bike_order) == MountainBike:
                table.setItem(row_count, 0, QTableWidgetItem("Mountain"))
            elif type(order.bike_order) == RoadBike:
                table.setItem(row_count, 0, QTableWidgetItem("Road"))
            elif type(order.bike_order) == TrackBike:
                table.setItem(row_count, 0, QTableWidgetItem("Track"))
            elif type(order.bike_order) == BMXBike:
                table.setItem(row_count, 0, QTableWidgetItem("BMX"))
            elif type(order.bike_order) == KidsBike:
                table.setItem(row_count, 0, QTableWidgetItem("Kids"))
            table.setItem(row_count, 1, QTableWidgetItem(str(order.bike_order.colour)))
            table.setItem(row_count, 2, QTableWidgetItem(str(order.bike_order.pedals)))
            table.setItem(row_count, 3, QTableWidgetItem(str(order.bike_order.gears)))
            table.setItem(row_count, 4, QTableWidgetItem(str(order.bike_order.chain)))        
            table.setItem(row_count, 5, QTableWidgetItem(str(order.bike_order.wheels)))       
            table.setItem(row_count, 6, QTableWidgetItem(str(order.bike_order.brakes)))  
            table.setItem(row_count, 7, QTableWidgetItem(str(order.bike_order.lights)))  
        TableChassisInventory(table, window.SeatStationInventoryTotalChassisCount)
    
    def updateCompletedOrdersTable(order):
        table = window.Completed_Orders_Table
        row_count = table.rowCount()
        table.insertRow(row_count)

        # Add completed order data
        table.setItem(row_count, 0, QTableWidgetItem(str(order.id)))
        table.setItem(row_count, 1, QTableWidgetItem(str(order.customer.id)))
        table.setItem(row_count, 2, QTableWidgetItem(order.bike_order.bike_type))
        table.setItem(row_count, 3, QTableWidgetItem(order.bike_order.fork))
        table.setItem(row_count, 4, QTableWidgetItem(order.bike_order.frame))
        table.setItem(row_count, 5, QTableWidgetItem(order.bike_order.colour))
        table.setItem(row_count, 6, QTableWidgetItem(order.bike_order.pedals))
        table.setItem(row_count, 7, QTableWidgetItem(order.bike_order.gears))
        table.setItem(row_count, 8, QTableWidgetItem(order.bike_order.chain))
        table.setItem(row_count, 9, QTableWidgetItem(order.bike_order.wheels))
        table.setItem(row_count, 10, QTableWidgetItem(order.bike_order.brakes))
        table.setItem(row_count, 11, QTableWidgetItem(order.bike_order.lights))
        table.setItem(row_count, 12, QTableWidgetItem(order.bike_order.seat))

    def newOrder():
        global customers, orders
        # Customer data
        name = window.NewOrder_NameLineEdit.text()
        email = window.NewOrder_EmailLineEdit.text()
        phone = window.NewOrder_PhoneLineEdit.text()
        address1 = window.NewOrder_AddressLine1LineEdit.text()
        address2 = window.NewOrder_AddressLine2LineEdit.text()
        city = window.NewOrder_CityLineEdit.text()
        postcode = window.NewOrder_PostcodeLineEdit.text()

        # Bike data
        bike_type = window.NewOrder_BikeTypeComboBox.currentText()
        colour = window.NewOrder_ColourComboBox.currentText()
        pedal = window.NewOrder_PedalTypeComboBox.currentText()
        chain = window.NewOrder_ChainTypeComboBox.currentText()
        gear = window.NewOrder_GearTypeComboBox.currentText()
        wheel = window.NewOrder_WheelTypeComboBox.currentText()
        brake = window.NewOrder_BrakeTypeComboBox.currentText()
        light = window.NewOrder_LightTypeComboBox.currentText()
        seat = window.NewOrder_SeatTypeComboBox.currentText()

        # Reset Error Message Before checking
        window.NewOrder_ErrorMessage.setEnabled(False)
        window.NewOrder_ErrorMessage.setText("")

        # Error Messages / Checking
        if name == "":
            window.NewOrder_ErrorMessage.setEnabled(True)
            window.NewOrder_ErrorMessage.setText("Your order cannot be completed without a name. \nPlease enter a name and try again.")
            return
        elif email == "":
            # Check valid email to be implemented
            window.NewOrder_ErrorMessage.setEnabled(True)
            window.NewOrder_ErrorMessage.setText("Your order cannot be completed without an email. \nPlease enter an email and try again.")
            return
        elif phone == "":
            # Check valid phone number to be implemented
            window.NewOrder_ErrorMessage.setEnabled(True)
            window.NewOrder_ErrorMessage.setText("Your order cannot be completed without a phone number. \nPlease enter a phone number and try again.")
            return
        elif address1 == "":
            window.NewOrder_ErrorMessage.setEnabled(True)
            window.NewOrder_ErrorMessage.setText("Your order cannot be completed without a correct address. \nPlease enter a correct address and try again.")
            return
        elif address2 == "":
            window.NewOrder_ErrorMessage.setEnabled(True)
            window.NewOrder_ErrorMessage.setText("Your order cannot be completed without a correct address. \nPlease enter a correct address and try again.")
            return
        elif city == "":
            window.NewOrder_ErrorMessage.setEnabled(True)
            window.NewOrder_ErrorMessage.setText("Your order cannot be completed without a correct address. \nPlease enter a city and try again.")
            return
        elif postcode == "":
            window.NewOrder_ErrorMessage.setEnabled(True)
            window.NewOrder_ErrorMessage.setText("Your order cannot be completed without a correct address. \nPlease enter postcode and try again.")
            return
        else:
            address = Address(address1, address2, city, postcode)
            customer = Customer(name, email, phone, address)
            customers[customer] = customer

        if colour == "":
            window.NewOrder_ErrorMessage.setEnabled(True)
            window.NewOrder_ErrorMessage.setText("Your order cannot be completed without a colour. \nPlease enter one and try again.")
        else:
            if bike_type == "Standard":
                bike = Bike(colour, pedal, brake, light, seat, gear, chain, wheel)
            elif bike_type == "Mountain Bike":
                bike = MountainBike(colour, pedal, brake, light, seat, gear, chain, wheel)
            elif bike_type == "Road Bike":
                bike = RoadBike(colour, pedal, brake, light, seat, gear, chain, wheel)
            elif bike_type == "Track Bike":
                bike = TrackBike(colour, pedal, brake, light, seat, gear, chain, wheel)
            elif bike_type == "BMX":
                bike = BMXBike(colour, pedal, brake, light, seat, gear, chain, wheel)
            elif bike_type == "Kids":
                bike = KidsBike(colour, pedal, brake, light, seat, gear, chain, wheel)
            else:
                ValueError("This should not be possible but the bike type is wrong")

            if bike and customer:
                order = Order(customer, bike)
                orders[order.id] = order
                fork_Station_Order.append(order)
                updatedOrderTable(order)
                if len(fork_Station_Order) == 1:
                    setForkOrderInformation(True)
                window.NewOrder_ErrorMessage.setEnabled(True)
                window.NewOrder_ErrorMessage.setText("Your order has been completed.")

                # Reset all the boxes
                # Customer data
                window.NewOrder_NameLineEdit.setText("")
                window.NewOrder_EmailLineEdit.setText("")
                window.NewOrder_PhoneLineEdit.setText("")
                window.NewOrder_AddressLine1LineEdit.setText("")
                window.NewOrder_AddressLine2LineEdit.setText("")
                window.NewOrder_CityLineEdit.setText("")
                window.NewOrder_PostcodeLineEdit.setText("")

                # Bike data
                window.NewOrder_BikeTypeComboBox.setCurrentIndex(-1)
                window.NewOrder_ColourComboBox.setCurrentIndex(-1)
                window.NewOrder_PedalTypeComboBox.setCurrentIndex(-1)
                window.NewOrder_ChainTypeComboBox.setCurrentIndex(-1)
                window.NewOrder_GearTypeComboBox.setCurrentIndex(-1)
                window.NewOrder_WheelTypeComboBox.setCurrentIndex(-1)
                window.NewOrder_BrakeTypeComboBox.setCurrentIndex(-1)
                window.NewOrder_LightTypeComboBox.setCurrentIndex(-1)
                window.NewOrder_SeatTypeComboBox.setCurrentIndex(-1)

    def orderBox():
        bike_type = window.NewOrder_BikeTypeComboBox.currentText()

        window.NewOrder_ColourComboBox.setEnabled(True)
        window.NewOrder_PedalTypeComboBox.setEnabled(True)
        window.NewOrder_ChainTypeComboBox.setEnabled(True)
        window.NewOrder_GearTypeComboBox.setEnabled(True)
        window.NewOrder_WheelTypeComboBox.setEnabled(True)
        window.NewOrder_BrakeTypeComboBox.setEnabled(True)
        window.NewOrder_LightTypeComboBox.setEnabled(True)
        window.NewOrder_SeatTypeComboBox.setEnabled(True)

        if bike_type == "Standard":
            # Colours
            window.NewOrder_ColourComboBox.model().item(0).setEnabled(True) # Black
            window.NewOrder_ColourComboBox.model().item(1).setEnabled(True) # Blue
            window.NewOrder_ColourComboBox.model().item(2).setEnabled(True) # Green
            window.NewOrder_ColourComboBox.model().item(3).setEnabled(True) # Grey
            window.NewOrder_ColourComboBox.model().item(4).setEnabled(True) # Orange
            window.NewOrder_ColourComboBox.model().item(5).setEnabled(True) # Pink
            window.NewOrder_ColourComboBox.model().item(6).setEnabled(True) # Purple
            window.NewOrder_ColourComboBox.model().item(7).setEnabled(True) # Red
            window.NewOrder_ColourComboBox.model().item(8).setEnabled(True) # Yellow
            window.NewOrder_ColourComboBox.model().item(9).setEnabled(True) # White

            #Pedals
            window.NewOrder_PedalTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_PedalTypeComboBox.model().item(1).setEnabled(True) # Premium
            window.NewOrder_PedalTypeComboBox.model().item(2).setEnabled(False) # Carbon Fibre
            window.NewOrder_PedalTypeComboBox.model().item(3).setEnabled(False) # Kids

            #Chain
            window.NewOrder_ChainTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_ChainTypeComboBox.model().item(1).setEnabled(True) # Premium
            window.NewOrder_ChainTypeComboBox.model().item(2).setEnabled(False) # Track

            #Gears
            window.NewOrder_GearTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_GearTypeComboBox.model().item(1).setEnabled(True) # Low
            window.NewOrder_GearTypeComboBox.model().item(2).setEnabled(True) # High
            window.NewOrder_GearTypeComboBox.model().item(3).setEnabled(False) # Kids

            #Wheels
            window.NewOrder_WheelTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_WheelTypeComboBox.model().item(1).setEnabled(True) # Offroad
            window.NewOrder_WheelTypeComboBox.model().item(2).setEnabled(True) # Road
            window.NewOrder_WheelTypeComboBox.model().item(3).setEnabled(False) # Carbon Fibre
            window.NewOrder_WheelTypeComboBox.model().item(4).setEnabled(False) # Kids

            #Brakes
            window.NewOrder_BrakeTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_BrakeTypeComboBox.model().item(1).setEnabled(True) # Premium Disc
            window.NewOrder_BrakeTypeComboBox.model().item(2).setEnabled(True) # None

            #Lights
            window.NewOrder_LightTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_LightTypeComboBox.model().item(1).setEnabled(True) # Premium LEDs
            window.NewOrder_LightTypeComboBox.model().item(2).setEnabled(True) # None

            #Seat
            window.NewOrder_SeatTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_SeatTypeComboBox.model().item(1).setEnabled(True) # Premium Gel
            window.NewOrder_SeatTypeComboBox.model().item(2).setEnabled(False) # Carbon Fibre
            
            #Setting Parts to standard by default
            window.NewOrder_PedalTypeComboBox.setCurrentIndex(0)
            window.NewOrder_ChainTypeComboBox.setCurrentIndex(0)
            window.NewOrder_GearTypeComboBox.setCurrentIndex(0)
            window.NewOrder_WheelTypeComboBox.setCurrentIndex(0)
            window.NewOrder_BrakeTypeComboBox.setCurrentIndex(0)
            window.NewOrder_LightTypeComboBox.setCurrentIndex(0)
            window.NewOrder_SeatTypeComboBox.setCurrentIndex(0)

        elif bike_type == "Mountain Bike":
            # Colours
            window.NewOrder_ColourComboBox.model().item(0).setEnabled(True) # Black
            window.NewOrder_ColourComboBox.model().item(1).setEnabled(True) # Blue
            window.NewOrder_ColourComboBox.model().item(2).setEnabled(True) # Green
            window.NewOrder_ColourComboBox.model().item(3).setEnabled(True) # Grey
            window.NewOrder_ColourComboBox.model().item(4).setEnabled(True) # Orange
            window.NewOrder_ColourComboBox.model().item(5).setEnabled(True) # Pink
            window.NewOrder_ColourComboBox.model().item(6).setEnabled(True) # Purple
            window.NewOrder_ColourComboBox.model().item(7).setEnabled(True) # Red
            window.NewOrder_ColourComboBox.model().item(8).setEnabled(True) # Yellow
            window.NewOrder_ColourComboBox.model().item(9).setEnabled(True) # White

            #Pedals
            window.NewOrder_PedalTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_PedalTypeComboBox.model().item(1).setEnabled(True) # Premium
            window.NewOrder_PedalTypeComboBox.model().item(2).setEnabled(False) # Carbon Fibre
            window.NewOrder_PedalTypeComboBox.model().item(3).setEnabled(False) # Kids

            #Chain
            window.NewOrder_ChainTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_ChainTypeComboBox.model().item(1).setEnabled(True) # Premium
            window.NewOrder_ChainTypeComboBox.model().item(2).setEnabled(False) # Track

            #Gears
            window.NewOrder_GearTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_GearTypeComboBox.model().item(1).setEnabled(True) # Low
            window.NewOrder_GearTypeComboBox.model().item(2).setEnabled(False) # High
            window.NewOrder_GearTypeComboBox.model().item(3).setEnabled(False) # Kids

            #Wheels
            window.NewOrder_WheelTypeComboBox.model().item(0).setEnabled(False) # Standard
            window.NewOrder_WheelTypeComboBox.model().item(1).setEnabled(True) # Offroad
            window.NewOrder_WheelTypeComboBox.model().item(2).setEnabled(False) # Road
            window.NewOrder_WheelTypeComboBox.model().item(3).setEnabled(False) # Carbon Fibre
            window.NewOrder_WheelTypeComboBox.model().item(4).setEnabled(False) # Kids

            #Brakes
            window.NewOrder_BrakeTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_BrakeTypeComboBox.model().item(1).setEnabled(True) # Premium Disc
            window.NewOrder_BrakeTypeComboBox.model().item(2).setEnabled(False) # None

            #Lights
            window.NewOrder_LightTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_LightTypeComboBox.model().item(1).setEnabled(True) # Premium LEDs
            window.NewOrder_LightTypeComboBox.model().item(2).setEnabled(False) # None

            #Seat
            window.NewOrder_SeatTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_SeatTypeComboBox.model().item(1).setEnabled(True) # Premium Gel
            window.NewOrder_SeatTypeComboBox.model().item(2).setEnabled(False) # Carbon Fibre
            
            #Setting Parts to standard by default
            window.NewOrder_PedalTypeComboBox.setCurrentIndex(0)
            window.NewOrder_ChainTypeComboBox.setCurrentIndex(0)
            window.NewOrder_GearTypeComboBox.setCurrentIndex(1)
            window.NewOrder_WheelTypeComboBox.setCurrentIndex(1)
            window.NewOrder_BrakeTypeComboBox.setCurrentIndex(0)
            window.NewOrder_LightTypeComboBox.setCurrentIndex(0)
            window.NewOrder_SeatTypeComboBox.setCurrentIndex(0)

            #Disabling Fixed Boxes
            window.NewOrder_WheelTypeComboBox.setEnabled(False)

        elif bike_type == "Road Bike":
            # Colours
            window.NewOrder_ColourComboBox.model().item(0).setEnabled(True) # Black
            window.NewOrder_ColourComboBox.model().item(1).setEnabled(True) # Blue
            window.NewOrder_ColourComboBox.model().item(2).setEnabled(True) # Green
            window.NewOrder_ColourComboBox.model().item(3).setEnabled(True) # Grey
            window.NewOrder_ColourComboBox.model().item(4).setEnabled(True) # Orange
            window.NewOrder_ColourComboBox.model().item(5).setEnabled(True) # Pink
            window.NewOrder_ColourComboBox.model().item(6).setEnabled(True) # Purple
            window.NewOrder_ColourComboBox.model().item(7).setEnabled(True) # Red
            window.NewOrder_ColourComboBox.model().item(8).setEnabled(True) # Yellow
            window.NewOrder_ColourComboBox.model().item(9).setEnabled(True) # White

            #Pedals
            window.NewOrder_PedalTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_PedalTypeComboBox.model().item(1).setEnabled(True) # Premium
            window.NewOrder_PedalTypeComboBox.model().item(2).setEnabled(False) # Carbon Fibre
            window.NewOrder_PedalTypeComboBox.model().item(3).setEnabled(False) # Kids

            #Chain
            window.NewOrder_ChainTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_ChainTypeComboBox.model().item(1).setEnabled(True) # Premium
            window.NewOrder_ChainTypeComboBox.model().item(2).setEnabled(False) # Track

            #Gears
            window.NewOrder_GearTypeComboBox.model().item(0).setEnabled(False) # Standard
            window.NewOrder_GearTypeComboBox.model().item(1).setEnabled(False) # Low
            window.NewOrder_GearTypeComboBox.model().item(2).setEnabled(True) # High
            window.NewOrder_GearTypeComboBox.model().item(3).setEnabled(False) # Kids

            #Wheels
            window.NewOrder_WheelTypeComboBox.model().item(0).setEnabled(False) # Standard
            window.NewOrder_WheelTypeComboBox.model().item(1).setEnabled(False) # Offroad
            window.NewOrder_WheelTypeComboBox.model().item(2).setEnabled(True) # Road
            window.NewOrder_WheelTypeComboBox.model().item(3).setEnabled(False) # Carbon Fibre
            window.NewOrder_WheelTypeComboBox.model().item(4).setEnabled(False) # Kids

            #Brakes
            window.NewOrder_BrakeTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_BrakeTypeComboBox.model().item(1).setEnabled(True) # Premium Disc
            window.NewOrder_BrakeTypeComboBox.model().item(2).setEnabled(False) # None

            #Lights
            window.NewOrder_LightTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_LightTypeComboBox.model().item(1).setEnabled(True) # Premium LEDs
            window.NewOrder_LightTypeComboBox.model().item(2).setEnabled(False) # None

            #Seat
            window.NewOrder_SeatTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_SeatTypeComboBox.model().item(1).setEnabled(True) # Premium Gel
            window.NewOrder_SeatTypeComboBox.model().item(2).setEnabled(False) # Carbon Fibre
            
            #Setting Parts to standard by default
            window.NewOrder_PedalTypeComboBox.setCurrentIndex(0)
            window.NewOrder_ChainTypeComboBox.setCurrentIndex(0)
            window.NewOrder_GearTypeComboBox.setCurrentIndex(2)
            window.NewOrder_WheelTypeComboBox.setCurrentIndex(2)
            window.NewOrder_BrakeTypeComboBox.setCurrentIndex(0)
            window.NewOrder_LightTypeComboBox.setCurrentIndex(0)
            window.NewOrder_SeatTypeComboBox.setCurrentIndex(0)

            #Disabling Fixed Boxes
            window.NewOrder_GearTypeComboBox.setEnabled(False)
            window.NewOrder_WheelTypeComboBox.setEnabled(False)

        elif bike_type == "Track Bike":
            # Colours
            window.NewOrder_ColourComboBox.model().item(0).setEnabled(True) # Black
            window.NewOrder_ColourComboBox.model().item(1).setEnabled(True) # Blue
            window.NewOrder_ColourComboBox.model().item(2).setEnabled(True) # Green
            window.NewOrder_ColourComboBox.model().item(3).setEnabled(True) # Grey
            window.NewOrder_ColourComboBox.model().item(4).setEnabled(True) # Orange
            window.NewOrder_ColourComboBox.model().item(5).setEnabled(True) # Pink
            window.NewOrder_ColourComboBox.model().item(6).setEnabled(True) # Purple
            window.NewOrder_ColourComboBox.model().item(7).setEnabled(True) # Red
            window.NewOrder_ColourComboBox.model().item(8).setEnabled(True) # Yellow
            window.NewOrder_ColourComboBox.model().item(9).setEnabled(True) # White

            #Pedals
            window.NewOrder_PedalTypeComboBox.model().item(0).setEnabled(False) # Standard
            window.NewOrder_PedalTypeComboBox.model().item(1).setEnabled(False) # Premium
            window.NewOrder_PedalTypeComboBox.model().item(2).setEnabled(True) # Carbon Fibre
            window.NewOrder_PedalTypeComboBox.model().item(3).setEnabled(False) # Kids

            #Chain
            window.NewOrder_ChainTypeComboBox.model().item(0).setEnabled(False) # Standard
            window.NewOrder_ChainTypeComboBox.model().item(1).setEnabled(False) # Premium
            window.NewOrder_ChainTypeComboBox.model().item(2).setEnabled(True) # Track

            #Gears
            window.NewOrder_GearTypeComboBox.model().item(0).setEnabled(False) # Standard
            window.NewOrder_GearTypeComboBox.model().item(1).setEnabled(False) # Low
            window.NewOrder_GearTypeComboBox.model().item(2).setEnabled(True) # High
            window.NewOrder_GearTypeComboBox.model().item(3).setEnabled(False) # Kids

            #Wheels
            window.NewOrder_WheelTypeComboBox.model().item(0).setEnabled(False) # Standard
            window.NewOrder_WheelTypeComboBox.model().item(1).setEnabled(False) # Offroad
            window.NewOrder_WheelTypeComboBox.model().item(2).setEnabled(False) # Road
            window.NewOrder_WheelTypeComboBox.model().item(3).setEnabled(True) # Carbon Fibre
            window.NewOrder_WheelTypeComboBox.model().item(4).setEnabled(False) # Kids

            #Brakes
            window.NewOrder_BrakeTypeComboBox.model().item(0).setEnabled(False) # Standard
            window.NewOrder_BrakeTypeComboBox.model().item(1).setEnabled(False) # Premium Disc
            window.NewOrder_BrakeTypeComboBox.model().item(2).setEnabled(True) # None

            #Lights
            window.NewOrder_LightTypeComboBox.model().item(0).setEnabled(False) # Standard
            window.NewOrder_LightTypeComboBox.model().item(1).setEnabled(False) # Premium LEDs
            window.NewOrder_LightTypeComboBox.model().item(2).setEnabled(True) # None

            #Seat
            window.NewOrder_SeatTypeComboBox.model().item(0).setEnabled(False) # Standard
            window.NewOrder_SeatTypeComboBox.model().item(1).setEnabled(False) # Premium Gel
            window.NewOrder_SeatTypeComboBox.model().item(2).setEnabled(True) # Carbon Fibre
            
            #Setting Parts to standard by default
            window.NewOrder_PedalTypeComboBox.setCurrentIndex(2)
            window.NewOrder_ChainTypeComboBox.setCurrentIndex(2)
            window.NewOrder_GearTypeComboBox.setCurrentIndex(2)
            window.NewOrder_WheelTypeComboBox.setCurrentIndex(3)
            window.NewOrder_BrakeTypeComboBox.setCurrentIndex(2)
            window.NewOrder_LightTypeComboBox.setCurrentIndex(2)
            window.NewOrder_SeatTypeComboBox.setCurrentIndex(2)

            #Disabling Fixed Boxes
            window.NewOrder_PedalTypeComboBox.setEnabled(False)
            window.NewOrder_ChainTypeComboBox.setEnabled(False)
            window.NewOrder_GearTypeComboBox.setEnabled(False)
            window.NewOrder_WheelTypeComboBox.setEnabled(False)
            window.NewOrder_BrakeTypeComboBox.setEnabled(False)
            window.NewOrder_LightTypeComboBox.setEnabled(False)
            window.NewOrder_SeatTypeComboBox.setEnabled(False)

        elif bike_type == "BMX":
            # Colours
            window.NewOrder_ColourComboBox.model().item(0).setEnabled(True) # Black
            window.NewOrder_ColourComboBox.model().item(1).setEnabled(True) # Blue
            window.NewOrder_ColourComboBox.model().item(2).setEnabled(True) # Green
            window.NewOrder_ColourComboBox.model().item(3).setEnabled(True) # Grey
            window.NewOrder_ColourComboBox.model().item(4).setEnabled(True) # Orange
            window.NewOrder_ColourComboBox.model().item(5).setEnabled(True) # Pink
            window.NewOrder_ColourComboBox.model().item(6).setEnabled(True) # Purple
            window.NewOrder_ColourComboBox.model().item(7).setEnabled(True) # Red
            window.NewOrder_ColourComboBox.model().item(8).setEnabled(True) # Yellow
            window.NewOrder_ColourComboBox.model().item(9).setEnabled(True) # White

            #Pedals
            window.NewOrder_PedalTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_PedalTypeComboBox.model().item(1).setEnabled(True) # Premium
            window.NewOrder_PedalTypeComboBox.model().item(2).setEnabled(False) # Carbon Fibre
            window.NewOrder_PedalTypeComboBox.model().item(3).setEnabled(False) # Kids

            #Chain
            window.NewOrder_ChainTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_ChainTypeComboBox.model().item(1).setEnabled(True) # Premium
            window.NewOrder_ChainTypeComboBox.model().item(2).setEnabled(False) # Track

            #Gears
            window.NewOrder_GearTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_GearTypeComboBox.model().item(1).setEnabled(False) # Low
            window.NewOrder_GearTypeComboBox.model().item(2).setEnabled(False) # High
            window.NewOrder_GearTypeComboBox.model().item(3).setEnabled(False) # Kids

            #Wheels
            window.NewOrder_WheelTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_WheelTypeComboBox.model().item(1).setEnabled(True) # Offroad
            window.NewOrder_WheelTypeComboBox.model().item(2).setEnabled(False) # Road
            window.NewOrder_WheelTypeComboBox.model().item(3).setEnabled(False) # Carbon Fibre
            window.NewOrder_WheelTypeComboBox.model().item(4).setEnabled(False) # Kids

            #Brakes
            window.NewOrder_BrakeTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_BrakeTypeComboBox.model().item(1).setEnabled(True) # Premium Disc
            window.NewOrder_BrakeTypeComboBox.model().item(2).setEnabled(False) # None

            #Lights
            window.NewOrder_LightTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_LightTypeComboBox.model().item(1).setEnabled(True) # Premium LEDs
            window.NewOrder_LightTypeComboBox.model().item(2).setEnabled(True) # None

            #Seat
            window.NewOrder_SeatTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_SeatTypeComboBox.model().item(1).setEnabled(True) # Premium Gel
            window.NewOrder_SeatTypeComboBox.model().item(2).setEnabled(False) # Carbon Fibre
            
            #Setting Parts to standard by default
            window.NewOrder_PedalTypeComboBox.setCurrentIndex(0)
            window.NewOrder_ChainTypeComboBox.setCurrentIndex(0)
            window.NewOrder_GearTypeComboBox.setCurrentIndex(0)
            window.NewOrder_WheelTypeComboBox.setCurrentIndex(0)
            window.NewOrder_BrakeTypeComboBox.setCurrentIndex(0)
            window.NewOrder_LightTypeComboBox.setCurrentIndex(2)
            window.NewOrder_SeatTypeComboBox.setCurrentIndex(0)

            #Disabling Fixed Boxes
            window.NewOrder_GearTypeComboBox.setEnabled(False)

        elif bike_type == "Kids":
            # Colours
            window.NewOrder_ColourComboBox.model().item(0).setEnabled(True) # Black
            window.NewOrder_ColourComboBox.model().item(1).setEnabled(True) # Blue
            window.NewOrder_ColourComboBox.model().item(2).setEnabled(True) # Green
            window.NewOrder_ColourComboBox.model().item(3).setEnabled(True) # Grey
            window.NewOrder_ColourComboBox.model().item(4).setEnabled(True) # Orange
            window.NewOrder_ColourComboBox.model().item(5).setEnabled(True) # Pink
            window.NewOrder_ColourComboBox.model().item(6).setEnabled(True) # Purple
            window.NewOrder_ColourComboBox.model().item(7).setEnabled(True) # Red
            window.NewOrder_ColourComboBox.model().item(8).setEnabled(True) # Yellow
            window.NewOrder_ColourComboBox.model().item(9).setEnabled(True) # White

            #Pedals
            window.NewOrder_PedalTypeComboBox.model().item(0).setEnabled(False) # Standard
            window.NewOrder_PedalTypeComboBox.model().item(1).setEnabled(False) # Premium
            window.NewOrder_PedalTypeComboBox.model().item(2).setEnabled(False) # Carbon Fibre
            window.NewOrder_PedalTypeComboBox.model().item(3).setEnabled(True) # Kids

            #Chain
            window.NewOrder_ChainTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_ChainTypeComboBox.model().item(1).setEnabled(True) # Premium
            window.NewOrder_ChainTypeComboBox.model().item(2).setEnabled(False) # Track

            #Gears
            window.NewOrder_GearTypeComboBox.model().item(0).setEnabled(False) # Standard
            window.NewOrder_GearTypeComboBox.model().item(1).setEnabled(False) # Low
            window.NewOrder_GearTypeComboBox.model().item(2).setEnabled(False) # High
            window.NewOrder_GearTypeComboBox.model().item(3).setEnabled(True) # Kids

            #Wheels
            window.NewOrder_WheelTypeComboBox.model().item(0).setEnabled(False) # Standard
            window.NewOrder_WheelTypeComboBox.model().item(1).setEnabled(False) # Offroad
            window.NewOrder_WheelTypeComboBox.model().item(2).setEnabled(False) # Road
            window.NewOrder_WheelTypeComboBox.model().item(3).setEnabled(False) # Carbon Fibre
            window.NewOrder_WheelTypeComboBox.model().item(4).setEnabled(True) # Kids

            #Brakes
            window.NewOrder_BrakeTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_BrakeTypeComboBox.model().item(1).setEnabled(True) # Premium Disc
            window.NewOrder_BrakeTypeComboBox.model().item(2).setEnabled(False) # None

            #Lights
            window.NewOrder_LightTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_LightTypeComboBox.model().item(1).setEnabled(True) # Premium LEDs
            window.NewOrder_LightTypeComboBox.model().item(2).setEnabled(False) # None

            #Seat
            window.NewOrder_SeatTypeComboBox.model().item(0).setEnabled(True) # Standard
            window.NewOrder_SeatTypeComboBox.model().item(1).setEnabled(True) # Premium Gel
            window.NewOrder_SeatTypeComboBox.model().item(2).setEnabled(False) # Carbon Fibre
            
            #Setting Parts to standard by default
            window.NewOrder_PedalTypeComboBox.setCurrentIndex(3)
            window.NewOrder_ChainTypeComboBox.setCurrentIndex(0)
            window.NewOrder_GearTypeComboBox.setCurrentIndex(3)
            window.NewOrder_WheelTypeComboBox.setCurrentIndex(4)
            window.NewOrder_BrakeTypeComboBox.setCurrentIndex(0)
            window.NewOrder_LightTypeComboBox.setCurrentIndex(0)
            window.NewOrder_SeatTypeComboBox.setCurrentIndex(0)

            #Disabling Fixed Boxes
            window.NewOrder_PedalTypeComboBox.setEnabled(False)
            window.NewOrder_GearTypeComboBox.setEnabled(False)
            window.NewOrder_WheelTypeComboBox.setEnabled(False)

#Station System Plan

# Station Button Pressed
    # Check if there is one or more orders
        # Check if first order is being displayed
            # Check if there is enough inventory to make it
                # Remove from inventory required amount
                # Add Order to Next station list
                # Remove order from this station list
                # UpdateStationOrderInformation()
                # UpdateRequiredAmounts() to 0
            # Else
                # Disable Button
        # Else
            # display first order of list
            # UpdateRequiredAmounts() to required amounts
    # Else:
        # Display defualt values

# When Inventory increases or decreases check the station order
# If the station order required amount > inventory
    # disable button
# if station order required amount <= inventory
    # enable button

# Fork Station Functions

    def forkAssembled():
        global fork_Station_Order
        if len(fork_Station_Order) > 0:

            if fork_Station_Order[0].id == int(window.ForkStation_OrderNumber_Value.text()):
                if fork_Station_Order[0].bike_order.fork == "Tubular Steel" and window.ForkStationTubularSteelRequiredCount.value() <= inventory["Steel"][0].value():
                    if type(fork_Station_Order[0].bike_order)== Bike:
                        InventoryChange("Steel", - window.ForkStationTubularSteelRequiredCount.value())
                        InventoryChange("Standard Forks", + 1)
                    elif type(fork_Station_Order[0].bike_order)== MountainBike:
                        InventoryChange("Steel", - window.ForkStationTubularSteelRequiredCount.value())
                        InventoryChange("Mountain Forks", + 1)
                    elif type(fork_Station_Order[0].bike_order)== BMXBike:
                        InventoryChange("Steel", - window.ForkStationTubularSteelRequiredCount.value())
                        InventoryChange("BMX Forks", + 1)
                    elif type(fork_Station_Order[0].bike_order)== KidsBike:
                        InventoryChange("Steel", - window.ForkStationTubularSteelRequiredCount.value())
                        InventoryChange("Kids Forks", + 1)
                    else:
                        TypeError("fork_Station_Order[0].bike_order type is not a Bike type")
                    ForkOrderToFrameOrder()

                elif fork_Station_Order[0].bike_order.fork == "Tubular Aluminium" and window.ForkStationTubularAluminiumRequiredCount.value() <= inventory["Aluminium"][0].value():
                    # Take away required amount
                    InventoryChange("Aluminium", - window.ForkStationTubularAluminiumRequiredCount.value())
                    # Add the new part to inventory
                    InventoryChange("Road Forks", + 1)
                    ForkOrderToFrameOrder()

                elif fork_Station_Order[0].bike_order.fork == "Carbon Fibre" and window.ForkStationCarbonRequiredCount.value() <= inventory["Carbon Fibre"][0].value():
                     # Take away required amount
                    InventoryChange("Carbon Fibre", - window.ForkStationCarbonRequiredCount.value())
                    # Add the new part to inventory
                    InventoryChange("Track Forks", + 1)
                    ForkOrderToFrameOrder()

                else:
                    # Disable Button
                    window.ForkWeldedButton.setEnabled(False)
            else:
                # Display the first order
                setForkOrderInformation(True)
        else:
            # Default Values
            setForkOrderInformation(False)

    def ForkOrderToFrameOrder():
        global fork_Station_Order, frame_Station_Order

        if len(fork_Station_Order) > 0:
            if len(fork_Station_Order) == 1:
                # No order after current one

                # Add Order to Next station list
                frame_Station_Order.append(fork_Station_Order[0])
                # Get Next station to update order information
                setFrameOrderInformation(True)
                # Remove order from this station list
                fork_Station_Order.pop(0)
                # Set order information to default
                setForkOrderInformation(False)

            else:
                # Add Order to Next station list
                frame_Station_Order.append(fork_Station_Order[0])
                # Get Next station to update order information
                setFrameOrderInformation(True)
                # Remove order from this station list
                fork_Station_Order.pop(0)
                # UpdateStationOrderInformation()
                setForkOrderInformation(True)
        else:
            ValueError("fork_station_order has no elements (orders) but is somehow triggered to update to the next order")

    def setForkOrderInformation(next_order: bool):
        """
        Sets the fork station order information box with the correct order information whether an order exists or not.
        Also updates the required amounts of materials for the order.
        """
        if next_order:
            # Set new order information
            order = fork_Station_Order[0]
            window.ForkStation_OrderNumber_Value.setText(str(order.id))
            window.ForkStation_BikeType_Value.setText(str(order.bike_order.bike_type))
            window.ForkStation_Colour_Value.setText(str(order.bike_order.colour))
            window.ForkStation_Pedal_Value.setText(str(order.bike_order.pedals))
            window.ForkStation_Chain_Value.setText(str(order.bike_order.chain))
            window.ForkStation_Gear_Value.setText(str(order.bike_order.gears))
            window.ForkStation_Wheel_Value.setText(str(order.bike_order.wheels))
            window.ForkStation_Brakes_Value.setText(str(order.bike_order.brakes))
            window.ForkStation_Lights_Value.setText(str(order.bike_order.lights))
            window.ForkStation_Seat_Value.setText(str(order.bike_order.seat))
            window.ForkStationForkValue.setText(str(order.bike_order.fork))

            # Set Required amounts for new order
            if order.bike_order.frame == "Tubular Steel":
                window.ForkStationTubularSteelRequiredCount.display(order.bike_order.frame_count)
                window.ForkStationTubularAluminiumRequiredCount.display(0)
                window.ForkStationCarbonRequiredCount.display(0)
                if window.ForkStationTubularSteelRequiredCount.value() > inventory["Steel"][0].value():
                    # Set button to disabled
                    window.ForkWeldedButton.setEnabled(False)
                else:
                    window.ForkWeldedButton.setEnabled(True)
                    
            elif order.bike_order.frame == "Tubular Aluminium":
                window.ForkStationTubularSteelRequiredCount.display(0)
                window.ForkStationTubularAluminiumRequiredCount.display(order.bike_order.frame_count)
                window.ForkStationCarbonRequiredCount.display(0)
                if window.ForkStationTubularAluminiumRequiredCount.value() > inventory["Aluminium"][0].value():
                    # Set button to disabled
                    window.ForkWeldedButton.setEnabled(False)
                else:
                    window.ForkWeldedButton.setEnabled(True)

            elif order.bike_order.frame == "Carbon Fibre":
                window.ForkStationTubularSteelRequiredCount.display(0)
                window.ForkStationTubularAluminiumRequiredCount.display(0)
                window.ForkStationCarbonRequiredCount.display(order.bike_order.frame_count)
                if window.ForkStationCarbonRequiredCount.value() > inventory["Carbon Fibre"][0].value():
                    # Set button to disabled
                    window.ForkWeldedButton.setEnabled(False)
                else:
                    window.ForkWeldedButton.setEnabled(True)
            else:
                ValueError("This shouldn't be possible but the frame material in a bike class is wrong")
        else:
            window.ForkStation_OrderNumber_Value.setText("[Order ID]")
            window.ForkStation_BikeType_Value.setText("[Bike Type]")
            window.ForkStation_Colour_Value.setText("[Colour]")
            window.ForkStation_Pedal_Value.setText("[Pedal Type]")
            window.ForkStation_Chain_Value.setText("[Chain Type]")
            window.ForkStation_Gear_Value.setText("[Gear Type]")
            window.ForkStation_Wheel_Value.setText("[Wheel Type]")
            window.ForkStation_Brakes_Value.setText("[Brake Type]")
            window.ForkStation_Lights_Value.setText("[Lights Type]")
            window.ForkStation_Seat_Value.setText("[Seat Type]")
            window.ForkStationForkValue.setText("[Fork Type]")
            window.ForkStationTubularSteelRequiredCount.display(0)
            window.ForkStationTubularAluminiumRequiredCount.display(0)
            window.ForkStationCarbonRequiredCount.display(0)
            window.ForkWeldedButton.setEnabled(False)

# Frame Station Functions

    def frameAssembled():
        global frame_Station_Order
        if len(frame_Station_Order) > 0:

            if frame_Station_Order[0].id == int(window.FrameStation_OrderNumber_Value.text()):
                if frame_Station_Order[0].bike_order.frame == "Tubular Steel" and window.FrameStationTubularSteelRequiredCount.value() <= inventory["Steel"][0].value():
                    if type(frame_Station_Order[0].bike_order)== Bike:
                        InventoryChange("Steel", - window.FrameStationTubularSteelRequiredCount.value())
                        InventoryChange("Standard Frames", + 1)
                    elif type(frame_Station_Order[0].bike_order)== MountainBike:
                        InventoryChange("Steel", - window.FrameStationTubularSteelRequiredCount.value())
                        InventoryChange("Mountain Frames", + 1)
                    elif type(frame_Station_Order[0].bike_order)== BMXBike:
                        InventoryChange("Steel", - window.FrameStationTubularSteelRequiredCount.value())
                        InventoryChange("BMX Frames", + 1)
                    elif type(frame_Station_Order[0].bike_order)== KidsBike:
                        InventoryChange("Steel", - window.FrameStationTubularSteelRequiredCount.value())
                        InventoryChange("Kids Frames", + 1)
                    else:
                        TypeError("fork_Station_Order[0].bike_order type is not a Bike type")

                    FrameOrderToChassisOrder()
                elif frame_Station_Order[0].bike_order.frame == "Tubular Aluminium" and window.FrameStationTubularAluminiumRequiredCount.value() <= inventory["Aluminium"][0].value():
                    # Take away required material
                    InventoryChange("Aluminium", - window.FrameStationTubularAluminiumRequiredCount.value())
                    # Add the new part to inventory
                    InventoryChange("Road Frames", + 1)
                    FrameOrderToChassisOrder()

                elif frame_Station_Order[0].bike_order.frame == "Carbon Fibre" and window.FrameStationCarbonRequiredCount.value() <= inventory["Carbon Fibre"][0].value():
                    # Take away required material
                    InventoryChange("Carbon Fibre", - window.FrameStationCarbonRequiredCount.value())
                    # Add the new part to inventory
                    InventoryChange("Track Frames", + 1)
                    FrameOrderToChassisOrder()

                else:
                    # Disable Button
                    window.FrameWeldedButton.setEnabled(False)
            else:
                # Display the first order
                setFrameOrderInformation(True)
        else:
            # Default Values
            setFrameOrderInformation(False)

    def FrameOrderToChassisOrder():
        global frame_Station_Order, chassis_Station_Order

        if len(frame_Station_Order) > 0:
            if len(frame_Station_Order) == 1:
                # No order after current one

                # Add Order to Next station list
                chassis_Station_Order.append(frame_Station_Order[0])
                # Get Next station to update order information
                setChassisOrderInformation(True)
                # Remove order from this station list
                frame_Station_Order.pop(0)
                # Set order information to default
                setFrameOrderInformation(False)

            else:
                # Add Order to Next station list
                chassis_Station_Order.append(frame_Station_Order[0])
                # Get Next station to update order information
                setChassisOrderInformation(True)
                # Remove order from this station list
                frame_Station_Order.pop(0)
                # UpdateStationOrderInformation()
                setFrameOrderInformation(True)
        else:
            ValueError("frame_station_order has no elements (orders) but is somehow triggered to update to the next order")

    def setFrameOrderInformation(next_order: bool):
        """
        Sets the frame station order information box with the correct order information whether an order exists or not.
        Also updates the required amounts of materials for the order.
        """
        if next_order:
            # Set new order information
            order = frame_Station_Order[0]
            window.FrameStation_OrderNumber_Value.setText(str(order.id))
            window.FrameStation_Bike_Value.setText(str(order.bike_order.bike_type))
            window.FrameStation_Colour_Value.setText(str(order.bike_order.colour))
            window.FrameStation_Pedal_Value.setText(str(order.bike_order.pedals))
            window.FrameStation_Chain_Value.setText(str(order.bike_order.chain))
            window.FrameStation_Gear_Value.setText(str(order.bike_order.gears))
            window.FrameStation_Wheel_Value.setText(str(order.bike_order.wheels))
            window.FrameStation_Brakes_Value.setText(str(order.bike_order.brakes))
            window.FrameStation_Lights_Value.setText(str(order.bike_order.lights))
            window.FrameStation_Seat_Value.setText(str(order.bike_order.seat))
            window.FrameStationFrameValue.setText(str(order.bike_order.frame))

            # Set Required amounts for new order
            if order.bike_order.frame == "Tubular Steel":
                window.FrameStationTubularSteelRequiredCount.display(order.bike_order.frame_count)
                window.FrameStationTubularAluminiumRequiredCount.display(0)
                window.FrameStationCarbonRequiredCount.display(0)
                if window.FrameStationTubularSteelRequiredCount.value() > inventory["Steel"][0].value():
                    # Set button to disabled
                    window.FrameWeldedButton.setEnabled(False)
                else:
                    window.FrameWeldedButton.setEnabled(True)
                    
            elif order.bike_order.frame == "Tubular Aluminium":
                window.FrameStationTubularSteelRequiredCount.display(0)
                window.FrameStationTubularAluminiumRequiredCount.display(order.bike_order.frame_count)
                window.FrameStationCarbonRequiredCount.display(0)
                if window.FrameStationTubularAluminiumRequiredCount.value() > inventory["Aluminium"][0].value():
                    # Set button to disabled
                    window.FrameWeldedButton.setEnabled(False)
                else:
                    window.FrameWeldedButton.setEnabled(True)

            elif order.bike_order.frame == "Carbon Fibre":
                window.FrameStationTubularSteelRequiredCount.display(0)
                window.FrameStationTubularAluminiumRequiredCount.display(0)
                window.FrameStationCarbonRequiredCount.display(order.bike_order.frame_count)
                if window.FrameStationCarbonRequiredCount.value() > inventory["Carbon Fibre"][0].value():
                    # Set button to disabled
                    window.FrameWeldedButton.setEnabled(False)
                else:
                    window.FrameWeldedButton.setEnabled(True)
            else:
                ValueError("This shouldn't be possible but the frame material in a bike class is wrong")
        else:
            window.FrameStation_OrderNumber_Value.setText("[Order ID]")
            window.FrameStation_Bike_Value.setText("[Bike Type]")
            window.FrameStation_Colour_Value.setText("[Colour]")
            window.FrameStation_Pedal_Value.setText("[Pedal Type]")
            window.FrameStation_Chain_Value.setText("[Chain Type]")
            window.FrameStation_Gear_Value.setText("[Gear Type]")
            window.FrameStation_Wheel_Value.setText("[Wheel Type]")
            window.FrameStation_Brakes_Value.setText("[Brake Type]")
            window.FrameStation_Lights_Value.setText("[Lights Type]")
            window.FrameStation_Seat_Value.setText("[Seat Type]")
            window.FrameStationTubularSteelRequiredCount.display(0)
            window.FrameStationTubularAluminiumRequiredCount.display(0)
            window.FrameStationCarbonRequiredCount.display(0)
            window.FrameWeldedButton.setEnabled(False)


# Chassis Station Functions

    def ChassisAssembled():
        global chassis_Station_Order
        if len(chassis_Station_Order) > 0:

            if chassis_Station_Order[0].id == int(window.ChassisStation_OrderNumber_Value.text()):
                if chassis_Station_Order[0].bike_order.fork == "Tubular Steel" and chassis_Station_Order[0].bike_order.frame == "Tubular Steel":

                    #Check the Bike type
                    if chassis_Station_Order[0].bike_order.bike_type == "Standard":
                        if window.ChassisStationInventoryStandardForksCount.value() > 0 and window.ChassisStationInventoryStandardFrameCount.value() > 0:
                            # Remove Inventory
                            InventoryChange("Standard Forks", - 1.0)
                            InventoryChange("Standard Frames", - 1.0)
                            # Add New Chassis To Inventory
                            InventoryChange("Standard Chassis", 1.0)
                        else:
                            ValueError("Somehow the button to assemble is enabled even without required amounts")
                    elif chassis_Station_Order[0].bike_order.bike_type == "Mountain Bike":
                        if window.ChassisStationInventoryMountainForksCount.value() > 0 and window.ChassisStationInventoryMountainFrameCount.value() > 0:
                            # Remove Inventory
                            InventoryChange("Mountain Forks", - 1.0)
                            InventoryChange("Mountain Frames", - 1.0)
                            # Add New Chassis To Inventory
                            InventoryChange("Mountain Chassis", 1.0)
                        else:
                            ValueError("Somehow the button to assemble is enabled even without required amounts")
                    elif chassis_Station_Order[0].bike_order.bike_type == "BMX":
                        if window.ChassisStationInventoryBMXForksCount.value() > 0 and window.ChassisStationInventoryBMXFrameCount.value() > 0:
                            # Remove Inventory
                            InventoryChange("BMX Forks", - 1.0)
                            InventoryChange("BMX Frames", - 1.0)
                            # Add New Chassis To Inventory
                            InventoryChange("BMX Chassis", 1.0)
                        else:
                            ValueError("Somehow the button to assemble is enabled even without required amounts")
                    elif chassis_Station_Order[0].bike_order.bike_type == "Kids":
                        if window.ChassisStationInventoryKidsForksCount.value() > 0 and window.ChassisStationInventoryKidsFrameCount.value() > 0:
                            # Remove Inventory
                            InventoryChange("Kids Forks", - 1.0)
                            InventoryChange("Kids Frames", - 1.0)
                            # Add New Chassis To Inventory
                            InventoryChange("Kids Chassis", 1.0)
                        else:
                            ValueError("Somehow the button to assemble is enabled even without required amounts")
                    else:
                        TypeError("The bike type for the order is wrong for the matieral being used. Should not be possible.")

                    # Move the order to next station
                    ChassisOrderToPaintOrder()

                elif chassis_Station_Order[0].bike_order.fork == "Tubular Aluminium" and window.ChassisStationInventoryAluminiumForksCount.value() >= 1 and chassis_Station_Order[0].bike_order.frame == "Tubular Aluminium" and window.ChassisStationInventoryAluminiumFrameCount.value() >= 1:
                    # Remove Inventory
                    InventoryChange("Road Forks", - 1.0)
                    InventoryChange("Road Frames", - 1.0)
                    #Check the Bike type
                    if chassis_Station_Order[0].bike_order.bike_type == "Road Bike":
                        # Add New Chassis To Inventory
                        InventoryChange("Road Chassis", 1.0)

                    # Move the order to next station
                    ChassisOrderToPaintOrder()
                
                elif chassis_Station_Order[0].bike_order.fork == "Carbon Fibre" and window.ChassisStationInventoryCarbonForksCount.value() >= 1 and chassis_Station_Order[0].bike_order.frame == "Carbon Fibre" and window.ChassisStationInventoryCarbonFrameCount.value() >= 1:
                    # Remove Inventory
                    InventoryChange("Track Forks", - 1.0)
                    InventoryChange("Track Frames", - 1.0)
                    if chassis_Station_Order[0].bike_order.bike_type == "Track Bike":
                        # Add New Chassis To Inventory
                        InventoryChange("Track Chassis", 1.0)

                    ChassisOrderToPaintOrder()

                else:
                    # Disable Button
                    window.ChassisAssemblyButton.setEnabled(False)
            else:
                # Display the first order
                setChassisOrderInformation(True)
        else:
            # Default Values
            setChassisOrderInformation(False)

    def ChassisOrderToPaintOrder():
        global chassis_Station_Order, paint_Station_Order

        if len(chassis_Station_Order) > 0:
            if len(chassis_Station_Order) == 1:
                # No order after current one

                # Add Order to Next station list
                paint_Station_Order.append(chassis_Station_Order[0])
                # Get Next station to update order information
                setPaintOrderInformation(True)
                # Remove order from this station list
                chassis_Station_Order.pop(0)
                # Set order information to default
                setChassisOrderInformation(False)

            else:
                # Add Order to Next station list
                paint_Station_Order.append(chassis_Station_Order[0])
                # Get Next station to update order information
                setPaintOrderInformation(True)
                # Remove order from this station list
                chassis_Station_Order.pop(0)
                # UpdateStationOrderInformation()
                setChassisOrderInformation(True)
        else:
            ValueError("fork_station_order has no elements (orders) but is somehow triggered to update to the next order")

    def setChassisOrderInformation(next_order: bool):
        """
        Sets the Chassis station order information box with the correct order information whether an order exists or not.
        Also updates the required amounts of materials for the order.
        """
        if next_order:
            # Set new order information
            order = chassis_Station_Order[0]
            window.ChassisStation_OrderNumber_Value.setText(str(order.id))
            window.ChassisStation_BikeType_Value.setText(str(order.bike_order.bike_type))
            window.ChassisStation_Colour_Value.setText(str(order.bike_order.colour))
            window.ChassisStation_Pedal_Value.setText(str(order.bike_order.pedals))
            window.ChassisStation_Chain_Value.setText(str(order.bike_order.chain))
            window.ChassisStation_Gear_Value.setText(str(order.bike_order.gears))
            window.ChassisStation_Wheel_Value.setText(str(order.bike_order.wheels))
            window.ChassisStation_Brakes_Value.setText(str(order.bike_order.brakes))
            window.ChassisStation_Lights_Value.setText(str(order.bike_order.lights))
            window.ChassisStation_Seat_Value.setText(str(order.bike_order.seat))

            if chassis_Station_Order[0].bike_order.bike_type == "Standard" or chassis_Station_Order[0].bike_order.bike_type == "Mountain Bike" or chassis_Station_Order[0].bike_order.bike_type == "BMX" or chassis_Station_Order[0].bike_order.bike_type == "Kids":
                window.ChassisAssemblyChassisType.setText(str(chassis_Station_Order[0].bike_order.bike_type))
                window.ChassisAssemblyForkType.setText(str("Steel"))
                window.ChassisAssemblyFrameType.setText(str("Steel"))

            elif chassis_Station_Order[0].bike_order.bike_type == "Road Bike":
                window.ChassisAssemblyChassisType.setText(str(chassis_Station_Order[0].bike_order.bike_type))
                window.ChassisAssemblyForkType.setText(str("Aluminium"))
                window.ChassisAssemblyFrameType.setText(str("Aluminium"))

            elif chassis_Station_Order[0].bike_order.bike_type == "Track Bike":
                window.ChassisAssemblyChassisType.setText(str(chassis_Station_Order[0].bike_order.bike_type))
                window.ChassisAssemblyForkType.setText(str("Carbon Fibre"))
                window.ChassisAssemblyFrameType.setText(str("Carbon Fibre"))

            else:
                ValueError("The bike type for the order is wrong and does not match bikes being made in this factory.")

            # If has required amount enable button
            if chassis_Station_Order[0].bike_order.fork == "Tubular Steel" and chassis_Station_Order[0].bike_order.frame == "Tubular Steel":
                if type(chassis_Station_Order[0].bike_order) == Bike:
                    if window.ChassisStationInventoryStandardForksCount.value() > 0 and window.ChassisStationInventoryStandardFrameCount.value() > 0:
                        window.ChassisAssemblyButton.setEnabled(True)
                    else:
                        window.ChassisAssemblyButton.setEnabled(False)
                elif type(chassis_Station_Order[0].bike_order) == MountainBike:
                    if window.ChassisStationInventoryMountainForksCount.value() > 0 and window.ChassisStationInventoryMountainFrameCount.value() > 0:
                        window.ChassisAssemblyButton.setEnabled(True)
                    else:
                        window.ChassisAssemblyButton.setEnabled(False)
                elif type(chassis_Station_Order[0].bike_order) == BMXBike:
                    if window.ChassisStationInventoryBMXForksCount.value() > 0 and window.ChassisStationInventoryBMXFrameCount.value() > 0:
                        window.ChassisAssemblyButton.setEnabled(True)
                    else:
                        window.ChassisAssemblyButton.setEnabled(False)
                elif type(chassis_Station_Order[0].bike_order) == KidsBike:
                    if window.ChassisStationInventoryKidsForksCount.value() > 0 and window.ChassisStationInventoryKidsFrameCount.value() > 0:
                        window.ChassisAssemblyButton.setEnabled(True)
                    else:
                        window.ChassisAssemblyButton.setEnabled(False)
                else:
                    TypeError("Bike type is not recognised for chassis_Station_Order[0].bike_order")

            elif chassis_Station_Order[0].bike_order.fork == "Tubular Aluminium" and window.ChassisStationInventoryAluminiumForksCount.value() > 0 and chassis_Station_Order[0].bike_order.frame == "Tubular Aluminium" and window.ChassisStationInventoryAluminiumFrameCount.value() > 0:
                window.ChassisAssemblyButton.setEnabled(True)

            elif chassis_Station_Order[0].bike_order.fork == "Carbon Fibre" and window.ChassisStationInventoryCarbonForksCount.value() > 0 and chassis_Station_Order[0].bike_order.frame == "Carbon Fibre" and window.ChassisStationInventoryCarbonFrameCount.value() > 0:
                window.ChassisAssemblyButton.setEnabled(True)
            else:
                window.ChassisAssemblyButton.setEnabled(False)
            

        else:
            # Default order information
            window.ChassisStation_OrderNumber_Value.setText("[Order ID]")
            window.ChassisStation_BikeType_Value.setText("[Bike Type]")
            window.ChassisStation_Colour_Value.setText("[Colour]")
            window.ChassisStation_Pedal_Value.setText("[Pedal Type]")
            window.ChassisStation_Chain_Value.setText("[Chain Type]")
            window.ChassisStation_Gear_Value.setText("[Gear Type]")
            window.ChassisStation_Wheel_Value.setText("[Wheel Type]")
            window.ChassisStation_Brakes_Value.setText("[Brake Type]")
            window.ChassisStation_Lights_Value.setText("[Lights Type]")
            window.ChassisStation_Seat_Value.setText("[Seat Type]")

            #Default station information
            window.ChassisAssemblyChassisType.setText("[Chassis Type]")
            window.ChassisAssemblyForkType.setText(str("[Fork Type]"))
            window.ChassisAssemblyFrameType.setText(str("[Frame Type]"))
            # Disable button
            window.ChassisAssemblyButton.setEnabled(False)


# Paint Station Functions
    def PaintStationHasRequiredAmount() -> bool:
        if paint_Station_Order[0].bike_order.bike_type == "Standard":
                    if window.PaintStationNormalChassisCount.value() >= 1:
                        if inventory[paint_Station_Order[0].bike_order.colour + " Paint"][0].value() > 0:
                            return True
        elif paint_Station_Order[0].bike_order.bike_type == "Mountain Bike":
            if window.PaintStationMountainChassisCount.value() >= 1:
                        if inventory[paint_Station_Order[0].bike_order.colour + " Paint"][0].value() >= 1:
                            return True
        elif paint_Station_Order[0].bike_order.bike_type == "Road Bike":
            if window.PaintStationRoadChassisCount.value() >= 1:
                        if inventory[paint_Station_Order[0].bike_order.colour + " Paint"][0].value() >= 1:
                            return True
        elif paint_Station_Order[0].bike_order.bike_type == "Track Bike":
            if window.PaintStationTrackChassisCount.value() >= 1:
                        if inventory[paint_Station_Order[0].bike_order.colour + " Paint"][0].value() >= 1:
                            return True
        elif paint_Station_Order[0].bike_order.bike_type == "BMX":
            if window.PaintStationBMXChassisCount.value() >= 1:
                        if inventory[paint_Station_Order[0].bike_order.colour + " Paint"][0].value() >= 1:
                            return True
        elif paint_Station_Order[0].bike_order.bike_type == "Kids":
            if window.PaintStationKidsChassisCount.value() >= 1:
                        if inventory[paint_Station_Order[0].bike_order.colour + " Paint"][0].value() >= 1:
                            return True
        else:
            return False      
                
    def Painted():
        global paint_Station_Order
        if len(paint_Station_Order) > 0:
            if paint_Station_Order[0].id == int(window.PaintStation_OrderNumber_Value.text()):
                # Check has required amount
                if PaintStationHasRequiredAmount():
                    # Remove Inventory
                    if paint_Station_Order[0].bike_order.bike_type == "Standard":
                        InventoryChange("Standard Chassis", - 1.0)
                    elif paint_Station_Order[0].bike_order.bike_type == "Mountain Bike":
                        InventoryChange("Mountain Chassis", - 1.0)
                    elif paint_Station_Order[0].bike_order.bike_type == "Road Bike":
                        InventoryChange("Road Chassis", - 1.0)
                    elif paint_Station_Order[0].bike_order.bike_type == "Track Bike":
                        InventoryChange("Track Chassis", - 1.0)
                    elif paint_Station_Order[0].bike_order.bike_type == "BMX":
                        InventoryChange("BMX Chassis", - 1.0)
                    elif paint_Station_Order[0].bike_order.bike_type == "Kids":
                        InventoryChange("Kids Chassis", - 1.0)
                    InventoryChange(paint_Station_Order[0].bike_order.colour + " Paint", - 1.0)
                    # Move order to Pedal Station
                    PaintOrderToPedalOrder()
                else:
                    # Disable Button
                    window.ChassisAssemblyButton.setEnabled(False)
            else:
                # Display the first order
                setChassisOrderInformation(True)
        else:
            # Default Values
            setChassisOrderInformation(False)

    def PaintOrderToPedalOrder():
        global paint_Station_Order, pedal_Station_Order

        if len(paint_Station_Order) > 0:
            if len(paint_Station_Order) == 1:
                # No order after current one

                # Add Order to Next station list
                pedal_Station_Order.append(paint_Station_Order[0])
                # Next Station update table (Add to Pedals Station Chassis Inventory Table)
                updatePedalsTable()
                # Get Next station to update order information
                setPedalOrderInformation(True)
                # Remove order from this station list
                paint_Station_Order.pop(0)
                # Set order information to default
                setPaintOrderInformation(False)

            else:
                # Add Order to Next station list
                pedal_Station_Order.append(paint_Station_Order[0])
                # Next Station update table (Add to Pedals Station Chassis Inventory Table)
                updatePedalsTable()
                # Get Next station to update order information
                setPedalOrderInformation(True)
                # Remove order from this station list
                paint_Station_Order.pop(0)
                # UpdateStationOrderInformation()
                setPaintOrderInformation(True)
        else:
            ValueError("fork_station_order has no elements (orders) but is somehow triggered to update to the next order")

    def setPaintOrderInformation(next_order: bool):
        """
        Sets the Chassis station order information box with the correct order information whether an order exists or not.
        Also updates the required amounts of materials for the order.
        """
        if next_order:
            # Set new order information
            order = paint_Station_Order[0]
            window.PaintStation_OrderNumber_Value.setText(str(order.id))
            window.PaintStation_BikeType_Value.setText(str(order.bike_order.bike_type))
            window.PaintStation_Colour_Value.setText(str(order.bike_order.colour))
            window.PaintStation_Pedal_Value.setText(str(order.bike_order.pedals))
            window.PaintStation_Chain_Value.setText(str(order.bike_order.chain))
            window.PaintStation_Gear_Value.setText(str(order.bike_order.gears))
            window.PaintStation_Wheel_Value.setText(str(order.bike_order.wheels))
            window.PaintStation_Brakes_Value.setText(str(order.bike_order.brakes))
            window.PaintStation_Lights_Value.setText(str(order.bike_order.lights))
            window.PaintStation_Seat_Value.setText(str(order.bike_order.seat))

            if paint_Station_Order[0].bike_order.bike_type == "Standard":
                window.PaintStationChassisValue.setText("Standard Chassis")
            elif paint_Station_Order[0].bike_order.bike_type == "Mountain Bike":
                window.PaintStationChassisValue.setText("Mountain Chassis")
            elif paint_Station_Order[0].bike_order.bike_type == "Road Bike":
                window.PaintStationChassisValue.setText("Road Chassis")
            elif paint_Station_Order[0].bike_order.bike_type == "Track Bike":
                window.PaintStationChassisValue.setText("Track Chassis")
            elif paint_Station_Order[0].bike_order.bike_type == "BMX":
                window.PaintStationChassisValue.setText("Mountain Chassis")
            elif paint_Station_Order[0].bike_order.bike_type == "Kids":
                window.PaintStationChassisValue.setText("Mountain Chassis")
            else:
                ValueError("The bike type for the order is wrong and does not match bikes being made in this factory.")
            
            window.PaintStationColourValue.setText(str(order.bike_order.colour))

            if PaintStationHasRequiredAmount():
                window.PaintedButton.setEnabled(True)

        else:
            # Default order information
            window.PaintStation_OrderNumber_Value.setText("[Order ID]")
            window.PaintStation_BikeType_Value.setText("[Bike Type]")
            window.PaintStation_Colour_Value.setText("[Colour]")
            window.PaintStation_Pedal_Value.setText("[Pedal Type]")
            window.PaintStation_Chain_Value.setText("[Chain Type]")
            window.PaintStation_Gear_Value.setText("[Gear Type]")
            window.PaintStation_Wheel_Value.setText("[Wheel Type]")
            window.PaintStation_Brakes_Value.setText("[Brake Type]")
            window.PaintStation_Lights_Value.setText("[Lights Type]")
            window.PaintStation_Seat_Value.setText("[Seat Type]")

            #Default station information
            window.PaintStationChassisValue.setText("[Chassis Type]")
            window.PaintStationColourValue.setText("[Colour]")
            # Disable button
            window.PaintedButton.setEnabled(False)

# Pedal Station Functions

    def PedalStationHasRequiredAmount() -> bool:
        table = window.PedalStationChassisInventoryTable
        if pedal_Station_Order[0].bike_order.pedals == "Standard" and window.PedalStationInventoryNormalPedalsCount.value() >= 2:
            if type(pedal_Station_Order[0].bike_order) == Bike and table.item(0, 0).text() == "Standard" and table.item(0, 1).text() == pedal_Station_Order[0].bike_order.colour:
                return True
            elif type(pedal_Station_Order[0].bike_order) == MountainBike and table.item(0, 0).text() == "Mountain" and table.item(0, 1).text() == pedal_Station_Order[0].bike_order.colour:
                return True
            elif type(pedal_Station_Order[0].bike_order) == RoadBike and table.item(0, 0).text() == "Road" and table.item(0, 1).text() == pedal_Station_Order[0].bike_order.colour:
                return True
            elif type(pedal_Station_Order[0].bike_order) == BMXBike and table.item(0, 0).text() == "BMX" and table.item(0, 1).text() == pedal_Station_Order[0].bike_order.colour:
                return True
            else:
                ValueError("Should not be possible here.")

        elif pedal_Station_Order[0].bike_order.pedals == "Premium" and window.PedalStationInventoryPremiumPedalsCount.value() >= 2:
            if type(pedal_Station_Order[0].bike_order) == Bike and table.item(0, 0).text() == "Standard" and table.item(0, 1).text() == pedal_Station_Order[0].bike_order.colour:
                return True
            elif type(pedal_Station_Order[0].bike_order) == MountainBike and table.item(0, 0).text() == "Mountain" and table.item(0, 1).text() == pedal_Station_Order[0].bike_order.colour:
                return True
            elif type(pedal_Station_Order[0].bike_order) == RoadBike and table.item(0, 0).text() == "Road" and table.item(0, 1).text() == pedal_Station_Order[0].bike_order.colour:
                return True
            elif type(pedal_Station_Order[0].bike_order) == BMXBike and table.item(0, 0).text() == "BMX" and table.item(0, 1).text() == pedal_Station_Order[0].bike_order.colour:
                return True
            else:
                ValueError("Should not be possible here.")
        elif pedal_Station_Order[0].bike_order.pedals == "Carbon Fibre" and window.PedalStationInventoryCarbonPedalsCount.value() >= 2:
            if type(pedal_Station_Order[0].bike_order) == TrackBike and table.item(0, 0).text() == "Track" and table.item(0, 1).text() == pedal_Station_Order[0].bike_order.colour:
                return True
        elif pedal_Station_Order[0].bike_order.pedals == "Kids" and window.PedalStationInventoryKidsPedalsCount.value() >= 2:
            if type(pedal_Station_Order[0].bike_order) == KidsBike and table.item(0, 0).text() == "Kids" and table.item(0, 1).text() == pedal_Station_Order[0].bike_order.colour:
                return True
            else:
                ValueError("Should not be possible here.")
        else:
            ValueError("The order's pedal type is not matched with any known pedal in the factory. Shouldn't be possible.")
    
    def PedalsAssembled():
        global pedal_Station_Order
        if len(pedal_Station_Order) > 0:
            if pedal_Station_Order[0].id == int(window.PedalStation_OrderNumber_Value.text()):
                # Check has required amounts
                if PedalStationHasRequiredAmount():
                    # Remove Pedals From Inventory
                    if pedal_Station_Order[0].bike_order.pedals == "Standard":
                        InventoryChange("Normal Pedals", - 2.0)
                    elif pedal_Station_Order[0].bike_order.pedals == "Premium":
                        InventoryChange("Premium Pedals", - 2.0)
                    elif pedal_Station_Order[0].bike_order.pedals == "Carbon Fibre":
                        InventoryChange("Carbon Fibre Pedals", - 2.0)
                    elif pedal_Station_Order[0].bike_order.pedals == "Kids":
                        InventoryChange("Kids Pedals", - 2.0)

                    # Move order to Pedal Station
                    PedalOrderToDCOrder()
                else:
                    #Disable button
                    window.PedalAssembly_AssembledButton.setEnabled(False)
            else:
                # Display the first order
                setPedalOrderInformation(True)
        else:
            # Default Values
            setPedalOrderInformation(False)

    def PedalOrderToDCOrder():
        global pedal_Station_Order, drive_chain_Station_Order

        if len(pedal_Station_Order) > 0:
            if len(pedal_Station_Order) == 1:
                # No order after current one

                # Add Order to Next station list
                drive_chain_Station_Order.append(pedal_Station_Order[0])
                # Next Station update table (Add to Pedals Station Chassis Inventory Table)
                updateDriveChainTable()
                # Get Next station to update order information
                setDriveChainOrderInformation(True)
                # Remove order from this station list
                pedal_Station_Order.pop(0)
                # Update this stations Table
                updatePedalsTable()
                # Set order information to default
                setPedalOrderInformation(False)

            else:
                # Add Order to Next station list
                drive_chain_Station_Order.append(pedal_Station_Order[0])
                # Next Station update table (Add to Pedals Station Chassis Inventory Table)
                updateDriveChainTable()
                # Get Next station to update order information
                setDriveChainOrderInformation(True)
                # Remove order from this station list
                pedal_Station_Order.pop(0)
                # Update this stations Table
                updatePedalsTable()
                setPedalOrderInformation(True)
        else:
            ValueError("pedal_station_order has no elements (orders) but is somehow triggered to update to the next order")
        
    def setPedalOrderInformation(next_order: bool):
        """
        Sets the Pedal station order information box with the correct order information whether an order exists or not.
        Also updates the required amounts of materials for the order.
        """
        if next_order:
            # Set new order information
            order = pedal_Station_Order[0]
            window.PedalStation_OrderNumber_Value.setText(str(order.id))
            window.PedalStation_BikeType_Value.setText(str(order.bike_order.bike_type))
            window.PedalStation_Colour_Value.setText(str(order.bike_order.colour))
            window.PedalStation_Pedal_Value.setText(str(order.bike_order.pedals))
            window.PedalStation_Chain_Value.setText(str(order.bike_order.chain))
            window.PedalStation_Gear_Value.setText(str(order.bike_order.gears))
            window.PedalStation_Wheel_Value.setText(str(order.bike_order.wheels))
            window.PedalStation_Brakes_Value.setText(str(order.bike_order.brakes))
            window.PedalStation_Lights_Value.setText(str(order.bike_order.lights))
            window.PedalStation_Seat_Value.setText(str(order.bike_order.seat))

            # Station Info:
            if pedal_Station_Order[0].bike_order.bike_type == "Standard":
                window.PedalAssembly_ChassisType.setText("Standard Chassis")

            elif pedal_Station_Order[0].bike_order.bike_type == "Mountain Bike":
                window.PedalAssembly_ChassisType.setText("Mountain Chassis")

            elif pedal_Station_Order[0].bike_order.bike_type == "Road Bike":
                window.PedalAssembly_ChassisType.setText("Road Chassis")

            elif pedal_Station_Order[0].bike_order.bike_type == "Track Bike":
                window.PedalAssembly_ChassisType.setText("Track Chassis")

            elif pedal_Station_Order[0].bike_order.bike_type == "BMX":
                window.PedalAssembly_ChassisType.setText("BMX Chassis")

            elif pedal_Station_Order[0].bike_order.bike_type == "Kids":
                window.PedalAssembly_ChassisType.setText("Kids Chassis")

            else:
                ValueError("The bike type for the order is wrong and does not match bikes being made in this factory.")
            window.PedalAssembly_Colour.setText(str(order.bike_order.colour))
            window.PedalAssembly_PedalType.setText(str(order.bike_order.pedals))

            # If required amount for order set button to enabled
            if PedalStationHasRequiredAmount():
                window.PedalAssembly_AssembledButton.setEnabled(True)

        else:
            # Default order information
            window.PedalStation_OrderNumber_Value.setText("[Order ID]")
            window.PedalStation_BikeType_Value.setText("[Bike Type]")
            window.PedalStation_Colour_Value.setText("[Colour]")
            window.PedalStation_Pedal_Value.setText("[Pedal Type]")
            window.PedalStation_Chain_Value.setText("[Chain Type]")
            window.PedalStation_Gear_Value.setText("[Gear Type]")
            window.PedalStation_Wheel_Value.setText("[Wheel Type]")
            window.PedalStation_Brakes_Value.setText("[Brake Type]")
            window.PedalStation_Lights_Value.setText("[Lights Type]")
            window.PedalStation_Seat_Value.setText("[Seat Type]")

            #Default station information
            window.PedalAssembly_ChassisType.setText("[Chassis Type]")
            window.PedalAssembly_Colour.setText("[Colour]")
            window.PedalAssembly_PedalType.setText("[Pedal Type]")
            # Disable button
            window.PedalAssembly_AssembledButton.setEnabled(False)

# Drive Chain Station Functions

    def DCStationHasRequiredAmount() -> bool:
        table = window.DCStationChassisInventoryTable
        if drive_chain_Station_Order[0].bike_order.gears == "Standard" and window.DCStationInventoryNormalGearCounter.value() <= 0:
            return False
        elif drive_chain_Station_Order[0].bike_order.gears == "Low Speed" and window.DCStationInventoryLowSpeedGearCounter.value() <= 0:
            return False
        elif drive_chain_Station_Order[0].bike_order.gears == "High Speed" and window.DCStationInventoryHighSpeedGearCounter.value() <= 0:
            return False
        elif drive_chain_Station_Order[0].bike_order.gears == "Kids" and window.DCStationInventoryKidsGearCounter.value() <= 0:
            return False
        
        if drive_chain_Station_Order[0].bike_order.chain == "Standard" and window.DCStationInventoryNormalChainCounter.value() <= 0:
            return False
        elif drive_chain_Station_Order[0].bike_order.chain == "Premium" and window.DCStationInventoryPremiumChainCounter.value() <= 0:
            return False
        elif drive_chain_Station_Order[0].bike_order.chain == "Track" and window.DCStationInventoryTrackChainCounter.value() <= 0:
            return False
        
        
        if type(drive_chain_Station_Order[0].bike_order) == Bike and table.item(0, 0).text() == "Standard" and table.item(0, 1).text() == drive_chain_Station_Order[0].bike_order.colour and table.item(0, 2).text() == drive_chain_Station_Order[0].bike_order.pedals:
            return True
        elif type(drive_chain_Station_Order[0].bike_order) == MountainBike and table.item(0, 0).text() == "Mountain" and table.item(0, 1).text() == drive_chain_Station_Order[0].bike_order.colour and table.item(0, 2).text() == drive_chain_Station_Order[0].bike_order.pedals:
            return True
        elif type(drive_chain_Station_Order[0].bike_order) == RoadBike and table.item(0, 0).text() == "Road" and table.item(0, 1).text() == drive_chain_Station_Order[0].bike_order.colour and table.item(0, 2).text() == drive_chain_Station_Order[0].bike_order.pedals:
            return True
        elif type(drive_chain_Station_Order[0].bike_order) == BMXBike and table.item(0, 0).text() == "BMX" and table.item(0, 1).text() == drive_chain_Station_Order[0].bike_order.colour and table.item(0, 2).text() == drive_chain_Station_Order[0].bike_order.pedals:
            return True
        elif type(drive_chain_Station_Order[0].bike_order) == TrackBike and table.item(0, 0).text() == "Track" and table.item(0, 1).text() == drive_chain_Station_Order[0].bike_order.colour and table.item(0, 2).text() == drive_chain_Station_Order[0].bike_order.pedals:
            return True
        elif type(drive_chain_Station_Order[0].bike_order) == KidsBike and table.item(0, 0).text() == "Kids" and table.item(0, 1).text() == drive_chain_Station_Order[0].bike_order.colour and table.item(0, 2).text() == drive_chain_Station_Order[0].bike_order.pedals:
            return True
        else:
            return False
        
    def DriveChainAssembled():
        global drive_chain_Station_Order
        if len(drive_chain_Station_Order) > 0:
            if drive_chain_Station_Order[0].id == int(window.DCStation_OrderNumber_Value.text()):
                # Check has required amounts
                if DCStationHasRequiredAmount():
                    # Remove Pedals From Inventory
                    if drive_chain_Station_Order[0].bike_order.gears == "Standard":
                        InventoryChange("Standard Gears", - 1.0)
                    elif drive_chain_Station_Order[0].bike_order.gears == "Low Speed":
                        InventoryChange("Low Speed Gears", - 1.0)
                    elif drive_chain_Station_Order[0].bike_order.gears == "High Speed":
                        InventoryChange("High Speed Gears", - 1.0)
                    elif drive_chain_Station_Order[0].bike_order.pedals == "Kids":
                        InventoryChange("Kids Gears", - 1.0)
                    else:
                        ValueError("drive_chain_Station_Order[0].bike_order.gears IS NOT SET CORRECTLY")

                    if drive_chain_Station_Order[0].bike_order.chain == "Standard":
                        InventoryChange("Standard Chain", - 1.0)
                    elif drive_chain_Station_Order[0].bike_order.chain == "Premium":
                        InventoryChange("Premium Chain", - 1.0)
                    elif drive_chain_Station_Order[0].bike_order.chain == "Track":
                        InventoryChange("Track Chain", - 1.0)
                    else:
                        ValueError("drive_chain_Station_Order[0].bike_order.chain IS NOT SET CORRECTLY")

                    # Move order to Wheel Station
                    DriveChainOrderToWheelOrder()
                else:
                    #Disable button
                    window.DCAssembledButton.setEnabled(False)
            else:
                # Display the first order
                setDriveChainOrderInformation(True)
        else:
            # Default Values
            setDriveChainOrderInformation(False)

    def DriveChainOrderToWheelOrder():
        global drive_chain_Station_Order, wheel_Station_Order

        if len(drive_chain_Station_Order) > 0:
            if len(drive_chain_Station_Order) == 1:
                # No order after current one

                # Add Order to Next station list
                wheel_Station_Order.append(drive_chain_Station_Order[0])
                # Next Station update table (Add to Pedals Station Chassis Inventory Table)
                updateWheelTable()
                # Get Next station to update order information
                setWheelOrderInformation(True)
                # Remove order from this station list
                drive_chain_Station_Order.pop(0)
                # Update this stations Table
                updateDriveChainTable()
                # Set order information to default
                setDriveChainOrderInformation(False)

            else:
                # Add Order to Next station list
                wheel_Station_Order.append(drive_chain_Station_Order[0])
                # Next Station update table (Add to Pedals Station Chassis Inventory Table)
                updateWheelTable()
                # Get Next station to update order information
                setDriveChainOrderInformation(True)
                # Remove order from this station list
                drive_chain_Station_Order.pop(0)
                # Update this stations Table
                updateDriveChainTable()
                # Set order information to next order
                setDriveChainOrderInformation(True)
        else:
            ValueError("pedal_station_order has no elements (orders) but is somehow triggered to update to the next order")

    def setDriveChainOrderInformation(next_order: bool):
        """
        Sets the Pedal station order information box with the correct order information whether an order exists or not.
        Also updates the required amounts of materials for the order.
        """
        if next_order:
            # Set new order information
            order = drive_chain_Station_Order[0]
            window.DCStation_OrderNumber_Value.setText(str(order.id))
            window.DCStation_BikeType_Value.setText(str(order.bike_order.bike_type))
            window.DCStation_Colour_Value.setText(str(order.bike_order.colour))
            window.DCStation_Pedal_Value.setText(str(order.bike_order.pedals))
            window.DCStation_Chain_Value.setText(str(order.bike_order.chain))
            window.DCStation_Gear_Value.setText(str(order.bike_order.gears))
            window.DCStation_Wheel_Value.setText(str(order.bike_order.wheels))
            window.DCStation_Brakes_Value.setText(str(order.bike_order.brakes))
            window.DCStation_Lights_Value.setText(str(order.bike_order.lights))
            window.DCStation_Seat_Value.setText(str(order.bike_order.seat))

            # Station Info:
            if drive_chain_Station_Order[0].bike_order.bike_type == "Standard":
                window.DCAssemblyChassisValue.setText("Standard Chassis")
            elif drive_chain_Station_Order[0].bike_order.bike_type == "Mountain Bike":
                window.DCAssemblyChassisValue.setText("Mountain Chassis")
            elif drive_chain_Station_Order[0].bike_order.bike_type == "Road Bike":
                window.DCAssemblyChassisValue.setText("Road Chassis")
            elif drive_chain_Station_Order[0].bike_order.bike_type == "Track Bike":
                window.DCAssemblyChassisValue.setText("Track Chassis")
            elif drive_chain_Station_Order[0].bike_order.bike_type == "BMX":
                window.DCAssemblyChassisValue.setText("BMX Chassis")
            elif drive_chain_Station_Order[0].bike_order.bike_type == "Kids":
                window.DCAssemblyChassisValue.setText("Kids Chassis")
            else:
                ValueError("The bike type for the order is wrong and does not match bikes being made in this factory.")
            window.DCAssemblyColourValue.setText(str(order.bike_order.colour))
            window.DCAssemblyPedalValue.setText(str(order.bike_order.pedals))
            window.DCAssemblyChainValue.setText(str(order.bike_order.chain))
            window.DCAssemblyGearValue.setText(str(order.bike_order.gears))

            # If required amount for order set button to enabled
            if DCStationHasRequiredAmount():
                window.DCAssembledButton.setEnabled(True)

        else:
            # Default order information
            window.DCStation_OrderNumber_Value.setText("[Order ID]")
            window.DCStation_BikeType_Value.setText("[Bike Type]")
            window.DCStation_Colour_Value.setText("[Colour]")
            window.DCStation_Pedal_Value.setText("[Pedal Type]")
            window.DCStation_Chain_Value.setText("[Chain Type]")
            window.DCStation_Gear_Value.setText("[Gear Type]")
            window.DCStation_Wheel_Value.setText("[Wheel Type]")
            window.DCStation_Brakes_Value.setText("[Brake Type]")
            window.DCStation_Lights_Value.setText("[Lights Type]")
            window.DCStation_Seat_Value.setText("[Seat Type]")

            #Default station information
            window.DCAssemblyChassisValue.setText("[Chassis Type]")
            window.DCAssemblyColourValue.setText("[Colour]")
            window.DCAssemblyPedalValue.setText("[Pedal Type]")
            window.DCAssemblyChainValue.setText("[Chain Type]")
            window.DCAssemblyGearValue.setText("[Gear Type]")
            # Disable button
            window.DCAssembledButton.setEnabled(False)

# Wheel Station Functions

    def WheelHasRequiredAmount():
        table = window.WheelStationChassisInventory

        if wheel_Station_Order[0].bike_order.wheels == "Standard" and window.WheelStationInventory_NormalCount.value() <= 1:
            return False
        elif wheel_Station_Order[0].bike_order.wheels == "Offroad" and window.WheelStationInventory_OffroadCount.value() <= 1:
            return False
        elif wheel_Station_Order[0].bike_order.wheels == "Road" and window.WheelStationInventory_RoadCount.value() <= 1:
            return False
        elif wheel_Station_Order[0].bike_order.wheels == "Carbon Fibre" and window.WheelStationInventory_CarbonCount.value() <= 1:
            return False
        elif wheel_Station_Order[0].bike_order.wheels == "Kids" and window.WheelStationInventory_KidsCount.value() <= 1:
            return False
    
        if type(wheel_Station_Order[0].bike_order) == Bike and table.item(0, 0).text() == "Standard" and table.item(0, 1).text() == wheel_Station_Order[0].bike_order.colour and table.item(0, 2).text() == wheel_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == wheel_Station_Order[0].bike_order.gears and table.item(0, 4).text() == wheel_Station_Order[0].bike_order.chain:
            return True
        elif type(wheel_Station_Order[0].bike_order) == MountainBike and table.item(0, 0).text() == "Mountain" and table.item(0, 1).text() == wheel_Station_Order[0].bike_order.colour and table.item(0, 2).text() == wheel_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == wheel_Station_Order[0].bike_order.gears and table.item(0, 4).text() == wheel_Station_Order[0].bike_order.chain:
            return True
        elif type(wheel_Station_Order[0].bike_order) == RoadBike and table.item(0, 0).text() == "Road" and table.item(0, 1).text() == wheel_Station_Order[0].bike_order.colour and table.item(0, 2).text() == wheel_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == wheel_Station_Order[0].bike_order.gears and table.item(0, 4).text() == wheel_Station_Order[0].bike_order.chain:
            return True
        elif type(wheel_Station_Order[0].bike_order) == BMXBike and table.item(0, 0).text() == "BMX" and table.item(0, 1).text() == wheel_Station_Order[0].bike_order.colour and table.item(0, 2).text() == wheel_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == wheel_Station_Order[0].bike_order.gears and table.item(0, 4).text() == wheel_Station_Order[0].bike_order.chain:
            return True
        elif type(wheel_Station_Order[0].bike_order) == TrackBike and table.item(0, 0).text() == "Track" and table.item(0, 1).text() == wheel_Station_Order[0].bike_order.colour and table.item(0, 2).text() == wheel_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == wheel_Station_Order[0].bike_order.gears and table.item(0, 4).text() == wheel_Station_Order[0].bike_order.chain:
            return True
        elif type(wheel_Station_Order[0].bike_order) == KidsBike and table.item(0, 0).text() == "Kids" and table.item(0, 1).text() == wheel_Station_Order[0].bike_order.colour and table.item(0, 2).text() == wheel_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == wheel_Station_Order[0].bike_order.gears and table.item(0, 4).text() == wheel_Station_Order[0].bike_order.chain:
            return True
        else:
            return False

    def WheelsAssembled():
        global wheel_Station_Order
        if len(wheel_Station_Order) > 0:
            if wheel_Station_Order[0].id == int(window.WheelStation_OrderNumber_Value.text()):
                # Check has required amounts
                if WheelHasRequiredAmount():
                    # Remove Wheels From Inventory
                    if wheel_Station_Order[0].bike_order.wheels == "Standard":
                        InventoryChange("Standard Wheels", - 2.0)
                    elif wheel_Station_Order[0].bike_order.wheels == "Offroad":
                        InventoryChange("Offroad Wheels", - 2.0)
                    elif wheel_Station_Order[0].bike_order.wheels == "Road":
                        InventoryChange("Road Wheels", - 2.0)
                    elif wheel_Station_Order[0].bike_order.wheels == "Carbon Fibre":
                        InventoryChange("Carbon Fibre Wheels", - 2.0)
                    elif wheel_Station_Order[0].bike_order.wheels == "Kids":
                        InventoryChange("Kids Wheels", - 2.0)
                    else:
                        ValueError("wheel_Station_Order[0].bike_order.gears IS NOT SET CORRECTLY")

                    if wheel_Station_Order[0].bike_order.brakes == "None":
                        if wheel_Station_Order[0].bike_order.lights == "None":
                            # Skip Brake and Light Station and go straight to Seat Station
                            WheelStationToSeatStation()
                        else:
                            #Skip Brake Station Send to Light Station
                            WheelStationToLightsStation()
                    else:
                        # Move order to Wheel Station
                        WheelStationToBrakesStation()
                else:
                    #Disable button
                    window.WheelAssembly_AssembledButton.setEnabled(False)
            else:
                # Display the first order
                setWheelOrderInformation(True)
        else:
            # Default Values
            setWheelOrderInformation(False)

    def WheelStationToBrakesStation():
        global wheel_Station_Order, brakes_Station_Order

        if len(wheel_Station_Order) > 0:
            if len(wheel_Station_Order) == 1:
                # No order after current one

                # Add Order to Next station list
                brakes_Station_Order.append(wheel_Station_Order[0])
                # Next Station update table (Add to Pedals Station Chassis Inventory Table)
                updateBrakeTable()
                # Get Next station to update order information
                setBrakeOrderInformation(True)
                # Remove order from this station list
                wheel_Station_Order.pop(0)
                # Update this stations Table
                updateWheelTable()
                # Set order information to default
                setWheelOrderInformation(False)

            else:
                # Add Order to Next station list
                brakes_Station_Order.append(wheel_Station_Order[0])
                # Next Station update table (Add to Pedals Station Chassis Inventory Table)
                updateBrakeTable()
                # Get Next station to update order information
                setBrakeOrderInformation(True)
                # Remove order from this station list
                wheel_Station_Order.pop(0)
                # Update this stations Table
                updateWheelTable()
                # Set order information to next order
                setWheelOrderInformation(True)
        else:
            ValueError("wheel_station_order has no elements (orders) but is somehow triggered to update to the next order")

    def WheelStationToLightsStation():
        global wheel_Station_Order, lights_Station_Order

        if len(wheel_Station_Order) > 0:
            if len(wheel_Station_Order) == 1:
                # No order after current one

                # Add Order to Next station list
                lights_Station_Order.append(wheel_Station_Order[0])
                # Next Station update table (Add to Pedals Station Chassis Inventory Table)
                updateLightTable()
                # Get Next station to update order information
                setLightOrderInformation(True)
                # Remove order from this station list
                wheel_Station_Order.pop(0)
                # Update this stations Table
                updateWheelTable()
                # Set order information to default
                setWheelOrderInformation(False)

            else:
                # Add Order to Next station list
                lights_Station_Order.append(wheel_Station_Order[0])
                # Next Station update table (Add to Pedals Station Chassis Inventory Table)
                updateLightTable()
                # Get Next station to update order information
                setLightOrderInformation(True)
                # Remove order from this station list
                wheel_Station_Order.pop(0)
                # Update this stations Table
                updateWheelTable()
                # Set order information to next order
                setWheelOrderInformation(True)
        else:
            ValueError("pedal_station_order has no elements (orders) but is somehow triggered to update to the next order")

    def WheelStationToSeatStation():
        global wheel_Station_Order, seat_Station_Order

        if len(wheel_Station_Order) > 0:
            if len(wheel_Station_Order) == 1:
                # No order after current one

                # Add Order to Next station list
                seat_Station_Order.append(wheel_Station_Order[0])
                # Next Station update table (Add to Pedals Station Chassis Inventory Table)
                updateSeatTable()
                # Get Next station to update order information
                setSeatOrderInformation(True)
                # Remove order from this station list
                wheel_Station_Order.pop(0)
                # Update this stations Table
                updateWheelTable()
                # Set order information to default
                setWheelOrderInformation(False)

            else:
                # Add Order to Next station list
                seat_Station_Order.append(wheel_Station_Order[0])
                # Next Station update table (Add to Pedals Station Chassis Inventory Table)
                updateSeatTable()
                # Get Next station to update order information
                setSeatOrderInformation(True)
                # Remove order from this station list
                wheel_Station_Order.pop(0)
                # Update this stations Table
                updateWheelTable()
                # Set order information to next order
                setWheelOrderInformation(True)
        else:
            ValueError("pedal_station_order has no elements (orders) but is somehow triggered to update to the next order")

    def setWheelOrderInformation(next_order: bool):
        """
        Sets the Pedal station order information box with the correct order information whether an order exists or not.
        Also updates the required amounts of materials for the order.
        """
        if next_order:
            # Set new order information
            order = wheel_Station_Order[0]
            window.WheelStation_OrderNumber_Value.setText(str(order.id))
            window.WheelStation_BikeType_Value.setText(str(order.bike_order.bike_type))
            window.WheelStation_Colour_Value.setText(str(order.bike_order.colour))
            window.WheelStation_Pedal_Value.setText(str(order.bike_order.pedals))
            window.WheelStation_Chain_Value.setText(str(order.bike_order.chain))
            window.WheelStation_Gear_Value.setText(str(order.bike_order.gears))
            window.WheelStation_Wheel_Value.setText(str(order.bike_order.wheels))
            window.WheelStation_Brakes_Value.setText(str(order.bike_order.brakes))
            window.WheelStation_Lights_Value.setText(str(order.bike_order.lights))
            window.WheelStation_Seat_Value.setText(str(order.bike_order.seat))

            # Station Info:
            if wheel_Station_Order[0].bike_order.bike_type == "Standard":
                window.WheelAssembly_ChassisType.setText("Standard Chassis")
            elif wheel_Station_Order[0].bike_order.bike_type == "Mountain Bike":
                window.WheelAssembly_ChassisType.setText("Mountain Chassis")
            elif wheel_Station_Order[0].bike_order.bike_type == "Road Bike":
                window.WheelAssembly_ChassisType.setText("Road Chassis")
            elif wheel_Station_Order[0].bike_order.bike_type == "Track Bike":
                window.WheelAssembly_ChassisType.setText("Track Chassis")
            elif wheel_Station_Order[0].bike_order.bike_type == "BMX":
                window.WheelAssembly_ChassisType.setText("BMX Chassis")
            elif wheel_Station_Order[0].bike_order.bike_type == "Kids":
                window.WheelAssembly_ChassisType.setText("Kids Chassis")
            else:
                ValueError("The bike type for the order is wrong and does not match bikes being made in this factory.")
                
            window.WheelAssembly_Colour.setText(str(order.bike_order.colour))
            window.WheelAssembly_PedalType.setText(str(order.bike_order.pedals))
            window.WheelAssembly_ChainType.setText(str(order.bike_order.chain))
            window.WheelAssembly_GearType.setText(str(order.bike_order.gears))
            window.WheelAssembly_WheelType.setText(str(order.bike_order.wheels))

            # If required amount for order set button to enabled
            if WheelHasRequiredAmount():
                window.WheelAssembly_AssembledButton.setEnabled(True)

        else:
            # Default order information
            window.WheelStation_OrderNumber_Value.setText("[Order ID]")
            window.WheelStation_BikeType_Value.setText("[Bike Type]")
            window.WheelStation_Colour_Value.setText("[Colour]")
            window.WheelStation_Pedal_Value.setText("[Pedal Type]")
            window.WheelStation_Chain_Value.setText("[Chain Type]")
            window.WheelStation_Gear_Value.setText("[Gear Type]")
            window.WheelStation_Wheel_Value.setText("[Wheel Type]")
            window.WheelStation_Brakes_Value.setText("[Brake Type]")
            window.WheelStation_Lights_Value.setText("[Lights Type]")
            window.WheelStation_Seat_Value.setText("[Seat Type]")

            #Default station information
            window.WheelAssembly_ChassisType.setText("[Chassis Type]")
            window.WheelAssembly_Colour.setText("[Colour]")
            window.WheelAssembly_PedalType.setText("[Pedal Type]")
            window.WheelAssembly_ChainType.setText("[Chain Type]")
            window.WheelAssembly_GearType.setText("[Gear Type]")
            window.WheelAssembly_WheelType.setText("[Wheel Type]")
            # Disable button
            window.WheelAssembly_AssembledButton.setEnabled(False)

    # Brake Station Functions

    def BrakeHasRequiredAmount():
        table = window.BrakeStationChassisInventoryTable

        if brakes_Station_Order[0].bike_order.brakes == "Standard" and window.BrakeStationNormalBrakeCounter.value() <= 1:
            return False
        elif brakes_Station_Order[0].bike_order.brakes == "Premium" and window.BrakeStationPremiumBrakeCounter.value() <= 1:
            return False
    
        if type(brakes_Station_Order[0].bike_order) == Bike and table.item(0, 0).text() == "Standard" and table.item(0, 1).text() == brakes_Station_Order[0].bike_order.colour and table.item(0, 2).text() == brakes_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == brakes_Station_Order[0].bike_order.gears and table.item(0, 4).text() == brakes_Station_Order[0].bike_order.chain and table.item(0, 5).text() == brakes_Station_Order[0].bike_order.wheels:
            return True
        elif type(brakes_Station_Order[0].bike_order) == MountainBike and table.item(0, 0).text() == "Mountain" and table.item(0, 1).text() == brakes_Station_Order[0].bike_order.colour and table.item(0, 2).text() == brakes_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == brakes_Station_Order[0].bike_order.gears and table.item(0, 4).text() == brakes_Station_Order[0].bike_order.chain and table.item(0, 5).text() == brakes_Station_Order[0].bike_order.wheels:
            return True
        elif type(brakes_Station_Order[0].bike_order) == RoadBike and table.item(0, 0).text() == "Road" and table.item(0, 1).text() == brakes_Station_Order[0].bike_order.colour and table.item(0, 2).text() == brakes_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == brakes_Station_Order[0].bike_order.gears and table.item(0, 4).text() == brakes_Station_Order[0].bike_order.chain and table.item(0, 5).text() == brakes_Station_Order[0].bike_order.wheels:
            return True
        elif type(brakes_Station_Order[0].bike_order) == BMXBike and table.item(0, 0).text() == "BMX" and table.item(0, 1).text() == brakes_Station_Order[0].bike_order.colour and table.item(0, 2).text() == brakes_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == brakes_Station_Order[0].bike_order.gears and table.item(0, 4).text() == brakes_Station_Order[0].bike_order.chain and table.item(0, 5).text() == brakes_Station_Order[0].bike_order.wheels:
            return True
        elif type(brakes_Station_Order[0].bike_order) == TrackBike and table.item(0, 0).text() == "Track" and table.item(0, 1).text() == brakes_Station_Order[0].bike_order.colour and table.item(0, 2).text() == brakes_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == brakes_Station_Order[0].bike_order.gears and table.item(0, 4).text() == brakes_Station_Order[0].bike_order.chain and table.item(0, 5).text() == brakes_Station_Order[0].bike_order.wheels:
            return True
        elif type(brakes_Station_Order[0].bike_order) == KidsBike and table.item(0, 0).text() == "Kids" and table.item(0, 1).text() == brakes_Station_Order[0].bike_order.colour and table.item(0, 2).text() == brakes_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == brakes_Station_Order[0].bike_order.gears and table.item(0, 4).text() == brakes_Station_Order[0].bike_order.chain and table.item(0, 5).text() == brakes_Station_Order[0].bike_order.wheels:
            return True
        else:
            return False

    def BrakesAssembled():
        global brakes_Station_Order
        if len(brakes_Station_Order) > 0:
            if brakes_Station_Order[0].id == int(window.BrakesStation_OrderNumber_Value.text()):
                # Check has required amounts
                if BrakeHasRequiredAmount():
                    # Remove Brakes From Inventory
                    if brakes_Station_Order[0].bike_order.brakes == "Standard":
                        InventoryChange("Normal Brakes", - 2.0)
                    elif brakes_Station_Order[0].bike_order.brakes == "Premium":
                        InventoryChange("Premium Brakes", - 2.0)
                    else:
                        ValueError("brakes_Station_Order[0].bike_order.brakes IS NOT SET CORRECTLY")

                    if brakes_Station_Order[0].bike_order.lights == "None":
                        BrakeStationToSeatStation()
                    else:
                        BrakeStationToLightsStation()
                else:
                    #Disable button
                    window.BrakeAssemblyAssembledButton.setEnabled(False)
            else:
                # Display the first order
                setBrakeOrderInformation(True)
        else:
            # Default Values
            setBrakeOrderInformation(False)

    def BrakeStationToLightsStation():
        global brakes_Station_Order, lights_Station_Order

        if len(brakes_Station_Order) > 0:
            if len(brakes_Station_Order) == 1:
                # No order after current one

                # Add Order to Next station list
                lights_Station_Order.append(brakes_Station_Order[0])
                # Next Station update table (Add to Pedals Station Chassis Inventory Table)
                updateLightTable()
                # Get Next station to update order information
                setLightOrderInformation(True)
                # Remove order from this station list
                brakes_Station_Order.pop(0)
                # Update this stations Table
                updateBrakeTable()
                # Set order information to default
                setBrakeOrderInformation(False)

            else:
                # Add Order to Next station list
                lights_Station_Order.append(brakes_Station_Order[0])
                # Next Station update table (Add to Pedals Station Chassis Inventory Table)
                updateLightTable()
                # Get Next station to update order information
                setLightOrderInformation(True)
                # Remove order from this station list
                brakes_Station_Order.pop(0)
                # Update this stations Table
                updateBrakeTable()
                # Set order information to next order
                setBrakeOrderInformation(True)
        else:
            ValueError("brakes_Station_Order has no elements (orders) but is somehow triggered to update to the next order")

    def BrakeStationToSeatStation():
        global brakes_Station_Order, seat_Station_Order

        if len(brakes_Station_Order) > 0:
            if len(brakes_Station_Order) == 1:
                # No order after current one

                # Add Order to Next station list
                seat_Station_Order.append(brakes_Station_Order[0])
                # Next Station update table (Add to Pedals Station Chassis Inventory Table)
                updateSeatTable()
                # Get Next station to update order information
                setSeatOrderInformation(True)
                # Remove order from this station list
                brakes_Station_Order.pop(0)
                # Update this stations Table
                updateBrakeTable()
                # Set order information to default
                setBrakeOrderInformation(False)

            else:
                # Add Order to Next station list
                seat_Station_Order.append(brakes_Station_Order[0])
                # Next Station update table (Add to Pedals Station Chassis Inventory Table)
                updateSeatTable()
                # Get Next station to update order information
                setSeatOrderInformation(True)
                # Remove order from this station list
                brakes_Station_Order.pop(0)
                # Update this stations Table
                updateBrakeTable()
                # Set order information to next order
                setBrakeOrderInformation(True)
        else:
            ValueError("brakes_Station_Order has no elements (orders) but is somehow triggered to update to the next order")


    def setBrakeOrderInformation(next_order: bool):
        """
        Sets the Pedal station order information box with the correct order information whether an order exists or not.
        Also updates the required amounts of materials for the order.
        """
        if next_order:
            # Set new order information
            order = brakes_Station_Order[0]
            window.BrakesStation_OrderNumber_Value.setText(str(order.id))
            window.BrakesStation_BikeType_Value.setText(str(order.bike_order.bike_type))
            window.BrakesStation_Colour_Value.setText(str(order.bike_order.colour))
            window.BrakesStation_Pedal_Value.setText(str(order.bike_order.pedals))
            window.BrakesStation_Chain_Value.setText(str(order.bike_order.chain))
            window.BrakesStation_Gear_Value.setText(str(order.bike_order.gears))
            window.BrakesStation_Wheel_Value.setText(str(order.bike_order.wheels))
            window.BrakesStation_Brakes_Value.setText(str(order.bike_order.brakes))
            window.BrakesStation_Lights_Value.setText(str(order.bike_order.lights))
            window.BrakesStation_Seat_Value.setText(str(order.bike_order.seat))

            # Station Info:
            if brakes_Station_Order[0].bike_order.bike_type == "Standard":
                window.BrakeAssemblyChassisType.setText("Standard Chassis")
            elif brakes_Station_Order[0].bike_order.bike_type == "Mountain Bike":
                window.BrakeAssemblyChassisType.setText("Mountain Chassis")
            elif brakes_Station_Order[0].bike_order.bike_type == "Road Bike":
                window.BrakeAssemblyChassisType.setText("Road Chassis")
            elif brakes_Station_Order[0].bike_order.bike_type == "Track Bike":
                window.BrakeAssemblyChassisType.setText("Track Chassis")
            elif brakes_Station_Order[0].bike_order.bike_type == "BMX":
                window.BrakeAssemblyChassisType.setText("BMX Chassis")
            elif brakes_Station_Order[0].bike_order.bike_type == "Kids":
                window.BrakeAssemblyChassisType.setText("Kids Chassis")
            else:
                ValueError("The bike type for the order is wrong and does not match bikes being made in this factory.")
                
            window.BrakeAssemblyColourValue.setText(str(order.bike_order.colour))
            window.BrakeAssemblyPedalValue.setText(str(order.bike_order.pedals))
            window.BrakeAssemblyChainValue.setText(str(order.bike_order.chain))
            window.BrakeAssemblyGearValue.setText(str(order.bike_order.gears))
            window.BrakeAssemblyWheelValue.setText(str(order.bike_order.wheels))
            window.BrakeAssemblyBrakeValue.setText(str(order.bike_order.brakes))

            # If required amount for order set button to enabled
            if BrakeHasRequiredAmount():
                window.BrakeAssemblyAssembledButton.setEnabled(True)

        else:
            # Default order information
            window.BrakesStation_OrderNumber_Value.setText("[Order ID]")
            window.BrakesStation_BikeType_Value.setText("[Bike Type]")
            window.BrakesStation_Colour_Value.setText("[Colour]")
            window.BrakesStation_Pedal_Value.setText("[Pedal Type]")
            window.BrakesStation_Chain_Value.setText("[Chain Type]")
            window.BrakesStation_Gear_Value.setText("[Gear Type]")
            window.BrakesStation_Wheel_Value.setText("[Wheel Type]")
            window.BrakesStation_Brakes_Value.setText("[Brake Type]")
            window.BrakesStation_Lights_Value.setText("[Lights Type]")
            window.BrakesStation_Seat_Value.setText("[Seat Type]")

            #Default station information
            window.BrakeAssemblyChassisType.setText("[Chassis Type]")
            window.BrakeAssemblyColourValue.setText("[Colour]")
            window.BrakeAssemblyPedalValue.setText("[Pedal Type]")
            window.BrakeAssemblyChainValue.setText("[Chain Type]")
            window.BrakeAssemblyGearValue.setText("[Gear Type]")
            window.BrakeAssemblyWheelValue.setText("[Wheel Type]")
            window.BrakeAssemblyBrakeValue.setText("[Brakes Type]")
            # Disable button
            window.BrakeAssemblyAssembledButton.setEnabled(False)

    # Light Station Functions
    def LightHasRequiredAmount():
        table = window.LightStation_ChassisInventory_Table

        if lights_Station_Order[0].bike_order.lights == "Standard" and window.LightStation_NormalLightCount.value() <= 1:
            return False
        elif lights_Station_Order[0].bike_order.lights == "Premium" and window.LightStation_PremiumLightCount.value() <= 1:
            return False
    
        if type(lights_Station_Order[0].bike_order) == Bike and table.item(0, 0).text() == "Standard" and table.item(0, 1).text() == lights_Station_Order[0].bike_order.colour and table.item(0, 2).text() == lights_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == lights_Station_Order[0].bike_order.gears and table.item(0, 4).text() == lights_Station_Order[0].bike_order.chain and table.item(0, 5).text() == lights_Station_Order[0].bike_order.wheels and table.item(0, 6).text() == lights_Station_Order[0].bike_order.brakes:
            return True
        elif type(lights_Station_Order[0].bike_order) == MountainBike and table.item(0, 0).text() == "Mountain" and table.item(0, 1).text() == lights_Station_Order[0].bike_order.colour and table.item(0, 2).text() == lights_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == lights_Station_Order[0].bike_order.gears and table.item(0, 4).text() == lights_Station_Order[0].bike_order.chain and table.item(0, 5).text() == lights_Station_Order[0].bike_order.wheels and table.item(0, 6).text() == lights_Station_Order[0].bike_order.brakes:
            return True
        elif type(lights_Station_Order[0].bike_order) == RoadBike and table.item(0, 0).text() == "Road" and table.item(0, 1).text() == lights_Station_Order[0].bike_order.colour and table.item(0, 2).text() == lights_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == lights_Station_Order[0].bike_order.gears and table.item(0, 4).text() == lights_Station_Order[0].bike_order.chain and table.item(0, 5).text() == lights_Station_Order[0].bike_order.wheels and table.item(0, 6).text() == lights_Station_Order[0].bike_order.brakes:
            return True
        elif type(lights_Station_Order[0].bike_order) == BMXBike and table.item(0, 0).text() == "BMX" and table.item(0, 1).text() == lights_Station_Order[0].bike_order.colour and table.item(0, 2).text() == lights_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == lights_Station_Order[0].bike_order.gears and table.item(0, 4).text() == lights_Station_Order[0].bike_order.chain and table.item(0, 5).text() == lights_Station_Order[0].bike_order.wheels and table.item(0, 6).text() == lights_Station_Order[0].bike_order.brakes:
            return True
        elif type(lights_Station_Order[0].bike_order) == TrackBike and table.item(0, 0).text() == "Track" and table.item(0, 1).text() == lights_Station_Order[0].bike_order.colour and table.item(0, 2).text() == lights_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == lights_Station_Order[0].bike_order.gears and table.item(0, 4).text() == lights_Station_Order[0].bike_order.chain and table.item(0, 5).text() == lights_Station_Order[0].bike_order.wheels and table.item(0, 6).text() == lights_Station_Order[0].bike_order.brakes:
            return True
        elif type(lights_Station_Order[0].bike_order) == KidsBike and table.item(0, 0).text() == "Kids" and table.item(0, 1).text() == lights_Station_Order[0].bike_order.colour and table.item(0, 2).text() == lights_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == lights_Station_Order[0].bike_order.gears and table.item(0, 4).text() == lights_Station_Order[0].bike_order.chain and table.item(0, 5).text() == lights_Station_Order[0].bike_order.wheels and table.item(0, 6).text() == lights_Station_Order[0].bike_order.brakes:
            return True
        else:
            return False

    def LightsAssembled():
        global lights_Station_Order
        if len(lights_Station_Order) > 0:
            if lights_Station_Order[0].id == int(window.LightStation_OrderNumber_Value.text()):
                # Check has required amounts
                if LightHasRequiredAmount():
                    # Remove Brakes From Inventory
                    if lights_Station_Order[0].bike_order.lights == "Standard":
                        InventoryChange("Normal Lights", - 2.0)
                    elif lights_Station_Order[0].bike_order.lights == "Premium":
                        InventoryChange("Premium Lights", - 2.0)
                    else:
                        ValueError("lights_Station_Order[0].bike_order.brakes IS NOT SET CORRECTLY")

                    LightStationToSeatStation()
                else:
                    #Disable button
                    window.LightStation_Assembly_AssembledButton.setEnabled(False)
            else:
                # Display the first order
                setLightOrderInformation(True)
        else:
            # Default Values
            setLightOrderInformation(False)

    def LightStationToSeatStation():
        global lights_Station_Order, seat_Station_Order

        if len(lights_Station_Order) > 0:
            if len(lights_Station_Order) == 1:
                # No order after current one

                # Add Order to Next station list
                seat_Station_Order.append(lights_Station_Order[0])
                # Next Station update table
                updateSeatTable()
                # Get Next station to update order information
                setSeatOrderInformation(True)
                # Remove order from this station list
                lights_Station_Order.pop(0)
                # Update this stations Table
                updateLightTable()
                # Set order information to default
                setLightOrderInformation(False)

            else:
                # Add Order to Next station list
                seat_Station_Order.append(lights_Station_Order[0])
                # Next Station update table
                updateSeatTable()
                # Get Next station to update order information
                setSeatOrderInformation(True)
                # Remove order from this station list
                lights_Station_Order.pop(0)
                # Update this stations Table
                updateLightTable()
                # Set order information to next order
                setLightOrderInformation(True)
        else:
            ValueError("lights_Station_Order has no elements (orders) but is somehow triggered to update to the next order")

    def setLightOrderInformation(next_order: bool):
        """
        Sets the Light station order information box with the correct order information whether an order exists or not.
        Also updates the required amounts of materials for the order.
        """
        if next_order:
            # Set new order information
            order = lights_Station_Order[0]
            window.LightStation_OrderNumber_Value.setText(str(order.id))
            window.LightStation_BikeType_Value.setText(str(order.bike_order.bike_type))
            window.LightStation_Colour_Value.setText(str(order.bike_order.colour))
            window.LightStation_Pedal_Value.setText(str(order.bike_order.pedals))
            window.LightStation_Chain_Value.setText(str(order.bike_order.chain))
            window.LightStation_Gear_Value.setText(str(order.bike_order.gears))
            window.LightStation_Wheel_Value.setText(str(order.bike_order.wheels))
            window.LightStation_Brakes_Value.setText(str(order.bike_order.brakes))
            window.LightStation_Lights_Value.setText(str(order.bike_order.lights))
            window.LightStation_Seat_Value.setText(str(order.bike_order.seat))

            # Station Info:
            if lights_Station_Order[0].bike_order.bike_type == "Standard":
                window.LightStation_Assembly_ChassisType.setText("Standard Chassis")

            elif lights_Station_Order[0].bike_order.bike_type == "Mountain Bike":
                window.LightStation_Assembly_ChassisType.setText("Mountain Chassis")

            elif lights_Station_Order[0].bike_order.bike_type == "Road Bike":
                window.LightStation_Assembly_ChassisType.setText("Road Chassis")

            elif lights_Station_Order[0].bike_order.bike_type == "Track Bike":
                window.LightStation_Assembly_ChassisType.setText("Track Chassis")

            elif lights_Station_Order[0].bike_order.bike_type == "BMX":
                window.LightStation_Assembly_ChassisType.setText("BMX Chassis")

            elif lights_Station_Order[0].bike_order.bike_type == "Kids":
                window.LightStation_Assembly_ChassisType.setText("Kids Chassis")
            else:
                ValueError("The bike type for the order is wrong and does not match bikes being made in this factory.")
                
            window.LightStation_Assembly_Colour.setText(str(order.bike_order.colour))
            window.LightStation_Assembly_PedalType.setText(str(order.bike_order.pedals))
            window.LightStation_Assembly_ChainType.setText(str(order.bike_order.chain))
            window.LightStation_Assembly_GearType.setText(str(order.bike_order.gears))
            window.LightStation_Assembly_WheelType.setText(str(order.bike_order.wheels))
            window.LightStation_Assembly_BrakeType.setText(str(order.bike_order.brakes))
            window.LightStation_Assembly_LightType.setText(str(order.bike_order.lights))

            # If required amount for order set button to enabled
            if LightHasRequiredAmount():
                window.LightStation_Assembly_AssembledButton.setEnabled(True)

        else:
            # Default order information
            window.LightStation_OrderNumber_Value.setText("[Order ID]")
            window.SeatStation_BikeType_Value.setText("[Bike Type]")
            window.LightStation_Colour_Value.setText("[Colour]")
            window.LightStation_Pedal_Value.setText("[Pedal Type]")
            window.LightStation_Chain_Value.setText("[Chain Type]")
            window.LightStation_Gear_Value.setText("[Gear Type]")
            window.LightStation_Wheel_Value.setText("[Wheel Type]")
            window.LightStation_Brakes_Value.setText("[Brake Type]")
            window.LightStation_Lights_Value.setText("[Lights Type]")
            window.LightStation_Seat_Value.setText("[Seat Type]")

            #Default station information
            window.LightStation_Assembly_ChassisType.setText("[Chassis Type]")
            window.LightStation_Assembly_Colour.setText("[Colour]")
            window.LightStation_Assembly_PedalType.setText("[Pedal Type]")
            window.LightStation_Assembly_ChainType.setText("[Chain Type]")
            window.LightStation_Assembly_GearType.setText("[Gear Type]")
            window.LightStation_Assembly_WheelType.setText("[Wheel Type]")
            window.LightStation_Assembly_BrakeType.setText("[Brakes Type]")
            window.LightStation_Assembly_LightType.setText("[Light Type]")
            # Disable button
            window.LightStation_Assembly_AssembledButton.setEnabled(False)
        
    # Seat Station Functions
    def SeatHasRequiredAmount():
        table = window.SeatStationChassisInventoryTable

        if seat_Station_Order[0].bike_order.seat == "Standard" and window.SeatStationInventoryNormalSeatCount.value() < 1:
            return False
        elif seat_Station_Order[0].bike_order.seat == "Premium" and window.SeatStationInventoryPremiumSeatCount.value() < 1:
            return False
        elif seat_Station_Order[0].bike_order.seat == "Carbon Fibre" and window.SeatStationInventoryCarbonSeatCount.value() < 1:
            return False
    
        if type(seat_Station_Order[0].bike_order) == Bike and table.item(0, 0).text() == "Standard" and table.item(0, 1).text() == seat_Station_Order[0].bike_order.colour and table.item(0, 2).text() == seat_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == seat_Station_Order[0].bike_order.gears and table.item(0, 4).text() == seat_Station_Order[0].bike_order.chain and table.item(0, 5).text() == seat_Station_Order[0].bike_order.wheels and table.item(0, 6).text() == seat_Station_Order[0].bike_order.brakes and table.item(0, 7).text() == seat_Station_Order[0].bike_order.lights:
            return True
        elif type(seat_Station_Order[0].bike_order) == MountainBike and table.item(0, 0).text() == "Mountain" and table.item(0, 1).text() == seat_Station_Order[0].bike_order.colour and table.item(0, 2).text() == seat_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == seat_Station_Order[0].bike_order.gears and table.item(0, 4).text() == seat_Station_Order[0].bike_order.chain and table.item(0, 5).text() == seat_Station_Order[0].bike_order.wheels and table.item(0, 6).text() == seat_Station_Order[0].bike_order.brakes and table.item(0, 7).text() == seat_Station_Order[0].bike_order.lights:
            return True
        elif type(seat_Station_Order[0].bike_order) == RoadBike and table.item(0, 0).text() == "Road" and table.item(0, 1).text() == seat_Station_Order[0].bike_order.colour and table.item(0, 2).text() == seat_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == seat_Station_Order[0].bike_order.gears and table.item(0, 4).text() == seat_Station_Order[0].bike_order.chain and table.item(0, 5).text() == seat_Station_Order[0].bike_order.wheels and table.item(0, 6).text() == seat_Station_Order[0].bike_order.brakes and table.item(0, 7).text() == seat_Station_Order[0].bike_order.lights:
            return True
        elif type(seat_Station_Order[0].bike_order) == BMXBike and table.item(0, 0).text() == "BMX" and table.item(0, 1).text() == seat_Station_Order[0].bike_order.colour and table.item(0, 2).text() == seat_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == seat_Station_Order[0].bike_order.gears and table.item(0, 4).text() == seat_Station_Order[0].bike_order.chain and table.item(0, 5).text() == seat_Station_Order[0].bike_order.wheels and table.item(0, 6).text() == seat_Station_Order[0].bike_order.brakes and table.item(0, 7).text() == seat_Station_Order[0].bike_order.lights:
            return True
        elif type(seat_Station_Order[0].bike_order) == TrackBike and table.item(0, 0).text() == "Track" and table.item(0, 1).text() == seat_Station_Order[0].bike_order.colour and table.item(0, 2).text() == seat_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == seat_Station_Order[0].bike_order.gears and table.item(0, 4).text() == seat_Station_Order[0].bike_order.chain and table.item(0, 5).text() == seat_Station_Order[0].bike_order.wheels and table.item(0, 6).text() == seat_Station_Order[0].bike_order.brakes and table.item(0, 7).text() == seat_Station_Order[0].bike_order.lights:
            return True
        elif type(seat_Station_Order[0].bike_order) == KidsBike and table.item(0, 0).text() == "Kids" and table.item(0, 1).text() == seat_Station_Order[0].bike_order.colour and table.item(0, 2).text() == seat_Station_Order[0].bike_order.pedals and table.item(0, 3).text() == seat_Station_Order[0].bike_order.gears and table.item(0, 4).text() == seat_Station_Order[0].bike_order.chain and table.item(0, 5).text() == seat_Station_Order[0].bike_order.wheels and table.item(0, 6).text() == seat_Station_Order[0].bike_order.brakes and table.item(0, 7).text() == seat_Station_Order[0].bike_order.lights:
            return True
        else:
            return False
    
    def SeatAssembled():
        global seat_Station_Order
        if len(seat_Station_Order) > 0:
            if seat_Station_Order[0].id == int(window.SeatStation_OrderNumber_Value.text()):
                # Check has required amounts
                if SeatHasRequiredAmount():
                    # Remove Brakes From Inventory
                    if seat_Station_Order[0].bike_order.seat == "Standard":
                        InventoryChange("Normal Seat", - 1.0)
                    elif seat_Station_Order[0].bike_order.seat == "Premium":
                        InventoryChange("Premium Seat", - 1.0)
                    elif seat_Station_Order[0].bike_order.seat == "Carbon Fibre":
                        InventoryChange("Carbon Fibre Seat", - 1.0)
                    else:
                        ValueError("seat_Station_Order[0].bike_order.brakes IS NOT SET CORRECTLY")

                    SeatStationToCompletedOrders()
                else:
                    #Disable button
                    window.SeatStation_Seat_Assembled_Button.setEnabled(False)
            else:
                # Display the first order
                setSeatOrderInformation(True)
        else:
            # Default Values
            setSeatOrderInformation(False)

    def SeatStationToCompletedOrders():
        global seat_Station_Order, completed_Orders

        if len(seat_Station_Order) > 0:
            if len(seat_Station_Order) == 1:
                # No order after current one

                # Add Order to Next station list
                completed_Orders.append(seat_Station_Order[0])
                # Next Station update table
                updateCompletedOrdersTable(completed_Orders[-1])
                # Remove Order from orders dict
                orders.pop(seat_Station_Order[0].id)
                # Remove from orders table
                table = window.Orders_Table
                for row in range(table.rowCount()):
                    if int(table.item(row, 0).text()) == seat_Station_Order[0].id:
                        table.removeRow(row)
                        break

                # Remove order from this station list
                seat_Station_Order.pop(0)
                # Update this stations Table
                updateSeatTable()
                # Set order information to default
                setSeatOrderInformation(False)

            else:
                # Add Order to Next station list
                completed_Orders.append(seat_Station_Order[0])
                # Next Station update table
                updateCompletedOrdersTable(completed_Orders[-1])
                # Remove Order from orders dict
                orders.pop(seat_Station_Order[0].id)
                # Remove from orders table
                table = window.Orders_Table
                for row in range(table.rowCount()):
                    if int(table.item(row, 0).text()) == seat_Station_Order[0].id:
                        table.removeRow(row)
                        break

                # Remove order from this station list
                seat_Station_Order.pop(0)
                # Update this stations Table
                updateSeatTable()
                # Set order information to next order
                setSeatOrderInformation(True)
        else:
            ValueError("seat_Station_Order has no elements (orders) but is somehow triggered to update to the next order")
    
    def setSeatOrderInformation(next_order: bool):
        """
        Sets the Seat station order information box with the correct order information whether an order exists or not.
        Also updates the required amounts of materials for the order.
        """
        if next_order:
            # Set new order information
            order = seat_Station_Order[0]
            window.SeatStation_OrderNumber_Value.setText(str(order.id))
            window.SeatStation_BikeType_Value.setText(str(order.bike_order.bike_type))
            window.SeatStation_Colour_Value.setText(str(order.bike_order.colour))
            window.SeatStation_Pedal_Value.setText(str(order.bike_order.pedals))
            window.SeatStation_Chain_Value.setText(str(order.bike_order.chain))
            window.SeatStation_Gear_Value.setText(str(order.bike_order.gears))
            window.SeatStation_Wheel_Value.setText(str(order.bike_order.wheels))
            window.SeatStation_Brakes_Value.setText(str(order.bike_order.brakes))
            window.SeatStation_Lights_Value.setText(str(order.bike_order.lights))
            window.SeatStation_Seat_Value.setText(str(order.bike_order.seat))

            # Station Info:
            if seat_Station_Order[0].bike_order.bike_type == "Standard":
                window.SeatStation_Assembly_Chassis_Value.setText("Standard Chassis")
            elif seat_Station_Order[0].bike_order.bike_type == "Mountain Bike":
                window.SeatStation_Assembly_Chassis_Value.setText("Mountain Chassis")
            elif seat_Station_Order[0].bike_order.bike_type == "Road Bike":
                window.SeatStation_Assembly_Chassis_Value.setText("Road Chassis")
            elif seat_Station_Order[0].bike_order.bike_type == "Track Bike":
                window.SeatStation_Assembly_Chassis_Value.setText("Track Chassis")
            elif seat_Station_Order[0].bike_order.bike_type == "BMX":
                window.SeatStation_Assembly_Chassis_Value.setText("BMX Chassis")
            elif seat_Station_Order[0].bike_order.bike_type == "Kids":
                window.SeatStation_Assembly_Chassis_Value.setText("Kids Chassis")
            else:
                ValueError("The bike type for the order is wrong and does not match bikes being made in this factory.")
                
            window.SeatStation_Assembly_Colour_Value.setText(str(order.bike_order.colour))
            window.SeatStation_Assembly_Pedal_Value.setText(str(order.bike_order.pedals))
            window.SeatStation_Assembly_Chain_Value.setText(str(order.bike_order.chain))
            window.SeatStation_Assembly_Gear_Value.setText(str(order.bike_order.gears))
            window.SeatStation_Assembly_Wheel_Value.setText(str(order.bike_order.wheels))
            window.SeatStation_Assembly_Brake_Value.setText(str(order.bike_order.brakes))
            window.SeatStation_Assembly_Light_Value.setText(str(order.bike_order.lights))
            window.SeatStation_Assembly_Seat_Value.setText(str(order.bike_order.seat))

            # If required amount for order set button to enabled
            if SeatHasRequiredAmount():
                window.SeatStation_Seat_Assembled_Button.setEnabled(True)

        else:
            # Default order information
            window.SeatStation_OrderNumber_Value.setText("[Order ID]")
            window.SeatStation_BikeType_Value.setText("[Bike Type]")
            window.SeatStation_Colour_Value.setText("[Colour]")
            window.SeatStation_Pedal_Value.setText("[Pedal Type]")
            window.SeatStation_Chain_Value.setText("[Chain Type]")
            window.SeatStation_Gear_Value.setText("[Gear Type]")
            window.SeatStation_Wheel_Value.setText("[Wheel Type]")
            window.SeatStation_Brakes_Value.setText("[Brake Type]")
            window.SeatStation_Lights_Value.setText("[Lights Type]")
            window.SeatStation_Seat_Value.setText("[Seat Type]")

            #Default station information
            window.SeatStation_Assembly_Chassis_Value.setText("[Chassis Type]")
            window.SeatStation_Assembly_Colour_Value.setText("[Colour]")
            window.SeatStation_Assembly_Pedal_Value.setText("[Pedal Type]")
            window.SeatStation_Assembly_Chain_Value.setText("[Chain Type]")
            window.SeatStation_Assembly_Gear_Value.setText("[Gear Type]")
            window.SeatStation_Assembly_Wheel_Value.setText("[Wheel Type]")
            window.SeatStation_Assembly_Brake_Value.setText("[Brakes Type]")
            window.SeatStation_Assembly_Light_Value.setText("[Light Type]")
            window.SeatStation_Assembly_Seat_Value.setText("[Seat Type]")
            # Disable button
            window.SeatStation_Seat_Assembled_Button.setEnabled(False)

    # Menubar Page Changing
    stacked_widget = window.stackedWidget
    changePage(stacked_widget, 0) # Setting this page to always open first

    #Set up Inventory
    setupInventory()
    
    window.actionStations.triggered.connect(lambda: changePage(stacked_widget, 0))
    window.actionStationStatistics.triggered.connect(lambda: changePage(stacked_widget, 1))
    window.actionInventoryDashboard.triggered.connect(lambda: changePage(stacked_widget, 2))
    window.actionInventoryStatistics.triggered.connect(lambda: changePage(stacked_widget, 3))
    window.actionOrdersDashboard.triggered.connect(lambda: changePage(stacked_widget, 4))
    window.actionCompleted_Orders.triggered.connect(lambda: changePage(stacked_widget, 5))
    window.actionAdd_Order.triggered.connect(lambda: changePage(stacked_widget, 6))
    # Closing the app
    window.actionExit.triggered.connect(window.close)

    # New Orders:
    window.NewOrder_SubmitOrderButton.clicked.connect(newOrder)
    window.NewOrder_BikeTypeComboBox.currentTextChanged.connect(orderBox)

    #Station Buttons
    window.ForkWeldedButton.clicked.connect(forkAssembled)
    window.FrameWeldedButton.clicked.connect(frameAssembled)
    window.ChassisAssemblyButton.clicked.connect(ChassisAssembled)
    window.PaintedButton.clicked.connect(Painted)
    window.PedalAssembly_AssembledButton.clicked.connect(PedalsAssembled)
    window.DCAssembledButton.clicked.connect(DriveChainAssembled)
    window.WheelAssembly_AssembledButton.clicked.connect(WheelsAssembled)
    window.BrakeAssemblyAssembledButton.clicked.connect(BrakesAssembled)
    window.LightStation_Assembly_AssembledButton.clicked.connect(LightsAssembled)
    window.SeatStation_Seat_Assembled_Button.clicked.connect(SeatAssembled)
    


    UI_FILE.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()
    sys.exit(APP.exec())

    # To DO:
    # Customer Table