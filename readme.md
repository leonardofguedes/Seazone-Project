# Khanto

A empresa Khanto começou a desenvolver um novo sistema e precisa criar um banco de dados com 3 entidades: Imóveis, Anúncios e Reservas. Um imóvel pode ter diversos anúncios, mas um anúncio é referente apenas a um imóvel. Um anúncio pode ter várias reservas, mas uma reserva se refere a apenas um anúncio.

A tabela de imóveis deve conter: o código do imóvel, o limite de hóspedes, a quantidade de banheiros, se aceita animais de estimação, o valor de limpeza, a data de ativação, a data e horário de criação e a data e horaŕio de atualização.

A tabela de anúncios deve conter: a qual imóvel o anúncio pertence, nome da plataforma em que o anúncio foi publicado (ex: AirBnb) , a taxa da plataforma, a data e horário de criação e a data e horário de atualização.

A tabela de reservas deve conter: o código da reserva (gerado aleatoriamente), a qual anúncio a reserva pertence, data de check-in, data de check-out, preço total, campo de comentário, número de hóspedes, data e horário de criação e data e horário de atualização.

Datas e horários de criação e de atualização devem ser inseridos automaticamente no sistema, e não manualmente.

## 🚀 Começando

Caso deseje realizar o download, digite no terminal:

```
git clone https://github.com/leonardofguedes/Seazone-Project.git
```

### 📋 Pré-requisitos

Não utilize o requirements.txt para definir dependências. Ele está cheio de bibliotecas que usei anteriormente em outros projetos.

Para inserir os dados fictícios, digite no terminal:

```
python manage.py loaddata khanto/fixtures/dados-khanto.json
```

## ⚙️ Pendências por falta de tempo útil

1. Integração com Banco de Dados SQL [NÃO-CUMPRIDO]
2. Aprimoramento de testes de Views, Serializers e Templates [NÃO-CUMPRIDO]
3. Personalização do front [NÃO-CUMPRIDO]
4. Finaliz da Classe SearchView [NÃO-CUMPRIDO]

## ✒️ Autores

- **Leonardo Forgiarini Guedes** - _Trabalho Inicial_

## 📄 Licença

Este projeto está sob a licença (sua licença) - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.
