# FV-1 Reverb Effects Developer Kit
 [Spin Semiconductor FV-1](https://spinsemi.com/products.html)を用いたエフェクタの製作例<BR>
 ・BOXタイプ<BR>
 <img src="img/BOX/Assembly_Complete2.jpg" width="600"><BR>

 ・バーコーダー内蔵タイプ<BR>
 <img src="img/Barcoder/Barcoder2.jpg" width="600"><BR>

## 参考サイト
| リンク |備考 |
|:---|:---|
|[REVERBS/EFFECTS　日本語説明書](https://home-bake-instruments.localinfo.jp/posts/37592163/)|開発方法、EEPROM書き込み|
|[Getting Started with the FV-1](https://electric-canary.com/fv1start.html)|FV-1概要　|
|[2400円で作る高品質DSPマルチエフェクター](https://note.com/solder_state/n/n1c402a78a0fe) |Arduinoからプログラム変更、POT設定　|
|[FV-1を使った自作エフェクタ](http://studio-do.org/mini-effector/mini_effector_web01.html)|ロータリースイッチ、インテルHEXフォーマット|
|[アコギ用空間系エフェクター　FV-1](https://ameblo.jp/gustywind/entry-12778592028.html)|　|
|[Spin Semiconductor FV-1でエフェクターを自作する](https://marksard.github.io/2023/08/14/pocketeffector/)|　|
|[ASICチップ FV-1を使ったエフェクターの自作](http://dubelectro.seesaa.net/article/399349842.html)|　|

## 部品
- BOXタイプ・バーコーダー内蔵　共通

|        | リンク | 数量 | 備考 |
|:------|:---|:---:|:---|
|FV-1 DIP化モジュールキット|[FV-1](https://akizukidenshi.com/catalog/g/g115566/)| 1 |キットの方がIC単体より安い |
|低電圧動作パワーアンプ|[NJM2113D](https://akizukidenshi.com/catalog/g/g111192/)| 1 |DryWetのMix用 |
|I2C シリアルEEPROM|[24FC64-I/P](https://akizukidenshi.com/catalog/g/g103567/)| 1 |外部エフェクト保存用|
|ICソケット|[8P](https://akizukidenshi.com/catalog/g/g100017/)| 1 |EEPROM書込時クリップ使用なら不要 |
|基板取付用2連ボリューム|[B10kΩ](https://akizukidenshi.com/catalog/g/g112576/)| 4 |MIX用に2連、その他は１連でも可 |
|DIPロータリースイッチ|[16ポジション 0~F 負論理](https://akizukidenshi.com/catalog/g/g102277/)| 1 |負論理だと番号合わせやすい |
|半固定ボリューム|[GF063P 20kΩ](https://akizukidenshi.com/catalog/g/g114906/)| 2 |入力・出力ゲイン調整用 |
|小型 金属皮膜抵抗|[1/4W10kΩ](https://akizukidenshi.com/catalog/g/g108550/)| 4 | |
|チップ積層セラミックコンデンサー|[0.1μF50V](https://akizukidenshi.com/catalog/g/g111384/)| 3 | |
|片面丸型ユニバーサル基板|[20mm](https://akizukidenshi.com/catalog/g/g108753/)  | 1 | |
|ポテンショメータコントロールノブ|[D形](https://www.amazon.co.jp/dp/B084JC6CRS)| 3 |好みで 必ずD型を|
|ポテンショメータコントロールノブ|[D形](https://www.amazon.co.jp/dp/B0CW5WQ7RC) | 1 |好みで 必ずD型を|
|プラスチックスペーサー|[3-5](https://akizukidenshi.com/catalog/g/g115212/)| 2 | |
|5mmLED用ワンタッチブラケット|[LED5-16S](https://akizukidenshi.com/catalog/g/g111465/)| 1 | |
|抵抗内蔵5mmLED|[赤色 640nm](https://akizukidenshi.com/catalog/g/g106245/)| 1 | |
|超低頭小ねじ|M3×12mm| 2 |　|
|ナット|M3| 2 |　|
|EEPROMライター|[CH341A ROMライター](https://www.amazon.co.jp/dp/B07LGNTJ29)|  |クリップ付きなどもあり、Arduinoで書き込みも可|
<BR>
- BOXタイプ用

|        | リンク | 数量 | 備考 |
|:------|:---|:---:|:---|
|プラスチックケース|[SW-100B](https://www.amazon.co.jp/dp/B07BD5JGDB)| 1 | |
|3.5mmステレオミニジャック|[MJ-355W](https://akizukidenshi.com/catalog/g/g113305/)  | 2 | |
|オーディオ用電解コンデンサー|[1μF50V85℃ ニチコンFG](https://akizukidenshi.com/catalog/g/g104620/)| 8 | |
|3.3Vレギュレータモジュール|[AMS1117-3.3](https://www.amazon.co.jp/dp/B086WWGVCL)| 1 | |
|ボリューム配線用基板|[2連](https://www.findtec.jp/c-item-detail?ic=1001282)| 4 |なくても可|
|プラスチックスペーサー|[3-5](https://akizukidenshi.com/catalog/g/g115212/)| 4 | |
|さら小ねじ|M3×15mm| 4 | |
|ナット|M3| 2 |　|
<BR>
- バーコーダー内蔵用

|        | リンク | 数量 | 備考 |
|:------|:---|:---:|:---|
|バーコードリーダー|[BEVA](https://www.amazon.co.jp/dp/B077GRDQGP?th=1)| 1 | |
|チップ積層セラミックコンデンサー|[1μF50V X7R](https://akizukidenshi.com/catalog/g/g113699/)| 8 | |
|バーコーダー用アンプ基板|[HowToMakeBarcoder](https://github.com/hide63414/HowToMakeBarcoder)|1 | |
<BR>

## 回路図
VR1:入力レベル設定 FV-1のピークインジケータ点灯しないレベルにする<BR>
VR2:DRY-WETの割合設定<BR>
VR3:出力レベル設定<BR>

<details><summary>回路図</summary>
<img src="img/schematic.png">
</details>

## BOX内蔵タイプ作製例
完成品<BR>
<img src="img/BOX/Assembly_Complete2.jpg" width="600"><BR>
<details><summary>組み立て手順</summary>

1. FV-1用基板<BR>
上:部品面<BR>
下:半田面（C1,C9,C11の面実装コンデンサはこちらの面に実装）<BR>
<img src="img/PCB.jpg" width="600"><BR>

1. 部品実装<BR>
電解コンデンサは極性に注意<BR>
<img src="img/BOX/After_Mounting.jpg" width="600"><BR>
3.3V供給するためレギュレータを周囲のパッドを利用して取り付ける<BR>
<img src="img/BOX/3VRegulator.jpg" width="600"><BR>

1. 部品と配線接続<BR>
電源、可変抵抗、ロータリースイッチ、ステレオミニジャックを基板に接続する<BR>
<img src="img/BOX/Wiring_Complete.jpg" width="600"><BR>
J1:レギュレータのGNDと3.3V出力の接続<BR>
<img src="img/BOX/POWER_Wiring.jpg" width="600"><BR>
J2,J6:IN,OUTのステレオミニジャックとの接続 □がGND<BR>
<img src="img/BOX/IN-OUT_Wiring.jpg" width="600"><BR>
J3:可変抵抗(POT0-2)との接続　それぞれ3.3VとGNDもつなぐ<BR>
<img src="img/BOX/POT_Wiring.jpg" width="600"><BR>
　それぞれ3.3VとGNDもつなぐ<BR>
<img src="img/BOX/POT0-2.jpg" width="600"><BR>
J5:ロータリースイッチとの接続<BR>
<img src="img/BOX/RotarySwitch_Wiring2.jpg" width="600"><BR>
　φ20mmユニバーサル基板にロータリースイッチを実装する<BR>
<img src="img/BOX/RotarySwitch_Mount.jpg" width="600"><BR>
　φ20mmユニバーサル基板との接続　T0:8 S2:4 S1:2 S0:1 GND:C<BR>
<img src="img/BOX/RotarySwitch_Wiring.jpg" width="600"><BR>
VR2:可変抵抗の接続<BR>
<img src="img/BOX/DRY-WET_Wiring.jpg" width="600"><BR>
　可変抵抗と配線の接続(基板接続と同じ並びにする)<BR>
<img src="img/BOX/DRY-WET_Wiring2.jpg" width="600"><BR>

1. ケース加工<BR>
可変抵抗、ロータリースイッチ用の穴をあける<BR>
 ※固定用の穴とロータリースイッチの中心にずれあり<BR>
<img src="img/BOX/BoxHoleDrilling.jpg" width="600"><BR>
 可変抵抗の回転止めの穴(貫通してもよい)<BR>
<img src="img/BOX/BoxHoleDrilling3.jpg" width="600"><BR>
 基板固定用穴(皿もみ加工する)<BR>
<img src="img/BOX/BoxHoleDrilling4.jpg" width="600"><BR>
 穴情報(60x23 φ3.2)<BR>
<img src="img/BOX/PCB_Hole.jpg" width="600"><BR>

1. 基板と部品をケースに固定する<BR>
 ケースとロータリスイッチ用基板はスペーサを使って浮かせる
<img src="img/BOX/Box_PCBMounting.jpg" width="600"><BR>
<img src="img/BOX/Box_ComponentMounting.jpg" width="600"><BR>
 完成（電源表示LED追加）<BR>
<img src="img/BOX/Assembly_Complete.jpg" width="600"><BR>
</details>

## Barcoder内蔵タイプ作製例
完成品<BR>
<img src="img/Barcoder/Barcoder2.jpg" width="600"><BR>
<details><summary>組み立て手順</summary>

1. Barcoderを制作しておく<BR>
基本的にはBEVAを使用すること<BR>
[HowToMakeBarcoder](https://github.com/hide63414/HowToMakeBarcoder)<BR>

1. FV-1用基板分割と部品実装<BR>
EEPROM部分で基板を分割　C1,C9,C11の面実装コンデンサを実装<BR>
<img src="img/Barcoder/PCBAssembled2.jpg" width="600"><BR>
各種部品を実装　EEPROMはソケット使用　コンデンサは面実装品<BR>
<img src="img/Barcoder/PCBAssembled.jpg" width="600"><BR>

1. ケース加工<BR>
可変抵抗、ロータリースイッチ用の穴をあける<BR>
※固定用の穴とロータリースイッチの中心にずれあり<BR>
<img src="img/Barcoder/Cover.jpg" width="600"><BR>
<img src="img/Barcoder/Cover2.jpg" width="600"><BR>
可変抵抗、ロータリースイッチ取り付け<BR>
<img src="img/Barcoder/CoverParts.jpg" width="600"><BR>
<img src="img/Barcoder/CoverParts2.jpg" width="600"><BR>

1. 配線接続<BR>
各基板間の配線を接続する<BR>
　※電源は3.3Vに接続すること<BR>
　3.3V電源はバーコーダー基板にあり 下図3.3V表示部<BR>
<img src="img/Barcoder/VCC33V.jpg" width="600"><BR>
ロータリースイッチと可変抵抗
<img src="img/Barcoder/CoverPartsWiring.jpg" width="600"><BR>
EEPROM 3.3V(赤),GND(黒),SCK(黄),SDA(橙)<BR>
<img src="img/Barcoder/EEPROM.jpg" width="600"><BR>
FV-1基板(FV-1 OUT→Audio出力L白 写真と反対面に接続したほうが組み立てやすい）<BR>
<img src="img/Barcoder/PCBWiring.jpg" width="600"><BR>
基板間接続<BR>
　配線長さは次節の組み立てを参考に組み立てやすい長さにする<BR>
　可変抵抗と基板の接続先の詳細はBOXタイプ参照<BR>
<img src="img/Barcoder/Wiring2.jpg" width="600"><BR>
<img src="img/Barcoder/Wiring.jpg" width="600"><BR>
FV-1基板とBarcoderアンプ基板<BR>
　Barcoderアンプ基板のOUT1→FV-1基板IN<BR>
　FV-1基板OUT→Audioケーブル L(白)<BR>
<img src="img/Barcoder/BarcodeAmp.jpg" width="600"><BR>

1. 基板固定<BR>
バーコーダーのグリップ内の溝にFV-1基板を入れる<BR>
<img src="img/Barcoder/BarcoderGrip.jpg" width="600"><BR>
<img src="img/Barcoder/BarcoderGrip2.jpg" width="600"><BR>
Barcoderアンプ基板をねじ止め<BR>
<img src="img/Barcoder/FixPCBAmp.jpg" width="600"><BR>
<img src="img/Barcoder/FixPCBAmp2.jpg" width="600"><BR>

1. 組み立て<BR>
配線を挟まないようにカバーを重ねる<BR>
<img src="img/Barcoder/Assembled.jpg" width="600"><BR>
<img src="img/Barcoder/Assembled2.jpg" width="600"><BR>

1. 組み立て完成<BR>
窓部品を取り付けて完成<BR>
<img src="img/Barcoder/Barcoder.jpg" width="600"><BR>
</details>


## 外部エフェクト追加
<details><summary>追加方法</summary>

1. 概要<BR>
以下のサイトに詳しく記載されているので参考に。<BR>
[REVERBS/EFFECTS　日本語説明書](https://home-bake-instruments.localinfo.jp/posts/37592163/)<BR>

1. ユーザープログラムの入手<BR>
[List of FV-1 Programs](https://mstratman.github.io/fv1-programs/)から、SPNファイルをダウンロードする。
EEPROMには最大8種類書き込むことができる。

1. 開発プログラムのインストール<BR>
[Spin Semiconducotr](https://www.spinsemi.com/products.html)から、SpinAsm assembler for the SPN(をダウンロード、インストールする。

1. 書き込みデータ生成<BR>
assembler for the SPNを起動して、PROG0～7に書き込みたいSPNファイルを選択する。<BR>
各spnファイルを右クリックEdit This Fileで内容を確認できる。<BR>
Pot0,1,2の割り当てを確認できる。<BR>
<img src="img/EEPROM/SpinASM設定.jpg" width="600"><BR>
Intel Hexにチェックを入れ、Buildボタンを押す。<BR>
hexoutフォルダにhexファイルが出力されている。<BR>

1. hexファイルをbinファイルに変換<BR>
EEPROMに書き込み可能な形式に変換する。<BR>
    - 方法その１<BR>
[FV1_HexToBin](https://www.dropbox.com/s/jg1805mid4g4kpn/FV1_HexToBin.zip?dl=0)を使う<BR>
readme.txtの方法では変換できなかったので、以下の方法で変換した。<BR>
コマンドプロンプトを管理者として実行<BR>
srec_cat.exeのあるフォルダに移動<BR>
変換したいbinファイルも同じフォルダに保存(input.hex)とする<BR>
srec_cat input.hex -intel -o output.bin -binary<BR>
output.binが生成される<BR>
<BR>
    - 方法その２<BR>
変換用pythonプログラム[intelHex2bin.py](./hex2bin/intelHex2bin.py)を使用する。<BR>
プログラム中の hex_to_bin('input.hex', 'output.bin') の部分を任意のファイル名に変更して実行<BR>
<BR>
    - 変換したファイル<BR>
変換前output.bin 変換後20240908_test_SpinAsm Project.hex<BR>
<img src="img/EEPROM/Hex_Bin_File.jpg" width="600"><BR>

1. EEPROMに書き込む<BR>
書き込みプログラムと書き込み器を入手する<BR>
[AsProgrammer](https://github.com/nofeletru/UsbAsp-flash/releases)<BR>
[CH341A ROMライター](https://www.amazon.co.jp/dp/B07LGNTJ29) CH341用ならなんでもよさそう（クリップ付きなどもあり）<BR>
<BR>
書き込み機をPCに接続(必要ならドライバーをインストール)<BR>
書き込み機にEEPROMをセット<BR>
<img src="img/EEPROM/EEPROM_WRITER.jpg" width="600"><BR>
セットの方向に注意<BR>
<img src="img/EEPROM/EEPROM_WRITER2.jpg" width="600"><BR>
<BR>
AsProgrammaerを実行<BR>
通信をI2C、ターゲットに24CXX(使用するEEPROM)に設定<BR>
書き込みボタンで書き込む<BR>
<img src="img/EEPROM/AsProgrammer_EEPROM書き込み.png" width="600"><BR>
<BR>
1. EEPROMをソケットに挿入、ロータリスイッチで選択<BR>
ロータリスイッチ0～7はFV-1内臓のエフェクト<BR>
PROG0～8ロータリースイッチ8～Fに割り当てられる<BR>
</details>

## TOOLリンク
[SpinAsm software](https://www.spinsemi.com/products.html)　開発プログラム<BR>
[FV-1 Programs](https://mstratman.github.io/fv1-programs/)　エフェクタプログラム<BR>
[Free DSP Programs](http://www.spinsemi.com/programs.php)　エフェクタプログラム<BR>
[UsbAsp-flash](https://github.com/nofeletru/UsbAsp-flash/releases)　EEPROM書き込みプログラム<BR>
[CH341A ROMライター](https://www.amazon.co.jp/dp/B07LGNTJ29)　EEPROM書き込み器<BR>

