from datetime import datetime, date



class Unit:
    

    def __init__(self, unit_dict):

        self.id = unit_dict.get("id")
        self.layout_id = unit_dict.get("layout_id")
        self.layoutName = unit_dict.get("layoutName")
        self.available = unit_dict.get("available")
        self.availableOn = unit_dict.get("availableOn")
        self.bathrooms = unit_dict.get("bathrooms")
        self.bedrooms = unit_dict.get("bedrooms")
        self.displayPrice = unit_dict.get("displayPrice")
        self.modifiedAt = unit_dict.get("modifiedAt")
        self.name = unit_dict.get("name")
        self.occupied = unit_dict.get("occupied")

    def __repr__(self):
        return str({
            "layoutName": self.layoutName,
            "available": self.available,
            "availableOn": self.availableOn,
            "displayPrice": self.displayPrice,
            "name": self.name,
            "occupied": self.occupied
        })
        




    

