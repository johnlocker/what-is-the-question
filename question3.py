def question3(numbers):
    sortedNumbers = list(sorted(numbers, key = len))
    def question3Rec(sortedNumbers):
        checkNum = sortedNumbers.pop(0)
        if len(sortedNumbers) == 0:
            return True
        res = [checkNum for num in sortedNumbers if checkNum == num[:len(checkNum)]]
        if len(res) == 0:
            return question3Rec(sortedNumbers)
        else:
            return False
    return question3Rec(sortedNumbers)

assert question3(["911", "9876543", "9112345"]) == False