# CROSS_GAME_BOX

## このスクリプトについて

このスクリプトは、[へいぞ](https://www.pixiv.net/users/75527577)氏考案の女子ボクシングアナログゲーム「[Cross Game Box](https://heizo2019.jimdofree.com/guest/crossgameboxrule/)」用のゲームスクリプトです。
Windowsからはcross_game_box.exe(Pyinstallerでコンパイルしたもの)を実行するか、Python3（3.9及び3.11で検証済み）をインストールした上でcross_game_box_start.bat（バッチファイル）を実行してください。
Mac及びLinuxではPython3をインストールした上でcross_game_box_start.shに実行権限を与えて実行してください。

## 遊び方

1. 青コーナーのボクサーの名前を入力してください。
2. 青コーナーのボクサーの得意ブローを次の4つの中から0～3の数字で選択してください。
    0. ストレート
    1. フック
    2. ボディブロー
    3. アッパーカット
3. 青コーナーと同様に赤コーナーのボクサーの名前を入力してください。
4. 青コーナーのボクサーの得意ブローを0～3の数字で選択してください。
5. ノックダウン方式を次の2つから0もしくは1の数字で選択してください。
    0. 3ノックダウン：1ラウンド中に3回ダウンしたらTKOとなります
    1. フリーノックダウン：1ラウンド中のダウン回数の制限はありません。ただし、試合中に合計5回ダウンしたらTKOとなります。
6. ラウンド数を次の5つの中から4，6，8，10，12のいずれかの数字で選択してください。
    4. 4ラウンド
    6. 6ラウンド
    8. 8ラウンド
    10. 10ラウンド
    12. 12ラウンド

ここまで入力したら試合が開始します。
試合中はキーボードのいずれかのキー（Enterキー等）を入力することで試合が進行します。
試合が終了したらもう1試合行うかというメッセージが出てくるので終了する場合は「q」（全角/半角のどちらでも大丈夫です）を入力し、もう1試合行う場合はそれ以外のキーを入力してください。
試合ログは起動時に自動的に作成されるfight_logディレクトリにtxt形式で試合終了時に保存されます。