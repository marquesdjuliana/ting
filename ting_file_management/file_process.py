import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_content = txt_importer(path_file)

    if file_content is None:
        return

    file_name = path_file
    for i in range(len(instance)):
        existing_file = instance.search(i)
        if existing_file["nome_do_arquivo"] == file_name:
            return

    processed_data = {
        "nome_do_arquivo": file_name,
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": file_content,
    }

    instance.enqueue(processed_data)

    sys.stdout.write(str(processed_data) + "\n")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
