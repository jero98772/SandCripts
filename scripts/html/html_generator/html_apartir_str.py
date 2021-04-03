from flask import Flask,render_template,request
import os
#need learn gen file and extencion with os and opcional arguments
app = Flask(__name__)
def multrequest(items):	
	values = []
	for item in items:		
		item = request.form.get(item)
		try:
			item = float(item)
		except:	
			item = str(item)
		values.append([item])
	return values
def inmultrequest(items,search,replace):
	try:	
		for item in items:
			if item == search:
				items[items.index(item)] = replace
				break
			return item
	except:
		return "you 'search' item not are 'items' "
def genhtmlfile(name,code):
	filehtml = open(name+".html", "w") 
	filehtml.write(code) 
	filehtml.close() 
def geninput(item):
	item = str(item)
	inputText =  4*'\t'+'<input type="text" name="'+item+'" placeholder="'+item+'" >\n'
	return inputText
def genselect2bool(item):
	item = str(item)
	selectO =  4*'\t'+'<select name='+item+'>\n'
	option1 =  5*'\t'+'<option>yes</option>\n'
	option2 =  5*'\t'+'<option>no</option>\n'
	selectC =  4*'\t'+'</select>\n'
	return selectcode
def generatehtml(items):
	filas = 2
	webcode = ""
	fromO , fromC = '<form method="post" enctype="multipart/form-data">\n','</form>\n'
	tableO , tableC = '\t<table style=" width:100%;" border="1">\n','\t</table>\n'
	trO , trC  = 2*'\t'+'<tr>\n' , 2*'\t'+'</tr>\n'
	tdO , tdC  =  3*'\t'+'<td>\n' , 3*'\t'+'</td>\n'	
	webcode += fromO
	webcode += tableO
	webcode += trO
	for item in items :
		webcode += tdO+(4*'\t'+str(item)+'\n')+tdC
		webcode += tdO+str(geninput(item))+tdC
		if items.index(item) % filas == 1 and items.index(item) != 0 :
			webcode += trC
			webcode += trO
#when start say minimun of temperature °C need acomodate every thing
	webcode += tableC
	webcode += fromC
	print(webcode)
	name = "generarhtml"
	genhtmlfile(name,webcode)
@app.route("/" ,methods = ['GET','POST'])
def genhtml():
		return render_template("generarhtml.html")

"""
def test():
	fishdatastr = ["scientific_name" ,"common_name" ,"minph"  ,"maxph"  ,"mingh"  ,"maxgh"  ,"mintemperature" ,"maxtemperature"  ,"weight"  ,"large_of_fish_in_centimeters" ,"needed_liters"  ,"recommended_filtering  ","eats"   ,"can_eat"  ,"reproduction" ,"kill ","breathing" ,"mouth ","latitude  ","longitude  ", "country"  , "state"   ,"city      ","waterenv  ","temperament ","behavior ","swimming_zone"  ,"vel ", "light  ","gravel ","habitats", "habits"   ,"structural  ", "ornaments ","waterforce" , "ecosistem" ,"withpalnts ","forms_surroundings ","photo" ,"description ", "water " ]

	data = multrequest(fishdatastr)
	inmultrequest
	print(data)
	return render_template("main.html")
"""
fishdatastr = ["scientific_name" ,"common_name" ,"minph"  ,"maxph"  ,"mingh"  ,"maxgh"  ,"mintemperature" ,"maxtemperature"  ,"weight"  ,"large_of_fish_in_centimeters" ,"needed_liters"  ,"recommended_filtering  ","eats"   ,"can_eat"  ,"reproduction" ,"kill ","breathing" ,"mouth ","latitude  ","longitude  ", "country"  , "state"   ,"city      ","waterenv  ","temperament ","behavior ","swimming_zone"  ,"vel ", "light  ","gravel ","habitats", "habits"   ,"structural  ", "ornaments ","waterforce" , "ecosistem" ,"withpalnts ","forms_surroundings ","description ","photo" ]
if __name__=='__main__':
	#app.run(debug=True,host="0.0.0.0")
	generatehtml(fishdatastr)
	print(len(fishdatastr))
