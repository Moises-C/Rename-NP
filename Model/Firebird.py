# autopep8 --in-place --aggressive --aggressive <file>
import fdb
from tkinter import messagebox

class Firebird:

    def __init__(self):
        self._status_connection = None
        self.successfull = None
        self._CONNECTIONS = {
            'KPI': {
                "host": "kpi",
                "user": "sysdba",
                "pass": "Uzumy152",
                "port": 3050,
                "dialect": 3},
            'AIFA': {
                "host": '51.79.45.195:chapela',
                "port": 3050,
                "user": "sysdba",
                "pass": "masterkey",
                "dialect": 1},
            'REPORT': {
                "host": 'report',
                "port": 3050,
                "user": "sysdba",
                "pass": "Uzumy152",
                "dialect": 3},
            'CASA': {
                "host": '10.1.2.11:CASA', 
                "port": 3050,
                "user": "sysdba",
                "pass": "Arobl3s2024",
                "dialect": 1},
        }

    def stablish_connection(self, key):
        if key in self._CONNECTIONS:
            self.attrib_connection = self._CONNECTIONS[key]
            try:
                self.connect = fdb.connect(
                    dsn=self.attrib_connection["host"],
                    user=self.attrib_connection["user"],
                    password=self.attrib_connection["pass"],
                    port=self.attrib_connection["port"],
                    charset='ISO8859_1',
                    sql_dialect=self.attrib_connection["dialect"])
                self._query = self.connect.cursor()
                self._status_connection = True
            except BaseException as e :
                pass#print(e)
                self._status_connection = False
                # self.errorConexion()

    def status_connection(self):
        return self._status_connection            
    
    def execute(self, query):
        try:
            self._query.execute(query)
        except BaseException as e:
            pass
            #print(e)

    def execute_parameter(self, query, values):
        try:
            self._query.execute(query, values)
            self.successfull = True
        except BaseException as e:
            self.successfull = False
            print(f"Error al ejecutar: {e}")

    def errorConexion(self):
        messagebox.showerror(
            "ERROR...",
            "No se pudo establecer conexión con la base de datos.")

    def close_connection(self):
        try:
            self.connect.close()
            self._query.close()
            self._status_connection = False
        except:
            pass

    def default_titles(self):
        return [titles[0] for titles in self._query.description]

    def result_execute(self):
        return self._query

    def call_procedure(self, procedure, fields):
        self._query.callproc(procedure, fields)

    def save_changes(self):
        self.connect.commit()

    def result_dictonary(self, key):
        unique = {}
        for row in self._query.fetchall():
            if key not in unique:
                unique[row[key]] =row[key+1:]
        return unique

    def records(self):
        records = []
        for record in self.result_execute():
            records.append(list(record))
        return records

    def one_record(self, columna):
        result = None
        for registro in self.result_execute():
            result = registro[columna]
            return result
        return result
