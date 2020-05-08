import cherrypy
import sys
import json
from random import choice

class Server:
   
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
     
    def move(self):
        # Deal with CORS
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        cherrypy.response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
        if cherrypy.request.method == "OPTIONS":
            return ''     
        self.body = cherrypy.request.json
        self.board=self.body["game"]
        self.players=self.body["players"]
        self.you=self.body["you"]
        movefinal=self.AI()
        
        return {"move": {"from": movefinal[0] ,"to" : movefinal[1]},"message": "alors?" }
    #Fonction qui détermine tous les moves possibles en fonction de l'état du jeu.
    #Retourne une liste contenant des listes de couple de coordonées (from,to)    
    def possible_moves(self):
        moves = []
        for i in range(0,9):
            for j in range(0,9):
                if self.board[i][j]:
                    for k in range(-1,2):
                        for l in range(-1,2):
                            if not(k==0 and l==0)and i+k>=0 and i+k<=8 and j+l>=0 and j+l<=8 and(len(self.board[i][j])+len(self.board[i+k][j+l])<=5)and(self.board[i+k][j+l]):
                                moves.append([[i,j],[i+k,j+l]])
        return moves
    #Fonction qui permet de determiner quels sont les pions de l'ia.
    #Renvoie 0 ou 1         
    def wich_player(self):
        if self.players[0] == self.you:
            return 0 
        else:
            return 1 
    #Fonction qui vérifie plateau de jeu afin de déterminer si il y a possibilité de créer une tour de 5
    #Retourne un move possible ou False    
    def tour5(self):
        for move in self.possible_moves():
            if len(self.board[move[0][0]][move[0][1]])+len(self.board[move[0][0]][move[0][1]])==5 and self.board[move[0][0]][move[0][1]][-1]==self.wich_player():
                if self.board[move[1][0]][move[1][1]][-1]!=self.wich_player():
                    return move
        return False
    #Fonction qui vérifie le plateau de jeu afin de déterminer si il y a possibilité de prendre une tour
    #Retourne un move possible ou False 
    def take_a_tour(self):
        for move in self.possible_moves():
            if len(self.board[move[0][0]][move[0][1]])+len(self.board[move[0][0]][move[0][1]])<5 and self.board[move[0][0]][move[0][1]][-1]==self.wich_player():
                if self.board[move[1][0]][move[1][1]][-1]!=self.wich_player():
                    return move
        return False
    #Algorythme qui va renvoyer le meilleur move possible en fonction de l'état du jeu 
    def AI(self):
        if self.tour5()==False:
            if self.take_a_tour()==False:
                return choice(self.possible_moves())
            else:
                return self.take_a_tour()
        else:
            return self.tour5()
    @cherrypy.expose
    #Route ping
    def ping(self):
        return "pong"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=8082

    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': port})
    cherrypy.quickstart(Server())
