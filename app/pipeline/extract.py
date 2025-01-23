import os #biblioteca para manipular arquivos e pastas
import glob  #bilbioteca para listar arquivos
import pandas as pd
from typing import List

'''
função para ler arquivos de uma pasta da/input e retornar uma lista de dataframes

args: input_path (str) : caminho da patas de dataframes

return: lista de dataframes
'''

def extract_from_excel(path: str) -> List[pd.DataFrame] :
    all_files = glob.glob(os.path.join(path,"*.xlsx"))
    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list

