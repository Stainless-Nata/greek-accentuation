import unicodedata


def base(ch):
    return unicodedata.normalize("NFD", ch)[0]


def extract_diacritic(*diacritics):
    """
    Given a collection of Unicode diacritics, return a function that takes a
    Unicode character and returns the member of the collection the character
    has (or None).
    """
    def _(ch):
        decomposed_form = unicodedata.normalize("NFD", ch)
        for diacritic in diacritics:
            if diacritic in decomposed_form:
                return diacritic
    return _


def add_diacritic(base, diacritic):
    """
    Add the given diacritic to the given base character.
    """
    return unicodedata.normalize("NFC", base + diacritic)


def remove_diacritic(*diacritics):
    """
    Given a collection of Unicode diacritics, return a function that takes a
    string and returns the string without those diacritics.
    """
    def _(text):
        return unicodedata.normalize("NFC", "".join(
            ch
            for ch in unicodedata.normalize("NFD", text)
            if ch not in diacritics)
        )
    return _


PSILI = SMOOTH = "\u0313"
DASIA = ROUGH = "\u0314"

breathing = extract_diacritic(SMOOTH, ROUGH)

strip_breathing = remove_diacritic(SMOOTH, ROUGH)

OXIA = ACUTE = "\u0301"
VARIA = GRAVE = "\u0300"
PERISPOMENI = CIRCUMFLEX = "\u0342"

accent = extract_diacritic(ACUTE, GRAVE, CIRCUMFLEX)


DIAERESIS = "\u0308"

diaeresis = extract_diacritic(DIAERESIS)


YPOGEGRAMMENI = IOTA_SUBSCRIPT = "\u0345"

iota_subscript = extract_diacritic(IOTA_SUBSCRIPT)
ypogegrammeni = iota_subscript


SHORT = "\u0306"
LONG = "\u0304"

length = extract_diacritic(SHORT, LONG)

strip_length = remove_diacritic(SHORT, LONG)
