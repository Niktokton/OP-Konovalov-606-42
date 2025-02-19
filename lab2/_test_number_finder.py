from _number_finder import NumberFinder

def test_find_numbers_bigger_even():
    finder = NumberFinder(n_numbers=3, comparison_type='bigger', target_number=40)
    finder.find_numbers()
    assert finder.found_numbers == [42, 52, 62]


def test_find_numbers_smaller_even():
    finder = NumberFinder(n_numbers=3, comparison_type='smaller', target_number=80)
    finder.find_numbers()
    assert finder.found_numbers == [78, 68, 58]


def test_find_numbers_with_condition_ends_with():
    finder = NumberFinder(
        n_numbers=3,
        comparison_type='bigger',
        target_number=50,
        conditions={'ends_with': '8'}
    )
    finder.find_numbers()
    assert finder.found_numbers == [58, 88, 98]


def test_find_numbers_with_condition_not_equal_to():
    finder = NumberFinder(
        n_numbers=3,
        comparison_type='bigger',
        target_number=60,
        conditions={'not_equal_to': 28}
    )
    finder.find_numbers()
    assert finder.found_numbers == [70, 90, 110]


def test_check_conditions_no_divisor_found():
    finder = NumberFinder(n_numbers=3, comparison_type='bigger', target_number=37)
    assert not finder.check_conditions(37)


def test_print_results():
    finder = NumberFinder(n_numbers=3, comparison_type='bigger', target_number=30)
    finder.find_numbers()
    output = finder.print_results()
    assert output == [
        "30 30",
        "40 40",
        "50 50"
    ]
