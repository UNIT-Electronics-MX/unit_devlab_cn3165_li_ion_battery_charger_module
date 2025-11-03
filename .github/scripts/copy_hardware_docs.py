#!/usr/bin/env python3
"""
Script para copiar archivos de hardware y resources a docs y generar una página HTML
para visualizar el contenido.
"""

import os
import shutil
import json
from datetime import datetime
from pathlib import Path
from jinja2 import Template

# Configuración de rutas
BASE_DIR = Path(__file__).parent.parent.parent
HARDWARE_DIR = BASE_DIR / "hardware"
DOCS_DIR = BASE_DIR / "docs"
DOCS_HARDWARE_DIR = DOCS_DIR / "hardware"

# Extensiones de archivos por categoría
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'}
DOCUMENT_EXTENSIONS = {'.pdf', '.docx', '.doc', '.txt', '.md'}
DATA_EXTENSIONS = {'.json', '.xml', '.csv', '.yaml', '.yml'}

def ensure_directory(path):
    """Crear directorio si no existe"""
    path.mkdir(parents=True, exist_ok=True)

def get_file_info(file_path):
    """Obtener información del archivo"""
    stat = file_path.stat()
    return {
        'name': file_path.name,
        'size': stat.st_size,
        'size_human': format_size(stat.st_size),
        'modified': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
        'extension': file_path.suffix.lower(),
        'type': get_file_type(file_path.suffix.lower())
    }

def format_size(size_bytes):
    """Convertir bytes a formato legible"""
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f} {size_names[i]}"

def get_file_type(extension):
    """Determinar el tipo de archivo basado en la extensión"""
    if extension in IMAGE_EXTENSIONS:
        return 'image'
    elif extension in DOCUMENT_EXTENSIONS:
        return 'document'
    elif extension in DATA_EXTENSIONS:
        return 'data'
    else:
        return 'other'

def copy_hardware_files():
    """Copiar todos los archivos de hardware a docs/hardware"""
    print(" Copiando archivos de hardware...")
    
    # Crear directorio de destino
    ensure_directory(DOCS_HARDWARE_DIR)
    
    # Limpiar directorio existente
    if DOCS_HARDWARE_DIR.exists():
        shutil.rmtree(DOCS_HARDWARE_DIR)
    
    # Copiar todo el directorio hardware
    shutil.copytree(HARDWARE_DIR, DOCS_HARDWARE_DIR)
    
    print(f" Archivos copiados a {DOCS_HARDWARE_DIR}")

def scan_copied_files():
    """Escanear archivos copiados y generar estructura de datos"""
    print(" Escaneando archivos copiados...")
    
    file_structure = {}
    
    for root, dirs, files in os.walk(DOCS_HARDWARE_DIR):
        root_path = Path(root)
        relative_path = root_path.relative_to(DOCS_HARDWARE_DIR)
        
        # Crear estructura de carpetas
        current_dict = file_structure
        for part in relative_path.parts:
            if part not in current_dict:
                current_dict[part] = {'files': [], 'folders': {}}
            current_dict = current_dict[part]['folders']
        
        # Si estamos en el directorio raíz
        if str(relative_path) == '.':
            target_dict = file_structure
        else:
            # Navegar a la ubicación correcta
            target_dict = file_structure
            for part in relative_path.parts[:-1]:
                target_dict = target_dict[part]['folders']
            if relative_path.parts[-1] not in target_dict:
                target_dict[relative_path.parts[-1]] = {'files': [], 'folders': {}}
            target_dict = target_dict[relative_path.parts[-1]]
        
        # Agregar archivos
        if 'files' not in target_dict:
            target_dict['files'] = []
            
        for file in files:
            file_path = root_path / file
            file_info = get_file_info(file_path)
            file_info['path'] = str(file_path.relative_to(DOCS_DIR))
            target_dict['files'].append(file_info)
    
    return file_structure

def generate_html_page(file_structure):
    """Generar página HTML para visualizar los archivos"""
    print(" Generando página HTML...")
    
    html_template = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hardware Documentation - CN3165 Battery Charger Module</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css" rel="stylesheet">
    <style>
        .file-icon { margin-right: 8px; }
        .folder-icon { color: #ffc107; }
        .file-item { margin: 4px 0; padding: 8px; border-radius: 4px; transition: all 0.2s ease; }
        .file-item:hover { background-color: #f8f9fa; transform: translateX(5px); }
        .file-size { color: #6c757d; font-size: 0.9em; }
        .file-date { color: #6c757d; font-size: 0.85em; }
        .breadcrumb { background-color: #e9ecef; }
        .preview-modal img { max-width: 100%; height: auto; }
        .tree-item { margin-left: 20px; }
        .stats-card { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
        .type-badge { font-size: 0.75em; }
        .btn-group .btn { border-radius: 3px !important; }
        .file-actions { opacity: 0; transition: opacity 0.2s ease; }
        .file-item:hover .file-actions { opacity: 1; }
        .pdf-viewer { width: 100%; height: 600px; border: none; }
        .file-link { text-decoration: none !important; color: #495057; }
        .file-link:hover { color: #007bff; }
    </style>
</head>
<body>
    <nav class="navbar navbar-dark bg-dark">
        <div class="container-fluid">
            <span class="navbar-brand mb-0 h1">
                <i class="bi bi-cpu"></i>
                CN3165 Battery Charger Module - Hardware Documentation
            </span>
            <span class="navbar-text">
                Generado: {{ generated_time }}
            </span>
        </div>
    </nav>

    <div class="container-fluid mt-4">
        <div class="row">
            <div class="col-12">
                <div class="card stats-card mb-4">
                    <div class="card-body">
                        <div class="row text-center">
                            <div class="col-md-3">
                                <h3>{{ stats.total_files }}</h3>
                                <p class="mb-0">Total de Archivos</p>
                            </div>
                            <div class="col-md-3">
                                <h3>{{ stats.images }}</h3>
                                <p class="mb-0">Imágenes</p>
                            </div>
                            <div class="col-md-3">
                                <h3>{{ stats.documents }}</h3>
                                <p class="mb-0">Documentos</p>
                            </div>
                            <div class="col-md-3">
                                <h3>{{ stats.total_size }}</h3>
                                <p class="mb-0">Tamaño Total</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-12">
                <div class="card">
                    <div class="card-header">
                        <h5 class="card-title mb-0">
                            <i class="bi bi-folder-fill folder-icon"></i>
                            Estructura de Archivos
                        </h5>
                    </div>
                    <div class="card-body">
                        {{ render_tree(file_structure, "") }}
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal para previsualizar imágenes -->
    <div class="modal fade" id="imageModal" tabindex="-1">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="imageModalLabel">Vista Previa de Imagen</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body text-center">
                    <img id="modalImage" src="" alt="Vista previa" class="img-fluid">
                </div>
                <div class="modal-footer">
                    <a id="imageDirectLink" href="" target="_blank" class="btn btn-primary">
                        <i class="bi bi-box-arrow-up-right"></i> Abrir en nueva pestaña
                    </a>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal para previsualizar PDFs -->
    <div class="modal fade" id="pdfModal" tabindex="-1">
        <div class="modal-dialog modal-xl">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="pdfModalLabel">Vista Previa de PDF</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body p-0">
                    <iframe id="pdfViewer" class="pdf-viewer" src=""></iframe>
                </div>
                <div class="modal-footer">
                    <a id="pdfDirectLink" href="" target="_blank" class="btn btn-primary">
                        <i class="bi bi-box-arrow-up-right"></i> Abrir en nueva pestaña
                    </a>
                    <a id="pdfDownloadLink" href="" download class="btn btn-secondary">
                        <i class="bi bi-download"></i> Descargar
                    </a>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Función para mostrar vista previa de imágenes
        function previewImage(src, title) {
            document.getElementById('modalImage').src = src;
            document.getElementById('imageModalLabel').textContent = title;
            document.getElementById('imageDirectLink').href = src;
            new bootstrap.Modal(document.getElementById('imageModal')).show();
        }

        // Función para mostrar vista previa de PDFs
        function previewPDF(src, title) {
            document.getElementById('pdfViewer').src = src;
            document.getElementById('pdfModalLabel').textContent = title;
            document.getElementById('pdfDirectLink').href = src;
            document.getElementById('pdfDownloadLink').href = src;
            new bootstrap.Modal(document.getElementById('pdfModal')).show();
        }

        // Función para alternar carpetas
        function toggleFolder(element) {
            const content = element.nextElementSibling;
            const icon = element.querySelector('.folder-toggle');
            
            if (content.style.display === 'none') {
                content.style.display = 'block';
                icon.classList.remove('bi-chevron-right');
                icon.classList.add('bi-chevron-down');
            } else {
                content.style.display = 'none';
                icon.classList.remove('bi-chevron-down');
                icon.classList.add('bi-chevron-right');
            }
        }

        // Función para abrir archivo en nueva pestaña
        function openInNewTab(url) {
            window.open(url, '_blank');
        }

        // Manejar clicks con Ctrl para abrir en nueva pestaña
        document.addEventListener('click', function(e) {
            if (e.ctrlKey || e.metaKey) {
                const link = e.target.closest('a[onclick*="previewImage"]');
                if (link) {
                    e.preventDefault();
                    const src = link.getAttribute('onclick').match(/'([^']+)'/)[1];
                    window.open(src, '_blank');
                }
            }
        });
    </script>
</body>
</html>
    '''
    
    def get_file_icon(file_type, extension):
        """Obtener icono según el tipo de archivo"""
        if file_type == 'image':
            return 'bi-file-earmark-image'
        elif file_type == 'document':
            if extension == '.pdf':
                return 'bi-file-earmark-pdf'
            else:
                return 'bi-file-earmark-text'
        else:
            return 'bi-file-earmark'

    def render_tree(structure, path_prefix):
        """Renderizar árbol de archivos"""
        html = ""
        
        # Renderizar carpetas
        for folder_name, folder_data in structure.items():
            if folder_name == 'files':
                continue
                
            folder_path = f"{path_prefix}/{folder_name}" if path_prefix else folder_name
            folder_id = folder_path.replace('/', '_').replace(' ', '_')
            
            html += f'''
            <div class="tree-item">
                <div class="d-flex align-items-center file-item" style="cursor: pointer;" onclick="toggleFolder(this)">
                    <i class="bi bi-chevron-down folder-toggle"></i>
                    <i class="bi bi-folder-fill folder-icon file-icon"></i>
                    <strong>{folder_name}</strong>
                </div>
                <div id="{folder_id}" class="ms-3">
            '''
            
            # Renderizar archivos de la carpeta
            if 'files' in folder_data and folder_data['files']:
                for file_info in folder_data['files']:
                    icon_class = get_file_icon(file_info['type'], file_info['extension'])
                    type_color = {
                        'image': 'success',
                        'document': 'primary',
                        'data': 'info',
                        'other': 'secondary'
                    }.get(file_info['type'], 'secondary')
                    
                    file_link = f"hardware/{file_info['path'].replace('hardware/', '')}"
                    
                    # Configurar enlaces según el tipo de archivo
                    if file_info['type'] == 'image':
                        # Imágenes: preview modal + enlace directo
                        click_action = f"previewImage('{file_link}', '{file_info['name']}')"
                        link_attrs = f'style="cursor: pointer;" onclick="{click_action}" title="Click para vista previa - Ctrl+Click para abrir en nueva pestaña" oncontextmenu="window.open(\'{file_link}\', \'_blank\'); return false;"'
                    elif file_info['extension'].lower() == '.pdf':
                        # PDFs: abrir en nueva pestaña con viewer integrado
                        link_attrs = f'href="{file_link}" target="_blank" title="Abrir PDF en nueva pestaña"'
                    else:
                        # Otros archivos: abrir en nueva pestaña
                        link_attrs = f'href="{file_link}" target="_blank" title="Abrir archivo en nueva pestaña"'
                    
                    # Agregar botones adicionales para PDFs
                    extra_buttons = ""
                    if file_info['extension'].lower() == '.pdf':
                        extra_buttons = f'''
                        <div class="btn-group btn-group-sm ms-2 file-actions" role="group">
                            <button onclick="previewPDF('{file_link}', '{file_info['name']}')" class="btn btn-outline-success btn-sm" title="Vista previa PDF">
                                <i class="bi bi-eye"></i>
                            </button>
                            <a href="{file_link}" target="_blank" class="btn btn-outline-primary btn-sm" title="Abrir PDF en nueva pestaña">
                                <i class="bi bi-box-arrow-up-right"></i>
                            </a>
                            <a href="{file_link}" download class="btn btn-outline-secondary btn-sm" title="Descargar PDF">
                                <i class="bi bi-download"></i>
                            </a>
                        </div>
                        '''
                    elif file_info['type'] == 'image':
                        extra_buttons = f'''
                        <div class="btn-group btn-group-sm ms-2 file-actions" role="group">
                            <button onclick="previewImage('{file_link}', '{file_info['name']}')" class="btn btn-outline-success btn-sm" title="Vista previa de imagen">
                                <i class="bi bi-eye"></i>
                            </button>
                            <a href="{file_link}" target="_blank" class="btn btn-outline-primary btn-sm" title="Abrir imagen en nueva pestaña">
                                <i class="bi bi-box-arrow-up-right"></i>
                            </a>
                        </div>
                        '''
                    
                    html += f'''
                    <div class="d-flex align-items-center justify-content-between file-item">
                        <div class="d-flex align-items-center flex-grow-1">
                            <i class="bi {icon_class} file-icon"></i>
                            <a {link_attrs} class="text-decoration-none me-2 flex-grow-1">{file_info['name']}</a>
                            <span class="badge bg-{type_color} type-badge me-2">{file_info['type']}</span>
                            {extra_buttons}
                        </div>
                        <div class="text-end ms-3">
                            <small class="file-size d-block">{file_info['size_human']}</small>
                            <small class="file-date">{file_info['modified']}</small>
                        </div>
                    </div>
                    '''
            
            # Renderizar subcarpetas recursivamente
            if 'folders' in folder_data:
                html += render_tree(folder_data['folders'], folder_path)
            
            html += '''
                </div>
            </div>
            '''
        
        return html

    # Calcular estadísticas
    def calculate_stats(structure):
        stats = {'total_files': 0, 'images': 0, 'documents': 0, 'total_size_bytes': 0}
        
        def count_recursive(struct):
            for key, value in struct.items():
                if key == 'files':
                    for file_info in value:
                        stats['total_files'] += 1
                        stats['total_size_bytes'] += file_info['size']
                        if file_info['type'] == 'image':
                            stats['images'] += 1
                        elif file_info['type'] == 'document':
                            stats['documents'] += 1
                elif isinstance(value, dict) and 'folders' in value:
                    count_recursive(value['folders'])
                    if 'files' in value:
                        for file_info in value['files']:
                            stats['total_files'] += 1
                            stats['total_size_bytes'] += file_info['size']
                            if file_info['type'] == 'image':
                                stats['images'] += 1
                            elif file_info['type'] == 'document':
                                stats['documents'] += 1
        
        count_recursive(structure)
        stats['total_size'] = format_size(stats['total_size_bytes'])
        return stats

    # Preparar datos para el template
    template_data = {
        'file_structure': file_structure,
        'generated_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'stats': calculate_stats(file_structure),
        'render_tree': render_tree
    }
    
    # Renderizar template
    template = Template(html_template)
    html_content = template.render(**template_data)
    
    # Guardar archivo HTML
    html_file = DOCS_DIR / "index.html"
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f" Página HTML generada: {html_file}")

def main():
    """Función principal"""
    print(" Iniciando proceso de copia y generación de documentación...")
    
    try:
        # Copiar archivos
        copy_hardware_files()
        
        # Escanear archivos copiados
        file_structure = scan_copied_files()
        
        # Generar página HTML
        generate_html_page(file_structure)
        
        print("\n Proceso completado exitosamente!")
        print(f" Archivos copiados en: {DOCS_HARDWARE_DIR}")
        print(f"Página HTML disponible en: {DOCS_DIR}/index.html")
        
    except Exception as e:
        print(f" Error durante el proceso: {str(e)}")
        raise

if __name__ == "__main__":
    main()