"""
If you use mac, this simple code can help to inform you when running a time-consuming program.
"""
import os


def owari(error=False, repeat=2, jp_voice=True):

    if jp_voice:
        word_fin = "コード実行が終わりました。"
        word_err = "エラーが発生しました。"
        voice_fin = 'kyoko'
        voice_err = 'kyoko'
    else:
        word_fin = "Code have been finished."
        word_err = "Bug have been occured."
        voice_fin = 'Good\\ News'
        voice_err = 'Bad\\ News'

    if not error:
        os.system(f"say -v {voice_fin} {word_fin*repeat}")
    else:
        os.system(f"say -v {voice_err} {word_err*repeat}")
