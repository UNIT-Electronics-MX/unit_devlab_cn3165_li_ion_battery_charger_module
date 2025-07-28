# Makefile para generación de hojas de datos
# Módulo CN3165 Battery Charger

.PHONY: all pdf clean help install

# Variables
README = README.md
BUILD_DIR = build
DOCS_DIR = ../../docs
PYTHON_VENV = ../../../../.venv/bin/python

# Comando por defecto
all: pdf

# Generar PDF usando el script general
pdf:
	@echo "📄 Generando hoja de datos para CN3165 Battery Charger..."
	@mkdir -p $(BUILD_DIR)
	@$(PYTHON_VENV) generate_pdf.py
	@mkdir -p $(DOCS_DIR)
	@cp $(BUILD_DIR)/cn3165_battery_charger_module.pdf $(DOCS_DIR)/unit_cn3165_battery_charger_module_product_brief.pdf
	@echo "✅ PDF generado en $(BUILD_DIR)/ y copiado a $(DOCS_DIR)/"

# Instalar dependencias
install:
	@echo "📦 Instalando dependencias..."
	@$(PYTHON_VENV) -m pip install -r requirements.txt
	@echo "✅ Dependencias instaladas"

# Limpiar archivos generados
clean:
	@echo "🧹 Limpiando archivos generados..."
	@rm -rf $(BUILD_DIR)
	@echo "✅ Limpieza completada"

# Verificar que README.md existe
check:
	@if [ ! -f $(README) ]; then \
		echo "❌ Error: $(README) no encontrado"; \
		exit 1; \
	fi
	@echo "✅ $(README) encontrado"

# Mostrar información de ayuda
help:
	@echo "🛠️ GENERADOR DE HOJAS DE DATOS - CN3165 Battery Charger"
	@echo "======================================================"
	@echo ""
	@echo "Comandos disponibles:"
	@echo "  make pdf             - Genera PDF del product brief"
	@echo "  make install         - Instala dependencias"
	@echo "  make clean           - Limpia archivos generados"
	@echo "  make check           - Verifica que README.md existe"
	@echo "  make help            - Muestra esta ayuda"
	@echo ""
	@echo "📁 Salidas:"
	@echo "  - build/cn3165_battery_charger_module.pdf"
	@echo "  - ../../docs/unit_cn3165_battery_charger_module_product_brief.pdf"
