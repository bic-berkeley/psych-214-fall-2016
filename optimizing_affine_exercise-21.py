#: a callback we will pass to the fmin_powell function
def my_callback(params):
   print("Trying parameters " + str(params))
