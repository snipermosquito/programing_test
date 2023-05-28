# Fixpoint Co., Ltd.  programming test 

programming language:Python3.8<br />
フォルダ内に各設問に対応するプログラム(A1.py, A2.py, A3.py, A4.py)及び、読み込み対象とする監視ログファイル(log.txt)を置いて実行する. <br />

## Q1. 故障状態のサーバアドレスとそのサーバの故障期間を出力

　フォルダ内にlog.txtを設置した状態でA1.pyを実行する.<br />
　Example: python A1.py

### 出力について
　結果は「<server address>: out of order from <date&time> until <date&time>.」の形式で出力される.

## Q2. N回以上連続してタイムアウトした場合にのみ故障とみなすように変更
　フォルダ内にlog.txtを設置した状態でA2.pyを実行する. 故障判定に用いる回数 N はsysモジュールのargvを用いてコマンドライン引数として、「python A2.py N」の形で渡す.<br />
  Example: python A2.py 2 <br />
　上の例の場合、N = 2となる。
 
## Q3. 直近m回の平均応答時間がtミリ秒を超えた場合を過負荷状態とみなし、各サーバの過負荷状態となっている期間を追加で出力
　フォルダ内にlog.txtを設置した状態でA3.pyを実行する. Q2と同様の故障判定回数 N に加え、過負荷状態判定に用いる回数 m 及び平均応答時間 t をsysモジュールのargvを用いてコマンドライン引数として、「python A3.py N m t」の形で渡す.<br />
 　Example: python A3.py 2 3 100 <br />
　上の例の場合、N = 2、m = 3、t = 100となる.
 
## Q4. サブネットの故障期間を追加で出力
　フォルダ内にlog.txtを設置した状態でA4.pyを実行する. Q3と同様に故障判定回数 N 、過負荷状態判定に用いる回数 m 及び平均応答時間 t をsysモジュールのargvを用いてコマンドライン引数として、「python A4.py N m t」の形で渡す.<br/>　
