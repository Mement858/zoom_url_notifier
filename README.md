# zoom_url_notifier
utas上の講義zoomのURLを取ってきて、slackに表示するslackbot
## 使い方
- `pip install selenium slackbot bs4`や`pipenv install selenium slackbot bs4`などで適宜必要なモジュールを入れてください．
- `/plugins/my_mention.py`で、自分のアカウント、取得したい時間割コードに適宜変更してください
- `/plugins/`に`chromedriver`を置いてください
- `slackbot-settings.py`で、このslackbotを使用したいslackワークスペースのAPI TOKENを設定してください
- slackのワークスペースにbotを追加してくだい
- `python3 run.py`のあと，slackで`@[名前] url`でurlが表示されます
