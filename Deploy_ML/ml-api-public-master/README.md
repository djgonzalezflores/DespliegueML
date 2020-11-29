# Despliegue de sistemas predictivos
> Diplodatos 2019

## Instalar y ejecutar

```
$ docker-compose up --build -d
```

Para detener los servicios:

```
$ docker-compose down
```

## Tests

- Instalar un virtualenv con los requirements.txt del origen
```
virtualenv --python=python3.5 .env
source .env/bin/activate
pip install -r requirements.txt
```
- Correr los tests con nosetests
```
nosetests [<package_name>]
```

- Si no tienen python3.5 y no lo quieren instalar, pueden probar instanciando un container con python 3.5 montando un volumen para ver los cambios dinamicamente

```
docker run -v $(pwd):/src -it --net=host -w /src python:3.5 bash
pip install -r requirements.txt
nosetests [<package_name>]
```

```
PARA PODER CORRER LOCUST  
docker run -v $(pwd):/src -it --net=host -w /src python:3.8 bash

comando locust -f locustfile.py 

-v $(pwd):/src --> mapea la carpeta local (api) hacia la interna /src para poder ejecutar codigo desde el docker con los archivos de afuera

```


```
Para entrar a un docker en bash
docker exec -it <mycontainer> bash

```

