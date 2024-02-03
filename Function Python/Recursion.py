# 1 + (First+2) + (Second+3)..... [(Last -1)+n]
def tri_recurtion( k ):
    if (k > 0) :
        result = k + tri_recurtion(k -1)
        print(result ,end =' ')
    else :
        result = 0
    return result

value = int(input("Enter  your Value :"))
print("The recurtion example result:")
tri_recurtion(value)
