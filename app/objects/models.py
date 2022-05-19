from pydantic import BaseModel


class ReportOld:
    def __init__(self, report_name, parking_areas, time_filter=None):
        self.report_name = report_name
        # self.time_filter = TimeFilter(xxx,xxx,xxx)
        self.parking_areas = []
        for parking_area in parking_areas:
            new_parking_area = ParkingArea(
                parking_area.name, parking_area.parking_category
            )
            parking_areas.append(new_parking_area)


class Report:
    def __init__(self, report_name, parking_areas, date):
        self.report_name = report_name
        self.parking_areas = []
        self.date = date
        for area in parking_areas:
            new_area = ParkingArea(
                area.name,
                area.parking_category,
            )
            self.parking_areas.append(new_area)


class ParkingCategory:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class ParkingArea:
    def __init__(self, name, parking_category):
        self.name = name
        self.parking_category = parking_category


class ParkingOverview:
    def __init__(self, parking_categories):
        self.parking_categories = parking_categories


class ParkingCategoryModel(BaseModel):
    category: str
    value: int


class ParkingAreaModel(BaseModel):
    name: str
    parking_category: ParkingCategoryModel


class ParkingOverviewModel(BaseModel):
    parking_categories: list[ParkingCategoryModel]


class ReportModel(BaseModel):
    id: str
    report_name: str
    parking_areas: list[ParkingAreaModel]


class ReportFileModel(BaseModel):
    id: str
    report_name: str
    parking_areas: list
    date: str
