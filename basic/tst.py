from collections import Counter


def create_char_count_dict(input_string):
    char_count_dict = Counter(input_string)
    return dict(char_count_dict)

input_string = "ravinder"
output_dict = create_char_count_dict(input_string)
print(output_dict)
