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
| Letra | Ubicación letra respecto abecedario  | Ubicación letra respecto sub ubicación del abecedario  | Orden final de letra respecto a palabra | 
| ----- | ------------------------------------ | ------------------------------------------------------ | --------------------------------------- |
| G     |`_*_\|_*\|__\|_*\|*`                  |`8t4aZH`                                                |`0 `                                     |

Pero bien, ¿qué significan tantos simbolitos?
Pues, primero, tenemos que saber acerca de la cantidad de símbolos (también conocidas como letras) que tiene nuestro abecedario en español.
Ahí es donde entra esta bella línea que me agrega las letras mayúsculas, minúsculas, dígitos y caracteres especiales:


```python
self.abc = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + ['ñ','Ñ','á','é','í','ó','ú','Á','É','Í','Ó','Ú' ,' ','-']
```
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
