def test_input_text(expected_result, actual_result):
    assert (expected_result == actual_result), f"expected {expected_result}, got {actual_result}"


expected_result = int(input("Введите ожидаемый результат : "))
actual_result = int(input("Введите фактический результат : "))

test_input_text(expected_result, actual_result)
