from _number_system import NumberSystemConverter

def test_convert_to_base():
    converter = NumberSystemConverter("10+5", 2, None)
    assert converter.convert_to_base() == "1111"

    converter = NumberSystemConverter("8*2", 8, None)
    assert converter.convert_to_base() == "20"

    converter = NumberSystemConverter("255", 16, None)
    assert converter.convert_to_base() == "ff"


def test_count_digits():
    converter = NumberSystemConverter("7", 2, 1)
    assert converter.count_digits() == 3

    converter = NumberSystemConverter("18", 8, 0)
    assert converter.count_digits() == 1

    converter = NumberSystemConverter("555", 10, 5)
    assert converter.count_digits() == 3


def test_get_value_in_base():
    converter = NumberSystemConverter("17", 10, None)
    assert converter.get_value_in_base(2) == "10001"

    converter = NumberSystemConverter("21", 10, None)
    assert converter.get_value_in_base(3) == "210"

    converter = NumberSystemConverter("256", 10, None)
    assert converter.get_value_in_base(16) == "100"
