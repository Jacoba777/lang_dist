from model.lang import Language

MAZAHUA = Language('mazahua', __file__, 150000)
MIXTEC = Language('mixtec', __file__, 530000)
OTOMI = Language('otomi', __file__, 300000)
POPOLUCA = Language('popoluca', __file__, 17000)
TRIQUI_COPALA = Language('triqui_copala', __file__, 30000)
ZAPOTEC_ISTHMUS = Language('zapotec_isthmus', __file__, 85000)
ZAPOTEC_XHON = Language('zapotec_xhon', __file__, 50000)  # estimate

OTO_MANGUEAN = [
    MAZAHUA,
    MIXTEC,
    OTOMI,
    POPOLUCA,
    TRIQUI_COPALA,
    ZAPOTEC_ISTHMUS,
    ZAPOTEC_XHON,
]
