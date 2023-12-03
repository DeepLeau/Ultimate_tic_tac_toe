import time
import math
import sys


def verifier_victoire_grille(board,icone):       
    if board[0]==board[1]==board[2]==icone:
        return True
    elif board[3]==board[4]==board[5]==icone:
        return True
    elif board[6]==board[7]==board[8]==icone:
        return True
    elif board[0]==board[4]==board[8]==icone:
        return True
    elif board[2]==board[4]==board[6]==icone:
        return True
    elif board[0]==board[3]==board[6]==icone:
        return True
    elif board[1]==board[4]==board[7]==icone:
        return True
    elif board[2]==board[5]==board[8]==icone:
        return True
    else:
        return False
    

class Morpion:
    def __init__(self):
        self.board = [
                        [" ", " ", " "," ", " ", " "," ", " ", " "],
                        [" ", " ", " "," ", " ", " "," ", " ", " "],
                        [" ", " ", " "," ", " ", " "," ", " ", " "],
                        [" ", " ", " "," ", " ", " "," ", " ", " "],
                        [" ", " ", " "," ", " ", " "," ", " ", " "],
                        [" ", " ", " "," ", " ", " "," ", " ", " "],
                        [" ", " ", " "," ", " ", " "," ", " ", " "],
                        [" ", " ", " "," ", " ", " "," ", " ", " "],
                        [" ", " ", " "," ", " ", " "," ", " ", " "]
                     ]
        self.mainboard = [" "]*9
        self.tour = 1
        self.dernier_mvmt = [1000]
        self.icones = ["O", "X"]
        
    
    
    def verifier_victoire(self,icone):
        if self.mainboard[0]==self.mainboard[1]==self.mainboard[2]==icone:
            return True
        elif self.mainboard[3]==self.mainboard[4]==self.mainboard[5]==icone:
            return True
        elif self.mainboard[6]==self.mainboard[7]==self.mainboard[8]==icone:
            return True
        elif self.mainboard[0]==self.mainboard[4]==self.mainboard[8]==icone:
            return True
        elif self.mainboard[2]==self.mainboard[4]==self.mainboard[6]==icone:
            return True
        elif self.mainboard[0]==self.mainboard[3]==self.mainboard[6]==icone:
            return True
        elif self.mainboard[1]==self.mainboard[4]==self.mainboard[7]==icone:
            return True
        elif self.mainboard[2]==self.mainboard[5]==self.mainboard[8]==icone:
            return True
        else:
            return False
        
    def annuler_coup(self, coup):
        grille, position = coup
        self.board[grille][position] = " "
        self.tour -= 1
    
    def verifier_nulle(self):
        compteur = 0
        for i in range(9):
            for j in range(9):
                if self.board[i][j]!=" ":
                    compteur += 1
        if compteur == 81:
            return True
        return False
    
    def mouvement_possible_IA(self):
        coups_possibles = []
        grille = self.grille_possible(self.dernier_mvmt[-1])
        if grille == 1000:
            for morpion in range(9):
                for case in range(9):
                    coups_possibles.append(self.board[morpion][case])
        else :
            if self.mainboard[grille] == " ":
                coups_possibles.append((grille, self.grille_possible(grille)))
            else:
                for morpion in range(9):
                    if self.mainboard[morpion] == " ":
                        for i in range(9):
                            if self.board[morpion][i] == " ":
                                coups_possibles.append((morpion, i))
        return coups_possibles


    
    def grille_possible(self,dernier_mouvement):
        y = dernier_mouvement
        morpion1 = [9*i for i in range(0,9)]
        morpion2 = [9*i + 1 for i in range(0,9)]
        morpion3 = [9*i + 2 for i in range(0,9)]
        morpion4 = [9*i + 3 for i in range(0,9)]
        morpion5 = [9*i + 4 for i in range(0,9)]
        morpion6 = [9*i + 5  for i in range(0,9)]
        morpion7 = [9*i + 6  for i in range(0,9)]
        morpion8 = [9*i + 7 for i in range(0,9)]
        morpion9 = [9*i + 8 for i in range(0,9)]
        
        if y in morpion1:
            return 0
        if y in morpion2:
            return 1
        if y in morpion3:
            return 2
        if y in morpion4:
            return 3
        if y in morpion5:
            return 4
        if y in morpion6:
            return 5
        if y in morpion7:
            return 6
        if y in morpion8:
            return 7
        if y in morpion9:
            return 8
        else :
            return 1000
        
    def morpion_gagne(self,position):
        if self.mainboard[position]=="X" or self.mainboard[position] == "O":
            return True
        return False
    
    def jouer_IA(self, coup):
        grille = coup[0]
        position = coup[1]
        self.dernier_mvmt.append(position)
        if self.tour % 2 == 0:
            self.board[grille][position] = self.icones[1]
        else:
            self.board[grille][position] = self.icones[0]
        self.tour += 1

    
    def jouer_humain(self):
        X = self.grille_possible(self.dernier_mvmt[-1])
        if X == 1000:
            X = int(input("Vous pouvez jouer sur n'importe quelle morpion, choisissez un morpion entre 0 et 8 : "))
            while X not in [0,1,2,3,4,5,6,7,8]:
                print("Vous avez sélectionné un mauvais numéro")
                X = int(input("Sélectionnez un nombre entre 0 et 8 : "))
            y = int(input("Choisissez une case du morpion entre 0 et 8 : "))
            while y not in [0,1,2,3,4,5,6,7,8]:
                print("Vous avez sélectionné un mauvais numéro")
                y = int(input("Sélectionnez un nombre entre 0 et 8 : "))
        else :  
            if self.mainboard[X]!=" ":
                print("Ce morpion a déjà été gagné, vous pouvez sélectionner n'importe quel autre morpion non gagné")
                X = int(input("Sélectionnez un morpion entre 0 et 8 : "))
                while X not in [0,1,2,3,4,5,6,7,8]:
                    print("Vous avez sélectionné un mauvais numéro")
                    X = int(input("Sélectionnez un nombre entre 0 et 8 : "))
                y = int(input("Choisissez une case du morpion entre 0 et 8 : "))
                while y not in [0,1,2,3,4,5,6,7,8]:
                    print("Vous avez sélectionné un mauvais numéro")
                    y = int(input("Sélectionnez un nombre entre 0 et 8 : "))
            else :
                print("Vous ne pouvez jouer que dans le morpion numéro", X)
                y = int(input("Sélectionnez un nombre entre 0 et 8 : "))
                while y not in [0,1,2,3,4,5,6,7,8]:
                    print("Vous avez sélectionné un mauvais numéro")
                    y = int(input("Sélectionnez un nombre entre 0 et 8 : "))
                while self.board[X][y] != " ":
                    print("Vous ne pouvez pas sélectionner cette case, elle est déjà occupé")
                    y = int(input("Resélectionnez une case : "))
        self.dernier_mvmt.append(y)
        if self.tour%2 == 0:
            self.board[X][y] = self.icones[1]
        else :
            self.board[X][y] = self.icones[0]
        self.tour += 1
        return X

    def evaluer(self):
        score = 0
        for i in range(9):
            if self.mainboard[i] == 'X':
                score += 10
            elif self.mainboard[i] == 'O':
                score -= 10
            else:
                # Évaluation pour bloquer l'adversaire et diriger vers une autre grille
                if self.tour % 2 == 0:
                    # Évaluation pour les cases vides du joueur O
                    score += self.evaluer_cases_vides(i, 'O')
                else:
                    # Évaluation pour les cases vides du joueur X
                    score -= self.evaluer_cases_vides(i, 'X')
        return score

    def evaluer_cases_vides(self, grille, icone):
        score = 0
        cases_vides = []
        for i in range(9):
            if self.board[grille][i] == " ":
                cases_vides.append(i)
        for case in cases_vides:
            # Évaluation pour diriger l'adversaire vers une autre grille
            if grille in [0, 2, 6, 8] and case == 4:
                score += 5
            elif grille == 4 and case in [0, 2, 6, 8]:
                score += 5
            else:
                score += 1
        return score



    
class Minimax:
    
    def __init__(self, profondeur):
        self.profondeur = profondeur
        self.alpha = float('-inf')
        self.beta = float('inf')

    def effectuer_coup(self, partie, joueurMaximisant):
        if joueurMaximisant:
            valeur, coup = self.minimax(partie, self.profondeur, float('-inf'), float('inf'), joueurMaximisant)
        else:
            valeur, coup = self.minimax(partie, self.profondeur, float('-inf'), float('inf'), joueurMaximisant)
        return coup



    def minimax(self, partie, profondeur, alpha, beta, joueurMaximisant):
        if profondeur == 0 or partie.verifier_nulle() or partie.verifier_victoire(partie.icones[partie.tour % 2]):
            return partie.evaluer(), None
    
        if joueurMaximisant:
            evalMax = float('-inf')
            meilleurCoup = None
            for coup in partie.mouvement_possible_IA():
                partie.jouer_IA(coup)
                eval = self.minimax(partie, profondeur - 1, alpha, beta, False)[0]
                partie.annuler_coup(coup)
                if eval > evalMax:
                    evalMax = eval
                    meilleurCoup = coup
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return evalMax, meilleurCoup
    
        else:
            evalMin = float('inf')
            meilleurCoup = None
            for coup in partie.mouvement_possible_IA():
                partie.jouer_IA(coup)
                eval = self.minimax(partie, profondeur - 1, alpha, beta, True)[0]
                partie.annuler_coup(coup)
                if eval < evalMin:
                    evalMin = eval
                    meilleurCoup = coup
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return evalMin, meilleurCoup




    
game = Morpion()   

ai = Minimax(5)

# Structure du jeu

game_over = False

while game_over == False and game.verifier_nulle() == False :
    
    print("-------------   -------------   -------------") 
    print("|", game.board[0][0], "|", game.board[0][1], "|", game.board[0][2], "|"," ","|", game.board[1][0], "|", game.board[1][1], "|", game.board[1][2],"|"," ","|", game.board[2][0], "|", game.board[2][1], "|", game.board[2][2], "|")  
    print("-------------   -------------   -------------") 
    print("|", game.board[0][3], "|", game.board[0][4], "|", game.board[0][5], "|"," ","|", game.board[1][3], "|", game.board[1][4], "|", game.board[1][5],"|"," ","|", game.board[2][3], "|", game.board[2][4], "|", game.board[2][5], "|")  
    print("-------------   -------------   -------------") 
    print("|", game.board[0][6], "|", game.board[0][7], "|", game.board[0][8], "|"," ","|", game.board[1][6], "|", game.board[1][7], "|", game.board[1][8],"|"," ","|", game.board[2][6], "|", game.board[2][7], "|", game.board[2][8], "|")  
    print("-------------   -------------   -------------") 
    print("\n")
    print("-------------   -------------   -------------") 
    print("|", game.board[3][0], "|", game.board[3][1], "|", game.board[3][2], "|"," ","|", game.board[4][0], "|", game.board[4][1], "|", game.board[4][2],"|"," ","|", game.board[5][0], "|", game.board[5][1], "|", game.board[5][2], "|")  
    print("-------------   -------------   -------------") 
    print("|", game.board[3][3], "|", game.board[3][4], "|", game.board[3][5], "|"," ","|", game.board[4][3], "|", game.board[4][4], "|", game.board[4][5],"|"," ","|", game.board[5][3], "|", game.board[5][4], "|", game.board[5][5], "|")  
    print("-------------   -------------   -------------") 
    print("|", game.board[3][6], "|", game.board[3][7], "|", game.board[3][8], "|"," ","|", game.board[4][6], "|", game.board[4][7], "|", game.board[4][8],"|"," ","|", game.board[5][6], "|", game.board[5][7], "|", game.board[5][8], "|")  
    print("-------------   -------------   -------------") 
    print("\n")
    print("-------------   -------------   -------------") 
    print("|", game.board[6][0], "|", game.board[6][1], "|", game.board[6][2], "|"," ","|", game.board[7][0], "|", game.board[7][1], "|", game.board[7][2],"|"," ","|", game.board[8][0], "|", game.board[8][1], "|", game.board[8][2], "|")  
    print("-------------   -------------   -------------") 
    print("|", game.board[6][3], "|", game.board[6][4], "|", game.board[6][5], "|"," ","|", game.board[7][3], "|", game.board[7][4], "|", game.board[7][5],"|"," ","|", game.board[8][3], "|", game.board[8][4], "|", game.board[8][5], "|")  
    print("-------------   -------------   -------------") 
    print("|", game.board[6][6], "|", game.board[6][7], "|", game.board[6][8], "|"," ","|", game.board[7][6], "|", game.board[7][7], "|", game.board[7][8],"|"," ","|", game.board[8][6], "|", game.board[8][7], "|", game.board[8][8], "|")  
    print("-------------   -------------   -------------") 


    # Tour du joueur humain 
        
    ai.joueurMaximisant = False
    X = game.jouer_humain()
        
    if game.tour%2 == 0:
        if verifier_victoire_grille(game.board[X],game.icones[0]) == True:
            game.mainboard[X] = game.icones[0]
            print("Félicitations joueur 1, vous avez remporté le morpion numéro",X)
            time.sleep(3)
    elif game.tour%2 != 0:
        if verifier_victoire_grille(game.board[X],game.icones[1]) == True:
            game.mainboard[X] = game.icones[1]
            print("Félicitations joueur 2, vous avez remporté le morpion numéro",X)
            time.sleep(3)

    if game.tour%2 == 0:
        game_over = game.verifier_victoire(game.icones[0])
        if game_over:
            print("Le joueur numéro 1 a gagné la partie")
            sys.exit()
    else :
        game_over = game.verifier_victoire(game.icones[1])
        if game_over :
            print("Le joueur numéro 2 a gagné la partie")
            sys.exit()

    #Tour de l'IA

    print("Au tour de l'ordinateur")
    ai.joueurMaximisant = True
    coup = ai.effectuer_coup(game,ai.joueurMaximisant)            
    game.jouer_IA(coup)
    (X,y) = coup
    
    if game.tour%2 == 0:
        if verifier_victoire_grille(game.board[X],game.icones[0]) == True:
            game.mainboard[X] = game.icones[0]
            print("Félicitations joueur 1, vous avez remporté le morpion numéro",X)
            time.sleep(3)
    elif game.tour%2 != 0:
        if verifier_victoire_grille(game.board[X],game.icones[1]) == True:
            game.mainboard[X] = game.icones[1]
            print("Félicitations joueur 2, vous avez remporté le morpion numéro",X)
            time.sleep(3)

    if game.tour%2 == 0:
        game_over = game.verifier_victoire(game.icones[0])
        if game_over:
            print("Le joueur numéro 1 a gagné la partie")
            sys.exit()
    else :
        game_over = game.verifier_victoire(game.icones[1])
        if game_over :
            print("Le joueur numéro 2 a gagné la partie")
            sys.exit()

        
print("Il y a match nul")
time.sleep(5)
    