class Item():
	def __init__(self, item_name):
		self.name = item_name
		self.description = None
		
	def set_description(self, item_description):
		self.description = item_description
		
	def get_description(self):
		return self.description
		
	def describe(self):
		print("There is a " + self.name + ". " + self.description + ".")
		
	def set_name(self, item_name):
		self.name = item_name
	
	def get_name(self):
		return self.name
	
	def get_details(self):
		print(self.name)
		print(self.description)

class Medicine(Item):
        def __init__(self, item_name):
                super().__init__(item_name)
                self.healthscore = 0

        def set_healthscore(self, medicine_score):
                self.healthscore = medicine_score

        def get_healthscore(self):
                return self.healthscore
        
