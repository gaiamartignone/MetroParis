from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._fermate = DAO.getAllFermate()
        self.mapid = {}
        for f in self._fermate:
            self.mapid[f.id_fermata] = f
        self.g = nx.DiGraph()
        self.gpesato = nx.DiGraph()
        self.gmulti= nx.MultiDiGraph

    def getBFSNodesFromTree(self, source):
        tree = nx.bfs_tree(self.g, source)
        nodi = list(tree.nodes())
        return nodi[1:]

    def getDFSNodesFromTree(self, source):
        tree = nx.dfs_tree(self.g, source)
        nodi = list(tree.nodes())
        return nodi[1:]

    def getBFSNodesFromEdges(self, source):
        archi = nx.bfs_edges(self.g, source)
        res = []
        for u, v in archi:
            res.append(v)
        return res

    def getDFSNodesFromEdges(self, source):
        archi = nx.dfs_edges(self.g, source)
        res = []
        for u, v in archi:
            res.append(v)
        return res

    def buildGraph(self):
        self.g.clear()
        self.g.add_nodes_from(self._fermate)
        #aggiungo anche gli archi
        self.modo3()

    def buildGraphPesato(self):
        self.gpesato.clear()
        self.gpesato.add_nodes_from(self._fermate)
        # aggiungo anche gli archi
        self.pesato()

    def pesato(self):
        self.buildGraph()
        for f,j in self.g.edges:
                peso = DAO.pesato(f.id_fermata,j.id_fermata)
                if f!=j and peso>0:
                    print(f.id_fermata,j.id_fermata,peso)
                    self.gpesato.add_edge(f,j, weight=peso)

    def pesatov2(self):


    def modo1(self):
        for f in self._fermate:
            for j in self._fermate:
                if f!=j and DAO.modo1(f.id_fermata,j.id_fermata):
                    self.g.add_edge(f,j)

    def modo2(self):
        for f in self._fermate:
            for conn in DAO.modo2(f):
                self.g.add_edge(f, self.mapid[conn.id_stazA])

    def modo3(self):
        for conn in DAO.modo3():
            self.g.add_edge(self.mapid[conn.id_stazP], self.mapid[conn.id_stazA])

    def getNumNodi(self):
        return len(self.g.nodes)

    def getNumArchi(self):
        return len(self.g.edges)


    @property
    def fermate(self):
        return self._fermate


if __name__ == "__main__":
    m = Model()
    m.pesato()
