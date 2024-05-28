import shutil
import os
from tqdm import tqdm

def copy_with_progress(source, destination):
    existing_files = set()

    # Registro dos arquivos existentes no destino
    for dirpath, _, filenames in os.walk(destination):
        for filename in filenames:
            destination_file = os.path.join(dirpath, filename)
            existing_files.add(os.path.relpath(destination_file, destination))

    # Conta o número total de arquivos a serem copiados
    total_files = sum(len(files) for _, _, files in os.walk(source))

    # Inicializa o tqdm
    with tqdm(total=total_files, desc='Copiando arquivos', unit='file') as pbar:
        for dirpath, dirnames, filenames in os.walk(source):
            for filename in filenames:
                source_file = os.path.join(dirpath, filename)
                destination_file = os.path.join(destination, os.path.relpath(source_file, source))
                destination_dir = os.path.dirname(destination_file)
                os.makedirs(destination_dir, exist_ok=True)
                # Copia o arquivo se não existir no destino
                if not os.path.exists(destination_file):
                    shutil.copy2(source_file, destination_file)
                # Se o arquivo existir no destino
                elif os.path.relpath(destination_file, destination) in existing_files:
                    # Verifica se há alterações e faz uma cópia incremental
                    if os.path.getmtime(source_file) > os.path.getmtime(destination_file):
                        shutil.copy2(source_file, destination_file)
                # Se o arquivo estiver faltando no destino, copia da origem para o destino
                elif os.path.relpath(destination_file, destination) not in existing_files:
                    shutil.copy2(source_file, destination_file)
                pbar.update(1)  # Atualiza o tqdm

    print("A cópia foi concluída com sucesso.")

source = '/home/celio/ok/'
destination = '/home/celio/ok2/'

copy_with_progress(source, destination)

