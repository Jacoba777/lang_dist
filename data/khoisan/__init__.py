from model.lang import Language

_FAMILY = 'khoisan'

KHOEKHOE = Language('khoekhoe', _FAMILY, 200000)
NARO = Language('naro', _FAMILY, 11000, 10000)
TAA = Language('taa', _FAMILY, 2500)

KHOISAN = [
    KHOEKHOE,
    NARO,
    TAA,
]
