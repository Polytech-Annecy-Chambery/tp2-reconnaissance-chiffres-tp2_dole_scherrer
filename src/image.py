from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np
import copy

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        im_bin = Image()
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))
        for h in range(self.H):
            for w in range(self.W):
                if self.pixels[h][w]>S:
                    im_bin.pixels[h][w]=255
                else :
                    im_bin.pixels[h][w]=0        
        return im_bin


    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        im_bin = Image()
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))
        hmax,hmin,wmax,wmin=0,self.H,0,self.W
        for h in range(self.H):
            for w in range(self.W):
                  if self.pixels[h][w] == 0:
                    if h < hmin:
                        hmin = h
                    if w < wmin:
                        wmin = w
                    if h > hmax:
                        hmax = h
                    if w > wmax:
                        wmax =w
                                
        im_bin.pixels = self.pixels[hmin:hmax+1,wmin:wmax+1]
        im_bin.H = hmax - hmin
        im_bin.W = wmax - wmin
        
        return (im_bin)
                    
                    
                

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        im_resized = Image()
        im_resized.pixels = resize(self.pixels, (new_H,new_W), 0)
        im_resized.pixels = np.uint8(im_resized.pixels*255)
        im_resized.H = new_H
        im_resized.W = new_W
        return (im_resized)


    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        sim=0
        for h in range(self.H):
            for w in range(self.W):
                if self.pixels[h][w]==im.pixels[h][w]:
                    sim+=1
        return sim/(self.H*self.W)
                    
                    
                    
                    
                    
                    