states=["china","japan","usa"]

def edit_items(list,func):
	for item in list:
		print(func(item))
	
	

edit_items(states, lambda item: item.capitalize()+'!')
