"""Tests para el módulo de configuración."""

import pytest
from config import Config


class TestConfig:
    """Test cases para la clase Config."""

    def test_gemini_model(self):
        """Test que verifica el modelo por defecto."""
        assert Config.GEMINI_MODEL == "gemini-pro"

    def test_chunk_size(self):
        """Test que verifica el tamaño de chunk por defecto."""
        assert Config.CHUNK_SIZE == 10000

    def test_chunk_overlap(self):
        """Test que verifica el overlap de chunk por defecto."""
        assert Config.CHUNK_OVERLAP == 1000

    def test_max_file_size(self):
        """Test que verifica el tamaño máximo de archivo."""
        expected_size = 50 * 1024 * 1024  # 50MB
        assert Config.MAX_FILE_SIZE == expected_size

    def test_vector_store_path(self):
        """Test que verifica la ruta del vector store."""
        assert Config.VECTOR_STORE_PATH == "faiss_index"

    def test_get_model_config(self):
        """Test que verifica la configuración del modelo."""
        model_config = Config.get_model_config()
        assert model_config["model"] == "gemini-pro"
        assert model_config["temperature"] == 0.7
        assert model_config["top_p"] == 0.9
        assert model_config["top_k"] == 40

    def test_validate_without_api_key(self, monkeypatch):
        """Test que verifica la validación sin API key."""
        monkeypatch.setenv("GOOGLE_API_KEY", "")
        with pytest.raises(ValueError, match="GOOGLE_API_KEY no está configurada"):
            Config.validate()

    def test_validate_with_api_key(self, monkeypatch):
        """Test que verifica la validación con API key."""
        monkeypatch.setenv("GOOGLE_API_KEY", "test_key")
        assert Config.validate() is True 