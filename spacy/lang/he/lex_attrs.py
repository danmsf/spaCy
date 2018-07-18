# coding: utf8
from __future__ import unicode_literals
from ...attrs import LIKE_NUM

_num_words = set("""
אחד
אחת
שתיים
שניים
שלוש
שלושה
שלושת
ארבע
ארבעה
ארבעת
חמש
חמישה
חמשת
שש
שישה
ששת
שבע
שבעה
שבעת
שמונה
שמונת
תשע
תשעה
תשעת
עשר
עשרה
עשרת
מאה
אלף
אלפיים
מיליון
מיליארד
""".split())

_ordinal_words = set("""
ראשון
שני
שלישי
רביעי
חמישי
שישי
שביעי
שמיני
תשיעי
עשירי
""".split())


def like_num(text):
    """
    check if text resembles a number
    """
    text = text.replace(',', '').replace('.', '')
    if text.isdigit():
        return True
    if text.count('/') == 1:
        num, denom = text.split('/')
        if num.isdigit() and denom.isdigit():
            return True
    if text in _num_words:
        return True
    if text in _ordinal_words:
        return True
    return False


LEX_ATTRS = {
    LIKE_NUM: like_num
}
