# coding: UTF-8

# urlを使うため
import urllib2
# html解析
from bs4 import BeautifulSoup
# 正規表現を使うため
import re

# 解析スタート村番号
START_VILLAGE_NUMBER = 1
# 解析数
NUMBER_OF_VILLAGE = 1

# urlリスト
urlList = []
# 設定した村数だけwebスクレイピングする
for i in range(NUMBER_OF_VILLAGE):
    # 村番号取得
    villageNumber = START_VILLAGE_NUMBER + i
    # - ゲーム日数を取得
    endPageHtml = urllib2.urlopen("http://www.wolfg.x0.com/index.rb?vid=" + villageNumber)
    endPageSoup = BeautifulSoup(endPageHtml, "html.parser")
    # ゲーム日数
    gameDay = 0
    # 9日を超えることはないのでrange(9)とする
    for gameDay in range(9):
        # リンクで_partyがあるところがゲーム終了日
        endPageHref = endPageSoup.find("a", href=re.compile("index.rb?vid=" + villageNumber + "&amp;meslog=00" + gameDay + "_party"))
        # _partyを発見した
        if endPageSoup is not None:
            break
    # -
    # プロローグのurl
    urlList.append("http://www.wolfg.x0.com/index.rb?vid=" + villageNumber + "&meslog=000_ready")
    urlList.append()
# ----------------------------------------- ここまで -----------------------

# アクセスするURL
url = "http://www.nikkei.com/markets/kabu"

# URLにアクセスしてhtmlを取得
html = urllib2.urlopen(url)

# htmlをBeaufifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# タイトル要素を取得する
title_tag = soup.title

# 要素の文字列を取得する
title = title_tag.string

# タイトル要素を出力
print title_tag

# タイトル文字列を出力
print title

# span要素すべてを摘出する
span = soup.find_all("span")

# print時にエラーとならないように最初に宣言しておく
nikkei_heikin = ""

# for文ですべてのspan要素の中からClass="mkc-stock_prices"となっているものを探す
for tag in span:
    # classの設定がされていない要素はエラーとなるためtryでエラー回避
    try:
        # tagの中からclass="n"のnの文字列を摘出
        # 配列で帰ってくるため，pop(0)で取り出す
        string_ = tag.get("class").pop(0)

        # 摘出したclassの文字列にmkc-stock_pricesと設定されているかを調べる
        if string_ in "mkc-stock_prices":
            # 設定されていたら，tagで囲まれた文字列を取り出す
            nikkei_heikin = tag.string
            # 摘出が完了したため，for文を抜ける
            break
    except:
        # パス
        pass

# 摘出した日経平均株価を出力
print nikkei_heikin