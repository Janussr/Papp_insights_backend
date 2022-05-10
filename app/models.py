from pydantic import BaseModel

class Report():
    def __init__(self, report_name, parking_areas, time_filter=None):
        self.report_name = report_name
        #self.time_filter = TimeFilter(xxx,xxx,xxx)
        self.parking_areas = []
        for parking_area in parking_areas:
            new_parking_area = ParkingArea(
                parking_area.name,
                parking_area.parking_categories
            )
            parking_areas.append(new_parking_area)


class ParkingCategory():
    def __init__(self, category_name, category_description):
        self.category_name = category_name
        self.category_description = category_description

class ParkingArea():
    def __init__(self, name, parking_categories):
        self.name = name
        self.parking_categories = []        
        for parking_category in parking_categories:
            new_category = ParkingCategory(
                parking_category.category_name,
                parking_category.category_description,
            )
            self.parking_categories.append(new_category)

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


class ParkingCategoryModel(BaseModel):
    category: str
    value: int

class ParkingAreaModel(BaseModel):
    name: str
    parking_categories: list[ParkingCategoryModel]   

class ReportModel(BaseModel):
    id: int
    report_name: str
    parking_areas: list[ParkingAreaModel]

class ReportFileModel(BaseModel):
    id: int
    report_name: str
    parking_areas: list