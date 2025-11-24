## Tutorial de utilização do Pyenv para reprodução dos resultados do artigo

1. Instalando as dependências do pyenv:

Importante executar, caso não tenha sido feito isso alguma vez no passado:
```
sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm gettext libncurses5-dev tk-dev tcl-dev blt-dev libgdbm-dev git python-dev python3-dev aria2 vim libnss3-tools python3-venv liblzma-dev libpq-dev 
```
2. Instalando o pyenv
```
curl -fsSL https://pyenv.run | bash
```

3. Escreva o texto abaixo **ao final do arquivo encontrado em** ~/.bashrc para definir como variáveis de ambiente globais:

OBS: "~/" é o caminho para /home/**seuUsuario**/

```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Colar o comando abaixo no terminal:
```
exec $SHELL
```


## Utilizando o pyenv:
- No terminal, execute os comandos abaixo: 
1.
    ```
    pyenv install 3.7.7 
    ```
    Instala o Python 3.7.7 no diretório do pyenv, feito um módulo.

2. 
    ```
    pyenv versions 
    ```
    Verifica se a versão em questão foi instalada
3. 
    ```
    pyenv virtualenv 3.7.7 nome_da_pasta
    ```
    Cria ambiente virtual com python 3.7.7 e com nome **nome_da_pasta** 
    
    Pode ser qualquer nome. Vamos considerar que o nome seja **rePOenv**
4. 
    ```
    pyenv local rePOenv 
    ```
    Coloca o ambiente local como ambiente virtual rePOenv
5. 
    ```
    python -V
    ```
    Verifica a versão atual do python nesse ambiente
6. 
    ```
    pip -V
    ```
    Verifica se o pip está num virtual enviroment
6. 
    ```
    pyenv local 3.7.7
    ```
    Configura o repositório local com o Python 3.7.7
    
7. 
    ```
    python --version 
    ```
    Verifica se a versão no repositório local é de fato a configurada antes

**Agora é possível instalar os pacotes neste ambiente!!!**
## Instalação dos pacotes necessários
- Atualiza o pip    
```
pip install --upgrade pip 
```

- Instala todas as dependências na versão correta do artigo.
```
    pip install tensorflow==2.1.0
    pip install pandas==1.0.3
    pip install numpy==1.18.1
    pip install --upgrade protobuf==3.20.3
```    

- Verifica todos os pacotes e versões instaladas
```
pip list 
```
Caso queira mais detalhes de um pacote..
    
    pip show [nome do pacote]
  

## **IMPORTANTE!**

Ativando e Desativando ambientes virtuais **após configurar a versão do Python no ambiente**:
- Ativando:
```
pyenv activate rePOenv
```
- Desativando:
```
source deactivate
```
**E em seguida**
```
pyenv shell system
```



## Desinstalando ambientes virtuais:
1. 
    ```
    pyenv uninstall rePOenv
    ```

2.
    ``` 
    pyenv virtualenvs 
    ```
    Verifica todos os ambientes virtuais criados

3. Se o ambiente ainda estiver listado, remova a pasta manualmente:
    ```
    rm -rf ~/.pyenv/versions/rePOenv
    ```
