def question2(s):
    def question2Rec(s):
        sLen = len(s)
        sRep = s.replace("()", "")
        if len(sRep) == 0:
            return True
        elif sLen == len(sRep):
            return False
        else:
            return question2Rec(sRep)
    return question2Rec(s)

assert question2("()()(())") == True
assert question2("()()())") == False