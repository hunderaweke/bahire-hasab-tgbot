from bahire_hasab import BahireHasab

def _bh(year):
    _bh = BahireHasab(year)
    table = f"""
ዓመተ ምህረት፡ {year}
ወንጌላዊ፡ {_bh.wengelawi}
እንቁጣጣሽ፡ {_bh.new_year} መስከረም 1
መስቀል፡ {_bh.elete_ken('መስከረም 17')} መስከረም 17
ጾመ ነቢያተ፡ {_bh.elete_ken('ኅዳር 15')} ኅዳር 15
ገና (ልደት)፡ {_bh.elete_ken('ታኅሣስ 29') if _bh.wengelawi != 'ዮሐንስ' else _bh.elete_ken("ታኅሣስ 28")} {"ታኅሣስ 29" if _bh.wengelawi != 'ዮሐንስ' else 'ታኅሣስ 28'}
ጾመ ገሃድ፡ {_bh.elete_ken('ጥር 10') if _bh.elete_ken('ጥር 11')== ('ረቡዕ' or 'አርብ')else 'የለም'}
ጥምቀት፡ {_bh.elete_ken('ጥር 11')} ጥር 11
ቃና ዘገሊላ፡ {_bh.elete_ken('ጥር 12')} ጥር 12
ጾመ ነነዌ፡ {_bh.elete_ken(_bh.neneweh)} {_bh.neneweh}
ዓቢይ ጾም፡ {_bh.elete_ken(_bh.atswamat_webealat("ዐብይ ጾም"))} {_bh.atswamat_webealat("ዐብይ ጾም")}
ደብረ ዘይት፡ {_bh.elete_ken(_bh.atswamat_webealat("ደብረ ዘይት"))} {_bh.atswamat_webealat("ደብረ ዘይት")}
ሆሳዕና፡ እሑድ {_bh.atswamat_webealat("ሆሳዕና")}
ስቅለት፡ አርብ {_bh.atswamat_webealat("ስቅለት")}
ትንሳኤ፡ እሑድ {_bh.atswamat_webealat("ትንሳኤ")}
እርገት፡ እሑድ {_bh.atswamat_webealat("ዕርገት")}
ጰራቅሊጦስ፡ እሑድ {_bh.atswamat_webealat("በዓለ ሀምሳ")}
ጾመ ሐዋርያት፡ ሰⶉ {_bh.atswamat_webealat("ጾመ ሐዋርያት")}
ጾመ ድኅነት፡ ረቡዕ {_bh.atswamat_webealat("ጾመ ድኅነት")}
    """
    return table