def decalage(motif):
    dico = {}
    for i in range(len(motif)-1):
        dico[motif[i]]=len(motif)-1-i
    return dico

def boyer_moore(texte, motif):
    n = len(texte)
    m = len(motif)
    decale = decalage(motif)
    i = m - 1
    correspondance=False
    j=-1
    while i < n:
        if texte[i]==motif[-1]:
            correspondance = True
            while j!=len(motif):
                j=j+1
                while correspondance==True:
                    if texte[i]==motif[j]:
                        pass
                    else:
                        correspondance=False
                        i=decale[texte[i]]
            if correspondance==True:
                    return i
        else:
            i=decale[texte[i]]
    return -1
#Appelez la fonction boyer_moore avec le texte à parcourir ainsi que le motif à chercher ! 
