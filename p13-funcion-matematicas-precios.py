#p13-funcion-matematicas-precios

import math as mt
print("DESMOSTRANDO EL USO DE FUNCIONES DE REDONDEO")


precio= 15.65
print(f"precio : {precio}")
print(f"Arriba :{mt.ceil(precio)}")
print(f"Abajo  :{mt.floor(precio)}")
print(f"Truncar :{mt.trunc(precio)}")
print(f"Normal :{round(precio)}")
print(f"2 dec :{round(precio,2)}")

