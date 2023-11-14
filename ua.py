def cebot():
     rc = random.choice
     device = str(rc(["DOOGEE","CUBOT","SHARP/SG","IRIS","bq","OUKITEL","Blackview"]))
     mode = str(rc(["A003SH","S61","N30","P60","A102SH","Edison 3","WP2","A60","MAX 2","P50","G7060"]))
     model = str(rc(["JeridB","S61","N30","P60","Recoa","G7060","Edison_3","WP2","A60","MAX_2"]))
     andro = str(rc(["31/12","29/10","30/11","27/8.1.0","21/5.0","26/8.0.0","28/9"]))
     dpi = str(rc(["540","320","360","500","160","480","240","272","408"]))
     pro = str(rc(["qcom","mt6765","mt6762","mt8127","mt6755","mt6580","MT6762"]))
     bhs = str(rc(["en_GB","en_US","ar_LY","id_ID","in_ID"]))
     pixel = str(rc(["1080x2160","720x1344","720x1416","720x1468","1080x2118","720x1488","600x976","800x1232","1080x2016","600x1208","720x1468","720x1442","640x1200","1080x2038","720x1368"]))
     return (f"Instagram 308.0.0.36.109 Android ({andro}; {dpi}dpi; {pixel}; {device}; {mode}; {model}; {pro}; {bhs}; 534961954)")
