# Q&A Gemini - Sistema de Preguntas y Respuestas con IA

Un sistema inteligente de preguntas y respuestas que utiliza Google Gemini AI para procesar documentos PDF y responder consultas de manera conversacional.

## 🚀 Características

- **Procesamiento de PDFs**: Extrae texto de documentos PDF usando PyMuPDF y OCR como respaldo
- **IA Conversacional**: Integración con Google Gemini AI para respuestas inteligentes
- **Búsqueda Vectorial**: Utiliza FAISS para búsqueda semántica eficiente
- **Interfaz Web**: Aplicación Streamlit intuitiva y fácil de usar
- **Múltiples Aplicaciones**: Diferentes versiones de la aplicación para diversos casos de uso

## 📋 Requisitos

- Python 3.8+
- Google API Key para Gemini AI
- Dependencias listadas en `requirements.txt`

## 🛠️ Instalación

1. **Clona el repositorio:**
```bash
git clone https://github.com/tu-usuario/Q&A-GEMINI.git
cd Q&A-GEMINI
```

2. **Crea un entorno virtual:**
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

3. **Instala las dependencias:**
```bash
pip install -r requirements.txt
```

4. **Configura las variables de entorno:**
Crea un archivo `.env` en la raíz del proyecto:
```env
GOOGLE_API_KEY=tu_api_key_aqui
```

## 🚀 Uso

### Aplicación Principal
```bash
streamlit run app.py
```

### Aplicación Simple
```bash
streamlit run app_simple.py
```

### Aplicación Básica
```bash
streamlit run app_basic.py
```

### Script de Q&A
```bash
python q-a.py
```

## 📁 Estructura del Proyecto

```
Q&A-GEMINI/
├── app.py              # Aplicación principal con OCR y PyMuPDF
├── app_simple.py       # Versión simplificada
├── app_basic.py        # Versión básica
├── q-a.py             # Script de línea de comandos
├── requirements.txt    # Dependencias del proyecto
├── faiss_index/       # Índices vectoriales (generados automáticamente)
└── README.md          # Este archivo
```

## 🔧 Configuración

### Google Gemini API
1. Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Crea una nueva API key
3. Agrega la key al archivo `.env`

### Dependencias Opcionales
- **Tesseract OCR**: Para extracción de texto de imágenes
- **PyMuPDF**: Para mejor extracción de texto de PDFs

## 📝 Casos de Uso

- **Análisis de Documentos**: Procesa informes, manuales, investigaciones
- **Asistente de Estudio**: Responde preguntas sobre material educativo
- **Investigación**: Analiza múltiples fuentes de información
- **Consultoría**: Procesa documentos técnicos y responde consultas

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## ⚠️ Notas Importantes

- Asegúrate de tener suficiente espacio en disco para los índices vectoriales
- La API de Google Gemini tiene límites de uso
- Los archivos PDF grandes pueden tardar en procesarse

## 🆘 Soporte

Si encuentras algún problema o tienes preguntas, por favor:

1. Revisa los issues existentes
2. Crea un nuevo issue con detalles del problema
3. Incluye información sobre tu sistema operativo y versión de Python

---

**Desarrollado con ❤️ usando Python, Streamlit y Google Gemini AI** 