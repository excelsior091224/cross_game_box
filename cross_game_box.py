import random, os
from datetime import datetime

# ダイスのクラス
class Dice:
    def __init__(self, dice_num, dice_size):
        # ダイスの数
        self.num = dice_num
        # ダイスの面数
        self.size = dice_size
    
    # ダイスを投げたときの処理
    def throw_dice(self):
        # ダイスの目を格納するリスト
        dice_roll = []
        # ダイスの数だけ繰り返すループ
        for i in range(self.num):
            # ダイスの面数からランダムな数（ダイスの出目）を変数numに代入
            num = random.randint(1, self.size)
            # ダイスの出目numをリストdice_rollに格納
            dice_roll.append(num)
        # ダイスの目が個数分入ったリストを返り値とする
        # 例：6面ダイス2個の場合：[1個目のダイスの目,2個目のダイスの目]
        return dice_roll

# 対戦ログを保存するフォルダを作成する関数
def make_folder():
    fight_log_dir = "fight_log"
    try:
        os.makedirs(fight_log_dir)
    except FileExistsError:
        pass
    return fight_log_dir

# 対戦ログを出力
def export_log(log_text,file_name):
    with open(file_name,'w',encoding='utf-8') as f:
        f.writelines([d+"\n" for d in log_text])

# ボクサーのクラス
class Boxer:
    def __init__(self, corner, name, fav_blow):
        # ボクサーのコーナー（赤or青）
        self.corner = corner
        # ボクサーの名前
        self.name = name
        self.fav_blow = fav_blow
        # 状態
        self.status = 0
        # 1ラウンドごとの優勢に回った回数
        self.attack_num = 0
        # 1ラウンドごとのダウン回数
        self.round_down_num = 0
        # 試合全体でのダウン回数
        self.total_down_num = 0
        # 試合のポイント数
        self.point = 0
        # 試合結果
        self.result = ''
        # （負けた場合の）決着方法
        self.conclusion = ''
        print('{}コーナー\n{}選手'.format(self.corner,self.name))

# 状態出力
def print_status(blue_boxer,red_boxer,log_text,STATUS):
    # 出力するテキスト
    print_text = '{}コーナー・{}選手:状態:{}'.format(blue_boxer.corner,blue_boxer.name,STATUS[blue_boxer.status])
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # 入力を待つ
    input()
    # 出力するテキスト
    print_text = 'このラウンドでのダウン:{}回'.format(blue_boxer.round_down_num)
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # 入力を待つ
    input()
    # 出力するテキスト
    print_text = '試合全体でのダウン:{}回'.format(blue_boxer.total_down_num)
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # 入力を待つ
    input()
    # 出力するテキスト
    print_text = '{}コーナー・{}選手:状態:{}'.format(red_boxer.corner,red_boxer.name,STATUS[red_boxer.status])
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # 入力を待つ
    input()
    # 出力するテキスト
    print_text = 'このラウンドでのダウン:{}回'.format(red_boxer.round_down_num)
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # 入力を待つ
    input()
    # 出力するテキスト
    print_text = '試合全体でのダウン:{}回'.format(red_boxer.total_down_num)
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    return blue_boxer,red_boxer,log_text

# 青コーナー優勢
def blue_superiority(DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW):
    # 状態が6（SS）未満の場合
    if blue_boxer.status < 6:
        # 状態を1段階上げる
        blue_boxer.status += 1
    # 優勢に回った回数を1加算
    blue_boxer.attack_num += 1
    # 出力するテキスト
    print_text = '「{name}選手のパンチが何度もヒット！」\n「{name}選手が優勢に試合を進めています」\n「{name}選手の状態が{status}に上昇しました」'.format(name=blue_boxer.name,status=STATUS[blue_boxer.status])
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # 入力を待つ
    input()
    blue_boxer,red_boxer,log_text = print_status(blue_boxer,red_boxer,log_text,STATUS)
    return blue_boxer,red_boxer,log_text

# 赤コーナー優勢
def red_superiority(DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW):
    # 状態が6（SS）未満の場合
    if red_boxer.status < 6:
        # 状態を1段階上げる
        red_boxer.status += 1
    # 優勢に回った回数を1加算
    red_boxer.attack_num += 1
    # 出力するテキスト
    print_text = '「{name}選手のパンチが何度もヒット！」\n「{name}選手が優勢に試合を進めています」\n「{name}選手の状態が{status}に上昇しました」'.format(name=red_boxer.name,status=STATUS[red_boxer.status])
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # 入力を待つ
    input()
    blue_boxer,red_boxer,log_text = print_status(blue_boxer,red_boxer,log_text,STATUS)
    return blue_boxer,red_boxer,log_text

# 互角
def evenness(DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW):
    # 出力するテキスト
    print_text = '「両者互角の攻防が続いてます！」'
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # 入力を待つ
    input()
    blue_boxer,red_boxer,log_text = print_status(blue_boxer,red_boxer,log_text,STATUS)
    return blue_boxer,red_boxer,log_text

# クリンチ
def clinch(DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW):
    # 青コーナーボクサーのステータスがSA以上SS以下の場合、Sに落とす
    if blue_boxer.status >= 4:
        blue_boxer.status = 3
    # それ以外の場合、ステータスを1段階落とす
    elif blue_boxer.status <= 3 and blue_boxer.status > 0:
        blue_boxer.status -= 1
    # 赤コーナーボクサーのステータスがSA以上SS以下の場合、Sに落とす
    if red_boxer.status >= 4:
        red_boxer.status = 3
    # それ以外の場合、ステータスを1段階落とす
    elif red_boxer.status <= 3 and red_boxer.status > 0:
        red_boxer.status -= 1
    # 出力するテキスト
    print_text = '「両者クリンチです」\n「{blue_name}選手の状態が{blue_status}に下がり、{red_name}選手の状態が{red_status}に下がりました」'.format(blue_name=blue_boxer.name,blue_status=STATUS[blue_boxer.status],red_name=red_boxer.name,red_status=STATUS[red_boxer.status])
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # 入力を待つ
    input()
    blue_boxer,red_boxer,log_text = print_status(blue_boxer,red_boxer,log_text,STATUS)
    return blue_boxer,red_boxer,log_text

# 青コーナーカウンター
def blue_counter(DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW):
    # 青コーナーの状態が6（SS）未満の場合
    if blue_boxer.status < 6:
        # 状態を1段階上げる
        blue_boxer.status += 1
    # 赤コーナーボクサーのステータスがSA以上SS以下の場合、Sに落とす
    if red_boxer.status >= 4:
        red_boxer.status = 3
    # それ以外の場合、ステータスを1段階落とす
    elif red_boxer.status <= 3 and red_boxer.status > 0:
        red_boxer.status -= 1
    # 優勢に回った回数を1加算
    blue_boxer.attack_num += 1
    # 出力するテキスト
    print_text = '「{blue_name}選手のカウンターパンチが{red_name}選手にヒットしました！」\n「{blue_name}選手の状態が{blue_status}に上昇し、{red_name}選手の状態が{red_status}に下がりました」'.format(blue_name=blue_boxer.name,blue_status=STATUS[blue_boxer.status],red_name=red_boxer.name,red_status=STATUS[red_boxer.status])
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # 入力を待つ
    input()
    blue_boxer,red_boxer,log_text = print_status(blue_boxer,red_boxer,log_text,STATUS)
    return blue_boxer,red_boxer,log_text

# 赤コーナーカウンター
def red_counter(DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW):
    # 赤コーナーの状態が6（SS）未満の場合
    if red_boxer.status < 6:
        # 状態を1段階上げる
        red_boxer.status += 1
    # 青コーナーボクサーのステータスがSA以上SS以下の場合、Sに落とす
    if blue_boxer.status >= 4:
        blue_boxer.status = 3
    # それ以外の場合、ステータスを1段階落とす
    elif blue_boxer.status <= 3 and blue_boxer.status > 0:
        blue_boxer.status -= 1
    # 優勢に回った回数を1加算
    red_boxer.attack_num += 1
    # 出力するテキスト
    print_text = '「{red_name}選手のカウンターパンチが{blue_name}選手にヒットしました！」\n「{red_name}選手の状態が{red_status}に上昇し、{blue_name}選手の状態が{blue_status}に下がりました」'.format(blue_name=blue_boxer.name,blue_status=STATUS[blue_boxer.status],red_name=red_boxer.name,red_status=STATUS[red_boxer.status])
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # 入力を待つ
    input()
    blue_boxer,red_boxer,log_text = print_status(blue_boxer,red_boxer,log_text,STATUS)
    return blue_boxer,red_boxer,log_text

# 相打ち
def draw(DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW):
    # 青コーナーの状態が0以上かつ6（SS）未満の場合
    if blue_boxer.status < 6 and blue_boxer.status >= 0:
        # 状態を1段階上げる
        blue_boxer.status += 1
    # 赤コーナーの状態が0以上かつ6（SS）未満の場合
    if red_boxer.status < 6 and red_boxer.status >= 0:
        # 状態を1段階上げる
        red_boxer.status += 1
    # 出力するテキスト
    print_text = '「{blue_name}選手と{red_name}選手のパンチがお互いにヒット！！　両者相打ちです！！」'.format(blue_name=blue_boxer.name,red_name=red_boxer.name)
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # 入力を待つ
    input()
    blue_boxer,red_boxer,log_text = print_status(blue_boxer,red_boxer,log_text,STATUS)
    return blue_boxer,red_boxer,log_text

# 青コーナーダウン
def blue_downed(DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW):
    # ラウンドあたりのダウン数に1加算
    blue_boxer.round_down_num += 1
    # 試合トータルでのダウン数に1加算
    blue_boxer.total_down_num += 1
    # 赤コーナーのステータスがS~SAAの場合
    if red_boxer.status >= 3 and red_boxer.status <= 5:
        # ステータスをSSに更新
        red_boxer.status = 6
    # AA以下の場合
    elif red_boxer.status <= 2:
        # ステータスをSに更新
        red_boxer.status = 3
    # 出力するテキスト
    print_text = '「{red_name}選手のパンチで{blue_name}選手がダウン！」\n「レフェリーがカウントを数えます！」\n「{red_name}選手の状態は{red_status}に上昇しています！」'.format(blue_name=blue_boxer.name,red_name=red_boxer.name,red_status=STATUS[red_boxer.status])
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # 入力を待つ
    input()
    blue_boxer,red_boxer,log_text = print_status(blue_boxer,red_boxer,log_text,STATUS)
    # 入力を待つ
    input()
    # 3ノックダウン制の場合
    if knockdown_type == 0:
        # 1ラウンドあたりのダウン数が3回以上になるか、試合トータルでのダウン数が5回以上でTKO
        if blue_boxer.round_down_num >= 3 or blue_boxer.total_down_num >= 5:
            blue_boxer,log_text = tko(blue_boxer,log_text)
        else:
            # 12面ダイス1個を振る
            dice_roll = sum(DICE.throw_dice())
            # 出力するテキスト
            print_text = '{}コーナー・ダイス：{}'.format(blue_boxer.corner,dice_roll)
            # テキストを出力
            print(print_text)
            # ログにテキストを追加
            log_text.append(print_text)
            # 入力を待つ
            input()
            # トータルでのダウン数が1回の場合
            if blue_boxer.total_down_num == 1:
                # DOWN['down_1']のダイス出目に応じた関数を実行する
                blue_boxer,log_text = DOWN['down_1'][dice_roll](blue_boxer,log_text)
            # 2回の場合
            elif blue_boxer.total_down_num == 2:
                # DOWN['down_2']のダイス出目に応じた関数を実行する
                blue_boxer,log_text = DOWN['down_2'][dice_roll](blue_boxer,log_text)
            # 3回の場合
            elif blue_boxer.total_down_num == 3:
                # DOWN['down_3']のダイス出目に応じた関数を実行する
                blue_boxer,log_text = DOWN['down_3'][dice_roll](blue_boxer,log_text)
            # 4回以上の場合
            else:
                # DOWN['down_3_or_more']のダイス出目に応じた関数を実行する
                blue_boxer,log_text = DOWN['down_4_or_more'][dice_roll](blue_boxer,log_text)
    # フリーノックダウン制の場合
    else:
        # 試合トータルでのダウン数が5回以上でTKO
        if blue_boxer.total_down_num >= 5:
            blue_boxer,log_text = tko(blue_boxer,log_text)
        else:
            # 12面ダイス1個を振る
            dice_roll = sum(DICE.throw_dice())
            # 出力するテキスト
            print_text = '{}コーナー・ダイス：{}'.format(blue_boxer.corner,dice_roll)
            # テキストを出力
            print(print_text)
            # 入力を待つ
            input()
            # ログにテキストを追加
            log_text.append(print_text)
            # トータルでのダウン数が1回の場合
            if blue_boxer.total_down_num == 1:
                # DOWN['down_1']のダイス出目に応じた関数を実行する
                blue_boxer,log_text = DOWN['down_1'][dice_roll](blue_boxer,log_text)
            # 2回の場合
            elif blue_boxer.total_down_num == 2:
                # DOWN['down_2']のダイス出目に応じた関数を実行する
                blue_boxer,log_text = DOWN['down_2'][dice_roll](blue_boxer,log_text)
            # 3回の場合
            elif blue_boxer.total_down_num == 3:
                # DOWN['down_3']のダイス出目に応じた関数を実行する
                blue_boxer,log_text = DOWN['down_3'][dice_roll](blue_boxer,log_text)
            # 4回以上の場合
            else:
                # DOWN['down_3_or_more']のダイス出目に応じた関数を実行する
                blue_boxer,log_text = DOWN['down_4_or_more'][dice_roll](blue_boxer,log_text)
    return blue_boxer,red_boxer,log_text

# 赤コーナーダウン
def red_downed(DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW):
    # ラウンドあたりのダウン数に1加算
    red_boxer.round_down_num += 1
    # 試合トータルでのダウン数に1加算
    red_boxer.total_down_num += 1
    # 青コーナーのステータスがS~SAAの場合
    if blue_boxer.status >= 3 and blue_boxer.status <= 5:
        # ステータスをSSに更新
        blue_boxer.status = 6
    # AA以下の場合
    elif blue_boxer.status <= 2:
        # ステータスをSに更新
        blue_boxer.status = 3
    # 出力するテキスト
    print_text = '「{blue_name}選手のパンチで{red_name}選手がダウン！」\n「レフェリーがカウントを数えます！」\n「{blue_name}選手の状態は{blue_status}に上昇しています！」'.format(blue_name=blue_boxer.name,blue_status=STATUS[blue_boxer.status],red_name=red_boxer.name)
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # 入力を待つ
    input()
    blue_boxer,red_boxer,log_text = print_status(blue_boxer,red_boxer,log_text,STATUS)
    # 入力を待つ
    input()
    # 3ノックダウン制の場合
    if knockdown_type == 0:
        # 1ラウンドあたりのダウン数が3回以上になるか、試合トータルでのダウン数が5回以上でTKO
        if red_boxer.round_down_num >= 3 or red_boxer.total_down_num >= 5:
            red_boxer,log_text = tko(red_boxer,log_text)
        else:
            # 12面ダイス1個を振る
            dice_roll = sum(DICE.throw_dice())
            # 出力するテキスト
            print_text = '{}コーナー・ダイス：{}'.format(red_boxer.corner,dice_roll)
            # テキストを出力
            print(print_text)
            # ログにテキストを追加
            log_text.append(print_text)
            # 入力を待つ
            input()
            # トータルでのダウン数が1回の場合
            if red_boxer.total_down_num == 1:
                # DOWN['down_1']のダイス出目に応じた関数を実行する
                red_boxer,log_text = DOWN['down_1'][dice_roll](red_boxer,log_text)
            # 2回の場合
            elif red_boxer.total_down_num == 2:
                # DOWN['down_2']のダイス出目に応じた関数を実行する
                red_boxer,log_text = DOWN['down_2'][dice_roll](red_boxer,log_text)
            # 3回の場合
            elif red_boxer.total_down_num == 3:
                # DOWN['down_3']のダイス出目に応じた関数を実行する
                red_boxer,log_text = DOWN['down_3'][dice_roll](red_boxer,log_text)
            # 4回以上の場合
            else:
                # DOWN['down_3_or_more']のダイス出目に応じた関数を実行する
                red_boxer,log_text = DOWN['down_4_or_more'][dice_roll](red_boxer,log_text)
    # フリーノックダウン制の場合
    else:
        # 試合トータルでのダウン数が5回以上でTKO
        if red_boxer.total_down_num >= 5:
            red_boxer,log_text = tko(red_boxer,log_text)
        else:
            # 12面ダイス1個を振る
            dice_roll = sum(DICE.throw_dice())
            # 出力するテキスト
            print_text = '{}コーナー・ダイス：{}'.format(red_boxer.corner,dice_roll)
            # テキストを出力
            print(print_text)
            # ログにテキストを追加
            log_text.append(print_text)
            # 入力を待つ
            input()
            # トータルでのダウン数が1回の場合
            if red_boxer.total_down_num == 1:
                # DOWN['down_1']のダイス出目に応じた関数を実行する
                red_boxer,log_text = DOWN['down_1'][dice_roll](red_boxer,log_text)
            # 2回の場合
            elif red_boxer.total_down_num == 2:
                # DOWN['down_2']のダイス出目に応じた関数を実行する
                red_boxer,log_text = DOWN['down_2'][dice_roll](red_boxer,log_text)
            # 3回の場合
            elif red_boxer.total_down_num == 3:
                # DOWN['down_3']のダイス出目に応じた関数を実行する
                red_boxer,log_text = DOWN['down_3'][dice_roll](red_boxer,log_text)
            # 4回以上の場合
            else:
                # DOWN['down_3_or_more']のダイス出目に応じた関数を実行する
                red_boxer,log_text = DOWN['down_4_or_more'][dice_roll](red_boxer,log_text)
    return blue_boxer,red_boxer,log_text

# 青コーナー強烈ダウン
def blue_strong_downed(DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW):
    # ラウンドあたりのダウン数に1加算
    blue_boxer.round_down_num += 1
    # 試合トータルでのダウン数に1加算
    blue_boxer.total_down_num += 1
    # 赤コーナーのステータスがS~SAAの場合
    if red_boxer.status >= 3 and red_boxer.status <= 5:
        # ステータスをSSに更新
        red_boxer.status = 6
    # AA以下の場合
    elif red_boxer.status <= 2:
        # ステータスをSに更新
        red_boxer.status = 3
    # 出力するテキスト
    print_text = '「{red_name}選手の{red_fav_blow}で{blue_name}選手がダウン！」\n「これは強烈なパンチがヒットしました！」\n「{blue_name}選手、大の字に倒れて動けません！」'.format(blue_name=blue_boxer.name,red_name=red_boxer.name,red_fav_blow=FAV_BLOW[red_boxer.fav_blow])
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # 入力を待つ
    input()
    blue_boxer,red_boxer,log_text = print_status(blue_boxer,red_boxer,log_text,STATUS)
    # 入力を待つ
    input()
    # 3ノックダウン制の場合
    if knockdown_type == 0:
        # 1ラウンドあたりのダウン数が3回以上になるか、試合トータルでのダウン数が5回以上でTKO
        if blue_boxer.round_down_num >= 3 or blue_boxer.total_down_num >= 5:
            blue_boxer,log_text = tko(blue_boxer,log_text)
        else:
            # 12面ダイス1個を振る
            dice_roll = sum(DICE.throw_dice())
            # 出力するテキスト
            print_text = '{}コーナー・ダイス：{}'.format(blue_boxer.corner,dice_roll)
            # テキストを出力
            print(print_text)
            # 入力を待つ
            input()
            # ログにテキストを追加
            log_text.append(print_text)
            # STRONG_DOWNのダイス出目に応じた関数を実行する
            blue_boxer,log_text = STRONG_DOWN[dice_roll](blue_boxer,log_text)
    # フリーノックダウン制の場合
    else:
        # 試合トータルでのダウン数が5回以上でTKO
        if blue_boxer.total_down_num >= 5:
            blue_boxer,log_text = tko(blue_boxer,log_text)
        else:
            # 12面ダイス1個を振る
            dice_roll = sum(DICE.throw_dice())
            # 出力するテキスト
            print_text = '{}コーナー・ダイス：{}'.format(blue_boxer.corner,dice_roll)
            # テキストを出力
            print(print_text)
            # 入力を待つ
            input()
            # ログにテキストを追加
            log_text.append(print_text)
            # STRONG_DOWNのダイス出目に応じた関数を実行する
            blue_boxer,log_text = STRONG_DOWN[dice_roll](blue_boxer,log_text)
    return blue_boxer,red_boxer,log_text

# 赤コーナー強烈ダウン
def red_strong_downed(DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW):
    # ラウンドあたりのダウン数に1加算
    red_boxer.round_down_num += 1
    # 試合トータルでのダウン数に1加算
    red_boxer.total_down_num += 1
    # 青コーナーのステータスがS~SAAの場合
    if blue_boxer.status >= 3 and blue_boxer.status <= 5:
        # ステータスをSSに更新
        blue_boxer.status = 6
    # AA以下の場合
    elif blue_boxer.status <= 2:
        # ステータスをSに更新
        blue_boxer.status = 3
    # 出力するテキスト
    print_text = '「{blue_name}選手の{blue_fav_blow}で{red_name}選手がダウン！」\n「これは強烈なパンチがヒットしました！」\n「{red_name}選手、大の字に倒れて動けません！」'.format(blue_name=blue_boxer.name,red_name=red_boxer.name,blue_fav_blow=FAV_BLOW[blue_boxer.fav_blow])
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # 入力を待つ
    input()
    blue_boxer,red_boxer,log_text = print_status(blue_boxer,red_boxer,log_text,STATUS)
    # 入力を待つ
    input()
    # 3ノックダウン制の場合
    if knockdown_type == 0:
        # 1ラウンドあたりのダウン数が3回以上になるか、試合トータルでのダウン数が5回以上でTKO
        if red_boxer.round_down_num >= 3 or red_boxer.total_down_num >= 5:
            red_boxer,log_text = tko(red_boxer,log_text)
        else:
            # 12面ダイス1個を振る
            dice_roll = sum(DICE.throw_dice())
            # 出力するテキスト
            print_text = '{}コーナー・ダイス：{}'.format(red_boxer.corner,dice_roll)
            # テキストを出力
            print(print_text)
            # ログにテキストを追加
            log_text.append(print_text)
            # 入力を待つ
            input()
            # STRONG_DOWNのダイス出目に応じた関数を実行する
            red_boxer,log_text = STRONG_DOWN[dice_roll](red_boxer,log_text)
    # フリーノックダウン制の場合
    else:
        # 試合トータルでのダウン数が5回以上でTKO
        if red_boxer.total_down_num >= 5:
            red_boxer,log_text = tko(red_boxer,log_text)
        else:
            # 12面ダイス1個を振る
            dice_roll = sum(DICE.throw_dice())
            # 出力するテキスト
            print_text = '{}コーナー・ダイス：{}'.format(red_boxer.corner,dice_roll)
            # テキストを出力
            print(print_text)
            # ログにテキストを追加
            log_text.append(print_text)
            # 入力を待つ
            input()
            # STRONG_DOWNのダイス出目に応じた関数を実行する
            red_boxer,log_text = STRONG_DOWN[dice_roll](red_boxer,log_text)
    return blue_boxer,red_boxer,log_text

# ダブルノックダウン
def double_knock_down(DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW):
    # ラウンドあたりのダウン数に1加算
    blue_boxer.round_down_num += 1
    # 試合トータルでのダウン数に1加算
    blue_boxer.total_down_num += 1
    # ラウンドあたりのダウン数に1加算
    red_boxer.round_down_num += 1
    # 試合トータルでのダウン数に1加算
    red_boxer.total_down_num += 1
    # 出力するテキスト
    print_text = '両者、ダブルノックダウン。'
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # 入力を待つ
    input()
    blue_boxer,red_boxer,log_text = print_status(blue_boxer,red_boxer,log_text,STATUS)
    # 3ノックダウン制の場合
    if knockdown_type == 0:
        # 青コーナーの1ラウンドあたりのダウン数が3回以上になるか、試合トータルでのダウン数が5回以上でTKO
        if blue_boxer.round_down_num >= 3 or blue_boxer.total_down_num >= 5:
            blue_boxer,log_text = tko(blue_boxer,log_text)
        # 赤コーナーの1ラウンドあたりのダウン数が3回以上になるか、試合トータルでのダウン数が5回以上でTKO
        elif red_boxer.round_down_num >= 3 or red_boxer.total_down_num >= 5:
            red_boxer,log_text = tko(red_boxer,log_text)
        else:
            # 青コーナー
            # 12面ダイス1個を振る
            dice_roll = sum(DICE.throw_dice())
            # 出力するテキスト
            print_text = '{}コーナー・ダイス：{}'.format(blue_boxer.corner,dice_roll)
            # テキストを出力
            print(print_text)
            # ログにテキストを追加
            log_text.append(print_text)
            # 入力を待つ
            input()
            # トータルでのダウン数が1回の場合
            if blue_boxer.total_down_num == 1:
                # DOWN['down_1']のダイス出目に応じた関数を実行する
                blue_boxer,log_text = DOWN['down_1'][dice_roll](blue_boxer,log_text)
            # 2回の場合
            elif blue_boxer.total_down_num == 2:
                # DOWN['down_2']のダイス出目に応じた関数を実行する
                blue_boxer,log_text = DOWN['down_2'][dice_roll](blue_boxer,log_text)
            # 3回以上の場合
            else:
                # DOWN['down_3_or_more']のダイス出目に応じた関数を実行する
                blue_boxer,log_text = DOWN['down_3_or_more'][dice_roll](blue_boxer,log_text)
            # 赤コーナー
            # 12面ダイス1個を振る
            dice_roll = sum(DICE.throw_dice())
            # 出力するテキスト
            print_text = '{}コーナー・ダイス：{}'.format(red_boxer.corner,dice_roll)
            # テキストを出力
            print(print_text)
            # ログにテキストを追加
            log_text.append(print_text)
            # 入力を待つ
            input()
            # トータルでのダウン数が1回の場合
            if red_boxer.total_down_num == 1:
                # DOWN['down_1']のダイス出目に応じた関数を実行する
                red_boxer,log_text = DOWN['down_1'][dice_roll](red_boxer,log_text)
            # 2回の場合
            elif red_boxer.total_down_num == 2:
                # DOWN['down_2']のダイス出目に応じた関数を実行する
                red_boxer,log_text = DOWN['down_2'][dice_roll](red_boxer,log_text)
            # 3回以上の場合
            else:
                # DOWN['down_3_or_more']のダイス出目に応じた関数を実行する
                red_boxer,log_text = DOWN['down_3_or_more'][dice_roll](red_boxer,log_text)
    # フリーノックダウン制の場合
    else:
        # 青コーナーの試合トータルでのダウン数が5回以上でTKO
        if blue_boxer.total_down_num >= 5:
            blue_boxer,log_text = tko(blue_boxer,log_text)
        # 赤コーナーの試合トータルでのダウン数が5回以上でTKO
        elif red_boxer.total_down_num >= 5:
            red_boxer,log_text = tko(red_boxer,log_text)
        else:
            # 青コーナー
            # 12面ダイス1個を振る
            dice_roll = sum(DICE.throw_dice())
            # 出力するテキスト
            print_text = '{}コーナー・ダイス：{}'.format(blue_boxer.corner,dice_roll)
            # テキストを出力
            print(print_text)
            # ログにテキストを追加
            log_text.append(print_text)
            # 入力を待つ
            input()
            # トータルでのダウン数が1回の場合
            if blue_boxer.total_down_num == 1:
                # DOWN['down_1']のダイス出目に応じた関数を実行する
                blue_boxer,log_text = DOWN['down_1'][dice_roll](blue_boxer,log_text)
            # 2回の場合
            elif blue_boxer.total_down_num == 2:
                # DOWN['down_2']のダイス出目に応じた関数を実行する
                blue_boxer,log_text = DOWN['down_2'][dice_roll](blue_boxer,log_text)
            # 3回以上の場合
            else:
                # DOWN['down_3_or_more']のダイス出目に応じた関数を実行する
                blue_boxer,log_text = DOWN['down_3_or_more'][dice_roll](blue_boxer,log_text)
            # 入力を待つ
            input()
            # 赤コーナー
            # 12面ダイス1個を振る
            dice_roll = sum(DICE.throw_dice())
            # 出力するテキスト
            print_text = '{}コーナー・ダイス：{}'.format(red_boxer.corner,dice_roll)
            # テキストを出力
            print(print_text)
            # ログにテキストを追加
            log_text.append(print_text)
            # 入力を待つ
            input()
            # トータルでのダウン数が1回の場合
            if red_boxer.total_down_num == 1:
                # DOWN['down_1']のダイス出目に応じた関数を実行する
                red_boxer,log_text = DOWN['down_1'][dice_roll](red_boxer,log_text)
            # 2回の場合
            elif red_boxer.total_down_num == 2:
                # DOWN['down_2']のダイス出目に応じた関数を実行する
                red_boxer,log_text = DOWN['down_2'][dice_roll](red_boxer,log_text)
            # 3回以上の場合
            else:
                # DOWN['down_3_or_more']のダイス出目に応じた関数を実行する
                red_boxer,log_text = DOWN['down_3_or_more'][dice_roll](red_boxer,log_text)
    return blue_boxer,red_boxer,log_text

# インターバル
def interval(blue_boxer,red_boxer,log_text):
    # 青コーナーのステータスが4（SA）以上の場合
    if blue_boxer.status >= 4:
        # 3（S）にする
        blue_boxer.status = 3
    # 青コーナーのステータスが0より上かつ3（S）以下の場合
    elif blue_boxer.status > 0 and blue_boxer.status <= 3:
        # 1段階下げる
        blue_boxer.status -= 1
    # 赤コーナーのステータスが4（SA）以上の場合
    if red_boxer.status >= 4:
        # 3（S）にする
        red_boxer.status = 3
    # 赤コーナーのステータスが0より上かつ3（S）以下の場合
    elif red_boxer.status > 0 and red_boxer.status <= 3:
        # 1段階下げる
        red_boxer.status -= 1
    # 出力するテキスト
    print_text = 'インターバルに入ります。'
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # 入力を待つ
    input()
    blue_boxer,red_boxer,log_text = print_status(blue_boxer,red_boxer,log_text,STATUS)
    # 入力を待つ
    input()
    return blue_boxer,red_boxer,log_text

# 採点
def scoring(blue_boxer,red_boxer,log_text):
    # 両者どちらかにダウンがあった場合
    if blue_boxer.round_down_num > 0 or red_boxer.round_down_num > 0:
        # 青0回赤1回の場合
        if blue_boxer.round_down_num == 0 and red_boxer.round_down_num == 1:
            # 青に10ポイント加算
            blue_point = 10
            # 赤に8ポイント加算
            red_point = 8
        # 青0回赤1回の場合
        elif blue_boxer.round_down_num == 1 and red_boxer.round_down_num == 0:
            # 青に8ポイント加算
            blue_point = 8
            # 赤に7ポイント加算
            red_point = 10
        # 青0回赤2回以上の場合
        elif blue_boxer.round_down_num == 0 and red_boxer.round_down_num >= 2:
            # 青に10ポイント加算
            blue_point = 10
            # 赤に7ポイント加算
            red_point = 7
        # 青2回以上赤0回の場合
        elif blue_boxer.round_down_num >= 2 and red_boxer.round_down_num == 0:
            # 青に7ポイント加算
            blue_point = 7
            # 赤に10ポイント加算
            red_point = 10
        # 青1回赤1回の場合
        elif blue_boxer.round_down_num == 1 and red_boxer.round_down_num == 1:
            # 青に8ポイント加算
            blue_point = 8
            # 赤に8ポイント加算
            red_point = 8
        # 青1回赤2回以上の場合
        elif blue_boxer.round_down_num == 1 and red_boxer.round_down_num >= 2:
            # 青に8ポイント加算
            blue_point = 8
            # 赤に7ポイント加算
            red_point = 7
        # 青2回以上赤1回の場合
        elif blue_boxer.round_down_num >= 2 and red_boxer.round_down_num == 1:
            # 青に7ポイント加算
            blue_point = 7
            # 赤に8ポイント加算
            red_point = 8
        # 青2回赤2回の場合
        elif blue_boxer.round_down_num == 2 and red_boxer.round_down_num == 2:
            # 青に8ポイント加算
            blue_point = 8
            # 赤に8ポイント加算
            red_point = 8
        # 青2回赤3回の場合
        elif blue_boxer.round_down_num == 2 and red_boxer.round_down_num == 3:
            # 青に7ポイント加算
            blue_point = 7
            # 赤に6ポイント加算
            red_point = 6
        # 青3回赤2回の場合
        elif blue_boxer.round_down_num == 3 and red_boxer.round_down_num == 2:
            # 青に6ポイント加算
            blue_point = 6
            # 赤に7ポイント加算
            red_point = 7
        # 青1回赤4回の場合
        elif blue_boxer.round_down_num == 1 and red_boxer.round_down_num == 4:
            # 青に10ポイント加算
            blue_point = 10
            # 赤に7ポイント加算
            red_point = 7
        # 青4回赤1回の場合
        elif blue_boxer.round_down_num == 4 and red_boxer.round_down_num == 1:
            # 青に7ポイント加算
            blue_point = 7
            # 赤に10ポイント加算
            red_point = 10
    # 両者ともにダウンしなかった場合
    else:
        # 青の優勢回数が赤の優勢回数より多かった場合
        if blue_boxer.attack_num > red_boxer.attack_num:
            # 青に10ポイント加算
            blue_point = 10
            # 赤に9ポイント加算
            red_point = 9
        # 赤の優勢回数が青の優勢回数より多かった場合
        elif blue_boxer.attack_num < red_boxer.attack_num:
            # 青に9ポイント加算
            blue_point = 9
            # 赤に10ポイント加算
            red_point = 10
        # 両者の優勢回数が同数だった場合
        else:
            # 青に10ポイント加算
            blue_point = 10
            # 赤に10ポイント加算
            red_point = 10
    # 両者にポイント加算
    blue_boxer.point += blue_point
    red_boxer.point += red_point
    # 出力するテキスト
    print_text = 'このラウンドの判定：\n{}コーナー：{}点：{}コーナー：{}点'.format(blue_boxer.corner,blue_point,red_boxer.corner,red_point)
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # 入力を待つ
    input()
    # 出力するテキスト
    print_text = '現在までのポイント：\n{}コーナー：{}点：{}コーナー：{}点'.format(blue_boxer.corner,blue_boxer.point,red_boxer.corner,red_boxer.point)
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # ラウンドでの優勢回数を0にリセット
    blue_boxer.attack_num = 0
    red_boxer.attack_num = 0
    # ラウンドでのダウン回数カウントを0にリセット
    blue_boxer.round_down_num = 0
    red_boxer.round_down_num = 0
    return blue_boxer,red_boxer,log_text

# KO
def ko(downed_boxer,log_text):
    # resultを'●'とする
    downed_boxer.result = '●'
    # conclusionを'KO'とする
    downed_boxer.conclusion = 'KO'
    # 出力するテキスト
    print_text = 'カーンカーンカーン！\n「{name}選手、立つことが出来ません！！　10カウントが数え上げられました！！」'.format(name=downed_boxer.name)
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    return downed_boxer,log_text

# TKO
def tko(downed_boxer,log_text):
    # resultを'●'とする
    downed_boxer.result = '●'
    # conclusionを'TKO'とする
    downed_boxer.conclusion = 'TKO'
    # 出力するテキスト
    print_text = 'カーンカーンカーン！\n「レフェリーが試合を止めました！　{name}選手、立ち上がれず！！」'.format(name=downed_boxer.name)
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    return downed_boxer,log_text

# カウント8で立つ
def standup_8(downed_boxer,log_text):
    # 出力するテキスト
    print_text = '「{name}選手、カウント8で立ち上がりました！　試合再開です！」'.format(name=downed_boxer.name)
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    return downed_boxer,log_text

# カウント9で立つ
def standup_9(downed_boxer,log_text):
    # 出力するテキスト
    print_text = '「{name}選手、カウント9で立ち上がりました！　試合再開です！」'.format(name=downed_boxer.name)
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    return downed_boxer,log_text

# ダイス対照表
DICE_TABLE = {
    'normal':{1:blue_superiority,2:blue_superiority,3:blue_superiority,4:blue_superiority,5:red_superiority,6:red_superiority,7:red_superiority,8:red_superiority,9:evenness,10:evenness,11:blue_downed,12:red_downed},
    'blue_A':{1:blue_superiority,2:blue_superiority,3:blue_superiority,4:blue_superiority,5:red_superiority,6:red_superiority,7:red_superiority,8:red_superiority,9:evenness,10:blue_downed,11:red_downed,12:red_downed},
    'blue_AA':{1:blue_superiority,2:blue_superiority,3:blue_superiority,4:red_superiority,5:red_superiority,6:red_superiority,7:clinch,8:draw,9:blue_downed,10:red_downed,11:red_downed,12:red_downed},
    'blue_A_red_A':{1:blue_superiority,2:blue_superiority,3:blue_superiority,4:blue_superiority,5:red_superiority,6:red_superiority,7:red_superiority,8:red_superiority,9:clinch,10:draw,11:blue_downed,12:red_downed},
    'blue_AA_red_A':{1:blue_superiority,2:blue_superiority,3:blue_superiority,4:red_superiority,5:red_superiority,6:red_superiority,7:evenness,8:clinch,9:draw,10:blue_downed,11:red_downed,12:red_downed},
    'blue_A_red_AA':{1:blue_superiority,2:blue_superiority,3:blue_superiority,4:red_superiority,5:red_superiority,6:red_superiority,7:evenness,8:clinch,9:draw,10:blue_downed,11:blue_downed,12:red_downed},
    'blue_AA_red_AA':{1:blue_superiority,2:blue_superiority,3:red_superiority,4:red_superiority,5:blue_counter,6:red_counter,7:clinch,8:draw,9:blue_downed,10:blue_downed,11:red_downed,12:red_downed},
    'red_A':{1:blue_superiority,2:blue_superiority,3:blue_superiority,4:blue_superiority,5:red_superiority,6:red_superiority,7:red_superiority,8:red_superiority,9:evenness,10:blue_downed,11:blue_downed,12:red_downed},
    'red_AA':{1:blue_superiority,2:blue_superiority,3:blue_superiority,4:red_superiority,5:red_superiority,6:red_superiority,7:clinch,8:draw,9:blue_downed,10:blue_downed,11:blue_downed,12:red_downed},
    'blue_S':{1:blue_superiority,2:blue_superiority,3:red_superiority,4:red_superiority,5:red_counter,6:clinch,7:clinch,8:draw,9:blue_downed,10:red_downed,11:red_downed,12:red_strong_downed},
    'blue_SS':{1:blue_superiority,2:blue_superiority,3:red_superiority,4:red_superiority,5:red_counter,6:clinch,7:draw,8:blue_downed,9:blue_downed,10:red_strong_downed,11:red_strong_downed,12:red_strong_downed},
    'blue_S_red_S':{1:blue_superiority,2:blue_superiority,3:red_superiority,4:red_superiority,5:blue_counter,6:red_counter,7:clinch,8:draw,9:blue_downed,10:blue_strong_downed,11:red_downed,12:red_strong_downed},
    'blue_SS_red_S':{1:blue_superiority,2:blue_superiority,3:red_superiority,4:red_superiority,5:blue_counter,6:red_counter,7:clinch,8:double_knock_down,9:blue_downed,10:blue_downed,11:red_strong_downed,12:red_strong_downed},
    'red_S':{1:blue_superiority,2:blue_superiority,3:red_superiority,4:red_superiority,5:blue_counter,6:clinch,7:clinch,8:draw,9:blue_downed,10:blue_downed,11:blue_strong_downed,12:red_downed},
    'red_SS':{1:blue_superiority,2:blue_superiority,3:red_superiority,4:red_superiority,5:blue_counter,6:clinch,7:draw,8:blue_strong_downed,9:blue_strong_downed,10:blue_strong_downed,11:red_downed,12:red_downed},
    'blue_S_red_SS':{1:blue_superiority,2:blue_superiority,3:red_superiority,4:red_superiority,5:blue_counter,6:red_counter,7:clinch,8:double_knock_down,9:blue_strong_downed,10:blue_strong_downed,11:red_downed,12:red_downed},
    'blue_SS_red_SS':{1:blue_superiority,2:blue_superiority,3:red_superiority,4:red_superiority,5:blue_counter,6:red_counter,7:clinch,8:double_knock_down,9:blue_strong_downed,10:blue_strong_downed,11:red_strong_downed,12:red_strong_downed},
}

# 選手の状態
STATUS = {0:'ノーマル',1:'A',2:'AA',3:'S',4:'SA',5:'SAA',6:'SS'}

# ダウン時ダイス
DOWN = {
    'down_1':{1:ko,2:ko,3:standup_8,4:standup_8,5:standup_8,6:standup_8,7:standup_8,8:standup_8,9:standup_8,10:standup_8,11:standup_9,12:standup_9},
    'down_2':{1:ko,2:ko,3:tko,4:standup_8,5:standup_8,6:standup_8,7:standup_8,8:standup_8,9:standup_9,10:standup_9,11:standup_9,12:standup_9},
    'down_3':{1:ko,2:ko,3:ko,4:tko,5:standup_8,6:standup_8,7:standup_8,8:standup_8,9:standup_9,10:standup_9,11:standup_9,12:standup_9},
    'down_4_or_more':{1:ko,2:ko,3:ko,4:tko,5:tko,6:standup_8,7:standup_8,8:standup_8,9:standup_9,10:standup_9,11:standup_9,12:standup_9}
}

# 強烈ダウン時ダイス
STRONG_DOWN = {1:ko,2:ko,3:ko,4:tko,5:tko,6:standup_9,7:standup_9,8:standup_9,9:standup_9,10:standup_9,11:standup_9,12:standup_9}

# ノックダウン方式
KNOCKDOWN_TYPE = {0:'3ノックダウン',1:'フリーノックダウン'}

FAV_BLOW = ['ストレート','フック','ボディブロー','アッパーカット']

# ダイス（12面ダイス1個）作成
DICE = Dice(1,12)

# ボクサー作成関数
def make_boxer(FAV_BLOW,corner):
    name = input('{}コーナーのボクサーを作成します。名前を入力してください:'.format(corner))
    while True:
        try:
            fav_blow = int(input('得意ブローを次の中から選択してください。\n0:{}\n1:{}\n2:{}\n3:{}:'.format(FAV_BLOW[0],FAV_BLOW[1],FAV_BLOW[2],FAV_BLOW[3])))
        except ValueError:
            print("数字を入力してください。")
        else:
            if fav_blow < 0 or fav_blow > 3:
                print('0から3で選択してください。')
            else:
                boxer = Boxer(corner,name,fav_blow)
                print('得意ブロー：{}'.format(FAV_BLOW[fav_blow]))
                return boxer

# ノックダウン方式決定関数
def decide_knockdown_type(KNOCKDOWN_TYPE):
    while True:
        try:
            knockdown_type = int(input('ノックダウン方式を決定してください。\n0:{}\n1:{}:'.format(KNOCKDOWN_TYPE[0],KNOCKDOWN_TYPE[1])))
        except ValueError:
            print("数字を入力してください。")
        else:
            if knockdown_type < 0 or knockdown_type > 1:
                print('0か1で選択してください。')
            elif knockdown_type == 0:
                print(KNOCKDOWN_TYPE[0])
                return knockdown_type
            else:
                print(KNOCKDOWN_TYPE[1])
                return knockdown_type

# ラウンド数決定関数
def decide_round_num():
    while True:
        try:
            round_num = int(input('ラウンド数を決定してください。\n4ラウンド\n6ラウンド\n8ラウンド\n10ラウンド\n12ラウンド:'))
        except ValueError:
            print("数字を入力してください。")
        else:
            if round_num != 4 and round_num != 6 and round_num != 8 and round_num != 10 and round_num != 12:
                print('4、6、8、10、12のいずれかの数字を入力してください')
            else:
                print('{}ラウンド'.format(round_num))
                return round_num

# 試合関数
def match(DICE,DICE_TABLE,FAV_BLOW,STATUS,DOWN,STRONG_DOWN,KNOCKDOWN_TYPE,knockdown_type,round_num,FIGHT_LOG_DIR,blue_boxer,red_boxer):
    # 開始時刻
    fight_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    # ログファイル名
    file_name = '{}/{}_{}_vs_{}.txt'.format(FIGHT_LOG_DIR,fight_datetime,blue_boxer.name,red_boxer.name)
    # 試合ログを格納するリスト
    log_text = []
    # 試合のラウンド数
    max_round = round_num
    # 現在のラウンド
    current_round = 1
    # 現在のターン
    current_turn = 1
    # 出力するテキスト
    print_text = '女子ボクシング{}回戦試合\n{}方式\n{}コーナー：{} VS {}コーナー：{}'.format(round_num,KNOCKDOWN_TYPE[knockdown_type],blue_boxer.corner,blue_boxer.name,red_boxer.corner,red_boxer.name)
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # 入力を待つ
    input()
    # 出力するテキスト
    print_text = '試合開始！'
    # テキストを出力
    print(print_text)
    # ログにテキストを追加
    log_text.append(print_text)
    # ログに空白行を追加
    log_text.append('')
    # 現在のラウンドが最大ラウンド以下かつ両者のresultが空白の間ループ
    while current_round <= max_round and red_boxer.result == '' and blue_boxer.result == '':
        # 入力を待つ
        input()
        # 出力するテキスト
        print_text = '第{}ラウンド{}ターン'.format(current_round,current_turn)
        # テキストを出力
        print(print_text)
        # ログにテキストを追加
        log_text.append(print_text)
        # 入力を待つ
        input()
        # 12面ダイス1個を振る
        dice_roll = sum(DICE.throw_dice())
        # 出力するテキスト
        print_text = 'ダイス：{}'.format(dice_roll)
        # テキストを出力
        print(print_text)
        # ログにテキストを追加
        log_text.append(print_text)
        # 入力を待つ
        input()
        if blue_boxer.status == 0 and red_boxer.status == 0:
            blue_boxer,red_boxer,log_text = DICE_TABLE['normal'][dice_roll](DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW)
        elif blue_boxer.status == 1 and red_boxer.status == 0:
            blue_boxer,red_boxer,log_text = DICE_TABLE['blue_A'][dice_roll](DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW)
        elif blue_boxer.status == 2 and red_boxer.status == 0:
            blue_boxer,red_boxer,log_text = DICE_TABLE['blue_AA'][dice_roll](DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW)
        elif blue_boxer.status == 1 and red_boxer.status == 1:
            blue_boxer,red_boxer,log_text = DICE_TABLE['blue_A_red_A'][dice_roll](DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW)
        elif blue_boxer.status == 2 and red_boxer.status == 1:
            blue_boxer,red_boxer,log_text = DICE_TABLE['blue_AA_red_A'][dice_roll](DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW)
        elif blue_boxer.status == 1 and red_boxer.status == 2:
            blue_boxer,red_boxer,log_text = DICE_TABLE['blue_A_red_AA'][dice_roll](DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW)
        elif blue_boxer.status == 2 and red_boxer.status == 2:
            blue_boxer,red_boxer,log_text = DICE_TABLE['blue_AA_red_AA'][dice_roll](DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW)
        elif blue_boxer.status == 0 and red_boxer.status == 1:
            blue_boxer,red_boxer,log_text = DICE_TABLE['red_A'][dice_roll](DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW)
        elif blue_boxer.status == 0 and red_boxer.status == 2:
            blue_boxer,red_boxer,log_text = DICE_TABLE['red_AA'][dice_roll](DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW)
        elif (blue_boxer.status >= 3 and blue_boxer.status <= 5) and red_boxer.status <= 2:
            blue_boxer,red_boxer,log_text = DICE_TABLE['blue_S'][dice_roll](DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW)
        elif blue_boxer.status == 6 and red_boxer.status <= 2:
            blue_boxer,red_boxer,log_text = DICE_TABLE['blue_SS'][dice_roll](DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW)
        elif (blue_boxer.status >= 3 and blue_boxer.status <= 5) and (red_boxer.status >= 3 and red_boxer.status <= 5):
            blue_boxer,red_boxer,log_text = DICE_TABLE['blue_S_red_S'][dice_roll](DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW)
        elif blue_boxer.status == 6 and (red_boxer.status >= 3 and red_boxer.status <= 5):
            blue_boxer,red_boxer,log_text = DICE_TABLE['blue_SS_red_S'][dice_roll](DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW)
        elif blue_boxer.status <= 2 and (red_boxer.status >= 3 and red_boxer.status <= 5):
            blue_boxer,red_boxer,log_text = DICE_TABLE['red_S'][dice_roll](DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW)
        elif blue_boxer.status <= 2 and red_boxer.status == 6:
            blue_boxer,red_boxer,log_text = DICE_TABLE['red_SS'][dice_roll](DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW)
        elif (blue_boxer.status >= 3 and blue_boxer.status <= 5) and red_boxer.status == 6:
            blue_boxer,red_boxer,log_text = DICE_TABLE['blue_S_red_SS'][dice_roll](DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW)
        elif blue_boxer.status == 6 and red_boxer.status == 6:
            blue_boxer,red_boxer,log_text = DICE_TABLE['blue_SS_red_SS'][dice_roll](DICE,knockdown_type,blue_boxer,red_boxer,log_text,STATUS,DOWN,STRONG_DOWN,FAV_BLOW)
        # 入力を待つ
        input()
        if blue_boxer.result == '●' and red_boxer.result == '●':
            # 出力するテキスト
            print_text = '両者、WKOで引き分け。'
            # テキストを出力
            print(print_text)
            # ログにテキストを追加
            log_text.append(print_text)
            # 入力を待つ
            input()
            # 出力するテキスト
            print_text = '{}コーナー：{} {}ラウンド{}ターン 引き分け（WKO） {}コーナー：{}'.format(blue_boxer.corner,blue_boxer.name,current_round,current_turn,red_boxer.corner,red_boxer.name)
            # テキストを出力
            print(print_text)
            # ログにテキストを追加
            log_text.append(print_text)
            # 入力を待つ
            input()
            # ログファイル出力
            export_log(log_text,file_name)
            return
        elif blue_boxer.result == '●':
            # 赤のresultを'〇'にする
            red_boxer.result = '〇'
            # 出力するテキスト
            print_text = '「{name}選手の{conclusion}勝利です！！」'.format(name=red_boxer.name,conclusion=blue_boxer.conclusion)
            # テキストを出力
            print(print_text)
            # ログにテキストを追加
            log_text.append(print_text)
            # 入力を待つ
            input()
            # 出力するテキスト
            print_text = '{}{}コーナー：{} {}ラウンド{}ターン {} {}コーナー：{}{}'.format(blue_boxer.result,blue_boxer.corner,blue_boxer.name,current_round,current_turn,blue_boxer.conclusion,red_boxer.corner,red_boxer.name,red_boxer.result)
            # テキストを出力
            print(print_text)
            # ログにテキストを追加
            log_text.append(print_text)
            # 入力を待つ
            input()
            # ログファイル出力
            export_log(log_text,file_name)
            return
        elif red_boxer.result == '●':
            # 青のresultを'〇'にする
            blue_boxer.result = '〇'
            # 出力するテキスト
            print_text = '「{name}選手の{conclusion}勝利です！！」'.format(name=blue_boxer.name,conclusion=red_boxer.conclusion)
            # テキストを出力
            print(print_text)
            # ログにテキストを追加
            log_text.append(print_text)
            # 入力を待つ
            input()
            # 出力するテキスト
            print_text = '{}{}コーナー：{} {}ラウンド{}ターン {} {}コーナー：{}{}'.format(blue_boxer.result,blue_boxer.corner,blue_boxer.name,current_round,current_turn,red_boxer.conclusion,red_boxer.corner,red_boxer.name,red_boxer.result)
            # テキストを出力
            print(print_text)
            # ログにテキストを追加
            log_text.append(print_text)
            # 入力を待つ
            input()
            # ログファイル出力
            export_log(log_text,file_name)
            return
        if current_turn == 5:
            # ログに空白行を追加
            log_text.append('')
            # 出力するテキスト
            print_text = '{}ラウンド終了。'.format(current_round)
            # テキストを出力
            print(print_text)
            # ログにテキストを追加
            log_text.append(print_text)
            # 現在のターンを1にリセット
            current_turn = 1
            # 現在のラウンドに1加算
            current_round += 1
            # 入力を待つ
            input()
            # 現在のラウンドが最大ラウンド数を超えた場合
            if current_round > max_round:
                # 採点
                blue_boxer,red_boxer,log_text = scoring(blue_boxer,red_boxer,log_text)
                # 出力するテキスト
                print_text = '「最終ラウンド終了となりました。これより判定に入ります」'
                # テキストを出力
                print(print_text)
                # ログにテキストを追加
                log_text.append(print_text)
                # 入力を待つ
                input()
                # 青のポイントが赤のポイントを上回った場合
                if blue_boxer.point > red_boxer.point:
                    # 青のresultを'〇'にする
                    blue_boxer.result = '〇'
                    # 赤のresultを'●'にする
                    red_boxer.result = '●'
                    # 赤のconclusionを'判定'にする
                    red_boxer.conclusion = '判定'
                    # 出力するテキスト
                    print_text = '{}コーナー・{}選手の判定勝利です！！'.format(blue_boxer.corner,blue_boxer.name)
                    # テキストを出力
                    print(print_text)
                    # ログにテキストを追加
                    log_text.append(print_text)
                    # 入力を待つ
                    input()
                    # 出力するテキスト
                    print_text = '{}{}コーナー：{} {} {}コーナー：{}{}'.format(blue_boxer.result,blue_boxer.corner,blue_boxer.name,red_boxer.conclusion,red_boxer.corner,red_boxer.name,red_boxer.result)
                    # テキストを出力
                    print(print_text)
                    # ログにテキストを追加
                    log_text.append(print_text)
                    # 入力を待つ
                    input()
                    # ログファイル出力
                    export_log(log_text,file_name)
                    return
                # 赤のポイントが青のポイントを上回った場合
                elif blue_boxer.point < red_boxer.point:
                    # 青のresultを'●'にする
                    blue_boxer.result = '●'
                    # 赤のresultを'〇'にする
                    red_boxer.result = '〇'
                    # 青のconclusionを'判定'にする
                    blue_boxer.conclusion = '判定'
                    # 出力するテキスト
                    print_text = '{}コーナー・{}選手の判定勝利です！！'.format(red_boxer.corner,red_boxer.name)
                    # テキストを出力
                    print(print_text)
                    # ログにテキストを追加
                    log_text.append(print_text)
                    # 入力を待つ
                    input()
                    # 出力するテキスト
                    print_text = '{}{}コーナー：{} {} {}コーナー：{}{}'.format(blue_boxer.result,blue_boxer.corner,blue_boxer.name,blue_boxer.conclusion,red_boxer.corner,red_boxer.name,red_boxer.result)
                    # テキストを出力
                    print(print_text)
                    # ログにテキストを追加
                    log_text.append(print_text)
                    # 入力を待つ
                    input()
                    # ログファイル出力
                    export_log(log_text,file_name)
                    return
                # 両者のポイントが同点だった場合
                else:
                    # 出力するテキスト
                    print_text = '{}コーナー：{}：{}ポイント\n{}コーナー：{}：{}ポイント'.format(blue_boxer.corner,blue_boxer.name,blue_boxer.point,red_boxer.corner,red_boxer.name,red_boxer.point)
                    # テキストを出力
                    print(print_text)
                    # ログにテキストを追加
                    log_text.append(print_text)
                    # 入力を待つ
                    input()
                    # 出力するテキスト
                    print_text = '判定により引き分け。'
                    # テキストを出力
                    print(print_text)
                    # ログにテキストを追加
                    log_text.append(print_text)
                    # 入力を待つ
                    input()
                    # 出力するテキスト
                    print_text = '{}コーナー：{} 引き分け（判定） {}コーナー：{}'.format(blue_boxer.corner,blue_boxer.name,red_boxer.corner,red_boxer.name)
                    # テキストを出力
                    print(print_text)
                    # ログにテキストを追加
                    log_text.append(print_text)
                    # 入力を待つ
                    input()
                    # ログファイル出力
                    export_log(log_text,file_name)
                    return
            # まだ最大ラウンド数を超えていない場合
            else:
                # インターバル
                blue_boxer,red_boxer,log_text = interval(blue_boxer,red_boxer,log_text)
                # 採点
                blue_boxer,red_boxer,log_text = scoring(blue_boxer,red_boxer,log_text)
                # ログに空白行を追加
                log_text.append('')
        # 5ターン目未満の場合
        else:
            # ログに空白行を追加
            log_text.append('')
            # 現在のターンに1加算
            current_turn += 1

# メイン関数
def main(DICE,DICE_TABLE,FAV_BLOW,STATUS,DOWN,STRONG_DOWN,KNOCKDOWN_TYPE):
    FIGHT_LOG_DIR = make_folder()
    while True:
        blue_boxer = make_boxer(FAV_BLOW,'青')
        red_boxer = make_boxer(FAV_BLOW,'赤')
        knockdown_type = decide_knockdown_type(KNOCKDOWN_TYPE)
        round_num = decide_round_num()
        match(DICE,DICE_TABLE,FAV_BLOW,STATUS,DOWN,STRONG_DOWN,KNOCKDOWN_TYPE,knockdown_type,round_num,FIGHT_LOG_DIR,blue_boxer,red_boxer)
        continue_or_exit = input("もう1試合やりますか？　続ける場合「q」以外のキーを、終了する場合「q」を入力してください。:")
        if continue_or_exit == 'q' or continue_or_exit == 'ｑ':
            break

if __name__ == '__main__':
    main(DICE,DICE_TABLE,FAV_BLOW,STATUS,DOWN,STRONG_DOWN,KNOCKDOWN_TYPE)