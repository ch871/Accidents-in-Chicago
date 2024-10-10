from database.connect import area_colaction
area_colaction.create_index({'area': 1})

executionStats = (area_colaction
      .find({ 'area': '1211'})
      .hint({ 'area': 1})
      .explain()['executionStats'])

area_colaction.drop_indexes()

print(executionStats)

