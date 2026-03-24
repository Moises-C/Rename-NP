from Model.ConsultsDB import Consults
from Model.Query import Query

class  ConsultRepository:

    def __init__(self):
        self.consult = Consults()
        self.query = Query()

    def get_custom_declare(self):
        self.consult.key = "CASA"
        return self.consult.execute(self.query.custom_declare())
