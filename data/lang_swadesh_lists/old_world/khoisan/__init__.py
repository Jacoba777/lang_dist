from model.lang import Language

KHOEKHOE = Language('khoekhoe', __file__, 200000)
NARO = Language('naro', __file__, 11000, 10000)
TAA = Language('taa', __file__, 2500)

KHOISAN = [
    KHOEKHOE,
    NARO,
    TAA,
]
