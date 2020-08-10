from fizzbuzz import FizzBuzz
import pytest


class FizzBuzz数列と変換規則を扱うFizzBuzzクラス:
    @pytest.fixture(scope="function")
    def fizzBuzz(self):
        return FizzBuzz()

    class convertは数を文字列に変換する:
        def _1を渡すと文字列1を返す_test(self, fizzBuzz):
            assert "1" == fizzBuzz.convert(1)

    class _3の倍数の時は数の代わりにFizzに変換する:
        def _3を渡すと文字列Fizzを返す_test(self, fizzBuzz):
            assert "Fizz" == fizzBuzz.convert(3)

    class _5の倍数の時は数の代わりにBuzzに変換する:
        def _5を渡すと文字列Buzzを返す_test(self, fizzBuzz):
            assert "Buzz" == fizzBuzz.convert(5)
