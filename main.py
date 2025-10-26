# main.py
# Programa simple para probar la compilación automática en GitHub Actions

def saludar():
    print("👋 Hola desde el flujo de trabajo automatizado de GitHub Actions!")
    print("✅ Tu script de Python se ejecutó correctamente en la nube.")

def sumar(a, b):
    return a + b

if __name__ == "__main__":
    saludar()
    resultado = sumar(5, 7)
    print(f"El resultado de 5 + 7 es: {resultado}")
