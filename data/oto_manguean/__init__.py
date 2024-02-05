from model.lang import Language

_family = 'oto_manguean'

MAZAHUA = Language('mazahua', _family, 150000)
MIXTEC = Language('mixtec', _family, 530000)
OTOMI = Language('otomi', _family, 300000)
POPOLUCA = Language('popoluca', _family, 17000)
TRIQUI_COPALA = Language('triqui_copala', _family, 30000)
ZAPOTEC_ISTHMUS = Language('zapotec_isthmus', _family, 85000)
ZAPOTEC_XHON = Language('zapotec_xhon', _family, 50000)  # estimate

OTO_MANGUEAN = [
    MAZAHUA,
    MIXTEC,
    OTOMI,
    POPOLUCA,
    TRIQUI_COPALA,
    ZAPOTEC_ISTHMUS,
    ZAPOTEC_XHON,
]
