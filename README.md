# Robô Verve

O robô serve para automatizar o processo de submissão de um artigo para a plataforma Wordpress. Utiliza Python, Selenium, Beautiful Soup, entre outras tecnologias.

## Como funciona?
1. O robô verifica a pasta converted
1. O robô lê um arquivo em HTML e extrai de lá informações, como o título do artigo, os parágrafos e referências.
1. O sistema abre o navegador e busca o vídeo do verve no [Youtube](https://www.youtube.com) relacionado ao título, extraindo dele o link, o título e a imagem de capa. A imagem é salva para a pasta images.
1. O sistema acesa o [Wikimedia Commons](https://commons.wikimedia.org/wiki/Main_Page?uselang=pt-br) no navegador, busca pelo título do artigo. Caso apareça a opção "você quis dizer?", o sistema aceita a sugestão. Então, são extraídos os links das primeiras fotos da busca.
1. O sistema faz requisições **sem** a utilização do navegador para buscar no site [Pensador](https://www.pensador.com/) a frase mais compartilhada do autor (título do artigo). Caso haja frases cadastradas, o sistema adiciona o site como referência.
1. O artigo é montado como um arquivo HTML que obedece a um template padronizado utilizando as informações extraídas.
1. O sistema utiliza o navegador para entrar na plataforma do blog, faz o login, verifica a página de postagens e duplica a segunda postagem listada e faz algumas edições rápidas
1. O sistema abre a edição do post no navegador, muda o modo de edição para o modo código, copia e cola o artigo montado, e salva pela primeira vez o rascunho. Então submete a foto do Youtube como foto de miniatura, cria um SEO, uma metadescrição e salva novamente o rascunho.
1. O sistema processa o próximo arquivo
