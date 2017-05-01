def R(primary, secondary=None, name=None):
    from Recept.models import Receipt

    if secondary is None:
        secondary = primary
    if name is None:
        name = secondary
    Receipt.objects.get_or_create(name=name, primary=primary, secondary=secondary)


def create_objects():
    R('pannkakor')
    R('ris', 'lax', name='lax med kokosris & mangosalsa')
    R('paj', 'taco', name='tacopaj')
    R('nudlar', 'kyckling', name='pad thai')
    R('pasta', 'kyckling', name='krämig kycklingpasta med soltorkade tomater')
    R('paj', 'kyckling', name='krämig kycklingpaj')
    R('ris', 'fläskfärs', name='vietnamesisk fläskfärs')
    R('soppa', name='kelda tomatsoppa')
    R('pasta', 'feta', name='pasta med goda saker')
    R('grillad kyckling')
    R('fried rice', 'fläskfärs', name='fried rice med fläskfärs & ingefära')
    R('pasta', 'köttfärs', name='köttfärssås à la Ann-Sofi')
    R('tortillas', 'kalkon', name='quesadillas')
    R('hamburgare')
    R('tacos', 'taco')
    R('ris', 'kyckling', name='kinainspirerad kyckling')
    R('ris', 'kyckling', 'chicken à la king')
    R('paj', 'kyckling', 'chicken à la king')
    R('pasta', 'lasagne', name='spenatlasagne med chèvre')
    R('paj', 'vegetarisk', name='emmas chilipaj')
    R('tortillas', 'köttfärs', name='enchiladas')
    R('nudlar', 'fläskfärs', name='nudelwok med fläskfärs och pak choi')
    R('pasta', 'kyckling', name='kycklingcanneloni')
    R('ris', 'korv', name='korv stroganoff')
    R('potatis', 'fläsk', name='fläskfilé i svampsås')
    R('risotto', 'svamp', 'jamies svamprisotto')
    R('potatismos', 'köttbullar', 'köttbullar, potatismos och brunsås')
    R('pizza', name='köp pizza')
    R('pizza', name='pizzakit')
    R('ris', 'kyckling', 'köp thai')
    R('pommes', 'hamburgare', 'max-burgare')
    R('pyttipanna')
    R('bröd', 'falafel', 'falafel i pita')
