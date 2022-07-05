    def cls():
        for i in range (0,20):
                print('\n')
                
def nota():        
        print("Nota para el usuario:\n\n\tPuede cancelar el programa en cualquier momento oprimiendo 'Cnt+C'\n\n\n")

def Presentacion():
        print('\t\t*************************************************\n\t\t*\t\t\t\t\t\t*')
        print('\t\t*\tUniversidad de los llanos\t\t*')
        print('\t\t*\t    Maquinas electricas\t\t\t*')
        print('\t\t*\t       Laboratorio N_4\t\t\t*')
        print('\t\t*\t\t\t\t\t\t*\n\t\t*************************************************\n\n\n')

def Motor():
        while True:
                print('¿Hay mas de un motor?')
                Rta = str(input("Respuesta (si o no): "))                
                if Rta.isalpha() == False:
                        print("Error, solo respuestas de tipo 'si' o 'no' \n")
                else:
                        break             

        if Rta == 'si' or Rta == 'SI':
                while True:
                        print('\n¿Cuantos motores hay?')
                        try:
                                Numero_motores = int(input('Numero de motores: '))
                                while Numero_motores == 0 :
                                        print("Error, no puede haber '0' motores")
                                        Numero_motores = int(input('Numero de motores: '))
                                        
                        except ValueError:
                                print('Error, solo respuestas numericas de tipo entero')
                                continue
                        else:
                                break

        elif Rta == 'no' or Rta == 'NO':
                Numero_motores = 1


        #Variables
                
        N_M = 1 #Contadorpara la variable Numero de motores

        cv_m = 0 #Configuracion del voltaje del motor
        pp_m = 0 #Potencia activa del motor
        ps_m = 0 #Potencia aparente del motor
        pq_m = 0 #Potencia reactiva del motor
        fp_m = 0 #Factor de potencia del motor
        a_m  = 0 #Angulo de motor
        hp_m = 0 #Caballos de fuerza del motor

        #Diccionarios
        CV_M = {} #Diccionario de la variable cv_m
        PP_M = {} #Diccionario de la variable pp_m
        PS_M = {} #Diccionario de la variable ps_m
        PQ_M = {} #Diccionario de la variable pq_m
        FP_M = {} #Diccionario de la variable fp_m
        A_M  = {} #Diccionario de la variable a_m
        HP_M = {} #Diccionario de la variable hp_m

        #Listas
##        LCV_M = [] 
##        LPP_M = [] 
##        LPS_M = [] 
##        LPQ_M = [] 
##        LFP_M = [] 
##        LA_M  = [] 
##        LHP_M = []       

        while N_M <= Numero_motores:
                print('\nDescripcion de las caracteristicas del motor {}'.format(N_M))
                print('\nEl motor es:')
                print('\n\t1) Monofasico')
                print('\t2) Bifasico')
                print('\t3) Trifasico')
                
                while True:
                        print('\nSeleccione el numero de su opcion')
                        try:
                                cv_m = int(input('Respuesta: '))
                                while cv_m == 0 or cv_m >= 4 :
                                                print('\nError, solo las opciones mostradas')
                                                cv_m = int(input('Respuesta: '))

                                                                              
                        except ValueError:
                                print('Error, solo respuestas numericas de tipo entero')
                                continue
                        else:
                                aux = 0
                                break

                while True:
                        print('\nConoce la potencia activa (P) del motor {}'.format(N_M))
                        Rta = str(input("Respuesta (si o no): "))
                        if Rta.isalpha() == False:
                                print("Error, solo respuestas de tipo 'si' o 'no' \n")
                        else:
                                break

                if Rta == 'si' or Rta == 'SI':
                        while True:
                                try:
                                        pp_m = int(input('Ingrese el valor en Watts: '))
                                except ValueError:
                                        print('Error, solo respuestas numericas de tipo entero')
                                        continue
                                else:
                                        aux = 0
                                        break
                                
                elif Rta == 'no' or Rta == 'NO':
                        while True:
                                print('\n¿Conoce los caballos de fuerza del motor {}?'.format(N_M))
                                Rta = str(input('Respuesta (si o no): '))
                                if Rta.isalpha() == False:
                                        print("Error, solo respuestas de tipo 'si' o 'no' \n")
                                else:
                                        break				
                        if Rta == 'si' or Rta == 'SI':
                                while True:
                                        try:
                                                hp_m = int(input('Ingrese el valor: '))
                                        except ValueError:
                                                print('Error, solo respuestas numericas de tipo entero')
                                                continue
                                        else:
                                                aux = 0
                                                break
                        elif Rta == 'no' or Rta == 'NO':
                                aux = 0

                if aux == 0:
                        while True:
                                print('\n¿Conoce la potencia aparente (S) del motor {}?'.format(N_M))
                                Rta = str(input('Respuesta (si o no): '))
                                if Rta.isalpha() == False:
                                        print("Error, solo respuestas de tipo 'si' o 'no' \n")
                                else:
                                        break
                        if Rta == 'si' or Rta == 'SI':
                                while True:
                                        try:
                                                ps_m = int(input('Ingrese el valor en Voltio-Amperio: '))
                                        except ValueError:
                                                print('Error, solo respuestas numericas de tipo entero')
                                                continue
                                        else:
                                                aux = 1
                                                break
                        elif Rta == 'no' or Rta == 'NO':
                                aux = 1

                if aux == 1:
                        while True:
                                print('\n¿Conoce la potencia reactiva (Q) del motor {}?'.format(N_M))
                                Rta = str(input('Respuesta (si o no): '))
                                if Rta.isalpha() == False:
                                        print("Error, solo respuestas de tipo 'si' o 'no' \n")
                                else:
                                        break				
                        if Rta == 'si' or Rta == 'SI':
                                while True:
                                        try:
                                                pq_m = int(input('Ingrese el valor en Voltio-Amperio-reactivo: '))
                                        except ValueError:
                                                print('Error, solo respuestas numericas de tipo entero')
                                                continue
                                        else:
                                                aux = 2
                                                break
                        elif Rta == 'no' or Rta == 'NO':
                                aux = 2

                if aux == 2:
                        while True:
                                print('\n¿Conoce el factor de potencia del motor {}?'.format(N_M))
                                Rta = str(input('Respuesta (si o no): '))
                                if Rta.isalpha() == False:
                                        print("Error, solo respuestas de tipo 'si' o 'no' \n")
                                else:
                                        break				
                        if Rta == 'si' or Rta == 'SI':

                                while True:
                                        try:
                                                fp_m = float(input('Ingrese el valor: '))
                                                while fp_m <= 0.0 or fp_m >= 1.1:
                                                        print('El factor de potencia tiene que estar entre 0.1 hasta 1.0')
                                                        print('\nPor favor ingrese un valor adecuado')
                                                        fp_m = float(input('Valor: '))
                                                        
                                        except ValueError:
                                                print('Error, solo respuestas numericas de tipo decimal')
                                                continue
                                        else:
                                                aux = 3
                                                break                               

                        elif Rta == 'no' or Rta == 'NO':
                                while True:
                                        print('\n¿Conoce el angulo {}?'.format(N_M))
                                        Rta = str(input('Respuesta (si o no): '))
                                        if Rta.isalpha() == False:
                                                print("Error, solo respuestas de tipo 'si' o 'no' \n")
                                        else:
                                                break
                                if Rta == 'si' or Rta == 'SI':
                                       while True:
                                                try:
                                                        a_m = int(input('Ingrese el valor: '))

                                                        while a_m <= 0.0 or a_m >= 90:
                                                                print('El angulo tiene que estar entre 1 hasta 89')
                                                                print('\nPor favor ingrese un valor adecuado')
                                                                a_m = float(input('Valor: '))
                                                                
                                                except ValueError:
                                                        print('Error, solo respuestas numericas de tipo entero')
                                                        continue
                                                else:
                                                        aux = 0
                                                        break
                                                
                                elif Rta == 'no' or Rta == 'NO':
                                        aux = 0
                                
                CV_M [N_M] = cv_m
                PP_M [N_M] = pp_m
                PS_M [N_M] = ps_m
                PQ_M [N_M] = pq_m
                FP_M [N_M] = fp_m
                A_M  [N_M] = a_m
                HP_M [N_M] = hp_m

                if pp_m == 0 and \
                   hp_m == 0 and \
                   ps_m == 0 and \
                   pq_m == 0:
                   
                        print('\n\n*************************************************************************\n*\t\t\t\t\t\t\t\t\t*')
                        print('*\tError, muchos datos faltantes, el programa no puede continuar\t*')
                        print('*\t\t\t\t\t\t\t\t\t*\n*************************************************************************')
                        break
                
                cv_m = 0
                pp_m = 0
                hp_m = 0
                ps_m = 0
                pq_m = 0
                fp_m = 0
                a_m  = 0
                
                N_M += 1
                cls()
                Presentacion()

                
        print(CV_M,PP_M,HP_M,PS_M,PQ_M,FP_M,A_M)

        while True:
                print('¿Desea ver un resumen de los datos?')
                Rta = str(input("Respuesta (si o no): "))                
                if Rta.isalpha() == False:
                        print("Error, solo respuestas de tipo 'si' o 'no' \n")
                else:
                        break
                
        if Rta == 'si' or Rta == 'SI':
                print("\nNumero de motores: ",Numero_motores)
                        
                print("\n'Numero de fases de alimentacion' ")
                for kv in CV_M.items():
                        print ('\tmotor',kv[0],'\t Opcion N =',kv[1])

                print("\n'Potencia activa (P)' ")
                for kv in PP_M.items():
                        print ('\tmotor',kv[0],'\t',kv[1],'W')
                        
                print("\n'Caballos de fuerza (H.P)' ")
                for kv in HP_M.items():
                        print ('\tmotor',kv[0],'\t',kv[1],'hp')                        

                print("\n'Potencia aparente (S)' ")
                for kv in PS_M.items():
                        print ('\tmotor',kv[0],'\t',kv[1],'VA')

                print("\n'Potencia reactiva (Q)' ")
                for kv in PQ_M.items():
                        print ('\tmotor',kv[0],'\t',kv[1],'VAR')

                print("\n'Factor de potencia (F.P)' ")
                for kv in FP_M.items():
                        print ('\tmotor',kv[0],'\t',kv[1])

                print("\n'Angulo (φ)' ")
                for kv in A_M.items():
                        print ('\tmotor',kv[0],'\t',kv[1])



                print('\n\n*************************************************************************\n*\t\t\t\t\t\t\t\t\t*')
                print('*\t\tFin del programa\t\t\t\t\t*')
                print('*\t\t\t\t\t\t\t\t\t*\n*************************************************************************')

     
        elif Rta == 'no' or Rta == 'NO':
                print('\n\n*************************************************************************\n*\t\t\t\t\t\t\t\t\t*')
                print('*\t\tFin del programa\t\t\t\t\t*')
                print('*\t\t\t\t\t\t\t\t\t*\n*************************************************************************')
                
def main():
        Presentacion()
        nota()
        Motor()

if __name__ == '__main__':
        try:
                main()
        except KeyboardInterrupt:
                print('\n\n*************************************************************************\n*\t\t\t\t\t\t\t\t\t*')
                print('*\t\tPrograma interrumpido por el usuario\t\t\t*')
                print('*\t\t\t\t\t\t\t\t\t*\n*************************************************************************')
