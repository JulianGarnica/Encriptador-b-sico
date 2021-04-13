# Encriptador
Este es un proyecto personal y de aprendizaje para el desarrollo de un encriptador. Fue desarrollado con escasos conocimientos acerca de encriptamiento o temas relacionados en seguridad informática, por lo cual, posiblemente no sea el más óptimo y aún cuente con distintos errores. Así es, lo desarrollé siendo un manco. :trollface:

>**Nota:** Por el momento no maneja contraseña al encriptar y desencriptar

## Funcionamiento:
Ejemplo de encriptado de palabra "Gatito":

`_,nZ8fI8,1\|_|,6WDzqn,3\|_|_*,YWlIoR,5\|_|_|,FYaTQJ,2\|_|_|,9r3q4M,4\_*_|_*|__|_*|*,8t4aZH,0`

El patrón que sigue este encriptado es el siguiente:
Cada `\` es un separador por cada letra, es decir cada letra escrita se "transforma" en un código diferente y éste se diferencia con `\`.
Sigamos con el ejemplo con "Gatito":
- G ->  `_*_|_*|__|_*|*,8t4aZH,0`
- a ->  `_,nZ8fI8,1`
- t ->  `|_|_|,FYaTQJ,2`
- i ->  `|_|,6WDzqn,3`
- t ->  `|_|_|,9r3q4M,4`
- o ->  `|_|_*,YWlIoR,5`

Con esto claro, veamos cada parte que separé: todas llevan un mismo orden y un patrón de igual manera. Esta vez se separa con `,`.

Separándolo en tres partes de la siguiente manera:
| Letra | Ubicación letra respecto abecedario  | Ubicación letra respecto subgrupo del abecedario  | Orden final de letra respecto a palabra | 
| ----- | ------------------------------------ | ------------------------------------------------------ | --------------------------------------- |
| G     |`_*_\|_*\|__\|_*\|*`                  |`8t4aZH`                                                |`0 `                                     |

Pero bien, ¿qué significan tantos simbolitos?
Pues, primero, tenemos que saber acerca de la cantidad de símbolos (también conocidas como letras) que tiene nuestro abecedario en español.
Ahí es donde entra esta bella línea que me agrega las letras mayúsculas, minúsculas, dígitos y caracteres especiales:
```python
self.abc = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + ['ñ','Ñ','á','é','í','ó','ú','Á','É','Í','Ó','Ú' ,' ','-']
```
Haciendo un conteo me da un total de 76 caracteres, que para mi suerte es divisible por 4, haciendo así que pueda crear **subgrupos**, al hacer la división me da un total de 19 **subgrupos**, cada uno conformado de 4 caracteres, obviamente.
Dándome un listado similar a esto:
```python
['a', 'b', 'c', 'd']
['e', 'f', 'g', 'h']
['i', 'j', 'k', 'l']
['m', 'n', 'o', 'p']
['q', 'r', 's', 't']
['u', 'v', 'w', 'x']
['y', 'z', 'A', 'B']
['C', 'D', 'E', 'F']
['G', 'H', 'I', 'J']
['K', 'L', 'M', 'N']
['O', 'P', 'Q', 'R']
['S', 'T', 'U', 'V']
['W', 'X', 'Y', 'Z']
['0', '1', '2', '3']
['4', '5', '6', '7']
['8', '9', 'ñ', 'Ñ']
['á', 'é', 'í', 'ó']
['ú', 'Á', 'É', 'Í']
['Ó', 'Ú', ' ', '-']
```
Ya teniendo esta división de grupos, lo que sigue es crear strings súper raras para poder clasificarlos, así es, ¡sin una aparente lógica! De ahí nace:
```python
self.pre_grps = ['_','|_','|_|', '|_|_*', '|_|_|', '|_|_|*', '_|*_|_|*', '_*_|_*|__|', '_*_|_*|__|_*|*', '*|_*_|_*|__|_*|*_']
self.grps = self.pre_grps
#En esta parte en realidad me dio flojera poner más Strings, así que dupliqué cada string sobre sí mismo
for o in range(len(self.pre_grps)):
    self.grps.append(self.pre_grps[o]*2)
```
Con esto logrado, lo que sigue es asignar cada string súper rara a cada **subgrupo**
```python
['a', 'b', 'c', 'd'] _
['e', 'f', 'g', 'h'] |_
['i', 'j', 'k', 'l'] |_|
['m', 'n', 'o', 'p'] |_|_*
['q', 'r', 's', 't'] |_|_|
['u', 'v', 'w', 'x'] |_|_|*
['y', 'z', 'A', 'B'] _|*_|_|*
['C', 'D', 'E', 'F'] _*_|_*|__|
['G', 'H', 'I', 'J'] _*_|_*|__|_*|*
['K', 'L', 'M', 'N'] *|_*_|_*|__|_*|*_
['O', 'P', 'Q', 'R'] __
['S', 'T', 'U', 'V'] |_|_
['W', 'X', 'Y', 'Z'] |_||_|
['0', '1', '2', '3'] |_|_*|_|_*
['4', '5', '6', '7'] |_|_||_|_|
['8', '9', 'ñ', 'Ñ'] |_|_|*|_|_|*
['á', 'é', 'í', 'ó'] _|*_|_|*_|*_|_|*
['ú', 'Á', 'É', 'Í'] _*_|_*|__|_*_|_*|__|
['Ó', 'Ú', ' ', '-'] _*_|_*|__|_*|*_*_|_*|__|_*|*
```
Así que sí, de esta forma sencilla ya sacamos la primera columna de la anterior tabla y podemos saber el **subgrupo** al cual pertenece esa letra.

| Letra | Ubicación letra respecto abecedario  | **Subgrupo** |
| ----- | ------------------------------------ | ------------ |
| G     |`_*_\|_*\|__\|_*\|*`                  | ``` ['G', 'H', 'I', 'J'] ``` |

La siguiente columna de **Ubicación letra respecto subgrupo del abecedario** es sencillamente una Seed de un número pseudoaleatorio el cual siempre dará la posición de la letra respecto al subgrupo que mostramos anteriormente.
En el ejemplo con la letra G, esta letra se encuentra ubicada en la primera posición del subgrupo, por lo cual, podemos suponer que `8t4aZH == 0` (No de forma literal, OJO).

La forma en la que se obtiene esta semilla es un poco simple pero efectiva:

```python
while validado == False:
    letra_encrpt = []
    for a in range(cant_letras_encrp):
        letra_encrpt.append(random.choice(self.abc_encrypt))

    random.seed("".join(letra_encrpt))

    if random.randint(0,self.elem_grupo) == p_r_grp:
        validado = True
```

De aquí se forman estas siguientes líneas:

```python
random.seed(semilla_letra)
pos_letra = random.randint(0,self.elem_grupo)
```
Suponemos que 
- semilla_letra = 8t4aZH
- self.elem_grupo = 4 (porque son 4 elementos en cada **subgrupo**)
Al ejecutar esas líneas, la generación pseudoaleatoria siempre nos dará 0, cumpliendo con la posición anteriormente explicada.

Y para finalizar, el último número es la posición de esa letra en la palabra o frase escrita por el usuario, así que sí, sería tipo:

- G ->  `0`
- a ->  `1`
- t ->  `2`
- i ->  `3`
- t ->  `4`
- o ->  `5`

Estos procesos se repiten dependiendo de la cantidad de caracteres que existan, de esta forma terminamos felices con nuestro encriptado.
¡Ahora te invito a que analices el desencriptado! Que en realidad es bastante más sencillo de hacer y con lo dicho anteriormente es relativamente sencillo de llevar a cabo.

¡Saludos Gatunos!
![dce92ad-a4d890fb-40ec-4b0b-927d-c675f40053d1](https://user-images.githubusercontent.com/23285433/114487993-291cec00-9bd6-11eb-9b78-cfea88296466.png)
