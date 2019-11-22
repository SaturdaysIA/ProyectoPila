'''
 # probado con PS cc 2020 (version prueba)
 # USO:
import pytoshop as *   # se creara la var 'app' que es un POINTER de PS
 #establecer directorios
eff_dir = "C:/Users/Felipe Karelovic/Desktop/PyNT/effects/" #carpeta donde estan 'efectos'
savedir = 'C:/Users/Felipe Karelovic/Desktop/PyNT/output/' #carpeta donde se guarda
inp_dir = "C:/Users/Felipe Karelovic/Desktop/PyNT/input/" #carpeta de imgs a modificar
ngen=5 #Cuantas imgs crear por cada efecto en cada input
input_MRT(app=app,savedir=savedir,inp_dir=inp_dir,eff_dir=eff_dir, ngen)
'''

import os
from comtypes.client import CreateObject

global app
app = CreateObject("Photoshop.Application")


def errdir(x):
    if not os.path.exists(x):
        try: os.makedirs(x)
        except: print('dir '+x+'no existe ni se pudo crear')
    if x[len(x)-1:]!= '/': x= x+'/'
    return x

def getPS():
#casi inutil salvo si se cierra ps
#USO: app = getPS()
    from comtypes.client import CreateObject
    return CreateObject("Photoshop.Application")

def random_transform(Layer,H,W):
#cambia la capa 'efecto' con transformaciones de PS
#(rotacion, traslacion, inversion de color y resize)
# al azar, y con parametros al azar.
    import random as r
    deltaX = lambda: -int(H * (r.randrange(-40, 40, 5) / 100))
    deltaY = lambda: -int(W * (r.randrange(-40, 40, 5) / 100))
    if r.randint(0, 1):  Layer.Translate(deltaX(), 0)
    if r.randint(0, 1):  Layer.Translate(0, deltaY())
    if r.randint(0, 1):  Layer.Rotate(r.randrange(0,360,10))
    if r.randint(0, 4)==1:  Layer.Invert()
    if r.randint(0, 2)==1:  Layer.Resize(r.randrange(40,150,5),100)
    if r.randint(0, 2)==1:  Layer.Resize(100,r.randrange(40, 150, 5))

def load_effects(app,eff_dir):
    #cargar todos los efectos
    eflist= os.listdir(eff_dir)
    effects = []
    for i in range(len(eflist)):
        if not eflist[i].find('png')==-1 or not eflist[i].find('jpg')==-1:
            effects.append(app.Open(eff_dir+eflist[i]))
    print('Cargados {} efectos con nombres: {}'.format(len(effects),[effects[e].name  for e in range(len(effects))]))
    return effects


def input_MRT(app,savedir,inp_dir,eff_dir,ngen=5):
    #principal fun, carga inputs y le aplica repetidamente los
    #efectos y luego los guarda.
    inp_dir = errdir(inp_dir)
    savedir = errdir(savedir)
    eff_dir = errdir(eff_dir)
    if inp_dir[len(inp_dir)-1:]!= '/': inp_dir= inp_dir+'/'
    if savedir[len(savedir)-1:]!= '/': savedir= savedir+'/'
    inlist = os.listdir(inp_dir)
    inlist = [inlist[i] for i in range(len(inlist)) if
              not inlist[i].find('png') == -1 or not inlist[i].find('jpg') == -1]
    print(
        'Se cargaran {} fotos a modificar con nombres: {}'.format(len(inlist), [inlist[e] for e in range(len(inlist))]))
    effects = load_effects(app=app,eff_dir=eff_dir)
    for i in range(len(inlist)):
        if not inlist[i].find('png') == -1 or not inlist[i].find('jpg') == -1:
            inp = app.Open(inp_dir + inlist[i])
            for effect in effects:
                v = 0

                for _ in range(ngen):
                    v+=1
                    app.ActiveDocument = effect
                    effect.Layers[0].duplicate(inp)
                    app.ActiveDocument = inp
                    random_transform(inp.Layers[0],inp.height,inp.width)
                    output_name = inp.name[:-4]+'v'+str(v)+inp.name[-4:]
                    inp.Export((savedir + '/' + output_name), 2)
                    inp.Layers[0].delete()
    [effect.Close(1) for effect in effects]
    print('Listo!')