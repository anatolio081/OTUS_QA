import pytest
import math
import random


class TestForIntegers:
    """
    Class for base operations with int variables
    """

    def test_sum(self, fix_module, fix_class):
        """
        simple sum test
        :param fix_module:
        :param fix_class:
        :return:
        """
        assert 2 + 3 == 5

    def test_substr(self, fix_module, fix_class):
        """
        simple subtraction test
        :param fix_module:
        :param fix_class:
        :return:
        """
        assert 5 - 3 == 2

    def test_pow(self, fix_module_r):
        """
        get value for pow from fix_module_r and check it
        :param fix_module_r:
        :return:
        """
        assert pow(2, fix_module_r) == 8


class TestForString:

    def test_sum_str(self, fix_class, fix_module, fix_func):
        """
        add one string to two string and compare with expected
        :param fix_class:
        :param fix_module:
        :param fix_func:
        :return:
        """
        assert "a" + "b" == "ab"

    @pytest.mark.parametrize("sentence,word", [
        ("mom washed frame", "mom"),
        ("dad drunk beer", "beer"),
        ("i want eat pizza", "pizza"),
        ("dont wanna be a bad student", "bad student")
    ])
    def test_finding_word(self, sentence, word, fix_func):
        assert word in sentence


def test_number_exists_in_tuple(fix_module_w_param_from_confest):
    """
    create tuple and check if 1,3,5 in it
    :param fix_module_w_param_from_confest:
    :return:
    """
    t = (1, 2, 3, 4, 5, 6)
    assert fix_module_w_param_from_confest in t


def test_appended_number_in_generated_list(fix_func):
    """
    generate list without 333
    append 333
    find 333 in list
    :param fix_module:
    :return:
    """
    generated = [i for i in range(0, 80)]
    generated.append(333)
    assert 333 in generated


def test_set_intersection(fix_module):
    """
    check intersection beetween 2 sets
    :param fix_module:
    :return:
    """
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    expected = {4, 5}
    assert expected == set1.intersection(set2)


def test_clear_dict(fix_module):
    """
        clear dict and check emptiness
        :param fix_module:
        :return:
        """
    d = {'1': 'one',
         '2': 'two',
         '3': 'three'}
    d.clear()
    print(d)
    assert d == {}


@pytest.mark.parametrize("test_input,expected", [
    ([1, 2, 3], [3, 2, 1]),
    (["a", "b", "c"], ["c", "b", "a"])])
def test_reversing_list(test_input, expected, fix_func):
    """
    reverse list, and check result with expected
    :return:
    """
    lr = reversed(test_input)
    assert list(reversed(test_input)) == expected
