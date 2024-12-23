def external_links(line):
    starting_index = line.index(":")
    list_of_words = line[starting_index + 1:].split()
    list_of_url = []
    for word in list_of_words:
        word = word[0:5]
        if word.isalnum() and word[0:3] == "URL":
            list_of_url.append(word)
    return set(list_of_url)

def dictionary_of_init_importance(list_of_lines):
    dict_imp = {}
    for line in list_of_lines:
        starting_index = line.index(",") + 1
        ending_index = line.index(":")
        dict_imp[line[:starting_index - 1]] = float(line[starting_index:ending_index])
    return dict_imp

def tuple_of_importance(dict_imp, list_of_lines):
    list_tuples = []
    for line in list_of_lines:
        ending_index = line.index(",")
        main_url = line[:ending_index]
        ext_urls = external_links(line)
        sum_imp = dict_imp[main_url]
        for url in ext_urls:
            sum_imp += dict_imp[url]
        list_tuples.append(((sum_imp / (len(ext_urls) + 1)), main_url))
    return list_tuples

with open("input_q7.txt", "r") as file:
    list_of_lines = file.readlines()

dict_imp = dictionary_of_init_importance(list_of_lines)
list_of_urls_and_imp = tuple_of_importance(dict_imp, list_of_lines)

with open("output_q7.txt", "w") as output_file:
    for item in list_of_urls_and_imp:
        output_file.write(f"{item[1]}: {item[0]:.4f}\n")

print("Results written to output.txt")