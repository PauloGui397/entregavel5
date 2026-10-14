import csv
import re
from datetime import datetime


class FormatoInvalidoError(Exception):
    pass


def validar_email(email):
    return bool(re.fullmatch(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", email))


def validar_cpf(cpf):
    return bool(re.fullmatch(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf))


def validar_telefone(telefone):
    return bool(re.fullmatch(r"\(\d{2}\)\s\d{5}-\d{4}", telefone))


def validar_data(data):
    if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", data):
        return False

    try:
        datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        return False

    return True


def validar_registro(registro):
    if not validar_email(registro["email"]):
        raise FormatoInvalidoError("E-mail inválido")

    if not validar_cpf(registro["cpf"]):
        raise FormatoInvalidoError("CPF inválido")

    if not validar_telefone(registro["telefone"]):
        raise FormatoInvalidoError("Telefone inválido")

    if not validar_data(registro["data"]):
        raise FormatoInvalidoError("Data inválida")


registros_validos = []
registros_invalidos = []

try:
    with open("dados.csv", "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)

        for numero_linha, registro in enumerate(leitor, start=2):
            try:
                validar_registro(registro)
            except (FormatoInvalidoError, ValueError, KeyError) as erro:
                registros_invalidos.append((numero_linha, registro, str(erro)))
            else:
                registros_validos.append(registro)

except FileNotFoundError:
    print("Erro: arquivo dados.csv não encontrado.")
except (ValueError, KeyError) as erro:
    print(f"Erro ao ler o arquivo: {erro}")
else:
    total_registros = len(registros_validos) + len(registros_invalidos)

    relatorio = [
        "=============================================",
        "          RELATÓRIO DE ANÁLISE DE DADOS",
        "=============================================",
        f"Total de registros: {total_registros}",
        f"Registros válidos: {len(registros_validos)}",
        f"Registros inválidos: {len(registros_invalidos)}",
        "",
        "REGISTROS VÁLIDOS",
    ]

    for registro in registros_validos:
        relatorio.append(
            f"E-mail: {registro['email']} | CPF: {registro['cpf']} | "
            f"Telefone: {registro['telefone']} | Data: {registro['data']}"
        )

    relatorio.append("")
    relatorio.append("REGISTROS INVÁLIDOS")

    for numero_linha, registro, motivo in registros_invalidos:
        relatorio.append(f"Linha {numero_linha}: {motivo}")

    relatorio.append("=============================================")

    with open("relatorio.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("\n".join(relatorio))

    print("\n".join(relatorio))

finally:
    print("\nAnálise finalizada.")