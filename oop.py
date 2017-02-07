class pet(object):

     def __init__(self,pet__type=None, name='general'):

        self.pet__type=pet__type
        self.name=name
		
          if self.pet_type !='far'
               self.pet_type ='feathers'
			   
class bird(pet):#demonstrates inheritance of class bird from class pet
   __pn=0 #demonstrates encapsulation 
   
  def move_out(self):
     print ("fly away")
	 
   def set_pn_number(self,number):
	 self.__pn = number
	 
	 def get_pn_number(self):
	 return self.__pn
	 
	 
	 
	 class insect(pet):#demonstrates inheritance of class insect from class pet
   __pn=0 #demonstrates encapsulation 
   
  def move_out(self):
     print ("crawl away")
	 
   def set_pn_number(self,number):
	 self.__pn = number
	 
	 def get_pn_number(self):
	 return self.__pn
	 
	 def pet_move_out(any_pet):# shows polymorphism
	 return any_pet.move_out()
	 
	 
	 
	 
	