# Documentação do Script de Transferência de Arquivos

## Descrição

Este script em Python foi desenvolvido para realizar a cópia de arquivos de uma pasta de origem para uma pasta de destino, com a capacidade de exibir uma barra de progresso durante o processo de cópia. Além disso, o script verifica se os arquivos já existem no destino e, se existirem, realiza uma cópia incremental apenas se houver alterações nos arquivos de origem.

## Requisitos de Instalação

Antes de executar o script, verifique se o seu sistema atende aos seguintes requisitos:

- Python 3 instalado.
- Gerenciador de pacotes pip configurado corretamente.
- As bibliotecas Python `shutil`, `os` e `tqdm` instaladas. Você pode instalar as dependências com o seguinte comando:

    ```
    pip install shutil os tqdm
    ```

## Uso

1. **Download do Script**:

    Faça o download do script `tranf.py` para o seu computador.

2. **Configuração das Pastas de Origem e Destino**:

    Abra o script `tranf.py` em um editor de texto e defina as variáveis `source` e `destination` com os caminhos completos das pastas de origem e destino, respectivamente.

3. **Execução do Script**:

    Abra o terminal ou prompt de comando e navegue até o diretório onde o script `tranf.py` está localizado. Em seguida, execute o seguinte comando:

    ```
    python3 tranf.py
    ```

4. **Acompanhamento da Cópia**:

    Durante a execução do script, uma barra de progresso será exibida, indicando o progresso da cópia dos arquivos.

5. **Conclusão**:

    Após a conclusão da cópia, uma mensagem será exibida indicando que a operação foi realizada com sucesso.

## Exemplo de Uso

Suponha que você tenha os seguintes caminhos de pasta de origem e destino:

- Pasta de origem: `/home/user/origem/`
- Pasta de destino: `/home/user/destino/`

Após configurar os caminhos no script `tranf.py`, execute o script conforme descrito na seção "Execução do Script". O script copiará os arquivos da pasta de origem para a pasta de destino, exibindo uma barra de progresso durante o processo.

