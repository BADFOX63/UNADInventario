# UNADInventario
Este repositorio contiene la solución al **Problema 3: Auditoría de Inventario** seleccionado para la evaluación final práctica del curso.

Descripción del Problema
Se requiere una herramienta para auditar el inventario y decidir qué artículos necesitan ser reabastecidos. La información se gestiona a través de una matriz de datos con la estructura: `[Código Artículo, Nombre, Stock Actual, Stock Mínimo Requerido]`.

Matriz de Datos: Implementación de una estructura bidimensional con 5 artículos iniciales.
Modularidad: Creación de una función/módulo para automatizar el cálculo del pedido exacto.
 Lógica de Negocio:
    Si el $Stock Actual < Stock Mínimo$, se solicita la diferencia exacta: (Mínimo - Actual).
    Si el $Stock Actual \ge Stock Mínimo$, la cantidad a solicitar es cero (0).
Salida: Impresión en consola de un informe tabular detallando el nombre del artículo y la cantidad solicitada.
