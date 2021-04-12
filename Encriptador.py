import string
import random

class encript_machine:
    def __init__(self):
        #_Datos primordiales_
        self.abc = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + ['ñ','Ñ','á','é','í','ó','ú','Á','É','Í','Ó','Ú' ,' ','-']
        self.abc_encrypt = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits)
        self.pre_grps = ['_','|_','|_|', '|_|_*', '|_|_|', '|_|_|*', '_|*_|_|*', '_*_|_*|__|', '_*_|_*|__|_*|*', '*|_*_|_*|__|_*|*_']
        self.grps = self.pre_grps
        for o in range(len(self.pre_grps)):
            self.grps.append(self.pre_grps[o]*2)

        self.separador = "\\"
        
        self.denominador = 16
        self.elem_grupo = 4

    def encriptar(self, mensaje):
        

        cont = len(self.abc)/self.denominador
        i = 0
        cant_letras_encrp = 6
        cont_grps = 0
        pre_encriptado = []
        encriptado = []
        grupos = []
        list_msg_orig = list(mensaje)
        list_msg = list(mensaje)
        #_limpieza de datos_
        while i != len(self.abc):
            
            indice = i+self.elem_grupo
            
            #Conjunto de letras seleccionadas
            con_letras = self.abc[i:indice]
            grupos.append(con_letras)
            
            #print(con_letras)
            #print(cont_grps)
            #print(list_msg)
            #Sistema que pasa por cada letra del mensaje enviado
            for j in list_msg:
                
                #Pregunta por los grupitos de letras si la letra se encuentra
                if (j in con_letras):
                    #hacer paseo por cantidad de veces en la que la letra se encuentra
                    for k in range(list_msg.count(j)):  
                        #Obtiene grupo y asigna

                        #cont_grps = posición de grupo
                        #j = letra
                        #antepenultima = posición de la letra respecto al grupo en el que está
                        #Ultima = Posición de la letra respecto al orden del escrito por user

                        pre_encriptado.append([cont_grps,j, con_letras.index(j), list_msg_orig.index(j)])

                        list_msg_orig[list_msg_orig.index(j)] = None
                        #Elimina la letra deseada dentro de la lista
                        try:
                            list_msg.pop(list_msg.index(j))
                        except:
                            pass

            cont_grps += 1
            i = indice
            
            if(list_msg == []):
                i = len(self.abc)

        
        #_Encriptadito papá_
        for x in pre_encriptado:
            #Número de grupo
            n_grupo = x[0]
            #Letra
            letra = x[1]
            #posición respecto al grupo
            p_r_grp = x[2]
            #Posición respecto a lo que escribió el user
            posc_user = x[3]
            
            
            validado = False
            
            while validado == False:
                letra_encrpt = []
                for a in range(cant_letras_encrp):
                    letra_encrpt.append(random.choice(self.abc_encrypt))

                random.seed("".join(letra_encrpt))

                if random.randint(0,self.elem_grupo) == p_r_grp:
                    validado = True

            #Semilla posición respecto al grupo
            semilla_p_r_grp = "".join(letra_encrpt)

            encriptado.append(",".join([self.grps[n_grupo], semilla_p_r_grp, str(posc_user)]))
        
        encriptado = self.separador.join(encriptado)
        return encriptado

    def desencriptar(self, encriptado):
        lista_desencriptado = encriptado.split(self.separador)
        grupos = []
        pre_desencriptado = {}
        desencriptado = ""
        i = 0
        orden = []

        while i != len(self.abc):
            
            indice = i+self.elem_grupo
            
            #Conjunto de letras seleccionadas
            con_letras = self.abc[i:indice]
            grupos.append(con_letras)

            i = indice

        for x in lista_desencriptado:
            val_des = x.split(',')
            #posición respecto al grupo
            p_r_grp = val_des[0]
            #semilla de letra
            semilla_letra = val_des[1]
            #Posición respecto a lo que escribió el user
            posc_user = int(val_des[2])
            orden.append(posc_user)

            #indice de lista de posición respecto al grupo
            indice_p_r_grp = self.grps.index(p_r_grp)


            random.seed(semilla_letra)
            pos_letra = random.randint(0,self.elem_grupo)
            letra = grupos[indice_p_r_grp][pos_letra]

            pre_desencriptado[posc_user] =  letra

        #Ordenamiento

        for elemento in sorted(orden):
            v = pre_desencriptado
            desencriptado += v[elemento]
            
        return desencriptado


en = encript_machine()
valor_encriptado = en.encriptar(input())
valor_desencriptado = en.desencriptar(valor_encriptado)
print('\n\n============ VALOR ENCRIPTADO ================ \n\n', valor_encriptado)
print('\n\n============ VALOR DESENCRIPTADO ================ \n\n', valor_desencriptado)