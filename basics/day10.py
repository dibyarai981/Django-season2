class mobile:
    def __init__(self,color,brand,shape,materail):
        self.color = color
        self.brand = brand
        self.shape = shape 
        self.materail= materail 

    def describe(self):
            return(F"It is {self.color} in color, It is {self.brand} in brand, It is {self.shape} in shape, It is made of {self.materail} materail")
            
mobile1 = mobile("blue","abc","rectangle","abc")
mobile2= mobile("green","asd","circle","klm")

print(mobile1.describe())