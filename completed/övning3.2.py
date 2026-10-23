årskkort=int(input("hur mycket kostar ett årskort?"))
biljett=int(input("hur mycket kostar ett biljett?"))
antal_besök=int(input("hur många gånger tänker du gå till gymmet under ett år?"))
total_kostnad=biljett*antal_besök
if total_kostnad > årskkort:
    print("Välj årskkort")
else:
    print("Köp biljetter")