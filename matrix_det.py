

import copy


# function for getting matrix
def matrix(a, i):
    mat = copy.deepcopy(a)
    if len(mat) ==2:
        return mat
    else:
        mat.pop(0)
        for j in mat:
            j.pop(i)
        return mat


# function for computing the determinant of a matrix

def det(a):
    if len(a) ==1:
        diff = a[0]
        return diff
    elif len(a)==2:
        diff = a[0][0]*a[1][1] - [1][0]*a[0][1]
        return diff
    else:
        diff = 0
        for i in range(len(a[0])):
            diff += ((-1)**i)*a[0][i]*det(matrix(a,i))

        return diff

# testing 
A = [5]
B = [[2,9],[6,5]]
C = [[2,9,0],[6,5,1],[9,3,7]]

print("The determinant of the Matrix A is:  ", det(A))
print("The determinant of the Matrix A is:  ", det(B))
print("The determinant of the Matrix A is:  ", det(C))
        
