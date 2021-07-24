vowels = "aeiou"


def iterative_count_consonants(input_str):
    count = 0
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowels and input_str[i].isalpha():
            count += 1
    return count


def recursive_count_consonants(input_str):
    pass

input_str = "abc de"
print(input_str)
print(iterative_count_consonants(input_str))
print(recursive_count_consonants(input_str))
input_str = "LuCiDPrograMMiNG"
print(input_str)
print(iterative_count_consonants(input_str))
print(recursive_count_consonants(input_str))
