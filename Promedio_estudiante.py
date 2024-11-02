CantExam=int(input("Escriba la cantidad de examenes que hizo el estudiante:  "))

if (CantExam==1): 
    exam1=int(input("Escriba la nota 1:  "))
    exam2=0
    exam3=0  
    SUMA=exam1+exam2+exam3
    Nota=SUMA/1
elif (CantExam==2):
    exam1=int(input("Escriba la nota 1:  "))  
    exam2=int(input("Escriba la nota 2:  "))
    exam3=0
    SUMA=exam1+exam2+exam3
    Nota=SUMA/2
elif CantExam==3:
    exam1=int(input("Escriba la nota 1:  "))  
    exam2=int(input("Escriba la nota 2:  "))  
    exam3=int(input("Escriba la nota 3:  ")) 
    SUMA=exam1+exam2+exam3
    Nota=SUMA/3
       
print("La nota del estudiante es de",Nota)

if(Nota>=70):
    print("Aprobado")
elif(Nota<=70) and (Nota>=60):
    print("Ampliación")
elif(Nota<=59):
    print("Reprobado")