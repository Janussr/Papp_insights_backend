from parking_category import ParkingCategory

class Report():

    def __init__(self, report_name, parking_areas, parking_categories, time_filter):
        self.report_name = report_name
        self.time_filter = TimeFilter(xxx,xxx,xxx)
        self.parking_areas = []         
        self.parking_categories = []        
        for parking_category in parking_categories:
            new_category = ParkingCategory(
                parking_category.category_name,
                parking_category.category_description,
            )
            self.parking_categories.append(new_category)