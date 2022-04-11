import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        seznamy = json.load(json_file)
    if field in seznamy:
        seznam = seznamy[field]
        return seznam
    else:
        return None


def linear_search(sekvence, hledane_cislo):
    indices = []
    idx = 0
    count = 0
    while idx < len(sekvence):
        if sekvence[idx] == hledane_cislo:
            indices.append(idx)
            count = count + 1
            idx = idx + 1
        else:
            idx = idx + 1
    return {
        "positions": indices,
        "count": count,
    }


def pattern_search(dna_seq, pattern):
    idx = 0
    pozice = []
    while idx < (len(dna_seq) - len(pattern)):
        podminky = []
        for prvek in pattern:
            if prvek == dna_seq[idx]:
                podminky.append(True)
            idx = idx + 1
        idx = idx + 1 - len(pattern)
        if len(podminky) == len(pattern):
            pozice.append(idx)
    mnozina_pozic = set(pozice)
    return mnozina_pozic






def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    hledani_cisla = linear_search(sequential_data, 9)
    print(hledani_cisla)
    dna_seq = read_data("sequential.json", "dna_sequence")
    print(pattern_search(dna_seq, "TA"))
    pass


if __name__ == '__main__':
    main()