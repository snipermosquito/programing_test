# Programming Test 

programming language:Python3.8<br />
フォルダ内に各設問に対応するプログラム(A1.py, A2.py, A3.py, A4.py)及び、読み込み対象とする監視ログファイル(log.txt)を置いて実行する. <br />

## Q1. 故障状態のサーバアドレスとそのサーバの故障期間を出力

　フォルダ内にlog.txtを設置した状態でA1.pyを実行する.結果は標準出力に表示される.<br />
　Example: python A1.py <br />
　なお、結果を別ファイルに書き出したい場合はコマンドライン引数としてファイル名を渡すことが可能である. <br />
　Example: python A1.py A1.out <br />
　上の例では A1.out に結果が書き出される.

### 出力について
　故障したサーバ{server address}について、タイムアウトの検出が開始した日時を{date&time1}、次に応答が確認された日時を{date&time2}として、 <br />
 「{server address}: out of order from {date&time1} until {date&time2}.」 <br />
 の形式で出力される. ただし、タイムアウト後に実行時点までで応答が確認されていない場合、until以下は表示されない.

## Q2. 故障の判定条件を追加
　フォルダ内にlog.txtを設置した状態でA2.pyを実行する. 故障判定に用いる回数 N はsysモジュールのargvを用いてコマンドライン引数として、「python A2.py N」の形で渡す. <br />
　Example: python A2.py 2 <br />
　上の例の場合、N = 2となる. なお、A1.pyと同様にファイル名を渡すことで結果の書き出しが可能である. <br />
　Example: python A2.py 2 A2.out <br />
　上の例では A2.out に結果が書き出される.
### 出力について
　N 回以上連続でタイムアウトが検出された場合を故障とみなし、故障したサーバ{server address}について、タイムアウトの検出が開始した日時を{date&time1}、次に応答が確認された日時を{date&time2}として、 <br />
 「{server address}: out of order from {date&time1} until {date&time2}.」 <br />
 の形式で出力される. ただし、タイムアウト後に実行時点までで応答が確認されていない場合、until以下は表示されない.
  
## Q3. 各サーバの過負荷状態となっている期間を追加で出力
　フォルダ内にlog.txtを設置した状態でA3.pyを実行する. Q2と同様の故障判定回数 N に加え、過負荷状態判定に用いる回数 m 及び平均応答時間 t をsysモジュールのargvを用いてコマンドライン引数として、「python A3.py N m t」の形で渡す. <br />
　Example: python A3.py 2 3 100 <br />
　上の例の場合、N = 2、m = 3、t = 100となる. また、ファイル名を渡すことで結果の書き出しが可能である. <br />
　Example: python A3.py 2 3 100 A3.out <br />
　上の例では A3.out に結果が書き出される.
### 出力について
  初めにサーバの故障についての確認結果が [timeout] の表示に続いてA2.pyの場合と同様に出力される. <br />
　次に過負荷状態の期間が [overload] の表示に続いて出力される. 直近 m 回の平均応答時間が t ミリ秒を超えた場合を過負荷状態とみなし、過負荷状態のサーバ【server address】について、過負荷状態が検出された時から数えて m-1 回前の確認日時を{date&time1}、過負荷状態の解消が確認された日時を{date&time2}として、 <br /> <br />
 「{server address}: under heavy load from {date&time1} until {date&time2}.」 <br /> <br />
 の形式で出力される. ただし、実行時点で過負荷状態の解消が確認されていない場合、until以下は表示されない. <br />
  
## Q4. サブネットの故障期間を追加で出力
　フォルダ内にlog.txtを設置した状態でA4.pyを実行する. Q3と同様に故障判定回数 N 、過負荷状態判定に用いる回数 m 及び平均応答時間 t をsysモジュールのargvを用いてコマンドライン引数として、「python A4.py N m t」の形で渡す. <br/>　
　Example: python A4.py 2 3 100 <br />
　ファイル名を渡すことで結果の書き出しが可能である. <br />
　Example: python A4.py 2 3 100 A4.out <br />
　上の例では A4.out に結果が書き出される.
### 出力について
  A3.pyと同様、初めにサーバーの故障についての確認結果が [timeout] の表示に続いて出力された後、過負荷状態の期間が [overload] の表示に続いて出力される. <br />
　次に [subnet malfunction] の表示に続いてサブネットの故障期間が出力される. サブネット {sub net} 内のサーバ全てについて N 回以上連続でのタイムアウトが確認されたとき、サブネット内の各サーバのタイムアウト開始日時の中で最も遅かったものを{date&time1}、サブネット内のいずれかのサーバで次に応答が確認された日時を{date&time2}として、 <br />
 「{sub net}: faulty subnet from {date&time1} until {date&time2}.」 <br />
 の形式で出力される. ただし、実行時点でいずれのサーバからも応答が確認されていない場合、until以下は表示されない. <br />
