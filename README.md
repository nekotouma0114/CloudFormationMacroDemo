# なにこれ

一つのSecurity GroupにいろんなIPからのHTTP/HTTPS許可が必要だったから、
それをいい感じにCloudFormationのマクロ機能で生成するやつのデモ

# 使い方

1. lambda_handler.pyを基にlambda関数を作成する
2. macro.ymlでスタックを作成するarnには1で作った関数のarnを入力する
3. vpc_sg.ymlでスタックを作成する許可したいIPをCustomerCidrIpにList<String>形式で入力する
    ex) 192.168.2.1/32 192.168.2.2/32

詳細はこちらで記事を書きました

【AWS】CloudFormation::Macroを使って多数のIPを接続許可する

https://qiita.com/nekotouma0114/items/ff2e99a3203588ee537e

# 抱えてる問題

- ~~コードが汚い~~
- CustomerCidrIpの入力値を更新してもCloudFormation側で変更が認識されずに更新できない
