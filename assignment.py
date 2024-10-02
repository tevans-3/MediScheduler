#Unbalanced assignment problem 
#References: https://kanchiuniv.ac.in/coursematerials/OperationResearch.pdf

#Sets: 
#Let BWT be the set of students who bike, walk or use transit. 
#Let CAR be the set of students who do not bike, do not walk, and do not use transit.

#Parameters: 
#n = number of preceptors 
#m = number of students 

#Distance matrix: 
#n x m matrix D_ij where entry d_ij is the distance student i must commute if assigned to site j 

#Decision variables:
#x_ij, i = 1 if student_i is matched to site_j, 0 otherwise 

#Objective function: 
#Minimize Z = SUM N i= 1 SUM M j = 1 d_ij x_ij
#subject to the constraints: 
#SUM N i = 1 x_ij, j = 1,2,...,n
#SUM M j = 1 x_ij, i = 1,2,...,n

#Each site can accept at most one student at a time. 

#Objective function: 
#We want to minimize the total distance travelled by students who bike, walk, or use transit.
import numpy as np 
cost = np.array([[4, 1, 3], [2, 0, 5], [3, 2, 2]])
from scipy.optimize import linear_sum_assignment
row_ind, col_ind = linear_sum_assignment(cost)
print(row_ind, col_ind)

class ScipyLinearSumAssignment: 
    def __init__(self, cost): 
        self.run = linear_sum_assignment(cost)
        self.row_ind = self.run[0]
        self.col_ind = self.run[1]
        self.matches = [(x,y) for x,y in zip(self.row_ind, self.col_ind)]

        def get_matches(self):
            return self.matches 

class HungarianAlgorithm: 
    def __init__(self, parameters):
        """
        """
        pass
