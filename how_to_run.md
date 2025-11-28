## Tutorial de utilização do Conda para reprodução dos resultados do artigo

1. Instalando o Miniconda:

Dá pra baixar pelo navegador o script também e, em seguida, no gerenciador de arquivos, alterar a propriedade do script para ser reconhecido como um executável. Mas caso queira fazer tudo em linha de comando (recomendo):
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod u+x Miniconda3-latest-Linux-x86_64.sh
```
2. Siga o passo a passo para instalação do Miniconda através do terminal
2.1. Aceitando os termos
2.2. Confirmando o caminho onde o miniconda ficará 
2.3. **Confirmando a adição das variáveis de ambiente no .bashrc**.

Colar o comando abaixo no terminal para confirmar as alterações nas variáveis de ambiente sem precisar fechar e abrir o bash:
```
exec $SHELL
```

3. Crie seu ambiente virtual, **especificando as versões do Python e versões de outros pacotes necessários

```
conda create --name nome_ambiente_virtual_alterável python=3.7.7 pandas=1.0.3 numpy=1.18.1 tensorflow=2.1.0 protobuf=3.20.3
```



## Utilizando o conda:
- **1.** No terminal, ative o ambiente virtual: 

    ```
    conda activate nome_ambiente_virtual_alterável 
    ```
2.  Verifique se o Python está na versão correta (provavelmente estará)
    ```
    python -V
    ```
    
3. Verifique se o pip está no virtual enviroment
    ```
    pip -V
    ```
    
4. Verifique todos os pacotes e versões instaladas
```
pip list 
```
5. Caso queira mais detalhes de um pacote..
```
pip show [nome do pacote] 
```

    
    
  

## **IMPORTANTE!**

Ativando e Desativando ambientes virtuais **após configurar a versão do Python no ambiente**:
- Ativando:
```
conda activate nome_ambiente_virtual_alterável
```
- Desativando:
```
conda deactivate
```




## Desinstalando ambientes virtuais:
1. 
    ```
    conda env remove --name nome_ambiente_virtual_alterável
    ```

