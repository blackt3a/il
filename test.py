import json
name = ""
tel = ""
addr=""
birth = "" 
mail = "" #could be None
other1 = "" #could be None
other2 = ""
other3 = ""




'''
meta_data = {
        "name":name,
        "tel":tel,
        "addr":addr,
        "birth":birth,
        "mail":mail,
        "other1":other1,
        "other2":other2,
        "other3":other3
    }

print(json.dumps(meta_data))

'''




        
class person:
    def __init__(self,name=None,tel=None,work=None,home_addr=None,birth=None,mail=None,slang=None,other=None):
        #check if the status  valid first
        if name is None:
            self._name = ""
        else:
            self._name = name


        if tel is None:
            self._tel = ""
        else:
            self._tel = tel

        if work is None:
            self._work = ""
        else:
            self._work = work

        if home_addr is None:
            self._home_addr = ""
        else:
            self._home_addr = home_addr


        if birth is None:
            self._birth = ""
        else:
            self._birth = birth

        if mail is None:
            self._mail = ""
        else:
            self._mail = mail

        if slang is None:
            self._slang = ""
        else:
            self._slang = slang


        if type(other) is not list:
            self._other = []
            if other is not None:
                self._other.append(other)





#####################################
########################################
    def meta_json(self):
        #creat a dic type
        json_result={
                "name": self._name,
                "tel":  self._tel,
                "work_addr": self._work,
                "home_addr": self._home_addr,
                "birth":self._birth,
                "mail": self._mail,
                "slang": self._slang,
                "other":self._other
            }



        return json.dumps(json_result)


    # Method to return the object's state as a JSON string

    def to_psk(self):

        def get_aka_name(self):
            aka = ""
            name_ = ""
            name_parts = self._name.split()
            
            initials = [part[0].upper() for part in name_parts]
            aka =  "".join(initials) 
            name_ = "".join([part for part in name_parts])
            return aka ,name_


        aka,name_ = get_aka_name(self) 


        def get_random():
            pass



        def name_tel(self):
            return name_+self._tel
   

        def name_birth(self):
            return name_+self._birth
   

        def name_random(self):
            ramdon=""
            return name_+ramdon
   



        def aka_tel(self):
            return aka+self._tel
   
        def func1(self):
            pass
   
        def func2(self):
            pass
   
        def func3(self):
            pass
   
        psks = []
        psks.append(name_tel(self))
        psks.append(name_birth(self))
        psks.append(name_random(self))
        psks.append(aka_tel(self))
        return psks




























#def __init__(self,name=None,tel=None,addr=None,birth=None,mail=None,other=None):
#Mohan  Bansal,Manager,ZO BHOPAL,7389949987,mohanbansal@unionbankofindia.bank 

Per= person(name="Mohan Bansal",tel="7389949987",work="Manager,ZO BHOPAL",mail="mohanbansal@unionbankofindia.bank")
print(Per.meta_json())
print(Per.to_psk())
