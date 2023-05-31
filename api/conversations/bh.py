from bahire_hasab import BahireHasab
from io import BytesIO


def _bh(year):
    _bh = BahireHasab(year)
    table = f"""
    ዓመተ ምህረት፡          {year}

    ወንጌላዊ፡              {_bh.wengelawi}

    እንቁጣጣሽ፡             {_bh.new_year} መስከረም 1

    ጾመ ነነዌ፡              {_bh.elete_ken(_bh.neneweh)} {_bh.neneweh}

    ዓቢይ ጾም፡              {_bh.elete_ken(_bh.atswamat_webealat("ዐብይ ጾም"))} {_bh.atswamat_webealat("ዐብይ ጾም")}

    ደብረ ዘይት፡             {_bh.elete_ken(_bh.atswamat_webealat("ደብረ ዘይት"))} {_bh.atswamat_webealat("ደብረ ዘይት")}
 
    ሆሳዕና፡                 እሑድ {_bh.atswamat_webealat("ሆሳዕና")}

    ስቅለት፡                 አርብ {_bh.atswamat_webealat("ስቅለት")}

    ትንሳኤ፡                 እሑድ {_bh.atswamat_webealat("ትንሳኤ")}

    እርገት፡                 እሑድ {_bh.atswamat_webealat("ዕርገት")}

    ጰራቅሊጦስ፡               እሑድ {_bh.atswamat_webealat("በዓለ ሀምሳ")}

    ጾመ ሐዋርያት፡             ሰኞ {_bh.atswamat_webealat("ጾመ ሐዋርያት")}

    ጾመ ድኅነት፡              ረቡዕ {_bh.atswamat_webealat("ጾመ ድኅነት")}


             @ethiopianholidaysbot
    """
    return table


