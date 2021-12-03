from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    imb = image.binarisation(S)
    iml=imb.localisation()
    simmax,indmax=0,0
    for i in range(len(liste_modeles)):
        im_resize=iml.resize(liste_modeles[i].H,liste_modeles[i].W)
        sim=im_resize.similitude(liste_modeles[i])
        if sim>simmax:
            simmax=sim
            indmax=i
    return indmax
