def toRoman(num):
    if num<1 or num>4000:
        return "invalid"
    result = ""
    while num>0:
        if num >= 1000:
            result += "M"
            num -= 1000
        elif num>=900:
            result+="CM"
            num -=900
        elif num>=800:
            result+="DCCC"
            num -=800
        elif num>=700:
            result+="DCC"
            num -=700
        elif num>=600:
            result+="DC"
            num -=600
        elif num >= 500:
            result += "D"
            num -= 500
        elif num>=400:
            result+="CD"
            num -=400
        elif num>=100:
            result += "C"
            num -= 100
        elif num>=90:
            result+="XC"
            num -=90
        elif num>=80:
            result+="LXXX"
            num -=80
        elif num>=70:
            result+="LXX"
            num -= 70   
        elif num>=60:
            result+="LX"
            num -=60
        elif num>=50:
            result += "L"
            num -= 50
        elif num>=40:
            result += "XL"
            num -= 40
        elif num>=10:
            result += "X"
            num -= 10
        elif num==9: 
            result += "IX"
            num -= 9
        elif num>=5: 
            result += "V"
            num -= 5
        elif num==4: 
            result += "IV"
            num -= 4
        else:
            result += "I"
            num -= 1
    return result
