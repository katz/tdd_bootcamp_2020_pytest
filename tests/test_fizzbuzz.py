from fizzbuzz import FizzBuzz
import pytest


class FizzBuzzテストクラス:
    @pytest.fixture(scope="function")
    def fizzBuzz(self):
        return FizzBuzz()

    def _1を渡すと文字列1を返す_test(self, fizzBuzz):
        assert "1" == fizzBuzz.convert(1)

    def _2を渡すと文字列2を返す_test(self):
        # 準備
        fizzBuzz = FizzBuzz()
        # 実行 & 検証
        assert "2" == fizzBuzz.convert(2)

    def _3を渡すと文字列Fizzを返す_test(self):
        # 準備
        fizzBuzz = FizzBuzz()
        # 実行 & 検証
        assert "Fizz" == fizzBuzz.convert(3)
