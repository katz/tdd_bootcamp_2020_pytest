## Python3 + pytestでTDD Boot Camp 2020のテスト駆動開発をやってみる

[TDD Boot Camp 2020 Online #1 基調講演/ライブコーディング](https://www.youtube.com/watch?v=Q-FJ3XmFlT8) を参考に、Python3 + pytestでテスト駆動開発をやってみた。


## 環境
* Windows 10 version 2004 ( OS Build 19041.388)
* Python 3.7.7
* pytest 6.0.1
* VSCode 1.47.3
* VSCode拡張機能
  * [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  * [Python Test Explorer for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter)



## 環境構築方法

まずはPowershellを立ち上げ、普通にvenv作ってactivateする

```powershell
python3 -m venv venv
venv/Scripts/Activate.ps1
```

あとは、依存ライブラリをインストールする。

```
pip install -r requirements.txt
```

そうすると、VSCodeのTestペインにテスト一覧が出てくる。

![VSCode上でテスト実行結果を表示してる例](https://raw.githubusercontent.com/katz/tdd_bootcamp_2020_pytest/master/assets/pytest_vscode.png?sanitize=true)


## pytestがテストコードが書かれたクラス・関数を検出する動作のカスタマイズにおける工夫

pytest.iniを使って、pytestがテストコードとして検出するクラス・関数名をカスタマイズしている。

```ini
[pytest]
testpaths = tests
python_files = *.py
python_functions = *_test
python_classes = *
```

* テストファイル群の置き場所はtestsフォルダ以下にする
* 指定したフォルダ内にあるファイルのうち、拡張子が.pyで終わるものをまずは拾う
* 関数名は「_test」で終わるものだけ対象にする
  * `python_functions = *` と記述し全ての関数を対象に指定すると、`__eq__` などデフォルトで用意されている関数も検索対象になる
    * その場合、pytestのログが「`PytestCollectionWarning: cannot collect '__eq__' because it is not a function`」のようなメッセージで汚染されまくり、ログが見づらくなる
  * `python_functions`に何も設定しない場合、関数名が「test」で始まるものが対象になるが、テスト結果画面の冒頭がtestだらけで見づらくなってしまう。
  * 検出対象の関数を絞るためにどうせprefixかsuffixを付けないといけないのなら、suffixにしておけば、テスト結果を見たときに見やすい。
* クラス名に関しては全て対象にする
  * `python_classes`に何も設定しない場合、クラス名が「Test」で始まるものが対象になる。
