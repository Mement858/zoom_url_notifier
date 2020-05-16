# zoom_url_notifier
utas上の講義zoomのURLを取ってきて、slackに表示するslackbot
## 使い方
- `/plugins/my_mention.py`で、自分のアカウント、取得したい時間割コードに適宜変更してください
- `/plugins/`に`chromedriver`を置いてください
- `slackbot-settings.py`で、このslackbotを使用したいslackワークスペースのAPI TOKENを設定してください
- `python3 run.py`で動くはず