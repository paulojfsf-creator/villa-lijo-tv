# Villa Lijó Suítes — Guia Digital TV

Ecrã panorâmico de boas-vindas inspirado na referência visual da Villa Lijó: paisagens rotativas do Gerês, relógio e meteorologia no topo, acesso rápido ao guia MEO e oito cartões fotográficos com navegação por comando.

## O que inclui

- Fundo rotativo com fotografias locais do Gerês e da Villa.
- Acessos rápidos a boas-vindas, Gerês, restaurantes, trilhos, MEO, contactos e Wi-Fi.
- Guia completo com pequeno-almoço (08:30–10:00), piscina, regras, meteorologia, eventos e contactos úteis.
- Wi-Fi: `Villalijosuites` · palavra-passe: `Lijo_2026`.
- GNR Gerês: **253 900 100**.
- Navegação por setas, OK e Voltar no comando da TV.

## Publicar no GitHub Pages

1. Extraia o ZIP completo.
2. Carregue `index.html`, as pastas `assets`, `data` e `scripts`, a pasta oculta `.github` e os ficheiros de instruções para a raiz do repositório `villa-lijo-tv`.
3. Faça commit das alterações e aguarde a publicação do GitHub Pages.
4. Em **Actions → Atualizar guia MEO**, escolha **Run workflow** para obter logo a programação. Depois, o GitHub atualiza-a diariamente.
5. Reabra a página nas TVs.

Mantenha a pasta `assets` ao lado do `index.html`. As imagens de fundo são locais para carregar de forma fiável no navegador da TV.

## Imagens e nota

As fotografias do Gerês são de José Amorim e Andre Rodrigues83, do Wikimedia Commons, com licença CC BY-SA 4.0. A atribuição completa está em `IMAGE-CREDITS.txt`. A imagem da Villa já fazia parte do repositório.

A meteorologia usa a observação da estação IPMA de Terras de Bouro/Barral e a previsão IPMA do dia. A programação MEO pode mostrar o programa atual e o seguinte no canal selecionado. A página não consegue detetar qual canal está sintonizado na box.


### Programação MEO

A aplicação lê o ficheiro `data/meo-guide.json` para apresentar os programas que estão a decorrer e os seguintes no canal escolhido. O workflow em `.github/workflows/update-meo-guide.yml` consulta diariamente o guia público MEO e grava a programação no repositório. Na primeira instalação, abra **Actions → Atualizar guia MEO → Run workflow** para carregar a programação imediatamente. O workflow pede permissão para gravar o ficheiro de programação. Também pode executar `scripts/update-meo-guide.py` num computador com Python para atualizar manualmente.
