dict0 = {}
print(dict0)

# dict1, Key and Value are String
dict1 = {'key1':'Value1', 'key2':'Value2', 'key3':'Value3'}
print(dict1) # OUTPUT: {'key1': 'Value1', 'key2': 'Value2', 'key3': 'Value3'}

eats = {'APPLE':'FRUIT', 'POTATO':'ROOT', 'OKRA':'VEGETABLE'}
print(eats) # OUTPUT: {'OKRA': 'VEGITABLE', 'POTATO': 'ROOT', 'APPLE': 'FRUIT'}
print(eats['OKRA'])

eats['GRAINS']='RICE'
print(eats)
eats['GRAINS']='WHEAT'
print(eats)

eats['BANANA']='FRUIT'
print(eats)
eats['APPLE']='BERRY'
print(eats)