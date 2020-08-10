from fizzbuzz import FizzBuzz


class FizzBuzzテストクラス:
    def _1を渡すと文字列1を返す_test(self):
        # 準備
        fizzBuzz = FizzBuzz()
        # 実行
        actual = fizzBuzz.convert(1)
        # 検証
        assert "1" == actual
