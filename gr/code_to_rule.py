import json













"""
00000101000000000000000000000101101011
00000101000000000000000000000101101010
00000101000000000000000000000101101021
00000101000000000000000000000101101020
00000101000000000000000000000101101031
00000101000000000000000000000101101030
00000101000000000000000000000101101041
00000101000000000000000000000101101040
00000101000000000000000000000101101051
00000101000000000000000000000101101050
#total      = 100000000000000000000000000000000000000
#               #3
#name       =  000 #5
#phone      =     00000 #3
#place      =          000 #3
#addr       =             000 #3
#door       =                000  #6
#birth      =                   000000 #2
#mail       =                         00 #3
#slang      =                           000 #4
#random     =                              0000 #1
#extra_dic  =                                  0  #4
#total_len  =                                   0000 #1
#other      =                                       0


"""


class ctr:
    def __init__(self,code):
        self._code=""
        if isinstance(code,str):
            self._code=code
        elif isinstance(code,int):
            self._code="{:038d}".format(code)
        else:
             pass

        with open("./rules.json","r") as target:
            self._tmp_rule = json.load(target)
        


        #print(self._tmp_rule)
#        with open("./bit_rules.json","r") as target:
#            self._len = json.load(target)

        self._len={

                "name":{
                    "aka": 1,
                    "part":1,
                    "full":1,
                    "_t":3
                    },


                "phone":{
                    "total":1,
                    "min":  2,
                    "max":  2,
                    "_t":   5
                    },

                "place":{
                    "aka": 1,
                    "part":1,
                    "full":1,
                    "_t":  3
                    },

                "addr":{
                    "aka":1,
                    "part":1,
                    "full":1,
                    "_t":  3
                    },
                "door":{
                    "aka":1,
                    "part":1,
                    "full":1,
                    "_t":  3
                    },
                "birth":{
                    "Y":1,
                    "M":1,
                    "D":1,
                    "Y_M":1,
                    "M_D":1,
                    "Y_M_D":1,
                    "_t":6
                    },

                "mail":{
                    "name":1,
                    "domain":1,
                    "_t":2
                    },
                "slang":{
                    "aka":1,
                    "part":1,
                    "full":1,
                    "_t":3
                    },

                "random":{
                    "min":2,
                    "max":2,
                    "_t":4
                    },

                "other":{
                        "_t":1
                    },
                "extra_dic":{
                        "_t":1
                    },

                "total_len":{
                    "min":2,
                    "max":2,
                    "_t":4
                    }

            }

        print(self._len)












#total      = 100000000000000000000000000000000000000
#               #3
#name       =  000 #5
#phone      =     00000 #3
#place      =          000 #3
#addr       =             000 #3
#door       =                000  #6
#birth      =                   000000 #2
#mail       =                         00 #3
#slang      =                           000 #4
#random     =                              0000 #1
#extra_dic  =                                  0  #4
#total_len  =                                   0000 #1
#other      =                                       0







        self.dic = {
                "name":{
                    "_aka": 1*(10**37),                
                    "_part":1*(10**36),                
                    "_full":1*(10**35)                
                    },
                "phone":{
                    "_total":1*(10**34),
                    "_min":1*(10**32),
                    "_max":1*(10**30),
                    },
                "place":{
                    "_aka": 1*(10**29),                
                    "_part":1*(10**28),                
                    "_full":1*(10**27)                
                    },

                "addr":{
                    "_aka": 1*(10**26),                
                    "_part":1*(10**25),                
                    "_full":1*(10**24)                
                    },

                "door":{
                    "_aka": 1*(10**23),                
                    "_part":1*(10**22),                
                    "_full":1*(10**21)                
                    },


                "birth":{
                    "_Y":1*(10**20),
                    "_M":1*(10**19),
                    "_D":1*(10**18),
                    "_Y_M":1*(10**17),
                    "_M_D":1*(10**16),
                    "_Y_M_D":1*(10**15),
                    },

                "mail":{
                    "_name":1*(10**14),
                    "_domain":1*(10**13)
                    },

                "slang":{
                    "_aka":1*(10**12),
                    "_part":1*(10**11),
                    "_full":1*(10**10)
                    },

                "random":{
                        "_min":1*(10**9),
                        "_max":1*(10**7)
                    },
                "extra_dic":{
                        "_t":1*(10**5)
                        },
                "total_len":{
                        "_min":1*(10**4),
                        "_max":1*(10**2)
                        },

                "other":{
                        "_t":1
                        }









                }

    def get_code(self):
        return self._code

    def get_rule(self):
        if self._code:
            pass
        


























        print(self._tmp_rule)

a = ctr(101000000000000000000000101101011)
print(a.get_code())


