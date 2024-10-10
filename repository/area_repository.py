from database.connect import area_colaction


def get_count_eccident_by_area(area):
    return area_colaction.find_one({'area': area})["injuries"]["total"]


def get_contributing_factors(area):
    return area_colaction.find_one({'area': area})["contributing_factors"]


def get_statictic_injuries_by_area(area):
    return area_colaction.find_one({'area': area})["injuries"]
