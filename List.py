Huruf = ["A","B","C","D","E"]
Huruf2 = ["A","B","C","D","E"]
Thoriq = []
Rian = ["A"]

def Konso(e,L):
    NewList = list(L)
    NewList.insert(0,e)
    return NewList

def Konsi(L,e):
    NewList = list(L)
    NewList.append(e)
    return NewList

def FirstElmt(L):
    return L[0]

def Tail(L):
    return L[1:] 

def LastElmt(L):
    return L[-1]
    
def Head(L):
    return L[:-1]

def IsEmpty(L):
    return len(L) == 0

def IsOneElmnt(L):
    return len(L) == 1

def IsEqual(L1,L2):
    return L1 == L2

# def NbElmnt(L):
#     return len(L)

# print(NbElmnt(Huruf))

def NbElmnt(L):
    if IsEmpty(L):
        return 0
    else:
        return NbElmnt(Tail(L)) + 1

# def ElmtkeN(n,L):
#     return L[(n)]

# print(ElmtkeN(2,Huruf))

def ElmtkeN(n,L):
    if n == 0:
        return L[n]
    else:
        return ElmtkeN(n-1,Tail(L))
    
def Copy(L):
    if IsEmpty(L):
        return L
    else:
        return Konso(FirstElmt(L), Copy(Tail(L)))

def Inverse(L):
    if IsEmpty(L):
        return []
    else:
        return Konsi(Inverse(Tail(L)), FirstElmt(L))

def Konkat(L1,L2):
    if IsEmpty(L2):
        return L1
    else:
        return Konkat(Konsi(L1,FirstElmt(L2)),Tail(L2))

def IsMember(X,L):
    if IsEmpty(L):
        return False
    else:
        for i in L:
            i == X
print(Copy(Huruf))
print(Inverse(Huruf))
print(Konkat(Huruf,Huruf))
print(IsMember("E", Huruf))
# print(Konso("a", ["A","B","C","D","E"]))
# print(Konsi(Huruf, "a"))
# print(FirstElmt(Huruf))
# print(Tail(Huruf))
# print(LastElmt(Huruf))
# print(Head(Huruf))
# print(IsEmpty(Huruf))
# print(IsEmpty(Thoriq))
# print(IsOneElmnt(Huruf))
# print(IsOneElmnt(Rian))
# print(IsEqual(Huruf,Rian))
# print(NbElmnt(Huruf))
# print(ElmtkeN(4,Huruf))











# 

# 

# 

# 

# 



# 



# Konkat

# 

# IsFirst

# IsLast

# IsNbElmtN

# IsInverse

# IsXElmtkeN