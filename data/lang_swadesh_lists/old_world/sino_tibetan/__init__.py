from model.lang import Language

APATANI = Language('apatani', __file__, 45000)
BURMESE = Language('burmese', __file__, 33000000, 10000000)
CANTONESE = Language('cantonese', __file__, 82400000)
CHINESE_OLD = Language('chinese_old', __file__, extinct_year=0)
DZONGKHA = Language('dzongkha', __file__, 171000, 469000)
GAN = Language('gan', __file__, 23000000)
GARO = Language('garo', __file__, 1140000)
HAKKA = Language('hakka', __file__, 44000000)
KAREN = Language('karen', __file__, 4500000)
MANANG = Language('manang', __file__, 390)
MANDARIN_NANJINGESE = Language('mandarin_nanjingese', __file__, 70000000)
MANDARIN_SICHUANESE = Language('mandarin_sichuanese', __file__, 260000000)
MANDARIN_STANDARD = Language('mandarin_standard', __file__, 940000000, 200000000)
MEITEI = Language('meitei', __file__, 1800000, 1200000)
MIN_DONG = Language('min_dong', __file__, 11000000)  # This is HOKKEIN in particular; The spoken language of Taiwan
MIN_NAN = Language('min_nan', __file__, 48000000)
MIZO = Language('mizo', __file__, 1000000)
RALTE = Language('ralte', __file__, 900)
TEDIM = Language('tedim', __file__, 340000)
TIBETAN = Language('tibetan', __file__, 1200000)  # As spoken in Lhasa
TSHANGLA = Language('tshangla', __file__, 170000)
WU_SHANGHAINESE = Language('wu_shanghainese', __file__, 14000000)
WU_SUZHOUNESE = Language('wu_suzhounese', __file__, 10000000)  # Population is a guess
XIANG = Language('xiang', __file__, 38000000)

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