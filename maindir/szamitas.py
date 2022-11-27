index = 0
def szamolas(ink, inj):
    global index
    for i in range(len(ink)):
        index = index + (int(ink[i])*int(inj[i]))
    vegered = index/30
    return round(vegered,2)












