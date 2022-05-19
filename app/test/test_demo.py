from app.services import report_service

class TestClass:
    def test_calc_category(self):
        p_areas = ["O03 Nørgaardsvej 2", "P2 Kulturhuset"]
        date = "2022-01-01"
        new_p_areas = report_service.calculate_categories(p_areas, date)
        assert str(type(new_p_areas[0])) == "<class 'models.ParkingArea'>"
