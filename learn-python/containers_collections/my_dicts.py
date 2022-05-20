
def longest_list_in_dict():
    d = {"foo": "bar", "spam": ['green', 'eggs', 'and', 'ham']}
    max_key, max_value = max(d.items(), key=lambda x: len(set(x[1])))
    print(f'max_key, max_value, {max_key}, {max_key, max_value}')


if __name__ == '__main__':
    longest_list_in_dict()
