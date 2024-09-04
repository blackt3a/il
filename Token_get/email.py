




#ab@c.d.e
#a b@c.d.e
class token_email:
    def __init__(self,email):
        self._email = email
        self._token_list = []
        self.generate_token()


    def generate_token(self):
        slices = self._email.split("@")
        self._token_list.append("@")
        for item in slices:
            self._token_list.append(item)

            if " " in item:
                tmp = item.split(" ")
                self._token_list+=tmp


                
            if "." in item:
                tmp = item.split(".")
                self._token_list+=tmp



        
    def get_token(self):
        return self._token_list











if __name__ == "__main__":
    e = token_email("a b@c.d.e")
    print(e.get_token())
