# 基本仕様
- プログラミング言語:python
- 使用ライブラリ:Tkinter,google.generativeai
# 使用方法
1. Tkinter,google.generativeai,grpcioなどの必要なライブラリをインストールする。
2. https://aistudio.google.com/u/4/prompts/new_chat よりAPIキーを作成し、システム環境変数にGOOGLE_API_KEYとして登録を行う。
3. 最終課題.pyを実行する。
4. 起動したウィンドウのテキストボックス内に添削を行いたい文章を入力し、”添削”ボタンを押す。
## 注意事項
- ` All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1735116981.074834    8000 init.cc:229] grpc_wait_for_shutdown_with_timeout() timed out. `
と出る場合はgrpcioのバージョンを1.67.1に落とすと解決する場合があります。
- 添削ボタンを押した後にウィンドウが固まったように見えますが処理が少し重いだけです。
- geminiAPIの無料枠を上回るリクエストを行わないでください。
