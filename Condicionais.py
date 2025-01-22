{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/DanielEloy/AiGeminiViaPY/blob/main/Condicionais.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dsu3uJksx-M7"
      },
      "source": [
        "![dnc.png](data:image/png;base64,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)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Mn_vGqswyBr0"
      },
      "source": [
        "<br>Consultor: Everton Menezes </br>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xGapo2vByPhu"
      },
      "source": [
        "# Condicionais\n",
        "\n",
        "Os condicionais são utilizados para fazer comparações (condições) e caso elas sejam verdadeiras o nosso programa faz determinadas ações, e caso elas sejam falsas, nosso programa faz outras ações."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "e8uNOgEFyfu7"
      },
      "source": [
        "## Comparadores"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9MP8VLmcymuB"
      },
      "source": [
        "<b> Os principais comparadores utilizadas são:</b><br>\n",
        "\n",
        "> a `==` b : Verifica se ***a*** é igual a ***b***\n",
        "\n",
        "> a `!=` b : Verifica se ***a*** é diferente de ***b***\n",
        "\n",
        "> a `> ` b : Verifica se ***a*** é maior que ***b***\n",
        "\n",
        "> a `>=` b : Verifica se ***a*** é maior ou igual a ***b***\n",
        "\n",
        "> a `< ` b : Verifica se ***a*** é menor que ***b***\n",
        "\n",
        "> a `<=` b : Verifica se ***a*** é menor ou igual a ***b***\n",
        "\n",
        "A resposta da comparação sempre será um Booleano: `True` | `False`"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cP0BbpnO1PnC"
      },
      "source": [
        "# Declarando variáveis:\n",
        "a = 7\n",
        "b = 2"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qG0X0cUX1Ua4",
        "outputId": "39925d94-89ff-4f78-b5c7-df9761745b07"
      },
      "source": [
        " a == b\n"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {},
          "execution_count": 2
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uc7Okunc1cvX",
        "outputId": "ae8304fa-a120-46cc-b08e-9e716b013c46"
      },
      "source": [
        " a != b\n"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ykURydWb1clh",
        "outputId": "5867e1da-7d2a-4978-cc08-4150f231f34b"
      },
      "source": [
        " a > b\n"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EeqjPtWY1cau",
        "outputId": "73466c0a-2710-41a0-e6e9-92b8e08798ab"
      },
      "source": [
        " a >= b\n"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5BwSEfyO1cLg",
        "outputId": "72d66dcf-b1b1-4695-f664-d684bcdf338d"
      },
      "source": [
        " a < b\n"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mG4cGgNs1b3K",
        "outputId": "57d64d69-cc10-4fe9-9b20-ae18fcefa3c6"
      },
      "source": [
        " a <= b\n"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DzLvGpYc1w-J"
      },
      "source": [
        "<h1> Exercícios de Comparadores </h1>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WDXElJix2Tk6"
      },
      "source": [
        "1. Faça um programa que pede pra um usuário digitar 2 números e compare se eles são iguais."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2L_HxQOJ2S8F",
        "outputId": "955b1971-24f4-46b3-9f0e-e285d3f828e4"
      },
      "source": [
        "# Pedindo inputs\n",
        "c = float(input('Digite um numero: \\n'))\n",
        "d = float(input('Digite um numero: \\n'))\n",
        "\n",
        "comparacao = ( c == d)\n",
        "# Imprimindo comparação\n",
        "print('O primeiro numero é igual a o segundo ?\\nResposta: {}'.format(comparacao))"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um numero: \n",
            "7\n",
            "Digite um numero: \n",
            "3\n",
            "O primeiro numero é igual a o segundo ?\n",
            "Resposta: False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xbsjrO1u3HjN"
      },
      "source": [
        "2. Agora compare se a variável 1 digitada é maior ou igual a variável 2"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pSMXsPdk3HHQ",
        "outputId": "37b72ae7-3c22-436a-dc32-8b271bf815f2"
      },
      "source": [
        "comparacao = ( c >= d)\n",
        "# Imprimindo comparação\n",
        "print('O primeiro numero é maior ou igual a o segundo ?\\nResposta: {}'.format(comparacao))"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "O primeiro numero é maior ou igual a o segundo ?\n",
            "Resposta: True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DI8FF9DM3n-7"
      },
      "source": [
        "3. Dado o preço do lanche = 10.90 e da batata de 5.40. Calcule quanto vai sair a conta do usuário. O usuário deve inserir a quantidade de lanches que ele quer e a quantidade de batatas.\n",
        "Finalmente peça para o usuário falar quanto dinheiro ele tem na carteira e verifique se ele vai consegui pagar a conta."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YBVTudk_3nRk",
        "outputId": "ec8a0127-ce05-439e-91e5-792b20ec8edc"
      },
      "source": [
        "# Declarando variáveis\n",
        "lanchePreco = 10.90\n",
        "batataPreco = 5.40\n",
        "lancheQtd = float(input('Digite a quantidade de lanches ? \\n'))\n",
        "batataQtd = float(input('Digite a quantidade de batata ? \\n'))\n",
        "dinheiroTotal = float(input('Digite quanto dinheiro recebido ? \\n'))\n",
        "\n",
        "# Calculando custo total\n",
        "custoTotal = (lanchePreco * lancheQtd) + (batataPreco * batataQtd)\n",
        "comparacao = (dinheiroTotal >= custoTotal)\n",
        "\n",
        "# Imprimindo resposta\n",
        "print('A sua compra total ficou em R${:.2f}'.format(custoTotal))\n",
        "print('Você tem dinheiro suficiente para pagar ?\\nResposta: {}'.format(comparacao))"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a quantidade de lanches ? \n",
            "2\n",
            "Digite a quantidade de batata ? \n",
            "2\n",
            "Digite quanto dinheiro recebido ? \n",
            "50\n",
            "A sua compra total ficou em R$32.60\n",
            "Você tem dinheiro suficiente para pagar ?\n",
            "Resposta: True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ah4rntx_4-HA"
      },
      "source": [
        "## Condicionais simples if-else\n",
        "\n",
        "As condicionais simples possuem somente 2 caminhos para se seguir: o caminho verdadeiro e o falso. Após fazer a condição pelo if o programa vai seguir caminhos diferentes."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gKqBhf-85ktK"
      },
      "source": [
        "<h1> Estrutura do if-else </h1>\n",
        "\n",
        "```\n",
        "if condicao:\n",
        "  Bloco verdadeiro\n",
        "else:\n",
        "  Bloco falso\n",
        "```\n",
        "\n",
        "<h3> Pontos de atenção: </h3>\n",
        "\n",
        "*   Não esqueça dos `:`\n",
        "*   Não esqueça da `indentação`"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DXfNHBVnDYG9",
        "outputId": "025d90c6-ecab-43d5-d91e-2fcaed1f549e"
      },
      "source": [
        "# Exemplo True - False\n",
        "if True:\n",
        "  print('Verdadeiro')\n",
        "else:\n",
        "  print('Falso')\n",
        "\n",
        "print('Acabou')"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Verdadeiro\n",
            "Acabou\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0di5lY497D3F"
      },
      "source": [
        "<h3> Exemplo 1 </h3>\n",
        "Dado as variáveis:\n",
        "\n",
        "a = 2\n",
        "\n",
        "b = 3\n",
        "\n",
        "Compare se a == b e imprima uma mensagem de resultado."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Eo7GuxBQ7DMj"
      },
      "source": [
        "# Declarando as variáveis\n",
        "a = 2\n",
        "b = 3"
      ],
      "execution_count": 23,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QoytUlJk8BaL",
        "outputId": "7d914f87-2726-4e1c-9e77-25da610e73d7"
      },
      "source": [
        "# Desenhado o if\n",
        "if a==b:\n",
        "  print('A variavel a, que vale {} é igual a variavel b'.format(a))\n",
        "else:\n",
        "  print('A variavel a, que vale {} é diferente da variavel b, que vale {}'.format(a,b))\n",
        "\n",
        "print('Acabou')"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A variavel a, que vale 2 é diferente da variavel b, que vale 3\n",
            "Acabou\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "CaFq9p1x8DeC"
      },
      "source": [
        "Agora... mude a variável:\n",
        "\n",
        "b = 2\n",
        "\n",
        "e execute o mesmo código anterior"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YsBRHyMF8Lqx"
      },
      "source": [
        "# Redefinindo b\n",
        "b = 2"
      ],
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XPdDrqoV8ZbC"
      },
      "source": [
        "<h3> Exemplo 2 </h3>\n",
        "\n",
        "1. Faça um programa que pede pra um usuário digitar 2 números e:\n",
        "\n",
        "*   Se num1 >= num2 então multiplique o num2 por 5\n",
        "*   Caso contrário, multiplique o num1 por 5"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DIhYhyO19Xdy",
        "outputId": "1c4b15b1-ac23-4c57-c1da-5c86ddddead5"
      },
      "source": [
        "# Pedindo inputs\n",
        "num1 = float(input('Digite um numero: \\n'))\n",
        "num2 = float(input('Digite um numero: \\n'))\n",
        "\n",
        "# Fazendo o if\n",
        "if num1 >= num2:\n",
        "  print('\\nO primeiro numero é maior ou igual ao segundo numero,\\nEntão irei multiplicar por cinco\\nR: {}:'.format(num2*5))\n",
        "else:\n",
        "  print('\\nO segundo numero é maior que o primeiro numero,\\nEntão irei multiplicar por cinco\\nR: {}'.format(num1*5))"
      ],
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um numero: \n",
            "2\n",
            "Digite um numero: \n",
            "5\n",
            "\n",
            "O segundo numero é maior que o primeiro numero,\n",
            "Então irei multiplicar por cinco\n",
            "R: 10.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "53hsil9C-ubq"
      },
      "source": [
        "## Condicionais aninhados if-elif-else\n",
        "\n",
        "Esses condicionais são utilizados quando não temos somente 2 casos (True e False), mas sim quando temos vários casos"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fzn37wwE-9pV"
      },
      "source": [
        "<h1> Estrutura do if-elif-else </h1>\n",
        "\n",
        "```\n",
        "if condicao1:\n",
        "  Bloco condicao1 verdadeiro\n",
        "elif condicao2:\n",
        "  Bloco condicao2 verdadeiro\n",
        "  .\n",
        "  .\n",
        "  .\n",
        "else:\n",
        "  Bloco falso\n",
        "```"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "mkkDTQw8_Ttd"
      },
      "source": [
        "<h2> Exemplo </h2>\n",
        "Dado as variáveis:\n",
        "\n",
        "a = 2\n",
        "\n",
        "b = 3\n",
        "\n",
        "Compare e mostra para o usuário se uma é igual a outra, ou se uma é maior que outra, e neste caso, qual é a maior."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IeYvZN8C-8lA",
        "outputId": "7a2dca55-18d8-4566-b833-1ba4aaa9201d"
      },
      "source": [
        "# Declarando as variáveis\n",
        "\n",
        "# Montando o if-elif-else\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "*a* é igual a *b*\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5WAZpJMH_-kA"
      },
      "source": [
        "<h2> Exemplo 2 </h2>\n",
        "\n",
        "Agora faça um programa no qual o usuário vai digitar os 2 números e você fará essas comparações.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "keKfaHQ4AKbX",
        "outputId": "6457d5e0-0ab2-4842-c7cd-129c2e67a396"
      },
      "source": [
        "# Declarando as variáveis\n",
        "\n",
        "\n",
        "# Montando o if-elif-else\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o número a: 2\n",
            "Digite o número b: 3\n",
            "a é menor que b\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QdSZJR_xApNo"
      },
      "source": [
        "<h2> Exemplo 3 </h2>\n",
        "\n",
        "Faça um programa que o usuário vai digitar a vontade do que ele está de comer alguma coisa.\n",
        "\n",
        "Caso este input seja:\n",
        "\n",
        "* Lanche : então imprima : \"Vá ao Méqui\"\n",
        "\n",
        "* Pizza : então imprima : \"Vá ao Hut\"\n",
        "\n",
        "* Mexicano : então imprima : \"Vá ao Bell\"\n",
        "\n",
        "* Caso contrário : então imprima: \"Tente novamente\""
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5OWad-opOwpv",
        "outputId": "5aaddf74-5aee-442c-9656-c311b867143b"
      },
      "source": [],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Vontade = lanche\n",
            "Tente novamente\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XezVkckndHnk"
      },
      "source": [
        "## Operadores Lógicos\n",
        "\n",
        "Os operadores lógicos são usadas quando precisamos de múltiplas condições em 1 só if"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "t4oWC7VVdRJS"
      },
      "source": [
        "**negrito**> `and` : ambas as condições precisam ser satisfeitas simultaneamente\n",
        "\n",
        "> `or` : pelo menos 1 condição precisa ser satisfeita\n",
        "\n",
        "```\n",
        "True and True : True\n",
        "True and False : False\n",
        "True or False : True\n",
        "False or True : True\n",
        "False or False : False\n",
        "```\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IC46_mpQdUVn"
      },
      "source": [
        "<h2> Exemplo 1 </h2>\n",
        "\n",
        "Se eu tiver mais que 20 reais e preço do lanche for menor que 10 reais, então eu compro o lanche:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Zxpqgg6EdOvB"
      },
      "source": [],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IxMylkajdYS0"
      },
      "source": [
        "<h2> Exemplo 2 </h2>\n",
        "\n",
        "Se você tiver média nas notas > 7 ou nota na prova final > 7 você está aprovado."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "19bwS1gQdZyR"
      },
      "source": [],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Z2n03UzbdcoG"
      },
      "source": [
        "# Verificando Variáveis\n",
        "\n",
        "Esta funcionalidade é muito usada para testar e saber se podemos converter as variáveis dadas pelo usuário."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "r25150ecdfBN"
      },
      "source": [
        "> `.isnumeric( )` : #o input é numérico\n",
        "\n",
        "> `.isalpha( )` : #o input é texto\n",
        "\n",
        "> `.isalnum( )` : #o input é texto + num"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NMkrrJUtdhBM"
      },
      "source": [
        "<h2> Exemplo </h2>\n",
        "\n",
        "Peça para o usuário digitar alguma coisa e verifique o que é:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gNz1JXhwdi-8"
      },
      "source": [],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KOZpI7mldj_Z"
      },
      "source": [
        "# Exercícios"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HZZy1W73doX-"
      },
      "source": [
        "<h2> Exercício 1: </h2>\n",
        "\n",
        "Faça um programa que verifique se o usuário digitou um valor numérico ou não.\n",
        "\n",
        "* Caso Verdadeiro, imprima: 'Esse input é um número'\n",
        "\n",
        "* Caso Falso, imprima: 'Esse input não é um número, tente novamente'\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yel1IF1ydpzs"
      },
      "source": [],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "O-bH-WFKdrK9"
      },
      "source": [
        "<h2> Exercício 2: </h2>\n",
        "\n",
        "Peça para o usuário digitar um número e verifique se ele é par e imprima para o usuário essa informação.\n",
        "\n",
        "Dica.: números pares, quando são divididos por 2 possuem resto = 0"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5hllpCqKds-_"
      },
      "source": [],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "c9klAnx-dtQa"
      },
      "source": [
        "<h2> Exercício 3: </h2>\n",
        "\n",
        "Faça um programa no qual o usuário insira 2 inteiros. Verifique se o número 1 é divisível pelo número 2. Imprima essa informação para o usuário."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gIB2qixZdt9H"
      },
      "source": [],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1aLL6abedwwK"
      },
      "source": [
        "<h2> Desafio - calculadora: </h2>\n",
        "\n",
        "Faça um programa no qual o usuário vai digitar 2 números e também o tipo de operação que ele gostaria que fosse feita:\n",
        "\n",
        "* Soma\n",
        "* Subtração\n",
        "* Divisão\n",
        "* Multiplicação\n",
        "* Potência\n",
        "\n",
        "Imprima o resultado para o usuário da operação:\n",
        "\n",
        "Num1  `Operação`  Num2\n",
        "\n",
        "Caso o usuário não digite uma operação válida, dê uma mensagem de erro!"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VNXoWYDKdym5"
      },
      "source": [],
      "execution_count": null,
      "outputs": []
    }
  ]
}