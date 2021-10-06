"""
If you use mac, this simple code can help to inform you when running a time-consuming program.
"""
import os


def say(word, repeat=1, voice="kyoko"):
    os.system(f"say -v {voice} {word*repeat}")


def owari_voice(repeat=2, error=False, jp_voice=True):
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
        say(word_fin, repeat, voice_fin)
    else:
        say(word_err, repeat, voice_err)


def owari(nys=True, repeat=2, **args):

    nys_path = "/Users/alalalalaki/GitHub/Guide2EconRA/python/util/asset/nps.wav"

    if nys & os.path.exists(nys_path):
        for _ in range(repeat):
            os.system(f"afplay {nys_path}")
    else:
        owari_voice(repeat=repeat, **args)
