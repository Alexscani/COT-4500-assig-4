def isDDM(m, n) :
 
    for i in range(0, n) :        

        sum = 0
        for j in range(0, n) :
            sum = sum + abs(m[i][j])    
        sum = sum - abs(m[i][i])

        if (abs(m[i][i]) < sum) :
            return False
 
    return True
 

n = 5
m = [[ 9, 0, 5, 2, 1],
    [ 3, 9, 1, 2, 1],
    [ 0, 1, 7, 2, 3],
    [4, 2, 3, 12, 2],
    [3, 2, 4, 0, 8]]
 
if((isDDM(m, n))) :
    print ("TRUE")
else :
    print ("FALSE")
