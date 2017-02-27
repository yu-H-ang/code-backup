import numpy as np
import matplotlib.pyplot as plt
import sys

class Sudoku:
    def __init__(self):
        # build the sudoku board
        # @N: board size, 9
        # @n: board subgrid size 3
        # fill every block with a permutation of 1 to 9
        self.N = 9
        self.n = 3
        self.board = np.zeros((self.N, self.N), dtype=int)
        for i in range(0, self.N, self.n):
            for j in range(0, self.N, self.n):
                self.board[i:i+self.n, j:j+self.n] = \
                np.random.permutation(range(1, 1+self.N)).reshape(self.n, self.n)
    def __repr__(self):
        return('Sudoku(\nboard:\n%s\ncost:%d\n)'%(self.board, self.cost()))
    def printBoard(self):
        # print the board to screen
        for i in range(self.n):
            sys.stdout.write('+-------+-------+-------+\n')
            for j in range(self.n):
                sys.stdout.write('|')
                for k in range(self.n):
                    for l in range(self.n):
                        sys.stdout.write(' %d'%self.board[3*i+j,3*k+l])
                    sys.stdout.write(' |')
                sys.stdout.write('\n')
        sys.stdout.write('+-------+-------+-------+\n')
    def cost(self):
        # calculate the cost of a board,
        # defined as the number of duplicates in rows and columns
        costRow = sum([self.N-len(set(self.board[i,:])) for i in range(self.N)])
        costCol = sum([self.N-len(set(self.board[:,j])) for j in range(self.N)])
        return costRow + costCol
    def neighbor(self):
        newSdk = Sudoku()
        block = np.random.choice(range(self.N))
        switch = np.random.choice(range(self.N), 2, replace=False)
        newBoard = self.board.copy()
        i1 = block//self.n*3 + switch[0]//self.n
        j1 = block%self.n*3 + switch[0]%self.n
        i2 = block//self.n*3 + switch[1]//self.n
        j2 = block%self.n*3 + switch[1]%self.n
        newBoard[i1,j1], newBoard[i2,j2] = newBoard[i2,j2], newBoard[i1,j1]
        newSdk.board = newBoard
        return newSdk

class SimulatedAnnealing:
    def __init__(self, tStart, tEnd, tAlpha, num):
        self.Ts = tStart
        self.Te = tEnd
        self.alpha = tAlpha
        self.numIter = num
    def anneal(self, solution):
        old_cost = solution.cost()
        T = self.Ts
        T_min = self.Te
        alpha = self.alpha
        t = [T]
        c = [old_cost]
        while T > T_min:
            i = 1
            while i <= self.numIter:
                new_solution = solution.neighbor()
                new_cost = new_solution.cost()
                ap = self.acceptance_probability(old_cost, new_cost, T)
                if ap > np.random.random():
                    solution = new_solution
                    old_cost = new_cost
                i += 1
            print('(%f): %d'%(T,old_cost))
            T = T*alpha
            t.append(T)
            c.append(old_cost)
            if old_cost == 0:
                return solution, t, c
        return solution, t, c
    def acceptance_probability(self, old_cost, new_cost, T):
        if new_cost < old_cost:
            return 1.
        return np.exp((old_cost-new_cost)/T)

SA = SimulatedAnnealing(1., 0.0001, 0.95, 100)
sdk = Sudoku()
sol, t, c = SA.anneal(sdk)
sol.printBoard()
plt.plot(t, c, 'b.-')
plt.ylabel('cost')
plt.xlabel('temperature')
plt.show()
