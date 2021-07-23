# github-actions-gke-flask

## 概要

GKEにFlaskで作成したWebアプリをデプロイするための、サンプルコードです。

## 使い方

GCPのGKEクラスタを作成してください。

`GitHub - Settings - Secrets`の`Actions Secret`で下記を設定してください。

- GKE_PROJECT
- GKE_SA_KEY

また、サンプルコードではアプリ名を`web-app-04`としているので、適宜修正してください。

コードをpushすることでワークフローが実行されます。

## 説明

ワークフロー(`main.yaml`)は`push`をトリガーに下記の処理をシーケンシャルに実行します。

- lint(flake8)
- test(pytest)
- build
- deploy

lintが通らない場合はPEP8に従って修正してください。例えば、下記のように自動フォーマッターを利用しても良いです。

```
autopep8 -i YOUR_PYTHON_FILE
```
