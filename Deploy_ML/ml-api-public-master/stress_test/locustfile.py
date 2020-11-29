# import time
from locust import HttpUser, task
import random


_lst = []
_lst.append('Un producto realmente maravilloso. La pantalla oled cambia absolutamente todo, contraste infinito, brillo excelente. Pero sobre todo, lo mejor es el hdr dolby vision que se activa con netflix o sino el hdr10 pro, hdr technicolor y dlg pro. Todas nuevas tecnologías hdr que cambian por completo la imagen.')
_lst.append('Con fravega todo bien pero el tv es muy malo. Cuando anda es muy bueno , algo lento. Pero el software es malo, se tilda, hay q desenchufarlo para q arranque, no se conecta a internet. Philips dice q es x q tengo 3mb d pero no es asi x q el anterior andaba con 1mb perfectamente. Ya tube un philips hace tiempo y tenia el mismo tipo de defectos. Es a kerosene. Lo compre x q es el unico smart q encontre con sal de auriculares pero es un clavo. Philips ya no es lo de antes. Ahora solo procesadoras de cocina. Comprare el google y lño usare como monitor x q el smart. Nones.')
_lst.append('Le compré este tv a mi papá. El primer mes todo bien, buena imagen y todo. Después empezó a tener problemas. No responde al control remoto. Si se lo apaga y deja enfriar al las 3 o 4 horas vuelve a funcionar. Pero lo peor es que a veces se prende solo. Muy decepcionada con esto, es un televisor nuevo, no es posible que tenga estos problemas. Estamos llamando a phillips para que lo cambie por uno que no tenga estos problemas.')
_lst.append('Lindo smart. Sobre todo el teclado que tiene detrás es muy práctico. Para tener en cuenta: el parlante lo tiene detrás, lo que dificulta un poco el buen sonido. Imagen excelente. Para descargar app es un poco limitado, no es compatible con muchas todo ( por ejemplo flow no se puede descargar, es lo que más se usa en mi caso). Lo demás muy bien en relación al precio.')
_lst.append('Es un buen smart tv. La verdad que yo no tenía televisor antes, entonces no sé como funcionan los otros. Se ve bien, se escucha bien y funciona bien (por ahora!). Tiene algunas limitaciones a nivel apps ara instalar - por ejemplo no pude instalar spotify (nada que no se pueda solucionar con un cable hdmi y una compu).')
_lst.append('Quede muy decepcionado del funcionamiento de este tv. El sonido es muy malo, suena demasiado bajo, así que no es recomendable para grandes ambientes. Las aplicaciones smart son lentas. Los soportes de pie son bastante incómodos, por lo cual lo puse en un soporte de pared. No lo recomendaría para nada.')
_lst.append('Al principio y ahora muy de vez en cuando me pasaba que no lo podia apagar ni con el control ni de atras del tele. Es un poco lento para netflix y youtube aunque tambien puede ser su antena de wifi de bajo alcance para que funcione correctamente')
_lst.append('Buenas tardes, ayer recièn pude contratar telecentro. En el dìa de hoy la tv no funciona. La pantalla se pone azul y no responde a los mandos. Llamamos a philips, seguimos las instrucciones que nos dieron y hasta el momento no funciona')
_lst.append('El control es muy sensible, la pantalla no tiene la mejor definición. Pero es un producto económico dentro de la gama y es de buena marca. Bien por el precio. Si quieres algo mejor hay que pagar mucho mas')
_lst.append('A mi parecer cumple con todas las funciones, buena imagen, buena calidad de sonido, eso si, en algunos momentos el panel de aplicaciones o en el buscador del navegador se puede ralentizar un poco, pero nada que moleste demasiado.')


class QuickstartUser(HttpUser):

    @task(1)
    
    def index(self):
        self.client
        self.client.get("/")

    '''
    @task(2)
    def predict(self):
        _texto = "Texto de prueba"
        #_texto = "un texto de prueba"
        self.client.post("/predict", params={'text':_texto})
    '''

    @task(5)
    def prediction(self):
        _texto = get_texto()
        #_texto = "un texto de prueba para dediction"
        
        _nrand = random.random()
        if _nrand < .25:
            # error 404            
            self.client.get("/bad_path")
        elif _nrand >= .25 and _nrand < .45:
            # 408 / 400
            self.client.get("/prediction", json={'text':_texto})                
        else:
            # ok       
            self.client.post("/prediction", json={'text':_texto})                
    
    @task(3)
    def prediction_auth(self):
        _texto = get_texto()
        if random.random() > .45:
            self.client.post("/prediction_auth", json={'user':'', 
                                                       'pwd': '', 
                                                       'text':_texto})
        else:
            self.client.post("/prediction_auth", json={'user':'usuario', 
                                                       'pwd': 'password', 
                                                       'text':_texto})
        
    
    

    def on_start(self):
        pass


def get_texto():
    
    _idx = 0
    _val = random.randrange(100)

    if _val >= 1 and _val<10:
        _idx=0
    if _val >= 10 and _val<20:
        _idx=1
    if _val >= 20 and _val<10:
        _idx=2
    if _val >= 30 and _val<40:
        _idx=3
    if _val >= 40 and _val<50:
        _idx=4
    if _val >= 50 and _val<60:
        _idx=5
    if _val >= 60 and _val<70:
        _idx=6
    if _val >= 70 and _val<80:
        _idx=7
    if _val >= 80 and _val<90:
        _idx=8
    if _val >= 90 and _val<100:
        _idx=9

    return _lst[_idx]
        