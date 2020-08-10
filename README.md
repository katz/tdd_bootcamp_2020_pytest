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

```
python3 -m venv venv
venv/Scripts/Activate.ps1
```

あとは、依存ライブラリをインストールする。

```
pip install -r requirements.txt
```

そうすると、VSCodeのTestペインにテスト一覧が出てくる。

![VSCode上でテスト実行結果を表示してる例](https://raw.githubusercontent.com/katz/tdd_bootcamp_2020_pytest/master/assets/pytest_vscode.png?sanitize=true)
