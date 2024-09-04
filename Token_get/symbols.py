







class token_symbols:
    def __init__(self):
        self._symbol_lsit = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    



    def get_symbols(self):
        return self._symbol_lsit




if __name__ == "__main__":
    sym = token_symbols()
    print(sym.get_symbols())
