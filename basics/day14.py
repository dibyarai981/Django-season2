class apple:
    def micrphone(self):
        return "...."
    
class phone(apple):
    def microphone(self):
        
        return super().microphone() + "Hello!"
    
p = phone()
print(p.microphone())
