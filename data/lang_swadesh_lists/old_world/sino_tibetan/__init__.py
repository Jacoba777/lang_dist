from model.lang import Language

_FAMILY = 'sino_tibetan'

APATANI = Language('apatani', _FAMILY, 45000)
BURMESE = Language('burmese', _FAMILY, 33000000, 10000000)
CANTONESE = Language('cantonese', _FAMILY, 82400000)
CHINESE_OLD = Language('chinese_old', _FAMILY, extinct_year=0)
DZONGKHA = Language('dzongkha', _FAMILY, 171000, 469000)
GAN = Language('gan', _FAMILY, 23000000)
GARO = Language('garo', _FAMILY, 1140000)
HAKKA = Language('hakka', _FAMILY, 44000000)
KAREN = Language('karen', _FAMILY, 4500000)
MANANG = Language('manang', _FAMILY, 390)
MANDARIN_NANJINGESE = Language('mandarin_nanjingese', _FAMILY, 70000000)
MANDARIN_SICHUANESE = Language('mandarin_sichuanese', _FAMILY, 260000000)
MANDARIN_STANDARD = Language('mandarin_standard', _FAMILY, 940000000, 200000000)
MEITEI = Language('meitei', _FAMILY, 1800000, 1200000)
MIN_DONG = Language('min_dong', _FAMILY, 11000000)  # This is HOKKEIN in particular; The spoken language of Taiwan
MIN_NAN = Language('min_nan', _FAMILY, 48000000)
MIZO = Language('mizo', _FAMILY, 1000000)
RALTE = Language('ralte', _FAMILY, 900)
TEDIM = Language('tedim', _FAMILY, 340000)
TIBETAN = Language('tibetan', _FAMILY, 1200000)  # As spoken in Lhasa
TSHANGLA = Language('tshangla', _FAMILY, 170000)
WU_SHANGHAINESE = Language('wu_shanghainese', _FAMILY, 14000000)
WU_SUZHOUNESE = Language('wu_suzhounese', _FAMILY, 10000000)  # Population is a guess
XIANG = Language('xiang', _FAMILY, 38000000)

CHINESE = [
    CANTONESE,
    CHINESE_OLD,
    GAN,
    HAKKA,
    MANDARIN_NANJINGESE,
    MANDARIN_SICHUANESE,
    MANDARIN_STANDARD,
    MIN_DONG,
    MIN_NAN,
    WU_SHANGHAINESE,
    WU_SUZHOUNESE,
    XIANG,
]


SINO_TIBETAN = [
    APATANI,
    BURMESE,
    *CHINESE,
    DZONGKHA,
    GARO,
    KAREN,
    MANANG,
    MEITEI,
    MIZO,
    RALTE,
    TEDIM,
    TIBETAN,
    TSHANGLA,
]