from model.lang import Language

JEJU = Language('jeju', __file__, 5000)
KOREAN = Language('korean', __file__, 82000000, 0)


KOREANIC = [
    JEJU,
    KOREAN,
]
