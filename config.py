"""Configuración del proyecto Q&A Gemini AI."""

import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()


class Config:
    """Clase de configuración centralizada."""

    # Configuración de la API
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GEMINI_MODEL = "gemini-pro"

    # Configuración de procesamiento de PDFs
    MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB
    CHUNK_SIZE = 10000
    CHUNK_OVERLAP = 1000

    # Configuración de Streamlit
    STREAMLIT_PORT = int(os.getenv("STREAMLIT_SERVER_PORT", 8501))
    STREAMLIT_HOST = os.getenv("STREAMLIT_SERVER_ADDRESS", "localhost")

    # Configuración de la base de datos vectorial
    VECTOR_STORE_PATH = "faiss_index"

    @classmethod
    def validate(cls):
        """Validar que la configuración sea correcta."""
        if not cls.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY no está configurada")
        return True

    @classmethod
    def get_model_config(cls):
        """Obtener configuración del modelo."""
        return {
            "model": cls.GEMINI_MODEL,
            "temperature": 0.7,
            "top_p": 0.9,
            "top_k": 40
        } 