```markdown
# Documentação de Processos Básicos no Linux
Este documento serve como uma referência rápida para os comandos básicos no Linux. Ele é destinado a ajudar colegas de trabalho a realizar operações comuns e essenciais.

1. Acessar um Diretório
```sh
cd /caminho/do/diretorio
```

2. Listar um Diretório
```sh
ls
ls -l  # Listagem detalhada
ls -a  # Inclui arquivos ocultos
```

3. Verificar as Permissões de Arquivos/Diretórios
```sh
ls -l
```

4. Criar um Diretório
```sh
mkdir nome_do_diretorio
```

5. Apagar um Diretório
```sh
rmdir nome_do_diretorio  # Somente diretórios vazios
rm -r nome_do_diretorio  # Diretórios com conteúdo
```

6. Sincronizar um Diretório com Rsync
```sh
rsync -avz /origem/diretorio /destino/diretorio
```

7. Verificar o Tamanho Total do Diretório
```sh
du -sh /caminho/do/diretorio
```

8. Verificar o Tamanho do Conteúdo do Diretório
```sh
du -sh /caminho/do/diretorio/*
```

9. Verificar se o CIFS Está Instalado
```sh
modprobe -l | grep cifs
```

10. Montar uma Pasta Compartilhada do Windows no Linux
```sh
sudo mount -t cifs -o username=seu_usuario,password=sua_senha //ip_do_servidor/pasta_compartilhada /ponto/de/montagem
```

11. Desmontar uma Pasta Compartilhada do Windows no Linux
```sh
sudo umount /ponto/de/montagem
```

12. Verificar HD com LSBLK
```sh
lsblk
```

13. Criar Partição
Abra o utilitário fdisk:
```sh
sudo fdisk /dev/sdX
```
Dentro do fdisk, siga os passos para criar a partição.

14. Formatar HD
```sh
sudo mkfs.ext4 /dev/sdX1  # Substitua por sua partição específica
```

15. Verificar o ID de um HD
```sh
sudo blkid
```

16. Montar um HD
```sh
sudo mount /dev/sdX1 /ponto/de/montagem
```

17. Montar um HD com o ID de um HD no fstab
Edite o arquivo `/etc/fstab`:
```sh
sudo nano /etc/fstab
```
Adicione a linha correspondente ao seu HD. Por exemplo:
```sh
UUID=seu_uuid /ponto/de/montagem ext4 defaults 0 2
```
Salve e feche o arquivo.

Para montar todas as entradas do fstab:
```sh
sudo mount -a
```

## Comandos Úteis para o Dia a Dia
Verificar o Espaço em Disco:
```sh
df -h
```

Mostrar o Caminho Completo do Diretório Atual:
```sh
pwd
```

Copiar Arquivos e Diretórios:
```sh
cp arquivo_origem arquivo_destino
cp -r diretorio_origem diretorio_destino
```

Mover ou Renomear Arquivos e Diretórios:
```sh
mv arquivo_ou_diretorio_origem arquivo_ou_diretorio_destino
```

Remover Arquivos:
```sh
rm arquivo
rm -rf diretorio  # Remove diretórios e seu conteúdo
```
