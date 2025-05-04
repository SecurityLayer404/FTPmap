# ftpmap.py

**ftpmap.py** es un script en Python que se conecta a un servidor FTP (por defecto con acceso anónimo), enumera recursivamente directorios y archivos, y verifica permisos de lectura y escritura. Es útil para detectar configuraciones inseguras en servidores FTP.

## 🧰 Requisitos

- Python 3.x
- Acceso a un servidor FTP (puede ser anónimo o con usuario/contraseña)

## 📦 Instalación

No requiere instalación adicional. Asegurate de tener Python 3.

```bash
python3 --version
```

## 🚀 Uso

```bash
python3 ftpmap.py <host> [user] [password]
```

- `<host>`: Dirección IP o hostname del servidor FTP.
- `[user]` (opcional): Usuario FTP. Por defecto: `anonymous`
- `[password]` (opcional): Contraseña FTP. Por defecto: `anonymous@`

### Ejemplo

```bash
python3 ftpmap.py 192.168.1.100
```

## 🔍 Salida esperada

Muestra las rutas FTP accesibles y si son legibles o escribibles.

```
Path                                                     Read       Write      Comment
------------------------------------------------------------ ---------- ---------- --------------------
/uploads/                                                 YES        YES        FTP directory
/uploads/file.txt                                         YES        -          FTP file
```

## ⚠️ Advertencia

Este script debe usarse solo en sistemas que tengas permiso de auditar.
