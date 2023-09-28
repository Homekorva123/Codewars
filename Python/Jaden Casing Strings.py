def to_jaden_case(string):
    errArr = string.split(" ")
    jadenCaseArr = []
    for word in errArr:
        jadenCaseArr.append(word.capitalize())
        
    return " ".join(jadenCaseArr)