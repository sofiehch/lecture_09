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


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    pass


if __name__ == '__main__':
    main()