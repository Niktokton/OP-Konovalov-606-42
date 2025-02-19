from _word_solver import WordSolver

def test_value_dict():
    solver = WordSolver(n_letters=3, letters="abc")
    expected_output = "a - 0, b - 1, c - 2"
    assert solver.value() == expected_output


def test_generate_inner_words():
    solver = WordSolver(n_letters=4, letters="ab")
    generated_words = list(solver.generate_inner_words())
    expected_words = ['aa', 'ab', 'ba', 'bb']
    assert sorted(generated_words) == sorted(expected_words)


def test_is_valid_with_positions():
    """
    Проверка метода `is_valid`, когда задано условие на позиции букв.
    """
    solver = WordSolver(
        n_letters=4,
        letters="abcd",
        conditions={'positions': {1: {'b'}, 3: {'c'}}}
    )
    valid_word = "acda"
    invalid_word_1 = "bcad"
    invalid_word_2 = "abcd"
    assert solver.is_valid(valid_word) == True
    assert solver.is_valid(invalid_word_1) == False
    assert solver.is_valid(invalid_word_2) == False


def test_is_valid_with_occurrences():
    """
    Проверка метода `is_valid`, когда задано условие на количество вхождений букв.
    """
    solver = WordSolver(
        n_letters=4,
        letters="abcd",
        conditions={'occurrences': {'a': 2}}
    )
    valid_word = "abad"
    invalid_word_1 = "cbcd"
    invalid_word_2 = "aaaa"
    assert solver.is_valid(valid_word) == True
    assert solver.is_valid(invalid_word_1) == False
    assert solver.is_valid(invalid_word_2) == False


def test_count_words():
    """
    Проверка метода `count_words`. В данном случае проверяется подсчет всех возможных слов
    длиной 3 из букв 'a' и 'b'.
    """
    solver = WordSolver(n_letters=3, letters="ab")
    result = solver.count_words()
    assert result == 8


def test_count_words_with_conditions():
    """
    Проверка метода `count_words` с условиями на первую и последнюю букву.
    """
    solver = WordSolver(
        n_letters=3,
        letters="abc",
        conditions={
            'first': {'a'},
            'last': {'c'}
        }
    )
    result = solver.count_words()
    assert result == 12


test_value_dict()
test_generate_inner_words()
test_is_valid_with_positions()
test_is_valid_with_occurrences()
test_count_words()
test_count_words_with_conditions()
