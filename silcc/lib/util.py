class CIList(list):


    def __contains__(self, key):
        for t in self:
            if key.lower() == t.lower():
                return True
        return False



        
