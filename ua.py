import random
def goblin():
	rc = random.choice
	model = str(rc(["SM-A715F","SM-G935F","SM-A013M","SM-G930F","SM-G960F","SM-A515F","SM-G925F","SM-J700F","SM-A505FN","SM-A207F","SM-J260M","SM-J415G","SM-J260M","SM-J810M","SM-A705FN"]))
	cpu = str(rc(["a71","hero2","a01core","hero","starlte","a51","zerolte","j7velte","a50","a20e","j2corelte","j4primelte","j2corelte","j8y18lte","a70"]))
	chip = str(rc(["exynos9611","universal8890","mt6739","universal8890","universal8895","exynos9611","universal8890","universal7580","exynos9610","sdm450","universal7570","sdm450","universal7570","sdm450","exynos9610"]))
	id = str(rc(["588311699","588311699","527673568","488901722","592951823","586086077","542177874","546258798","574065856","573788610","571125264","562806511","548838374","543544784","524005426"]))
	andro = str(rc(["30/11","29/10","26/10","25/9","25/10","23/10"]))
	dpi = str(rc(["480","320"]))
	res = str(rc(["1080x2340","1080x1920","720x1384","720x1280","720x1560","720x1480","1080x2160"]))
	bhs = str(rc(["id_ID","en_US","ly_LY","en_GB","in_id"]))
	igv = ("315.0.0.26.121,310.0.0.28.118,305.0.0.34.110,300.0.0.33.135,295.0.0.0.22,290.0.0.25.131,285.0.0.0.128,280.0.0.13.119,275.0.0.0.106,270.0.0.3.143,265.0.0.31.123,260.0.0.11.112,255.0.0.18.121,250.0.0.27.145,245.0.0.0.200")
	igve = igv.split(",")
	igve = str(rc(igve)
	return (f"Instagram {versi} Android ({andro}; {dpi}dpi; {res}; samsung; {model}; {cpu}; {chip}; {bhs}; {id})")
ua = goblin()
print(f"ua:",ua)
