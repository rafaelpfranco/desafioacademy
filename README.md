
# Desafio Academy: Escolha otimizada

Dado n grupos de alunos, m ciclos e a quantidade de alunos de cada grupo o algoritmo propõe entregar a escolha do próximo grupo de maneira otimizada.

## Como utilizar


- Clone o projeto

```bash
  git clone https://github.com/rafaelpfranco/desafioacademy.git
```
- Inicializa um novo projeto no site [replit](https://replit.com): 
```bash
  Importe o projeto clonado
```
```bash
  Confirme a linguagem Python
```
```bash
  Ao inicializar escolha a opção: Use run command
```
```bash
  Aperte run a primeira vez para importar todas as dependências
```
Ambiente pronto para execução!



## Como funciona

- Primeiro passo é transformar a entrada json em um grafo, onde os alunos são os nós e o peso dos vértices são a quantidade de vezes que o aluno A esteve em um grupo com o Aluno B. 
- Segundo passo é escolher o próximo ciclo então para isso é definido que o primeiro aluno sempre estará no primeiro grupo, para escolher o próximo aluno é checado o menor peso desse aluno com todos os outros e escolhemos o menor, caso tenha vários pesos iguais escolhemos o primeiro menor, para escolher o terceiro indivíduo verificamos o peso do primeiro aluno com todos os outros mais o peso do segundo alunos com todos os outros, o que significa que estamos escolhendo a melhor escolha pensando em quem já está no grupo e isso é feito até completarmos o grupo.


