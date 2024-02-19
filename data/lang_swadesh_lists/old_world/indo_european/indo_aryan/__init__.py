from model.lang import Language

ASSAMESE = Language('assamese', __file__, 15000000)
BENGALI = Language('bengali', __file__, 234000000, 39000000)
BHOJPURI = Language('bhojpuri', __file__, 51000000)
CALO = Language('caló', __file__, 60000)
DHIVEHI = Language('dhivehi', __file__, 340000)
GUJARATI = Language('gujarati', __file__, 57000000, 5000000)
HINDI = Language('hindi', __file__, 340000000, 260000000)
KASHMIRI = Language('kashmiri', __file__, 7100000)
KONKANI = Language('konkani', __file__, 2260000)
MARATHI = Language('marathi', __file__, 83000000, 16000000)
NEPALI = Language('nepali', __file__, 16000000, 9000000)
ODIA = Language('odia', __file__, 35000000, 3600000)
PALI = Language('pali', __file__, extinct_year=-100)
PUNJABI = Language('punjabi', __file__, 111000000, 2000000)
RAJASTHANI = Language('rajasthani', __file__, 16000000)
ROMANI = Language('romani', __file__, 4600000)
SANSKRIT = Language('sanskrit', __file__, extinct_year=-600)
SARAIKI = Language('saraiki', __file__, 26000000)
SINDHI = Language('sindhi', __file__, 32000000)
SINHALA = Language('sinhala', __file__, 16000000, 2000000)
URDU = Language('urdu', __file__, 70000000, 160000000)


INDO_ARYAN = [
    ASSAMESE,
    BENGALI,
    BHOJPURI,
    CALO,
    DHIVEHI,
    GUJARATI,
    HINDI,
    KASHMIRI,
    KONKANI,
    MARATHI,
    NEPALI,
    ODIA,
    PALI,
    PUNJABI,
    RAJASTHANI,
    ROMANI,
    SANSKRIT,
    SARAIKI,
    SINDHI,
    SINHALA,
    URDU,
]
