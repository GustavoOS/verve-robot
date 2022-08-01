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


## Atenção

Todos os scripts descritos nessa documentação presumem que serão executados na mesma pasta que está essa documentação. Recomenda-se abrir este projeto no [Visual Studio Code](https://code.visualstudio.com/) e abrir o terminal integrado antes de se executar os comandos.

Todos os comandos foram testados no Linux, no Ubuntu.

## Instalação

### Robô

Antes de tudo, é preciso que o Python 3 esteja instalado. Siga esse [tutorial de instalação](https://tutorial.djangogirls.org/pt/python_installation/) caso não tenha instalado.


Usuários mais avançados de Python podem, opcionalmente, utilizar um [ambiente virtual](https://docs.python.org/pt-br/3/tutorial/venv.html).


Instale as dependências do projeto, com o seguinte comando no terminal
```console
pip3 install -r requirements.txt
```

Como o projeto utiliza o [pyperclip](https://pypi.org/project/pyperclip/) para copiar (equivalente ao famoso Ctrl + C), se atente à seguintes restrições:

#### Linux

Faz uso do xclip ou xsel. Garanta a instalação de um deles rodando no terminal (no caso do Ubuntu/Debian)
```console
sudo apt install xclip
```
ou
 ```console
sudo apt install xsel
```
#### Mac

 Faz uso dos comandos pbcopy e pbpaste, que devem vir instalados no navegador
#### Windows

Não é necessário nenhum módulo adicional

### Pandoc

Utilizado para converter o artigo do formato do Word para HTML.

Baixe o [instalador](https://github.com/jgm/pandoc/releases/tag/2.18) para o seu sistema operacional e o execute para instalar.

#### Convertendo um único arquivo
Imagine que o arquivo de entrada se chame euclides.docx e esteja dentro da pasta input. Para converter o documento e adicioná-lo na pasta converted (que precisa existir previamente), execute o seguinte comando:

```sh
pandoc -f docx  input/euclides.docx -t html -o converted/euclides.html
```

#### Convertendo vários arquivos de uma vez

Para processar um lote de arquivos que estão dentro da pasta input para colocá-los dentro da pasta converted (que não precisa estar previamente criada), execute o script bash abaixo. Para rodar script bash no Windows, execute em um terminal que interprete bash, como o git Bash (veja [Como instalar Git Bash no Windows](https://www.webdevdrops.com/git-bash-como-instalar-usar/) )

```sh
mkdir -p converted
for file in input/*; do
    name=$(echo "$file" | cut -f 1 -d '.')
    cat $file | pandoc -f docx -t html > $name.html
done
mv input/*.html converted/.
```

### Configurando ambiente

- É preciso ter o Chrome instalado na máquina

- Arquivo de ambiente

Para ser fácil alterar as senhas, caso necessário, isolamos as senhas em um arquivo que denominamos ".env" que deve ser colocado na mesma pasta que esta documentação. Deve ser preenchido desta maneira:

```sh
VERVE_LOGIN="insira o login aqui"
VERVE_PASSWORD="insira a senha aqui"
TEMPLATES="src/templates"
IMAGES="images"
```
As pastas templates e images são configuráveis, podendo ser configuradas nesse arquivo .env

- Criação da pasta de imagens

Crie a pasta de imagens, onde serão baixadas as imagens da thumbnail dos vídeos. O nome desta pasta deverá ser images, e deverá estar na mesma pasta que esta documentação. No terminal shell, essa criação pode ser feita através do seguinte comando

```sh
mkdir -p images
```

## Executando o script

Rode o seguinte comando:

```sh
python3 src/robot.py
```

ou

```sh
python src/robot.py
```
