def pour(jug1, jug2):
    max2, max1, fill = 4, 3, 2  #Change maximum capacity and final capacity
    print("%d\t%d" % (jug1, jug2))
    if jug2 is fill:
        return
    #fill 3g jug                              3 0
    elif jug2 is max2:
        pour(0, jug1)
#4g to 3g until 4g empty                      0 3
    elif jug1 != 0 and jug2 is 0:
        pour(0, jug1)
    #fill 3g jug0                            3 3
    elif jug1 is fill:
        pour(jug1, 0)
#3g to 4g until 4g full                       2 4 
    elif jug1 < max1:
        pour(max1, jug2)
    ##empty 4G into ground                    2 0   
    elif jug1 < (max2-jug2):
        pour(0, (jug1+jug2))
#rule8 pour water from 3G to4G until 3g is empty  0 2
    else:
        pour(jug1-(max2-jug2), (max2-jug2)+jug2)
 
print("JUG2\tJUG1")
pour(0, 0)