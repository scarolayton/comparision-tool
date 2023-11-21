#!/bin/bash
# I know that u didnt need it on this way but I tried for two days and It was imposible for me
# Iniciar el servidor backend
#!/bin/bash

# Ruta al archivo .tar.gz que contiene las imágenes de Docker
ARCHIVO_IMAGENES="image.tar.gz"

# Verificar si el archivo existe
if [ -f "$ARCHIVO_IMAGENES" ]; then
    echo "Descomprimiendo $ARCHIVO_IMAGENES..."
    tar -xzvf "$ARCHIVO_IMAGENES"

    # Obtener la lista de archivos .tar extraídos
    ARCHIVOS_TAR=$(ls *.tar 2>/dev/null)

    # Cargar cada archivo .tar como imagen en Docker
    for ARCHIVO in $ARCHIVOS_TAR; do
        echo "Cargando $ARCHIVO como imagen en Docker..."
        docker load -i "$ARCHIVO"
    done

    # Eliminar los archivos .tar extraídos (opcional)
else
    echo "El archivo $ARCHIVO_IMAGENES no existe."
fi
