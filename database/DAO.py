import math

from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.fermata import Fermata


class DAO:

    @staticmethod
    def getAllFermate():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM fermata"
        cursor.execute(query)

        for row in cursor:
            result.append(Fermata(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def modo1(f1,f2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM connessione 
                         WHERE id_stazP =%s and id_stazA=%s """

        cursor.execute(query,(f1,f2,))

        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        if len(result)>0:
            return True
        else:
            return False

    @staticmethod
    def modo2(f1):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM connessione 
                            WHERE id_stazP =%s """

        cursor.execute(query, (f1,))

        for row in cursor:
            result.append(Connessione(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def modo3():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM connessione """

        cursor.execute(query,)

        for row in cursor:
            result.append(Connessione(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def pesato(f1,f2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT id_stazP, id_stazA FROM connessione 
                         WHERE id_stazP =%s and id_stazA=%s """

        cursor.execute(query,(f1,f2,))

        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return len(result)

    @staticmethod
    def multigrafo(self, idmapfermate):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT c.id_stazP, c.id_stazA, l.id_linea, l.velocita
                    FROM connessione c, fermata f1, fermata f2, linea l
                    WHERE c.id_stazP =f1.id_fermata and c.id_stazA =f2.id_fermata and l.id_linea = c.id_linea  """

        cursor.execute(query,)

        for row in cursor:
            sP = idmapfermate[row['id_stazP']]
            sA = idmapfermate[row['id_stazA']]
            tempo = math.sqrt((sP.coordX-sA.coordX)**2 + (sP.coordY-sA.coordY)**2)
            result.append((sP,sA,tempo))
        cursor.close()
        conn.close()
        return result


