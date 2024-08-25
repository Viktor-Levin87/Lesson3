calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    a = len(string), str.upper(string), str.lower(string)
    print(a)
    count_calls()


def is_contains(string, list_to_search):
    for i in list_to_search:
        is_prime = False
        if string.lower() == i.lower():
            is_prime = True
            break
    print(is_prime)
    count_calls()


string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)
