""" 2つの値の足し算と引き算の結果を表示する. """


def calcadd(num1, num2):
    result_add = num1 + num2
    return result_add

def calcsub(num1, num2):
    result_sub = num1 - num2
    return result_sub

#ここはimportされた場合実行されない
if __name__ == "__main__":
    num1,num2=10,5
    add = calcadd(num1, num2)
    sub = calcsub(num1, num2)
    
    print(f"{add}")
    print(f"{sub}")
    #print(f"{add=}") #python3.8じゃないと動かない
    #print(f"{sub=}") #python3.8じゃないと動かない
