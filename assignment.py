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

class APModel: 
    def __init__(self, parameters):
        """
        """

