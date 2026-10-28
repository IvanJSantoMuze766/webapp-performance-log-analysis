# ⚡ Análisis de Rendimiento y Logs de Aplicación Web

Proyecto técnico que combina desarrollo backend y análisis de datos para auditar los tiempos de respuesta, errores HTTP y cuellos de botella en una plataforma web.

---

## 🎯 1. Planteamiento del Problema
Una aplicación en producción experimenta caídas intermitentes de velocidad y reportes de usuarios sobre fallas en endpoints específicos. Este proyecto analiza un archivo de registros (logs) del servidor para identificar qué rutas de la API degradan la experiencia de usuario y dónde se producen los mayores picos de latencia.

---

## 🛠️ 2. Tecnologías y Herramientas Utilizadas
* **Python (Pandas / Regex):** Procesamiento, limpieza y extracción de patrones en archivos de texto masivos (logs de servidor).
* **SQL / SQLite:** Almacenamiento estructurado de los registros de tráfico para consultas de agregación.
* **Node.js / Express (Entorno):** Contexto de desarrollo de la plataforma auditada.

---

## 📈 3. Enfoque del Análisis (Consultas / Scripts Clave)
1. **Identificación de Endpoints Lentos:** Agrupar las peticiones por ruta (`/api/v1/...`) y calcular el tiempo promedio de respuesta (latencia).
2. **Auditoría de Códigos de Error:** Cuantificar la frecuencia de errores HTTP (500 Internal Server Error, 404 Not Found) frente a peticiones exitosas (200 OK).
3. **Detección de Tráfico Anómalo:** Filtrar direcciones IP o patrones de llamadas repetitivas que saturen el backend.
