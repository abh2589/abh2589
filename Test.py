
my_var = 25 # Global Namespace 

def my_func(): #local namespace 
	global my_var
	print(my_var)
	return my_var

my_func()

