




class token_name:
    def __init__(self,name,config):
        self._name = name
        self._token_list = []
        #print(config)
        if config["aka"] is True:
            self._token_list.append(self.generate_aka())

        if config["part"] is True:
            self._token_list+= self.generate_part()


        if config["full"] is True:
            self._token_list.append(self.generate_full())


        #print(self._token_list)


        #self.generate_part()



 
    def generate_aka(self):
        name_parts = self._name.split()
        initials = [part[0].upper() for part in name_parts]
        aka_ =  "".join(initials) 
        return aka_
   
    def generate_part(self):
        name_parts = self._name.split()
        #name_ = "".join([part for part in name_parts])
        #self._token_list+=name_parts
        return name_parts

    def generate_full(self):
        
        name_parts = self._name.split()
        name_ = "".join([part for part in name_parts])
        return name_





    def get_token(self):
        return self._token_list
    

if __name__ == "__main__":
    pass
