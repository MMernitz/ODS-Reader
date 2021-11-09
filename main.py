from pandas_ods_reader import read_ods
import collections

# base_path = "eaqua_polybios_30sim_alltime_book1.ods"
# base_path = "eaqua_polybios_30sim_alltime_book3.ods"
# base_path = "eaqua_polybios_30sim_alltime.ods"
# base_path = "eaqua_cassiusdio_30sim_alltime.ods"
# base_path = "eaqua_diodorus_30sim_alltime.ods"
base_path="eaqua_plutarch_30sim_alltime.ods"
sheet_index = 1
df = read_ods(base_path)
authors = {}

print(f'Es wurden insgesamt {len(df)} Zeilen gefunden.')


def print_content(file):
    for index, row in file.iterrows():
        if not row[5] in authors:
            authors[row[5]] = 1
        else:
            authors[row[5]] += 1

    count_authors = len(authors)
    print(f'Es gab insgesamt {count_authors} Autoren.')
    sorted_list = sorted(authors.items(), key=lambda kv: kv[1], reverse=True)
    sorted_list_dict = collections.OrderedDict(sorted_list)

    for author in sorted_list_dict:
        print(f'{author} wurde {sorted_list_dict[author]} mal gefunden.')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_content(df)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
