from pipeline.extract import extract_from_excel


path = "data/input"
if __name__ == "__main__":
    data_fram_list = extract_from_excel(path)
    print(data_fram_list)