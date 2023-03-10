# Importing the necessary libraries
from __future__ import division  # Ensures division always returns a float
from math import gcd # Importing the greatest common divisor function
import string # Importing the string module for letter manipulation
import numpy as np # Importing the numpy library for array manipulation
# Defining a function to shift a list to the left
def shift(list,n): 
    return list[n:] + list[:n]
num = dict(zip(range(0,26),string.ascii_lowercase)) # Creating a dictionary to map numbers to letters
A = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.0236,0.0015,0.01974,0.00074]
a9=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b="AOJBHXPRALZXDJSVQKXSQMEYFGHMPZSSJACKNIDIGOZBKERXPWVTRZFDHMAIPDJMFYPRLPRHPZDNVXXZQAUKXWYPGRPOJVFUXSLPVTRTJWZZSSUWBQYCLPVTRVSXCKYSVIAJLTLMECLWLQAMDCEMZOYILMFZFDHMAIPDJMFYPRLPRHPZDITGTBCMRVTBYPRXQWFORXZBLPRHFHLWALZFKWZKWWLBYKHVATRGEZSAGYSSZMNXOTGWGYESHAVTDWVMNTOOEWZKYHDIGKCAJAIGYRWUREPFZMEYPZXWCKYSVBUKOCGZFNPZANGKOVWZREPPJWJYLHLPRYTUZBBLEVWOVXWMGCVNLRSBBANVGNGUZHZIPNPASIZYLWVBHVASFKRMWWTTLYZHZWHMSHABOKEHWZGUNCEMUUXSSVQNLJWIDATSLMIKYWFOZXDJSVQKXSQMEYLWVVBZSWFOOAEGZMQXPKTIPQLBVTRZEIHXRTNSHIFYTBLWGNPVSTYNZKMVSUCHMVNZPTGZLUFGZMFGTRUWYJWMQWHNLRTMGZPFYWGUMSVWUODVSTYHPODTEORVLQAZSSCQGISSFUNGXQGWXCTZDKBUVWKWHZDOALZXDJSVQKXSQMEOYOJIGNPFVQFGRFWMNHWSLWAKTGWVGNPFGCGYZMGCFKPMGCUGOPWBGKCUGBBHPRKCQJPBDGGAADWVPKQSDBNLCOALGNPFWENYLFAVTOYAJAIGYRWUREPFKDBONSLPNZDVWLVJYCLTVQPOLIYRLZKWGNPCLPRXHCEIACLGKTBCWMWLTOYUZMEAAHZMCGDGSORZFDHMAIPHMZAKOOLJNETRGVGCLBLBUKYWFISRLGZIEOXCXKBROGLMRRECMKUKOVWZGKXDDMNTOAJAIGYRWUREPFKDBONSJWFKNCDLNTOAWVNITBYGBAOOEVRJWWLBYKQCGTQUJCMBUOYYALBTEYFWJTZRGVGGYGOMEOQMGCFZCIYOYKZFUZLUFHAT"
a=b.lower()
a=list(a)
a1=a
c=0 # Initializing a list to store the number of coincidences for each shift
d=[]
k=1
# Looping through each shift value from 1 to 30
while k<=30: # Shifting the elements in a1 to the right by 1 position
    a1 = np.roll(a1,1)#shift the list right

      # Looping through the elements in a and a1 in parallel
    for i,j in zip(a,a1):# zip(a,b) makes [(a0,b0),(a1,b1)] for all the element of a and b
        if i==j:
            c+=1# Incrementing c if the elements are the same
    print(f'Number of coincidences for {k} shift is: {c}')  # Printing the number of coincidences for the current shift value
    d.append(c)  # Storing the number of coincidences for the current shift value in the list d
    # Incrementing k and resetting c for the next iteration of the loop
    k+=1
    c=0
# Determining the maximum number of coincidences in the list d
L=max(d)
print ('Maximum number of coincidence(L):',L) 
L=d.index(L)
L+=1 # Finding the shift value that corresponds to the maximum number of coincidences
L1=sorted(set(d))[-2] # Determining the second highest number of coincidences in the list d
print ('Second highest number of coincidence(L1):',L1) # Printing the maximum and second highest number of coincidences and their corresponding shift values
L1=d.index(L1) # Finding the shift value that corresponds to the second highest number of coincidences
L1+=1
L2=sorted(set(d))[-3] # Determining the third highest number of coincidences in the list d
print ('Third highest number of coincidence:(L2)',L2)
L2=d.index(L2)
L2+=1
L3=sorted(set(d))[-4] # Determining the forth highest number of coincidences in the list d
print ('Fourth highest number of coincidence:(L3)',L3)
L3=d.index(L3)
L3+=1
L4=sorted(set(d))[-5] # Determining the fifth highest number of coincidences in the list d
print ('Fifth highest number of coincidence(L4):',L4)
L4=d.index(L4)
L4+=1
L5=sorted(set(d))[-6] # Determining the sixth highest number of coincidences in the list d
print ('Sixth highest number of coincidence:(L5)',L5)
L5=d.index(L5)
L5+=1
lth=[L,L1,L2,L3,L4,L5] 
print('\nPossible key lengths are:', L, ',', L1, ',', L2, ',', L3, ',', L4, ',', L5)
d1=gcd(L,L1)
d1=gcd(d1,L2)
d1=gcd(d1,L3)
d1=gcd(d1,L4)
d1=gcd(d1,L5)
print ('gcf of all above shifts:',d1) #the gcf of all elements of d
in1=0
while in1<=2:
    L=lth[in1]
    print('\nTake', L, 'as key length')
#####################    dividing in the L(max d) parts     ##########################
    z=[[]for x1 in range(0,L)]
    v1=0
    while v1<L:
        for i2 in range(v1,len(a),L):
           z[v1].append(a[i2])
        v1+=1
######################     cracking the caesar cipher    ##############################
    v1=0
    Array=[]
    while v1<L:
        W=[]
        for charc in a9:
            b1 = z[v1].count(charc)
            b1 = b1/26
            b1 = round(b1,7)
            W.append(b1)
        I =24
        J=[]
        t=0
        while I>=0:
            B= shift(A,t)
            K = np.dot(W,B)
            K = round(K,6)
            J.append(K)
            I -= 1
            t+=1
        Max1=max(J)#for the highest number in list
        F = [D for D, E in enumerate(J) if E==Max1] # retrieve the index of the maximum number
        F[0]=((26-F[0])%26)
        key=num[F[0]].upper()
        Array.append(key)
        S1=[]
        for character in z[v1]: #loop to getting the deciphered numbers
            number = ord(character) - 97
            number = ((number - F[0])%26)
            S1.append(number)
        a2=[]
        for id2 in S1: # Loop through each number and map it to its corresponding alphabet.
            a2.append(num[id2])
        z[v1]=a2
        v1+=1
    print('The Encryption Key:', ''.join(Array))    

###################### Reassembling the L sections to obtain the decrypted output ################
 
    v1=0
    var=0
    D1=[]
    vv=int(len(a)/L)
    while var<vv:
        while v1<L:
            D1.append(z[v1][var])
            v1+=1
        var+=1
        v1=0
    v1=0
    while v1<(len(a)%L):
        D1.append(z[v1][var])
        v1+=1
    print ('\n'+'Your plain Text:')
    print (''.join(str(elm) for elm in D1))
    in1+=1