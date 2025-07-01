from typing import Any
from pyarrow import Schema
from athena_udf import BaseAthenaUDF
import numpy_financial as npf

class TIRMensualUDF(BaseAthenaUDF):
    """
    UDF que calcula la TIR (Tasa Interna de Retorno) mensual usando numpy-financial
    """
    
    @staticmethod
    def handle_athena_record(input_schema: Schema, output_schema: Schema, arguments: list[Any]):
        # Validar que se reciba el arreglo de flujos de caja
        if not arguments or not arguments[0]:
            return None
            
        try:
            # Obtener el arreglo de flujos de caja
            cash_flows = arguments[0]
            
            # Validar que el arreglo tenga al menos un valor positivo y uno negativo
            if len(cash_flows) < 2:
                return None
                
            # Convertir a lista de números
            flows = [float(x) for x in cash_flows]
            
            # Verificar que haya al menos un valor positivo y uno negativo
            has_positive = any(x > 0 for x in flows)
            has_negative = any(x < 0 for x in flows)
            
            if not (has_positive and has_negative):
                return None
            
            # Calcular TIR mensual usando numpy-financial
            tir_mensual = npf.irr(flows)
            
            return float(tir_mensual) if tir_mensual is not None else None
            
        except Exception:
            return None

# Handler para Lambda
lambda_handler = TIRMensualUDF().lambda_handler
