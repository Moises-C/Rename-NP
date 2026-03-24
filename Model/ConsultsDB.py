from Model.Firebird import Firebird

class Consults:
    key = None
    
    def __init__(self):
        self.db = Firebird()
    
    def execute(self, query):
        try:
            self.titles_default = None
            self.db.stablish_connection(self.key)
            if self.db.status_connection():
                self.db.execute(query)
                records = self.db.records()
                self.titles_default = self.db.default_titles()
                self.close_connection()
                return records
            else:
                return f"No se pudo establecer conexion con la BD {self.key}"
        except BaseException as e:
            print(e)
            self.close_connection()
            return []

    def insert_arg(self, query, values):
        self.titles_default = None
        self.db.stablish_connection(self.key)
        if self.db.status_connection:
            self.db.execute_parameter(query, values)
            if self.db.successfull:
                self.save()
            self.close_connection()
        return self.db.successfull
                
    def execute_as_parameter(self,query, values):
        try:
            self.titles_default = None
            self.db.stablish_connection(self.key)
            if self.db.status_connection():
                self.db.execute_parameter(query, values)
                records = self.db.records()
                self.titles_default = self.db.default_titles()
                self.close_connection()
                return records
            else:
                return f"No se pudo establecer conexion con la BD {self.key}"
        except BaseException as e:
            self.close_connection()
            return []

    def execute_as_dict(self, query, key):
        try:
            self.titles_default = None
            self.db.stablish_connection(self.key)
            self.db.execute(query)
            records = self.db.result_dictonary(key)
            self.titles_default = self.db.default_titles()
            self.close_connection()
            return records
        except BaseException as e:
            #print(f"ERROR: {e}")
            self.close_connection()
            return []

    def save(self):
        self.db.save_changes()

    def execute_save_changes(self, query):
        self.db.stablish_connection(self.key)
        self.db.execute(query)
        self.db.save_changes()
        self.db.close_connection()

    def close_connection(self):
        self.db.close_connection()