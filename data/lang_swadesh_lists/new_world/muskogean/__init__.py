from model.lang import Language

CHICKASAW = Language('chickasaw', __file__, 75)
CHOCTAW = Language('choctaw', __file__, 9600)
MUSCOGEE = Language('muscogee', __file__, 4500)


MUSKOGEAN = [
    CHICKASAW,
    CHOCTAW,
    MUSCOGEE,
]
