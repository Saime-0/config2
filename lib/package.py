class Package:
    def  __init__(self, id):
        self._id = id

    def id(self) -> str:
        return self._id
    
    # def id() -> str:
    #     raise NotImplementedError