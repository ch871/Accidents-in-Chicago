from database.connect import area_collection


def get_count_eccident_by_area(area):
    return area_collection.find_one({'area': area})["injuries"]["total"]


def get_contributing_factors(area):
    return area_collection.find_one({'area': area})["contributing_factors"]


def get_statictic_injuries_by_area(area):
    return area_collection.find_one({'area': area})["injuries"]


def create_index():
    area_collection.create_index({'area': 1})
    executionStats = (area_collection
                      .find({'area': '1211'})
                      .hint({'area': 1})
                      .explain())
    return executionStats


print(create_index())


def drop_index():
    area_collection.drop_indexes()
    executionStats = (area_collection
                      .find({'area': '1211'})
                      .explain())
    return executionStats


print(drop_index())
