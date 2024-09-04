import json
import os
import itertools
import sys
import time
from Token_get.name import token_name
from Token_get.birth_day import token_birth_day
from Token_get.tel import token_tel
from Token_get.symbols import token_symbols
from Token_get.email import token_email
from Token_get.extra_dic import token_extra
from Log.log import _log
from Utils.result import _result





'''
#person data
{
    "name": "stephen wang",
    "tel": "7577464268",
    "work_addr":"some where",
    "home_addr":"some where else",
    "birth":"2007-11-07"
    "mail":"a b@c.d.e",
    "slang":"fuck man!",
    "other":"unknow"
}


#rule
{
    "name": True,
    "tel": True,
    "work_addr":False,
    "home_addr":False,
    "birth":True,
    "mail": True,
    "slang":False,
    "other":False,
    "extra_dic":True
}


'''



#open rule.json 


class psk_rules:
    def __init__(self,rules_file,person_file,save_file=None,extra_file=None):
        self._log = _log("psk")

        #init rules
        self._jr = self.load_json(rules_file)
        #init person
        self._jp = self.load_json(person_file)


        self._extra = extra_file

        self._file_name = save_file


        self._total_list = []
    
        self.parse_rules()
        
        self.generate_psks(save_file)
        
        self._result = _result(status="success",filepath=save_file,token_list=self._total_list)

    def load_json(self,file):
        self._log.info("loading =====>"+file)
        with open(file,"r") as target:
            data = json.load(target)
            return data

        self._log.info("load success")










    def parse_rules(self):
        if self._jr["name"]["select"] is True:
            self._log.info("name_selected")
            self._total_list+= token_name(self._jp["name"],self._jr["name"]).get_token()

        if self._jr["phone"]["select"] is True:
            self._log.info("tel_selected")
            self._total_list+= token_tel(self._jp["phone"],self._jr["phone"]).get_token()


        if self._jr["birth"]["select"] is True:
            self._log.info("birth_selected")
            self._total_list+= token_birth_day(self._jp["birth"],self._jr["birth"]).get_token()



        if self._jr["mail"]["select"] is True:
            self._log.info("mail selected")
            pass
            #self._total_list+= token_email(self._jp["mail"],self._jr["mail"]).get_token()


        if self._jr["extra_dic"]["select"] is True and self._extra is not None:
            self._log.info("extra_dic selected")
            pass
            #self._total_list+= token_extra(self._extra).get_token()


        self._log.info("parse finished")
        self._log.info("token_list====>"+str(self._total_list))

#   def generate_psks(self):
#       all_permutations = [list(itertools.permutations(self._total_list, r)) for r in range(1, len(self._total_list) + 1)]
#       for length, permutations in enumerate(all_permutations, start=1):
#           #print(f"Permutations of length {length}:")
#           for perm in permutations:
#               psk_string = ''.join(str(x) for x in perm)
#               if len(psk_string) >= 6:
#                   print(psk_string)


    def generate_psks(self,save_file):
        with open(save_file,"w") as target:
#           perm_gen = itertools.permutations(self._total_list)
#           for perm in perm_gen:
#               psk_string = ''.join(str(x) for x in perm)
#               target.write(psk_string+'\n')


            min_len = 6
            max_len = 20
            if self._jr["total_len"]["select"] is True:
                min_len = self._jr["total_len"]["min"]
                max_len = self._jr["total_len"]["max"]
                
            for r in range(1, len(self._total_list) + 1):
                
                for perm in itertools.permutations(self._total_list, r):
                    psk_string = ''.join(str(x) for x in perm)
                    if len(psk_string) >= min_len  and len(psk_string) <= max_len:
                        target.write(psk_string+'\n')






def main(rules,person_info):
    
    currentT = time.time()
    localT = time.localtime(currentT)

    timestamp = time.strftime("%Y%m%d%H%M%S",localT)

    rules = psk_rules(rules_file=rules,person_file=person_info,save_file=os.getcwd()+"/out/"+timestamp+".txt")
    rules._result.get_result()
    


if __name__ == "__main__":
    if len(sys.argv)!= 3:
        print("argc err")
        print("python3 rule.py rules.json person_info.json")
        sys.exit(1)
    main(sys.argv[1],sys.argv[2])












