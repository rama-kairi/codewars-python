# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'


def reverse_string(string):
    return string[::-1]


if __name__ == "__main__":
    print(reverse_string("world"))
    print(reverse_string("word"))
