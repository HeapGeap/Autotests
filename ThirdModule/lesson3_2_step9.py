def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"


full_string = input("Введите полную строку : ")
substring = input("Введите вхождение в строку : ")

test_substring(full_string, substring)

# s = 'My Name is Julia'
#
# if 'Name' in s:
#     print('Substring found')
#
# index = s.find('Name')
# if index != -1:
#     print(f'Substring found at index {index}')