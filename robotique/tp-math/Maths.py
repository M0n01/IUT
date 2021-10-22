import numpy as np

def R (alpha):
    return np.array([[np.cos(alpha),-np.sin(alpha)],[np.sin(alpha),np.cos(alpha)]]) # matrice de rotation

# EXERCICE 1



print("EXO 1: ")



# EXERCICE 2

angle = np.deg2rad(120) # converti 120 deg en rad
Pr = np.array([18, 4]) # vecteur Pr
Pw = np.array([-5,9]) # vecteur OR

print("EXO 2: ",Pw-R(angle)@Pr) # print 



# EXERCICE 3

alpha = np.arctan2(4-3,9-8)
print("EXO 3: ", R(alpha)@(np.array([5,-2])-np.array([9,4])))



# EXERCICE 4

Pr = np.array([4, 2])
Rw = np.array([-4, 8])

alpha = np.deg2rad(12)

Pw = R(alpha) @ Pr + Rw
Rw2 = np.array([-7, 9])

alpha2 = np.deg2rad(14)

print("EXO 4 :",R(alpha2).T@(Pw - Rw2))

