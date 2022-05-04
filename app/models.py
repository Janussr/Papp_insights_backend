from pydantic import BaseModel

class Report():
    def __init__(self, report_name, parking_areas, parking_categories, time_filter=None):
        self.report_name = report_name
        #self.time_filter = TimeFilter(xxx,xxx,xxx)
        self.parking_areas = []
        for parking_area in parking_areas:
            self.parking_areas.append(parking_area)

        self.parking_categories = []        
        for parking_category in parking_categories:
            new_category = ParkingCategory(
                parking_category.category_name,
                parking_category.category_description,
            )
            self.parking_categories.append(new_category)

class ParkingCategory():
    def __init__(self, category_name, category_description):
        self.category_name = category_name
        self.category_description = category_description

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


class ReportModel(BaseModel):
    report_name: str
    parking_areas: list
    parking_categories: list