#1番目の数値は1
#2番目の数値は1
#3番目以降の数値は、直前の2つの数値の和（以下は例：）
#3番目： 1 + 1 = 2　　2つ前　と　1つ前　の和
#4番目： 1 + 2 = 3
#5番目： 2 + 3 = 5
#6番目： 3 + 5 = 8

def fibonacci(n):
    

    if n == 0:
            return 0
    elif n== 1:
            return 1
    else:
           return fibonacci(n-2) + fibonacci(n-1)


