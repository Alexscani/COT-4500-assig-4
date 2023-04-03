def isDDM(m, n) :
 
    for i in range(0, n) :        

        sum = 0
        for j in range(0, n) :
            sum = sum + abs(m[i][j])    
        sum = sum - abs(m[i][i])

        if (abs(m[i][i]) < sum) :
            return False
 
    return True
 

n = 3
m = [[ 2, 2, 1 ],
    [ 2, 3, 0 ],
    [ 1, 0, 2 ]]
 
if((isDDM(m, n))) :
    print ("TRUE")
else :
    print ("FALSE")
