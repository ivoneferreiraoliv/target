def inverter_string(s):
    inverted_string = ""
    for i in range(len(s) - 1, -1, -1):
        inverted_string += s[i]
    return inverted_string

# Exemplo de uso
string_original = input("Digite uma string: ")
string_invertida = inverter_string(string_original)
print("String invertida:", string_invertida)
