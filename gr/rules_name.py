import json
import os



class rules_name:
    def __init__(self,rules_file):
        self._rules = self.ld_rules_file(rules_file)
        self._rules_name = ""
        self.analyse()


    def ld_rules_file(self,rules_file):
        
        with open(rules_file,"r") as target:
            rules = json.load(target)
            return rules






    def analyse(self):
        
        if self._rules["name"]["select"] is True:
            print("name_selected")
            self._rules_name+="-NAME"
            if self._rules["name"]["aka"] is True:
                self._rules_name+="_aka"
            if self._rules["name"]["part"] is True:
                self._rules_name+="_part"
            if self._rules["name"]["full"] is True:
                self._rules_name+="_full"



        if self._rules["phone"]["select"] is True:
            print("tel_selected")
            self._rules_name+="-PHONE"
            if self._rules["phone"]["total"] is True:
                self._rules_name+="_total"

            if self._rules["phone"]["slice_len"]["select"] is True:
                tmp = "_slice_len"+"I"+str(self._rules["phone"]["slice_len"]["min"])+"_"+str(self._rules["phone"]["slice_len"]["max"])+"I"
                self._rules_name+=tmp

        if self._rules["place"]["select"] is True:
            print("place_selected")
            self._rules_name+="-PLACE"
            if self._rules["place"]["aka"] is True:
                self._rules_name+="_aka"
            if self._rules["place"]["part"] is True:
                self._rules_name+="_part"
            if self._rules["place"]["full"] is True:
                self._rules_name+="_full"


        if self._rules["addr"]["select"] is True:
            print("addr_selected")
            self._rules_name+="-ADDR"
            if self._rules["addr"]["aka"] is True:
                self._rules_name+="_aka"
            if self._rules["addr"]["part"] is True:
                self._rules_name+="_part"
            if self._rules["addr"]["full"] is True:
                self._rules_name+="_full"


        if self._rules["door"]["select"] is True:
            print("door_selected")
            self._rules_name+="-DOOR"
            if self._rules["door"]["aka"] is True:
                self._rules_name+="_aka"
            if self._rules["door"]["part"] is True:
                self._rules_name+="_part"
            if self._rules["door"]["full"] is True:
                self._rules_name+="_full"


       
        if self._rules["birth"]["select"] is True:
            print("name_selected")
            self._rules_name+="-BIRTH"
            if self._rules["birth"]["separat"]["Y"] is True:
                self._rules_name+="_y"
            if self._rules["birth"]["separat"]["M"] is True:
                self._rules_name+="_m"
            if self._rules["birth"]["separat"]["D"] is True:
                self._rules_name+="_d"

            if self._rules["birth"]["combin"]["Y_M"] is True:
                self._rules_name+="_ym"

            if self._rules["birth"]["combin"]["M_D"] is True:
                self._rules_name+="_md"

            if self._rules["birth"]["combin"]["Y_M_D"] is True:
                self._rules_name+="_ymd"



        if self._rules["mail"]["select"] is True:
            print("mail_selected")
            self._rules_name+="-MAIL"
            if self._rules["mail"]["name"] is True:
                self._rules_name+="_name"
            if self._rules["mail"]["domain"] is True:
                self._rules_name+="_part"


        if self._rules["slang"]["select"] is True:
            print("slang_selected")
            self._rules_name+="-SLANG"
            if self._rules["slang"]["aka"] is True:
                self._rules_name+="_aka"
            if self._rules["slang"]["part"] is True:
                self._rules_name+="_part"
            if self._rules["slang"]["full"] is True:
                self._rules_name+="_full"



        if self._rules["random"]["select"] is True:
            print("random_selected")
            tmp="-R"+"I"+str(self._rules["random"]["len"]["min"])+"_"+str(self._rules["random"]["len"]["max"])+"I"
            self._rules_name+=tmp 


        if self._rules["other"]["select"] is True:
            print("other_selected")
            tmp="-O"
            self._rules_name+=tmp 


        if self._rules["extra_dic"]["select"] is True:
            print("extra_dic_selected")
            tmp="-E"
            self._rules_name+=tmp 



        if self._rules["total_len"]["select"] is True:
            print("range_selected")
            tmp="-L"+"I"+str(self._rules["total_len"]["range"]["min"])+"_"+str(self._rules["total_len"]["range"]["max"])+"I"
            self._rules_name+=tmp 









    def return_name(self):
        if self._rules_name == "":
            return self._rules_name
        if self._rules_name[0] == "-":
            return self._rules_name[1:]+".json"
        else:
            return self._rules_name+".json"



















if __name__ == "__main__":
    #print(rules_name("./rules.json").return_name())
    for root,dirs,files in os.walk("./rules"):
        #print(files)
        prefix = root
        print(prefix)
        for item in files:
            oldname = os.path.join(prefix,item)
            tmpname = rules_name(oldname).return_name()
            if tmpname == "":
                continue
            newname = os.path.join(prefix,tmpname)
            print(newname)
            os.rename(oldname,newname)
