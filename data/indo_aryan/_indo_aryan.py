from model.lang import Language

FAMILY = 'indo_aryan'

ASSAMESE = Language('assamese', FAMILY, 15000000)
BENGALI = Language('bengali', FAMILY, 234000000, 39000000)
BHOJPURI = Language('bhojpuri', FAMILY, 51000000)
CALO = Language('caló', FAMILY, 60000)
DHIVEHI = Language('dhivehi', FAMILY, 340000)
GUJARATI = Language('gujarati', FAMILY, 57000000, 5000000)
HINDI = Language('hindi', FAMILY, 340000000, 260000000)
KASHMIRI = Language('kashmiri', FAMILY, 7100000)
KONKANI = Language('konkani', FAMILY, 2260000)
MARATHI = Language('marathi', FAMILY, 83000000, 16000000)
NEPALI = Language('nepali', FAMILY, 16000000, 9000000)
ODIA = Language('odia', FAMILY, 35000000, 3600000)
PALI = Language('pali', FAMILY, extinct_year=-100)
PUNJABI = Language('punjabi', FAMILY, 111000000, 2000000)
RAJASTHANI = Language('rajasthani', FAMILY, 16000000)
ROMANI = Language('romani', FAMILY, 4600000)
SANSKRIT = Language('sanskrit', FAMILY, extinct_year=-600)
SARAIKI = Language('saraiki', FAMILY, 26000000)
SINDHI = Language('sindhi', FAMILY, 32000000)
SINHALA = Language('sinhala', FAMILY, 16000000, 2000000)
URDU = Language('urdu', FAMILY, 70000000, 160000000)


ALL_LANGS = [
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
