







class token_extra:
    def __init__(self,target_file="extra.txt"):
        self._token_list = []
        self._target_file = target_file
        with open(self._target_file,"r") as target:
            data = target.read()
            self._token_list = data.split()




    def get_token_list(self):
        return self._token_list









if __name__ == "__main__":
    ex = token_extra("extra.txt")
    print(ex.get_token_list())
