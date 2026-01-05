class framework:
    name:str
    language:str
    arch:str

    def set_framework(self,name,language,arch):
        self.name=name
        self.language=language
        self.arch=arch
    def display(self):
        print(self.name,self.language,self.arch)


framework1=framework()
framework1.set_framework("djongo","c","UI")
framework1.display()