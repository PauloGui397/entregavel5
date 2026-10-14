# Sprint 5 - Análise de Dados em Python

## Sobre o projeto

Este projeto foi desenvolvido para ler um arquivo CSV com informações de e-mail, CPF, telefone e data.

O programa verifica se os dados estão no formato correto e, no final, mostra quantos registros são válidos e inválidos.

## Validação dos dados

Para validar os dados, utilizei expressões regulares com o módulo `re`.

- **E-mail:** verifica se possui o formato de um endereço de e-mail.
- **CPF:** verifica se está no formato `000.000.000-00`.
- **Telefone:** verifica se segue o formato `(00) 00000-0000`.
- **Data:** verifica o formato `DD/MM/AAAA` e se a data existe.

A validação do CPF verifica apenas o formato, não os dígitos verificadores.

## Tratamento de erros

Utilizei `try`, `except`, `else` e `finally` para tratar possíveis erros durante a execução.

- `FileNotFoundError`: quando o arquivo CSV não é encontrado.
- `ValueError`: quando ocorre um erro relacionado a valores inválidos.
- `KeyError`: quando falta alguma coluna necessária no CSV.
- `FormatoInvalidoError`: exceção personalizada para identificar campos com formato inválido.

## Exemplo de entrada

Arquivo `dados.csv`:

```csv
email,cpf,telefone,data
ana@email.com,123.456.789-09,(11) 98765-4321,15/03/2025
bruno@email.com,987.654.321-00,(21) 91234-5678,20/04/2025
email_invalido,12345678900,11987654321,35/13/2025
carla@email.com,111.222.333-44,(31) 99876-5432,10/05/2025
```

## Exemplo de saída

```text
Total de registros: 4
Registros válidos: 3
Registros inválidos: 1

REGISTROS INVÁLIDOS
Linha 4: E-mail inválido
```

O relatório completo também mostra os dados válidos e é salvo no arquivo `relatorio.txt`.

## Como executar

Com os arquivos na mesma pasta, execute no terminal:

```bash
python entregavel5.py
```

## Arquivos

- `entregavel5.py` - programa principal
- `dados.csv` - arquivo de entrada
- `relatorio.txt` - relatório gerado
- `README.md` - descrição do projeto