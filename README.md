# Athena-UDF-Financial-Functions-TIR

## 📊 Descripción

Función definida por el usuario (UDF) para Amazon Athena que permite calcular la **Tasa Interna de Retorno (TIR)** mensual mediante una función AWS Lambda. Esta integración permite realizar cálculos financieros avanzados directamente en consultas SQL de Athena.

## 🚀 Características

- ✅ Cálculo de TIR mensual
- ✅ Integración nativa con Amazon Athena v3
- ✅ Procesamiento mediante AWS Lambda
- ✅ Soporte para arrays de flujos de caja
- ✅ Compatible con tablas existentes

## 📋 Requisitos

- Amazon Athena versión 3
- AWS Lambda function configurada
- Permisos IAM apropiados para invocar Lambda desde Athena

## 🔧 Configuración

### Función Lambda
Asegúrate de tener desplegada la función Lambda con el nombre:
```
Dev-financial-functions-TIR
```

### Sintaxis de la Función
```sql
USING EXTERNAL FUNCTION TIRMensual(flujos_caja array<double>) 
RETURNS double 
LAMBDA 'Dev-financial-functions-TIR'
```

## 📖 Ejemplos de Uso

### Ejemplo Básico
Cálculo de TIR con valores fijos:

```sql
USING EXTERNAL FUNCTION TIRMensual(flujos_caja array<double>) 
RETURNS double 
LAMBDA 'Dev-financial-functions-TIR'

SELECT TIRMensual(ARRAY[-10000.0, 1500.0, 2000.0, 2500.0, 3000.0, 3500.0]) as tir_mensual;
```

**Resultado esperado:**
- Inversión inicial: -$10,000
- Flujos mensuales: $1,500, $2,000, $2,500, $3,000, $3,500
- TIR calculada en formato decimal

### Ejemplo con Tabla
Aplicación sobre datos existentes:

```sql
USING EXTERNAL FUNCTION TIRMensual(flujos_caja array<double>) 
RETURNS double 
LAMBDA 'Dev-financial-functions-TIR'

SELECT 
    proyecto_id,
    TIRMensual(flujos_mensuales) as tir_mensual
FROM mi_tabla_proyectos;
```

### Ejemplo Avanzado
Consulta con filtros y formato:

```sql
USING EXTERNAL FUNCTION TIRMensual(flujos_caja array<double>) 
RETURNS double 
LAMBDA 'Dev-financial-functions-TIR'

SELECT 
    proyecto_id,
    nombre_proyecto,
    TIRMensual(flujos_mensuales) as tir_mensual,
    ROUND(TIRMensual(flujos_mensuales) * 100, 2) as tir_porcentaje
FROM mi_tabla_proyectos
WHERE array_length(flujos_mensuales) >= 6
ORDER BY tir_mensual DESC;
```

## 📊 Estructura de Datos

### Entrada (flujos_caja)
- **Tipo:** `array<double>`
- **Formato:** `[inversión_inicial, flujo_mes1, flujo_mes2, ..., flujo_mesN]`
- **Nota:** La inversión inicial debe ser negativa

### Salida
- **Tipo:** `double`
- **Formato:** Tasa decimal (ej: 0.15 = 15%)

## ⚠️ Consideraciones

1. **Inversión inicial:** Debe ser un valor negativo
2. **Mínimo de periodos:** Se recomienda al menos 3-4 flujos para cálculos precisos
3. **Convergencia:** La función puede no converger si los flujos no tienen una TIR real
4. **Performance:** El procesamiento se realiza en Lambda, considera los límites de timeout

## 🔍 Troubleshooting

### Error común: "Function not found"
- Verificar que la función Lambda esté desplegada
- Confirmar permisos IAM
- Validar el nombre de la función Lambda

### Error: "Invalid array format"
- Asegurar que todos los valores sean de tipo `double`
- Verificar que la inversión inicial sea negativa

## 📝 Notas Técnicas

- La función utiliza métodos numéricos para el cálculo iterativo de la TIR
- Los resultados se devuelven en formato decimal mensual
- Para TIR anual, multiplicar el resultado por 12

## 🤝 Contribuciones

Si encuentras bugs o tienes sugerencias de mejora, por favor crea un issue en este repositorio.

---

**Versión:** 1.0  
**Última actualización:** 2025  
**Compatibilidad:** Amazon Athena v3
