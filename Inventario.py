# ESTUDIANTE: JUAN ESTEBAN SAAVEDRA GUEVARA 
# PROBLEMA SELECCIONADO: Problema 3 (Auditoría de Inventario)

# MÓDULO (FUNCIÓN): Determina la cantidad exacta de artículos a solicitar
def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    # Lógica de Negocio:
    # Si el stock actual es menor al mínimo, se pide la diferencia
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    # Si hay suficiente stock, no se pide nada (cero)
    else:
        return 0

# MATRIZ DE DATOS: [Código Artículo, Nombre, Stock Actual, Stock Mínimo]
inventario_articulos = [
    ["ART-01", "Cuadernos A4", 15, 50],   # Requiere pedido (50 - 15 = 35)
    ["ART-02", "Bolígrafos Azules", 120, 100], # Stock suficiente (0)
    ["ART-03", "Marcadores", 5, 20],      # Requiere pedido (20 - 5 = 15)
    ["ART-04", "Resmas de Papel", 8, 8],   # Stock justo (0)
    ["ART-05", "Borradores", 2, 15]        # Requiere pedido (15 - 2 = 13)
]

# SALIDA: Generación del informe de pedidos solicitado
print("       INFORME DE AUDITORÍA DE INVENTARIO        ")
print(f"{'Artículo':<25} | {'Cantidad a Solicitar':<15}")
print("-" * 48)

# Recorrido de la matriz para evaluar cada artículo
for articulo in inventario_articulos:
    nombre_articulo = articulo[1]
    stock_act = articulo[2]
    stock_min = articulo[3]
    
    # Llamado al módulo para aplicar la lógica
    cantidad_final = calcular_cantidad_a_pedir(stock_act, stock_min)
    
    # Impresión de resultados en formato de lista
    print(f"{nombre_articulo:<25} | {cantidad_final:<15}")
