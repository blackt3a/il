

class token_tel:
    def __init__(self,tel,config):
        self._tel= tel

        self._token_list = []
        #print(config)

        if config["total"] is True:
            self._token_list.append(self._tel)
        
        if config["slice_len"]["select"] is True:
            self._token_list+= self.generate_slice(min_len=config["slice_len"]["min"],max_len=config["slice_len"]["max"])


 
    def generate_slice(self,min_len=3,max_len=7):
        slices = []

        '''
        123456789
        len=3
        123,456,789
        234,567,89
        len=4
        1234,5678,9
        2345,6789
        '''
        for i in range(min_len,max_len+1):
            start = 0
            #print(i)
            while start < len(self._tel):
                end = start + i
                if end >= len(self._tel):
                    end = len(self._tel)

                slices.append(self._tel[start:end])

                start = end


        return slices
            










    def get_token(self):
        return self._token_list
    

if __name__ == "__main__":
    tel = token_tel("12345667")
    print(tel.get_token())
