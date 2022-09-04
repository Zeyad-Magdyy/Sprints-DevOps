def myfun(list):
    
    meanSum = 0;
    evenNumbers =0;
    maxFloat = 0.0;
    evenIntList = []
    floatNumberList = []
    
    for i in range(0,len(list),1):  
        
        if  isinstance(list[i], int):
            
            if list[i] % 2 == 0 :
                meanSum = meanSum + list[i]
                evenNumbers = evenNumbers +1
                evenIntList.append(list[i])
                
                
        if  isinstance(list[i], float):
            
             if list[i] > maxFloat :
                 maxFloat = list[i]
                 floatNumberList.append(list[i])
        
    meanSum = meanSum/evenNumbers
    
    
    return print("Even Numbers in the list are" ,evenIntList),print("The Mean of the even numbers in the list is ", meanSum),print("Float Numbers in the list are" ,floatNumberList),print("The Maximum Float Number in the list is ", maxFloat)
    


 