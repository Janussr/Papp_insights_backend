import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name where the current directory is present.
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)
import report_service

class TestClass:

    def test_calc_category(self):
        p_areas = ['O03 Nørgaardsvej 2', 'P2 Kulturhuset']
        date = '2022-01-01'
        new_p_areas = report_service.calculate_categories(p_areas, date)
        assert str(type(new_p_areas[0])) == "<class 'models.ParkingArea'>"
    
