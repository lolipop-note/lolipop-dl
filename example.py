#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lolipop_dl import LolipopDL

#
# ロリポップ!のドメインを使用している場合
# 
# domain_plan:  0 (固定値)
# passwd:       ログインパスワード
# account:      アカウント (example.lolipop.jpならばexample)
# domain_id:    契約しているドメインに対応する数字 (example.lolipop.jpならばlolipop.jpに対応する数字)
#               ドメインと数字の対応はユーザー専用ページ(https://user.lolipop.jp/)のソースを
#               ドメインで検索することで確認できます。
#
# 例:
#     <option value='220' >littlestar.jp
#     <option value='0' >lolipop.jp
#     <option value='110' >lolitapunk.jp
#     <option value='290' >lomo.jp
#

lolipop = LolipopDL(domain_plan=0, passwd='12345678', account='example', domain_id='0')

#
# 独自ドメインを使用している場合
# 
# domain_plan:  1 (固定値)
# passwd:       ログインパスワード
# domain_name_2:セカンドレベルドメイン (example.comならばexample)
# domain_name_3:ファーストレベルドメイン (example.comならばcom)
#

#lolipop = LolipopDL(domain_plan=1, passwd='12345678', domain_name_2='example', domain_name_3='com')

#
# ログイン
#

lolipop.login()

#
# ログファイルのダウンロード
#
# addressid: ロリポップに登録している各アドレスに対応するID
#            「WEBツール >> アクセスログ >> アクセスログページ」
#            を参照した時のURLに記載されています。 (&id=の部分)
#            https://user.lolipop.jp/?mode=analyze&exec=setting&id=lolipopDomain
# sltDate:   ログをダウンロードしたい日付 (YYMMDD)
#

lolipop.download(addressid='lolipopDomain', sltDate=['120401', '120402'])
