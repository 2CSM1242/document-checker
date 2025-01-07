import google.generativeai as genai
import os

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

def main():
    Create_application()
    

def Proofread_text(user_message):
    gemini_pro = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="""
 あなたは文章改善の専門家です。これから渡される文章について、以下の指針に従って提案を行ってください：
1. 表現をより魅力的にするための改善点を指摘してください。
2. 必要に応じて追加すべき表現や補足情報を提案してください。
3. すべての項目を箇条書きで示し、各項目を・ではじめてください。
4. 具体的な例文などの提案を返す必要はありません。
5. 自動的に読みやすさを評価し、100点満点でスコアを出してください。評価は、文法、語彙の多様性、段落の分け方、文章の流れを基準に行い、それぞれ25点満点で評価します。
6. 点数の内訳と改善提案を提示してください。
7. 改善提案は以下の形式を守るようにしてください
    - 例:
    ・視覚的な表現の追加:
    読者の五感を刺激する描写を追加することで、より臨場感あふれる文章になります。(例：風の音、鳥のさえずり、水の流れる音など)

8. 最後に採点基準を提示してください"""
    )
    chat = gemini_pro.start_chat(history=[])

    response = chat.send_message(user_message)
    return response.text

    

import tkinter as tk
from tkinter import ttk

def Create_application():
    root = tk.Tk()
    root.title("文章校正アプリ")

    root.geometry("900x750")

# テキストボックスの作成と設置
    text = tk.Text(root, width=60, height=20, font=("メイリオ",15) , undo=True) 
    text.grid(row=0, column=0, padx=(80,0), pady=40)

# 校正ボタンの作成と設置
    ExeBtn = ttk.Button(root, text="校正", style="TButton", command=lambda:send_message(text,root))
    ExeBtn.grid()

# スクロールバーの作成と設置
    ybar = tk.Scrollbar(root, orient=tk.VERTICAL)
    ybar.grid(row=0, column=1, pady=40, sticky=tk.N + tk.S)
# テキストボックスとスクロールバーを連動
    ybar.config(command=text.yview)
    text.config(yscrollcommand=ybar.set)

# 校正ボタンのフォントを”アリアル”に変更
    style = ttk.Style()
    style.configure("TButton", font="Arial")

    root.mainloop()

# geminiにテキストボックスに入力した文章を渡し、添削内容を別ウィンドウで表示
def send_message(text,root):
    save_text = text.get("1.0", "end-1c")
    # テキストボックス内に何も入力されていない場合
    if save_text == "":
        return "[(0.1)]"
    correction = Proofread_text(save_text)

    # 添削内容を表示するためのウィンドウを作成
    subwindow = tk.Toplevel(root)
    subwindow.geometry("900x750")
    respons = tk.Text(subwindow, width=60, height=20, font=("メイリオ",15)) 
    respons.grid(row=0, column=0, padx=(40,0), pady=40)
    respons.insert(1.0, correction)

    ybar = tk.Scrollbar(subwindow, orient=tk.VERTICAL)
    ybar.grid(row=0, column=1, pady=40, sticky=tk.N + tk.S)
    ybar.config(command=respons.yview)
    respons.config(yscrollcommand=ybar.set)
    respons.config(state=tk.DISABLED)


    

            
if __name__ == "__main__":
    main()