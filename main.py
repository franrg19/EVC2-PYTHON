import os
import datetime
import time
import shutil
os.system('cls')

import colorama
from colorama import init,Fore,Style
init(autoreset=True)

#variables de color
rojo=Fore.RED
verde=Fore.GREEN
blanco=Fore.WHITE
negrita=Style.BRIGHT
tit_menu=Fore.LIGHTYELLOW_EX
reset=Style.RESET_ALL


#MUESTRA LA RUTA ACTUAL
def ruta_actual (): 
    ruta=os.getcwd()
    print(f"{rojo}\n📁 Ruta actual -> {ruta}")
    print("="*40)



#FUNCION PARA MOSTRAR MENU
def mostrar_menu (): 
    print(f" {tit_menu}  ==== 🗂️  GESTOR DE ARCHIVOS Y CARPETAS 🗂️ ==== ")
    print("1. Listar Contenido del directorio actual")
    print("2. Crear un nuevo directorio")
    print("3. Crear un archivo de texto")
    print("4. Escribir texto en un archivo existente")
    print("5. Eliminar archivo o directorio")
    print("6. Mostrar informacion del archivo")
    print("7. Renombrar elemento")
    print("8. Salir")
    
    
    
#FUNCION QUE PERMITE LISTAR EL CONTENIDO DEL DIRECTORIO    
def listar_contenido (): 
    try:
        print(f" {tit_menu} 📝 CONTENIDO DEL DIRECTORIO  ")
        print("="*40)
        
        elementos= os.listdir()
        
        if not elementos:
            print("El directorio se encuentra vacio")
            return
    
        for elemento in sorted(elementos):
            ruta_completa = os.path.join(os.getcwd(),elemento)
            if os.path.isdir(ruta_completa):
                print(f"📁 CARPETA -> {elemento}")
            else:
                tamaño_archivo= os.path.getsize(ruta_completa)
                print(f"📝 ARCHIVO -> {elemento} ({tamaño_archivo} bytes.)")
    except Exception as e:
        print(e)
            



#FUNCION PARA CREAR UN NUEVO DIRECTORIO
def crear_directorio (): 
    print(f" {tit_menu} 🗃️ CREAR NUEVO DIRECTORIO  ")
    print("="*40)

    nombreNvDirectorio = input("Escribe el nombre del nuevo directorio \n").strip()
    
    
    if not nombreNvDirectorio:
        print(f"❌ {rojo} El nombre no puede estar vacio")
        
    try:
        os.mkdir(nombreNvDirectorio)
        print(f"✅ {verde} Directorio creado correctamente")
    except FileExistsError:
        print(f"❌ {rojo} Error el directorio {nombreNvDirectorio} ya existe")
        
    except Exception as e:
        print(f"{rojo} Error inesperado al crear el directorio {e}")
        



#FUNCION PARA CREAR UN ARCHIVO
def crear_archivo ():
    print(f" {tit_menu} 📖 CREAR NUEVO ARCHIVO TXT  ")
    print("="*40) 
   
    nuevoArchivo=input("Escribe el nombre del nuevo archivo\n").strip()

   
    if not nuevoArchivo:
       print(f"❌ {rojo} El nombre no puede estar vacio")
       return
   
   
    if not nuevoArchivo.endswith('.txt'): # controlamos que siempre tenga la extension .txt
       nuevoArchivo += '.txt'
   
    try:
       if os.path.isfile(nuevoArchivo):
           print(f"❌ {rojo} El nombre del archivo ya existe")
           return
       
       contenido = input(f" Escribe el contenido {blanco}{negrita}(-Deja vacio para crear en blanco -){reset}\n")
       
       with open (nuevoArchivo,"w", encoding='UTF-8') as archivo:
           if contenido:
               archivo.write(contenido + "\n")
       print(f"{verde} ✅ Archivo creado correctamente")
    
    except Exception as e:
       print(f"{rojo} Error inesperado al crear el archivo{e}")
   


#ESCRIBIR EN ARCHIVO EXISTENTE
def escribirArchivo ():
    print(f" {tit_menu} ✍️  ESCRIBIR EN ARCHIVO EXISTENTE  ")
    print("="*40)

    nombreArchivo=input("Escribe el nombre del archivo: \n").strip()
    
    if not nombreArchivo:
        print(f"❌ {rojo} Error el nombre no puede estar vacio")
        return
    
    
    # controlamos que siempre tenga la extension .txt
    if not nombreArchivo.endswith('.txt'): 
       nombreArchivo += '.txt'
       
    
    try:
        if not os.path.exists(nombreArchivo):
            print(f"❌ Error el archivo no existe")
            return
        
        '''if not os.path.isfile(nombreArchivo):
            print(f"❌ Error {nombreArchivo} no es un archivo")
            return'''
        
        #MOSTRAMOS EL CONTENIDO ACTUAL DEL ARCHIVO
        print(f"{tit_menu} ⬇️  == CONTENIDO ACTUAL DEL ARCHIVO ==")
        with open(nombreArchivo,"r",encoding='UTF-8') as archivo:
            contenidoActual=archivo.read ()
            if contenidoActual:
                print(f"{blanco}" + contenidoActual)
            else:
                print(f"{rojo} El archivo esta vacio")
                print('*'*20) 
        
        #AQUI LE MANDAMOS EL NUEVO CONTENIDO PARA AÑADIR
        nuevoContenido=input("✍️ Escribe el nuevo contenido \n")
        with open(nombreArchivo,"a",encoding='UTF-8') as archivo:
            archivo.write(nuevoContenido + '\n')
            
        print(f"✅ {verde} Contenido añadido correctamente a: {nombreArchivo}")
    
    except Exception as e:
        print (f'Error al escribir en archivo:{e}')       
        


#ELIMINAR ARCHIVO O DIRECTORIO
def eliminarElemento ():
    print(f" {tit_menu} 🗑️  ELIMINAR ARCHIVO O DIRECTORIO  ")
    print("="*40)
    
    nombreElemento= input("Escribe el nombre del elemento a eliminar (incluye su extensión).\n").strip()
    
    if not nombreElemento:
        print(f"❌ {rojo} Error el nombre no puede estar vacio")
        return
    
    
    try:
        if not os.path.exists (nombreElemento):
            print(f"❌ {rojo} Error {nombreElemento} no existe")
            return
        
        
        if os.path.isdir(nombreElemento):
            tipo="directorio"
        else:
            tipo="archivo"
            
        confirmacion= input(f"⚠️ {tit_menu} Esta seguro de que quiere eliminar: {Fore.MAGENTA}{tipo} '{nombreElemento}' ?  (s/n): ").strip ().lower()
        
        if confirmacion != "s":
            print(f"❌ {rojo} Operación cancelada por el usuario")
            return
        
        if os.path.isdir(nombreElemento):
            shutil.rmtree(nombreElemento)
        else:
            os.remove(nombreElemento)
        
        print(f"✅ {verde} Elemento {nombreElemento} eliminado correctamente")
        
    except Exception as e:
        print(f"❌ {rojo} Error al eliminar {e}")
        
        

#MOSTRAR INFORMACION DEL ARCHIVO
def mostrarInfo ():
    print(f" {tit_menu} 🔍  MOSTRAR INFORMACION DEL ARCHIVO O DIRECTORIO ")
    print("="*40)
    
    nombre= input("Escribe el nombre del archivo o directorio \n")
    
    if not nombre:
        print(f"❌ {rojo} Error el nombre no puede estar vacio")
        return
    
    if not nombre.endswith('.txt'):
        nombre+='.txt'
    
    try:
        if not os.path.exists(nombre):
            print(f"❌ {rojo} Error el elemento {nombre} no existe")
            return
        
        informacion=os.stat(nombre)
        
        print(f"{blanco} 📋 Informacion de:  {Fore.YELLOW}{nombre}")
        print(f"Tamaño: {informacion.st_size} bytes")
        print(f"Fecha creacion: {datetime.datetime.fromtimestamp(informacion.st_ctime)}")
        print(f"Fecha ultima modificación: {datetime.datetime.fromtimestamp(informacion.st_mtime)}")
        print(f"Ruta completa: {os.path.abspath(nombre)}")
    
    except Exception as e:
        print(f"❌ {rojo} Error al obtener informacion {e}")
        

#RENOMBRAR ELEMENTO
def renombrarElemento ():
    print(f" {tit_menu} ✍️  RENOMBRAR ELEMENTO ")
    print("="*40)
    
    nombreActual=input("Escribe el nombre actual del elemento \n")
    
    if not nombreActual:
        print(f"❌ {rojo} El nombre no puede estar vacio")
        return
    
    try:
        if not os.path.exists(nombreActual):
            print(f"❌ {rojo} Error: {nombreActual} no existe.")
            return
        
        nombreNuevo=input("Introduce el nuevo nombre que quieres asignar \n").strip ()
        
        if not nombreNuevo:
            print(f"❌ {rojo} Error el nombre nuevo no puede estar vacio")
        
        if os.path.exists(nombreNuevo):
            print(f"❌ Error: {nombreNuevo} ya existe.")
            
        os.rename(nombreActual,nombreNuevo)
        print(f"✅ {verde} Renombrado correctamente {nombreActual} -> {nombreNuevo}")
    except Exception as e:
        print(f"❌ {rojo} Error al renombrar {e}")        
        



#FUNCION PRINCIPAL DEL PROGRAMA
def main ():
    print("=*="*20)
    print(f"{tit_menu} ==== 📁 BIENVENIDO A FILEBOX 📁 ====")
    print("=*="*20)

    while True:
        ruta_actual ()
        mostrar_menu()
        
        try:
            opcion=int(input("selecciona una opcion (8 para salir) \n"))
        except ValueError:
            print(f"{rojo} Introduce un valor valido (8 para salir \n)")
            continue
        
        match opcion:
            case 1:
                try:
                    listar_contenido ()
                except ValueError as e:print (e)
            case 2:
                try:
                    crear_directorio()
                except ValueError as e:print (e)
            case 3:
                try:
                    crear_archivo ()
                except ValueError as e:print(e)
            case 4:
                try:
                    escribirArchivo ()
                except ValueError as e:print (e)
            case 5:
                try:
                    eliminarElemento ()
                except ValueError as e:print(e)
            case 6:
                try:
                    mostrarInfo ()
                except ValueError as e:print(e)
            case 7:
                try:
                    renombrarElemento ()
                except ValueError as e: print(e)
            case 8:        
                print(f"\n{Fore.GREEN}👋 ¡Hasta luego! Gracias por usar el Gestor de Archivos")
                break
            
        
        
if __name__ == "__main__":
    main()

