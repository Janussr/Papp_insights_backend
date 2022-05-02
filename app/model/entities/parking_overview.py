class ParkingOverview():

    def __init__(self, booth_type, parking_categories):
        self.booth_type = booth_type
        self.parking_categories = []
        for parking_category in parking_categories:
            new_category = ParkingCategory(
                parking_category.category_name,
                parking_category.category_description,
            )
            self.parking_categories.append(new_category)
        