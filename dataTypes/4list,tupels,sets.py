array1 = ["1","2","3","4","5"]
array2 = ["1","2","3","4","5"]

array3 = ["1","2","3","4","5"]

array4 = ["1","2","3","4","5"]

array5 = ["1","2","3","4","5"]
array_of_array = [array1, array2, array3, array4, array5]



array6 = ["1","2","3","4","5"]
array7 = ["1","2","3","4","5"]

array8 = ["1","2","3","4","500"]

array9 = ["1","2","3","4","5"]

array10 = ["1","2","3","4","5"]

a = [array6,array7,array8,array9,array10]



def total (ar):

    total = 0
    for j in ar:
        for i in j:
            x = int(i)
            total = total + x
    return total

print(f'Your Total is :{total(array_of_array)}')





