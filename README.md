# _BowlingScoreKeeper_
Repositório base para experimento de TCC II relacionado a TDD.

## Instruções

O objetivo é desenvolver uma aplicação que consegue calcular o placar de um jogo de boliche completo (de apenas um jogador). Não há uma interface gráfica. Você pode trabalhar apenas com classes/objetos e com testes unitários utilizando o pacote `unittesting` (pacote da biblioteca padrão Python). Você não precisa criar um método `main`.

Os requisitos da aplicação são divididos em um conjunto de histórias de usuários que irão servir como sua lista de tarefas a serem feitas. Você deve desenvolver uma solução completa de maneira incremental sem uma compreensão inicial completa das regras gerais do jogo. Não leia as tarefas posteriores a que você está fazendo no momento e lide com os requisitos um de cada vez na ordem dada. Resolva o problema começando com a primeira história de usuário. Lembre-se de sempre começar com um caso de teste, seguindo o exemplo apresentado. Apenas quando uma história está completa, você deve passar para a próxima. Uma história está completa quando você está seguro de que seu programa implementa todas as funcionalidades estipuladas pelos requisitos da história de usuário. Isso implica que todos os casos de teste para aquela história e todos os casos de teste para as história anteriores estejam passando. Talvez você precisa alterar sua solução aos poucos conforme você avança para requisitos mais complexos.

## Histórias de Usuário

1. **Frame**
Cada turno de um jogo de boliche é chamado **frame** (quadro em português). 10 pinos são levantados em cada quadro/frame. O objetivo do jogador é derrubar o máximo de pinos possíveis em cada quadro/frame. O jogador tem duas chances para fazer isso, ou dois **throws** (jogadas em inglês). O valor de um jogada/throw é dado pelo número de pinos derrubados em cada jogada/throw.
  - **Requisito**: Definir um quadro/frame como uma composição de duas jogadas/throws. A primeira e segunda jogada/throw devem ser distinguíveis.
  - **Exemplo**: [2,4] é um quadro/frame de duas jogadas/throws, em que dois pinos foram derrubados na primeira jogada/throw e quatro pinos foram derrubados na segunda.
  
2. **Frame score**
O **score** (placar em português) é a soma todas as jogadas/throws.
  - **Requisitos**: Computar o placar/score de uma jogada/throw qualquer.
  - **Exemplo**: O placar/score de uma jogada/throw [2,6] é 8. O placar/score de uma jogada/throw [0,9] é 9.
  
3. **Game**
Um **game** (jogo em português) simples consiste em 10 quadros/frames.
  - **Requisito**: Definir um jogo/game, que consistem em 10 quadros/frames.
  - **Exemplo**: A sequência de quadros/frames [1,5] [3,6] [7,2] [3,6] [4,4] [5,3] [3,3] [4,5] [8,1] [2,6] representa um jogo/game. Você deve reutilizar esse jogo/game a partir de agora para representar diferentes cenários, modificando apenas alguns quadros/frames de cada vez.
  
4. **Game Score**
O placar/score de um jogo/game de boliche é a soma dos placares/scores de cada um dos seus quadros/frames.
  - **Requisito**: Computar o placar/score de um jogo/game.
  - **Exemplo**: O placar/score do jogo/game [1,5] [3,6] [7,2] [3,6] [4,4] [5,3] [3,3] [4,5] [8,1] [2,6] é 81.
  
5. **Strike**
Um quadro/frame é chamado de **strike** se todos os 10 pinos forem derrubados na primeira jogada/throw. Nesse caso, não há uma segunda jogada/throw. Um strike pode ser descrito como [10,0]. O placar/score de um strike é igual a 10 mais a soma das próximas duas jogadas/throws do(s) quadro(s)/frame(s) subsequentes.
  - **Requisito**: Reconhecer um quadro/frame como strike. Computar o placar/score de um strike. Computar o placar/score de um jogo/game contendo um strike.
  - **Exemplo**: Suponha-se que [10,0] e [3,6] são quadros/frames consecutivos. Então o primeiro quadro/frame é um strike e seu placar/score é igual a 10+3+6=19. O jogo/game [10,0] [3,6] [7,2] [3,6] [4,4] [5,3] [3,3] [4,5] [8,1] [2,6] tem o placar/score de 94.
  
6. **Spare**
Um quadro/frame é chamado de **spare** se todos os 10 pinos forem derrubados em duas jogadas/throws. O placar/score de um spare é 10 mais o valor da primeira jogada/throw do quadro/frame seguinte.
  - **Requisito**: Reconhecer um quadro/frame como spare. Computar o placar/score de um spare. Computar o placar/score de um jogo/game contendo um spare.
  - **Exemplo**: [1,9], [4,6], [7,3] são todos spare. Se você tem os quadros/frames [1,9] e [3,6] em seguida, o placar/score do spare (primeiro quadro/frame) é 10+3=13. O jogo/game [1,9] [3,6] [7,2] [3,6] [4,4] [5,3] [3,3] [4,5] [8,1] [2,6] tem o placar/score de 88.
  
7. **Strike and Spare**
Um strike pode ser seguido de um spare. O placar/score do strike não é afetado quando isso acontece.
  - **Requisito**: Computar o placar/score de um strike quando for seguido de um spare. Computar o placar/score de um jogo/game com um strike seguido de um spair.
  - **Exemplo**: Na sequência [10,0] [4,6] [7,2], um strike é seguido de um spare. Nesse caso, o placar/score do strike é de 10+4+6=20, e o placar/score do spare é de 4+6+7=17. O jogo/game [10,0] [4,6] [7,2] [3,6] [4,4] [5,3] [3,3] [4,5] [8,1] [2,6] tem o placar/score de 103.
  
8. **Multiple Strikes**
É possível fazer dois strikes em seguida. Se isso acontecer, para ser computado o placar/score do primeiro strike, deve-se contar com o valor de jogadas/throws de dois quadros/frames em sequência.
  - **Requisito**: Computar o placar/score de um strike que é seguido de um outro strike. Computar o placar/score de um jogo/game com dois strikes em sequência.
  - **Exemplo**: Na sequência [10,0] [10,0] [7,2], o placar/score do primeiro strike é de 10+10+7=27. O placar do segundo strike é de 10+7+2=19. O jogo/game [10,0] [10,0] [7,2] [3,6] [4,4] [5,3] [3,3] [4,5] [8,1] [2,6] tem o placar/score de 112.

9. **Multiple Spares**
É possível fazer dois spares em seguida. O placar/score do primeiro spare não é afetado quando isso acontece.
  - **Requisito**: Computar o placar/score de um jogo/game com dois spares em sequência.
  - **Exemplo**: O jogo/game [8,2] [5,5] [7,2] [3,6] [4,4] [5,3] [3,3] [4,5] [8,1] [2,6] tem o placar/score de 98.

10. **Spare as the Last Frame**
Quando o último quadro/frame de um jogo/game é um spare, o jogador recebe uma jogada/throw de bônus. Contudo, essa jogada/throw bônus não pertence a um quadro/frame padrão. Ela é utilizado apenas para calcular o placar/score do último spare.
  - **Requisito**: Computar o placar/score de um spare quando ele é o último quadro/frame do jogo/game. Computar o placar/score de um jogo/game quando seu último quadro/frame é um spare.
  - **Exemplo**: O último quadro/frame do jogo/game [1,5] [3,6] [7,2] [3,6] [4,4] [5,3] [3,3] [4,5] [8,1] [2,8] é um spare. Se a jogada/throw bônus for [7], o último quadro/frame tem o placar/score de 2+8+7=17. O jogo/game tem o placar/score de 90.
  
11. **Strike as the Last Frame**
Quando último quadro/frame de um jogo/game é um strike, o jogador recebe duas jogadas/throws de bônus. Contudo, essa jogada/throw bônus não pertence a um quadro/frame padrão. Elas são apenas usadas para se calcular o placar/score do último quadro/frame.
  - **Requisito**: Computar o placar/score de um strike quando ele é o último quadro/frame do jogo/game. Computar o placar/score de um jogo/game quando seu último quadro/frame é um strike.
  - **Exemplo**: O último quadro/frame do jogo/game [1,5] [3,6] [7,2] [3,6] [4,4] [5,3] [3,3] [4,5] [8,1] [10,0] é um strike. Se as jogadas/throws bônus forem [7,2] o placar/score do último quadro/frame é 10+7+2=19. O placar/score do jogo/game é 92.

12. **Bonus is a Strike**
Se o último quadro/frame de um jogo/game for um spare e a jogada/throw bônus for um strike, o jogador não recebe jogadas/throws bônus a mais.
  - **Requisito**: Computar o placar/score de um jogo/game em que o último quadro/frame é um spare e a jogada/throw bônus é um strike.
  - **Exemplo**: No jogo/game [1,5] [3,6] [7,2] [3,6] [4,4] [5,3] [3,3] [4,5] [8,1] [2,8], o último quadro/frame é um spare. Se a jogada/throw bônus for [10], o placar/score do jogo/game é 93.
  
13. **Best Score**
Um jogo/game perfeito consiste de 12 strikes em seguida (incluindo as duas jogadas/throws bônus) e tem um placar/score de 300.
  - **Requisito**: Checar se o placar/score de um jogo/game perfeito é 300.
  - **Exemplo**: Um jogo/game perfeito consiste em [10,0] [10,0] [10,0] [10,0] [10,0] [10,0] [10,0] [10,0] [10,0] [10,0], com as jogadas/throws bônus de [10,10]. Seu placar/score é 300.

14. **Real Game**
  - **Requisito**: Checar se o placar/score de um jogo/game [6,3] [7,1] [8,2] [7,2] [10,0] [6,2] [7,3] [10,0] [8,0] [7,3] [10] é 135.

Fim :D
