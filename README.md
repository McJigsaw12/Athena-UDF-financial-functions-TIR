# Athena-UDF-financial-functions-TIR
Código para realizar una consulta desde Athena a una Funcion de AWS Lambda mediante

El codigo funciona con la siguiente llamada en Athena en su version V3.

USING EXTERNAL FUNCTION TIRMensual(flujos_caja array<double>) 
RETURNS double LAMBDA 'Dev-financial-functions-TIR'    

SELECT TIRMensual(ARRAY[-10000.0, 1500.0, 2000.0, 2500.0, 3000.0, 3500.0]) as tir_mensual;



Para uso con una tabla:
USING EXTERNAL FUNCTION TIRMensual(flujos_caja array<double>) 
RETURNS double LAMBDA 'Dev-Athena-UDF'

SELECT 
    proyecto_id,
    TIRMensual(flujos_mensuales) as tir_mensual
FROM mi_tabla_proyectos;
