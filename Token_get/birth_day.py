

#birth_day should be like "2007-11-01"
class token_birth_day:
    def __init__(self,birth_day,config):
        self._birth_day = birth_day
        self._token_list = []
        
        #get split year month day to _token_list
        self._y_m_d = self._birth_day.split("-")
        
        self._bir_dic = {
                "year":self._y_m_d[0],
                "month":self._y_m_d[1],
                "day":self._y_m_d[2]
                }


        if config["combin"]["Y_M_D"] is True:
            self.Y_M_D()

        #conbia of year and month
        if config["combin"]["Y_M"] is True:
            self.Y_M()

        #conbia of month and day
        if config["combin"]["M_D"] is True:
            self.M_D()


        if config["separat"]["Y"] is True:
            self._token_list.append(self._bir_dic["year"])

        if config["separat"]["M"] is True:
            self._token_list.append(self._bir_dic["month"])

        if config["separat"]["D"] is True:
            self._token_list.append(self._bir_dic["day"])


    def Y_M_D(self):
        self._token_list.append(self._bir_dic["year"]+self._bir_dic["month"]+self._bir_dic["day"])
 
    def Y_M(self):
        #"0711" "200711"
        
        #self._token_list.append("".join(self._y_m_d[0]).join(self._y_m_d[1])) #bug here
        self._token_list.append(self._bir_dic["year"]+self._bir_dic["month"])
        self._token_list.append(self._bir_dic["year"][2:]+self._bir_dic["month"])


    def M_D(self):
        #“1101” 
        self._token_list.append(self._bir_dic["month"]+self._bir_dic["day"])


    def get_token(self):
        return self._token_list
    

if __name__ == "__main__":
    bd = token_birth_day("2007-11-01")
    print(bd._bir_dic)
    print(bd.get_token())
