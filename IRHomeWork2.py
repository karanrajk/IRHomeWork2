import numpy as np

b = 0.85
file = np.genfromtxt("input.txt", dtype=float)
itercount = 0
condition = False

print(file)
ndimension0 = np.amax(file, axis =0)

highdim = int(np.amax(ndimension0[0:2]))
#print(ndim1)

matrixA = np.zeros((highdim, highdim))
matrixM = np.zeros((highdim,highdim))

print(matrixA)
print(matrixM)

for r in file:
    i =int(r[0]-1)
    j =int(r[1]-1)
    k =r[2]
    matrixA[i,j] = k

print(matrixA)
sumofcols = matrixA.sum(axis=0)
print(sumofcols)

#Transposing the matrix to match the dimensionality
matrixA = np.transpose(matrixA)

print(matrixA)

# integer scalar arrays to be converted into scalar indices
matrixM = np.zeros((highdim,highdim))

for i, (r, sumofcols) in enumerate(zip(matrixA, sumofcols)):
    if sumofcols == 0:
        matrixM[i,:]= r
    else:
        matrixM[i,:] = r/sumofcols
        
#tanspose back
matrixM = matrixM.transpose()
print("Output of Matrix M")
print(matrixM)
rin =np.ones((highdim,1))
#print (rin)

rin = rin*(1/highdim)
#Initial Vector
print("Original Rank Vector")
print(rin)

#RandomSurferMethod
while condition == False:
    r = b*np.dot(matrixM,rin) +(1-b)*(np.ones((highdim,1)))*(1/highdim)
    #print(r)
    condition = np.allclose(r, rin)
    #print(condition)

    #if (r == rin):
     #   condition = True
        
    if condition == False:
        rin = r
    itercount += 1



print("Converged Rank Vector:")
print( r)

print("Number of iterations: ",itercount)
    
    