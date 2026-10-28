import pandas as pd

# Simulación de un DataFrame basado en los logs extraídos del servidor web
def analizar_rendimiento_servidor():
    print("--- INICIANDO AUDITORÍA DE LOGS DE APLICACIÓN ---")
    
    # Datos simulados de peticiones HTTP a la API
    data = {
        'endpoint': ['/api/users', '/api/products', '/api/checkout', '/api/users', '/api/checkout'],
        'metodo': ['GET', 'GET', 'POST', 'POST', 'POST'],
        'codigo_estado': [200, 200, 500, 201, 500],
        'tiempo_respuesta_ms': [120, 85, 1450, 210, 1800]
    }
    
    df = pd.DataFrame(data)
    
    # 1. Calcular el tiempo promedio de respuesta por endpoint
    latencia_promedio = df.groupby('endpoint')['tiempo_respuesta_ms'].mean().reset_index()
    print("\n[+] Tiempo de respuesta promedio (ms) por Endpoint:")
    print(latencia_promedio)
    
    # 2. Filtrar endpoints problemáticos (con errores HTTP 500)
    errores_criticos = df[df['codigo_estado'] >= 500]
    print("\n[+] Alerta: Peticiones que devolvieron Error de Servidor (500+):")
    print(errores_criticos[['endpoint', 'metodo', 'tiempo_respuesta_ms']])

if __name__ == "__main__":
    analizar_rendimiento_servidor()
