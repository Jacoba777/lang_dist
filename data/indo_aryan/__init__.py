from model.lang import Language

_FAMILY = 'indo_aryan'

ASSAMESE = Language('assamese', _FAMILY, 15000000)
BENGALI = Language('bengali', _FAMILY, 234000000, 39000000)
BHOJPURI = Language('bhojpuri', _FAMILY, 51000000)
CALO = Language('caló', _FAMILY, 60000)
DHIVEHI = Language('dhivehi', _FAMILY, 340000)
GUJARATI = Language('gujarati', _FAMILY, 57000000, 5000000)
HINDI = Language('hindi', _FAMILY, 340000000, 260000000)
KASHMIRI = Language('kashmiri', _FAMILY, 7100000)
KONKANI = Language('konkani', _FAMILY, 2260000)
MARATHI = Language('marathi', _FAMILY, 83000000, 16000000)
NEPALI = Language('nepali', _FAMILY, 16000000, 9000000)
ODIA = Language('odia', _FAMILY, 35000000, 3600000)
PALI = Language('pali', _FAMILY, extinct_year=-100)
PUNJABI = Language('punjabi', _FAMILY, 111000000, 2000000)
RAJASTHANI = Language('rajasthani', _FAMILY, 16000000)
ROMANI = Language('romani', _FAMILY, 4600000)
SANSKRIT = Language('sanskrit', _FAMILY, extinct_year=-600)
SARAIKI = Language('saraiki', _FAMILY, 26000000)
SINDHI = Language('sindhi', _FAMILY, 32000000)
SINHALA = Language('sinhala', _FAMILY, 16000000, 2000000)
URDU = Language('urdu', _FAMILY, 70000000, 160000000)


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
