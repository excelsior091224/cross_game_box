# CROSS_GAME_BOX

## Japanese(日本語)

### このスクリプトについて

このスクリプトは、[へいぞ](https://www.pixiv.net/users/75527577)氏考案の女子ボクシングアナログゲーム「[Cross Game Box](https://heizo2019.jimdofree.com/guest/crossgameboxtop/)」用のCUI（Character-based User Interface）ゲームスクリプトです。

Windowsからはcross_game_box.exe(セキュリティソフト誤検知対策としてブートローダーをローカルの環境でビルドしたPyinstallerでコンパイルしたもの)を実行するか、Python3（3.9及び3.11で検証済み）をインストールした上でcross_game_box_start.bat（バッチファイル）を実行してください。

Mac及びLinuxではPython3をインストールした上でcross_game_box_start.sh（シェルスクリプト）に実行権限を与えて実行してください。

### 遊び方

1. 表示言語を次の2つから0もしくは1で選択してください。以後は選択した言語で表示されます。
    - 0:日本語（Japanese）
    - 1:英語（English）
2. 12面ダイスと20面ダイスのどちらを使うか、12か20の数字を入力して選択してください。
3. 青コーナーのボクサーの名前を入力してください。
4. 青コーナーのボクサーの得意ブローを次の4つの中から0～3の数字で選択してください。
    - 0:ストレート
    - 1:フック
    - 2:ボディブロー
    - 3:アッパーカット
5. 青コーナーと同様に赤コーナーのボクサーの名前を入力してください。
6. 青コーナーと同様に赤コーナーのボクサーの得意ブローを0～3の数字で選択してください。
7. ノックダウン方式を次の2つから0もしくは1の数字で選択してください。
    - 0:3ノックダウン：1ラウンド中に3回ダウンしたらTKOとなります
    - 1:フリーノックダウン：1ラウンド中のダウン回数の制限はありません。ただし、試合中に合計5回ダウンしたらTKOとなります。
8. ラウンド数を次の5つの中から4，6，8，10，12のいずれかの数字で選択してください。
    - 4ラウンド
    - 6ラウンド
    - 8ラウンド
    - 10ラウンド
    - 12ラウンド

ここまで入力したら試合が開始します。

試合中はキーボードのいずれかのキー（Enterキー等）を入力することで試合が進行します。

試合が終了したらもう1試合行うかというメッセージが出てくるので終了する場合は「q」（全角/半角のどちらでも大丈夫です）を入力し、もう1試合行う場合はそれ以外のキーを入力してください。

試合ログは起動時に自動的に作成されるfight_logディレクトリにtxt形式で試合終了時に保存されます。

## English

### About this script

This is a CUI (Character-based User Interface) game script for  "[Cross Game Box](https://heizo2019.jimdofree.com/guest/crossgameboxrule/)" , a female boxing analog game designed by [Heizo](https://www.pixiv.net/users/75527577).

On Windows, run cross_game_box.exe (compiled with Pyinstaller, which is a bootloader built in your local environment to prevent false positives from security software), or install Python3 (verified with 3.9 and 3.11) and then run cross_game_box_start.bat (batch file).

On Mac and Linux, install Python3 and execute cross_game_box_start.sh (shell script) with execute permission.

### How to play

1. Select 0 or 1 from the following two display languages. The display will then be in the selected language.
    - 0:日本語（Japanese）
    - 1:英語（English）
2. Select whether you want to use a 12-sided dice or a 20-sided dice by entering the number 12 or 20.
3. Enter the name of the boxer in the blue corner.
4. Select the blue corner boxer's specialty blow from the following 4 options, numbered 0-3.
    - 0:Straight
    - 1:Hook
    - 2:Body blow
    - 3:Uppercut
5. Enter the name of the boxer in the red corner as in the blue corner.
6. As with the blue corner, select the number from 0 to 3 that the boxer in the red corner specializes in.
7. Select the knockdown method from the following two options with a number between 0 and 1.
    - 0:3 knockdowns: Three knockdowns in one round will result in a TKO.
    - 1:Free knockdown: No limit on the number of knockdowns in a round. However, a fighter will be scored a TKO if he goes down a total of five times during the match.
8. Select the number of rounds from the following five numbers: 4, 6, 8, 10, or 12.
    - 4 rounds
    - 6 rounds
    - 8 rounds
    - 10 rounds
    - 12 rounds

Once you have entered the information up to this point, the match will begin.

During a match, you must press any key on the keyboard (e.g., Enter key) to continue the match.

When the match is over, a message will appear asking if you want to play one more match, to exit, enter "q" (either full/half-width or half-width is fine), and to play another game, enter any other key.

The match log will be saved in txt format in the fight_log directory automatically created at startup when the match ends.
