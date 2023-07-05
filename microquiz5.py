class empleado:
 def __init__(self,rol,nombre,cedula):
  self.rol = rol
  self.nombre = nombre
  self.cedula = cedula
empleado1 = []
empleado2 = []
balance = []
empleado = {"empleado1":{"nombre":"jose","balance":1000}, "empleado2":{"nombre":"juan","balance": 2000}} 
empleado ["empleado1"]["balance"] += 500
print(empleado["empleado1"]["balance"]) 
def retirar_dinero(self,empleados,cantidad):
 if empleado in empleados:
  balance_actual = empleados[empleado]["balance"]
  if cantidad <= balance_actual:
   empleados[empleado]["balance"] -= cantidad
   print("retiro exitoso.nuevo balance:",empleados[empleado]["balance"])
  else:
   print("no tienes suficientes fondos para realizar el retiro")
 else:
  print("el empleado no existe")
def pago_de_salario(self,empleados,cantidad):
 for empleado in empleados:
  empleados[empleado]["balance"] += cantidad 
 print("pago de salario exitoso.nuevo balance:",empleados[empleado]["balance"])
class nomina:
 def __init__(self,presupuesto,cantidad_dinero_disponible):
  self.presupuesto = presupuesto
  self.cantidad_dinero_disponible = cantidad_dinero_disponible
  empleados = []
def pagar_nomina_empleados(self,empleado,monto_pago):
 if monto_pago != empleado.salario:
  return False
 return True
def registrar_empleados(self,rol):
 rol = input("ingrese el rol del empleado")
nombre = input("ingrese el nombre del empleado")
cedula = input("ingrese la cedula del empleado")
def agregar_saldo_presupuesto_nomina(self,nomina,saldo_a_agregar):
 nomina += saldo_a_agregar
 return nomina
presupuesto_nomina = 10000 
saldo_agregar = 5000
presupuesto_nomina = saldo_agregar
print("el presupuesto de la nomina es:",presupuesto_nomina)
def menu(self):
 opciones = ""
correr = True
while correr:
 opciones = input("seleccione una de las opciones:1.(registrar_empleados), 2.(mostrar empleados), 3.(pagar_nomina), 4.(agregar_presupuesto), 5.(salir_del_sistema")
def registrar_empleados():
 print("has elegido la opcion 1")
def mostrar_empleados():
 print("has elegido la opcion 2")
def pagar_nomina():
 print("has elegido la opcion 3")
def agregar_presupuesto():
 print("has elegido la opcion 4")
def salir_del_sistema():
 print("salir del sistema")
 if opciones == 1:
  registrar_empleados()
 elif opciones == 2:
  mostrar_empleados()
 elif opciones == 3:
  pagar_nomina()
 elif opciones == 4:
  agregar_presupuesto()
 elif opciones == 5:
  correr = False
 else:
  print("error: selecciona una de las opciones")
menu()
print("arreglo agregado")
print("version final")



 

