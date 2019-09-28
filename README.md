# python-choice

## Description

開発者が所属するスマートフォンアプリプロジェクトのSlackでの利便性を向上させるために
SlackBotを開発した。

## Demo

![](https://user-images.githubusercontent.com/38784824/65817606-70d26180-e244-11e9-8c4a-faa9725b01db.png)

## Feature

**@ラーメン君**宛にメンションを飛ばし、メッセージとして**ラーメン**と送ると、特定のSlackチャンネル内にいるactiveメンバーが
ランダムな順位を付けて返ってくる。

## installation

`$ git clone https://github.com/tsurusekazuki/python-choice.git`

## Deploy

```
$ git init
$ git add .
$ git commit -m "create new"
$ heroku login
$ heroku create heroku-slack-bot
$ git push heroku master
```

## Get Start

Localで起動

`$ python run.py`
