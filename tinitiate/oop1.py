class Tinitiate:
    'This is a brief note about the class, This is the TINITIATE Class'
    
    # CLASS VARIABLES / ATTRIBUTES
    # a class Variable
    ti_var   = 100
    # a class list
    ti_list  = ["a","b","c"]
    # a class tuple
    ti_tuple = ("x","y","z")
    # a class dictionary
    ti_dictionary = {"1":"A", "2":"b", "3":"c"}

    # CLASS FUNCTION
    def ti_function(self):
        "This is a class function"
        print("This is a message from the TINITIATE Class ti_function")

a = Tinitiate()
print(a.__doc__)
print(a.ti_list)
a.ti_list.append(-99999)
print(a.ti_list)
a.ti_function()

b = Tinitiate()
b.ti_list.append(-99999)
print(a.ti_list)
b.ti_function()
