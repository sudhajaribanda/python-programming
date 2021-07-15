def get_num3(n):
    s_digits = ["","one","two","three","four","five","six","seven","eight","nine"]
    two_digits = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen",
    "seventeen","eighteen","nineteen"]   
    num_tys = ["","ten","twenty","thirty","fourty","fifty","sixty",
    "seventy","eighty","ninety"]
    
    num_hundred = n // 100 
    num = s_digits[num_hundred]
    if num != "":
        num += " hundred"
    n = n%100 
    if num:
        num += " "
    if (n >= 10 and n <= 19):
        num += two_digits[n-10]
    else:
        if n >= 20:
            num += num_tys[n//10]
            n = n % 10 
            if n != 0:
                num += "-"
        num += s_digits[n]
    return num
def get_word(n):
    if n <= 10000000000:
        if n == 0:
            return "zero"
        n1 = n // 1000000000 
        n = n % 1000000000  
        if n1 != 0:
            num = get_num3(n1) + " billion"
        else:
            num = ""
        n1 = n // 1000000
        n = n % 1000000
        if n1 != 0:
            if num:
                num += " "
            num += get_num3(n1) + " million"
        n1 = n // 1000 
        n = n % 1000 
        if n1 != 0:
            if num:
                num += " "
            num += get_num3(n1) + " thousand"
        if n != 0:
            if num:
                num += " "
            num += get_num3(n)
        return num+" dollars"
    
n = int(input())
print(get_word(n))