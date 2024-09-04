import json




class rules_name:
    def __init__(self,rules_file):
        self._rules = self.ld_rules_file(rules_file)
        self._rules_name = ""
        self.analyse()


    def ld_rules_file(self,rules_file):
        
        with open(rules_file,"r") as target:
            data = target.read()
            rules = json.load(data)
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



        if self._jr["phone"]["select"] is True:
            print("tel_selected")
            self._rules_name+="-PHONE"
            if self._rules["phone"]["total"] is True:
                self._rules_name+="_total"

            if self._rules["phone"]["slice_len"]["select"] is True:
                tmp = "_slice_len"+"<"+self._rules["phone"]["slice_len"]["min"]+"_"+self._rules["phone"]["slice_len"]["max"]+">"
                self._rules_name+=tmp

        
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

            if self._rules["birth"]["separat"]["M_D"] is True:
                self._rules_name+="_md"

            if self._rules["birth"]["separat"]["Y_M_D"] is True:
                self._rules_name+="_ymd"




        if self._rules["total_len"]["select"] is True:
            print("range_selected")
            tmp="-R"+"<"+str(self._rules["total_len"]["range"]["min"])+"_"+str(self._rules["total_len"]["range"]["max"])+">"
            self._rules_name+=tmp 









        def re_name(self):
            return self._rules_name



















if __name__ == "__main__":
    pass
