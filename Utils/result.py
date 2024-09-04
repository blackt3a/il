import json

success = "success"
fail = "fail"

class _result:
    def __init__(self,status,remark=None,filepath=None,token_list=None):
        if status not in ["success","fail"]:
            raise BaseException("Must be success or fail")
        self._status = status

        if remark is None:
            self._remark = ""
        else:
            self._remark = remark

        if filepath is None:
            self._filepath = ""
        else:
            self._filepath  = filepath

        if token_list is None:
            self._token_list = []
        else:
            self._token_list = token_list

        self._result = {
                "status":self._status,
                "remark":self._remark,
                "filepath":self._filepath,
                "token":self._token_list
                }

    def get_result(self):
        return print(json.dumps(self._result))



if __name__ == "__main__":
    r = _result("fail")
    print(r.get_result())
