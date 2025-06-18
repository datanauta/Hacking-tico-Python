import subprocess

perfil_red = input('Introduzca el nombre del perfil de red WiFi: ')

try:
    resultado = subprocess.check_output(
        f'netsh wlan show profile name="{perfil_red}" key=clear',
        shell=True, encoding='utf-8', errors='backslashreplace'
    )

    # Buscar la línea que contiene la clave
    for line in resultado.split('\n'):
        if 'Contenido de la clave' in line or 'Key Content' in line:
            password = line.split(':')[1].strip()
            print(f'La contraseña de la red "{perfil_red}" es: {password}')
            break
    else:
        print(f'No se pudo encontrar la contraseña de la red "{perfil_red}".')

except subprocess.CalledProcessError:
    print(f'No se pudo obtener la información del perfil "{perfil_red}".')
