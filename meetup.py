#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import Modules
#For dealing with Json format
import json
#For retrieving something over on the internet
import requests

#beautify the dictionnary or the JSON
#https://docs.python.org/3/library/pprint.html
import pprint
#Configure pprint to indent with 4 spaces
pp = pprint.PrettyPrinter(indent=4)

meetup_api_link = 'https://api.meetup.com/2/cities?offset=0&format=json&photo-host=public&page=20&radius=50&order=size&desc=false&sig_id=114126632&sig=16a10d360a121adb445fdffbfe7465328f62342a'
resp = requests.get(url=meetup_api_link)
data = json.loads(resp.text)

print(pp.pprint(data))

#Question 1
#What type of object the variable 'data' is.

#you may need to uncomment theses lines
'''
cities = []
for i in data.get('results'):
	cities.append(i.get('city'))
'''

#Question 2
#Could you write the previous line in a List-comprehensions format
#documentation link
#http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
#Paragaphs 'From loops to comprehensions'

#Question 4
#I want you to create a list of all the city that start
#with the letter 'K' in their Postal Code

#Question 5
#ReDo the Question 5 by doing it with a list-comprehension

#Question 6 --usage of dir() and help
import platform
#https://docs.python.org/3/library/platform.html

#I would like to know if the Module 'platform' has a method (function)
#that can tell you  which python version that you are using?


'''
===========================================================================
===========================================================================
===========================================================================
'''
USERNAME= ['brad_frost', 'iflendra', 'kastov_yury', 'vladabazhan', 'csswizardry', 'eduardo_olv', 
	'vladarbatov', 'mizko', 'kurafire', 'shalt0ni', 'sachagreif', 'dancounsell', 
	'adhamdannaway', 'peterlandt', 'chadengle', 'pixeliris', 'whale', 'kerem', 'ateneupopular', 
	'boheme', 'cemshid', 'thrivesolo', 'enda', 'jollynutlet', 'adellecharles', 'peterme', 'mghoz', 
	'flamekaizar', 'jina', 'dustinlamont', 'idiot', 'joshhemsley', 'mlane', 'nexy_dre', 'sindresorhus', 
	'sillyleo', 'motherfuton', 'tomaslau', 'arminophen', 'guiiipontes', 'c_southam', 
	'mrjohnwalker', 'iconfinder', 'glif', '_hartjeg', 'soffes', 'teleject', 'brynn', 
	'rssems', 'felipenogs', 'gt', 'mattchevy', 'jaredfitch', 'andrewaashen', 'ladylexy', 
	'brandclay', 'abecherian', 'ManikRathee', 'vista', 'leemunroe', 'dingyi', 'putorti', 
	'dakshbhagya', 'dannpetty', 'teclaro', '_shahedk', 'kfriedson', 'kevin_granger', 'fffabs', 
	'pinceladasdaweb', 'suprb', '9lessons', 'itsjonq', 'aaroni', '_everaldo',"canrec", "carloscrvntsg",
	"reetajayendra", "pbaranco", "likewings", "delanicete", "joshkennedy", "xadusx", "nadezdaneverova",
	"i_ganin", "derekcramer", "raphaelnikson", "zombieoummy", "shiienurm", "sunnsit", "jonathanchrisp",
	"joelcannon", "bangherisetiawn", "pburjanec", "hilanimal", "massfocus", "c_southam", 
	"noammorrissey", "davidsasda", "_eyev_", "j04ntoh", "vm_f", "shaan360", "gmourier", 
	"rikitanone", "akmur", "moaazsidat", "bernieaho", "grysnsmth", "timoliverau", "rowancavanagh",
	"damirdurmo", "meecasso", "hathawaystephen", "craftbynick", "dland", "pjnes", "balintorosz",
	"903886562", "roskin_m", "trucy", "albertaugustin", "yalozhkin", "codysanfilippo", "dutchnadia",
	"kilperic", "pequelord", "hoangloi", "islamgaraev_tim", "superoutman", "shiienurm", "josue", 
	"joelcannon", "glauberamos", "jayvisavadia", "karalek", "embrcecreations", "amoslanka", 
	"damirdurmo", "alemasferrer", "willrax", "jehnglynn", "masterhopia316", "glauberamos", 
	"rasagy", "fireupman", "ravikumar8", "kimberlygs_", "lososina", "n2kza", "bagawarman", 
	"andyfang98", "viktor_dotsenko", "irfansami2", "timbalabuch", "monicaczarny", "moae84", 
	"autobanshaq", "marissamcpeak", "carlosblanco_eu", "ddddrew", "htmlstream", "tofslie", 
	"amlinarev", "saarabpreet", "svenphan", "scottfister", "funwatercat", "ya_zl01", 
	"pauljakobwhite", "areus", "cookingeasycom", "kirangopal", "grantharr_s", "rpatey",
	"aaronstump", "dfhdesign", "hejallan", "pf_creative", "rikas", "spacewood_", "sava2500", "sebygarilli", 
	"dustintheweb", "colynb", "linkinf88k", "wilsonnma", "lettershoppe", "vipinsanker", "spencerortega", 
	"soh3il", "he_jinsheng", "tomgreever", "meisso_jarno", "lukaszklis", "robturlinckx", "looneydoodle", 
	"alxleroydeval", "mizhgan", "kimberlygs_", "vista", "raresloth", "ntfblog", "j1tang", "jefffis", "jehnglynn", 
	"tgormtx", "dan_malarkey", "amoslanka", "mrmartineau", "kaibrach", "skylark64", "antjanus", "kirillgreen", 
	"brenton_clarke", "matejlatin", "froidz", "nickyzoid", "dreierdominic", "skogberg", "joelcipriano", 
	"inspiringbg", "donschnelly", "thimo_cz", "russell_baylis", "mashaaaaal", "areskub", "csteib", "petebernardo", 
	"ilya101010", "jckieangel", "jjsiii", "onkaar", "jbcordina", "lalalaura922", "heyllowlab", "nadya_lex", "suprb", 
	"pinceladasdaweb", "edwin_de_jongh", "francortz", "indigo90", "vishal19801", "jozh123", "anton0kurilov", 
	"originalgoatee", "chendahang", "alestart", "jningtho", "antongenkin", "turkutuuli", "razlagutt", "nepdud", 
	"snowshade", "nate_designer", "peachananr", "shuangshuangli", "quisif", "mrgnw", "devineninaresh", 
	"nathansimpsongd", "bruno1fernando", "mrxloka", "arpad05", "gunjanraik", "mangosango", "adellecharles", 
	"rikyushinichi", "ramdreamers", "victinx", "lingeswaran", "codydmd", "chexee", "sorenschroder", "zeppeppers", 
	"cotegrunenwald", "leelkennedy", "abujahed19", "dahparra", "borryshasian", "leogono", "ianlopshire", 
	"marciotoledo", "didpopcom", "fidelthomet", "ahmedelgabri", "andrewofficer", "ceekaytweet", "shanya_o", 
	"aarondgilmore", "herrhaase", "sikeane", "creativebrainbe", "jrxmember", "limpa123", "rbaassi", "haydn_woods", 
	"puzik", "i_makethings", "olgary", "arminophen", "and_zmei", "mkosterich", "suggeelson", "ektadary", 
	"nansysweet2", "tristandenyer", "aluisio_azevedo", "areandacom", "allenjordan", "hichamazhairi", "sachingawas", 
	"thekennythegame", "vashokk", "cattsmall", "elliotnolten", "tyagoneres", "mikewilliam1982", "n_tassone", 
	"rok_samsa", "eitarafa", "lucassimons1987", "maks_akmal", "007aasim", "phaistonian", "georgedyjr", 
	"gcmorley", "azizarsl", "flobota", "adamkirkwood", "creative_px", "sannigraphics", "kurtinc", "superhankai", 
	"strelov_d", "paladinstudio", "richwild", "rv_atom", "vlysergin", "mostafahawary", "gavr1l0", "umairulhaque", 
	"typografil", "spacekid", "seomarlboro", "chinagrimace", "deedubs", "marcosnwp", "hollymdewolf", "boundbystars", 
	"mrjohnwalker", "seantremaine", "jghyllebert", "the_frug", "solid_color", "pampersdry", "elcardoson", 
	"lisakey1986", "michaelcomiskey", "gordo", "olivermonschau", "davidmerrique", "plbabin", "mattdetails", 
	"michaelbrooksjr", "ariona_rian", "davidvb", "gokhunguneyhan", "brad_frost", "islamgaraev_tim", "kennyadr", 
	"ahmed_sa3ied", "simply_simpy", "bwagert", "gearoidorourke", "evgeny_ryabcev", "zackeeler", "ooomz", 
	"richcsmith", "raydeguzmanto", "jemmoudimed", "asna_farid", "davidhemphill", "joshuarule", "dreizle", "dannegm", 
	"majksner", "fgin69", "_zm", "motionthinks", "ShaneHelm", "bgiardelli", "ntnth", "avnagaraj", "stephenmdixon", 
	"jolliver", "osmond", "matthewkay_", "powerpointsuper", "itsselvam", "alexanderkirov", "brandon_arnold", 
	"julesholleboom", "laksgandikota", "kristoffintosh", "prheemo", "sconzen", "tazmattar", "mobfrank", 
	"alek_djuric", "normanbox", "konvictedofsin", "boheme", "aeon56", "gofrasdesign", "andresenfredrik", "upslon", 
	"jonpyefinch", "itsjaymem", "vamseekrishnain", "dsaltaren", "bbergher", "jackiesaik", "cheezonbread", 
	"onlymagugz", "kokikillara", "pavelbuben", "babojan", "thaoalpha1501", "lososina", "michaelcecetka", 
	"zensenmobile", "thramp", "Chakintosh", "jiceb", "aviddayentonbay", "depaulawagner", "sweetdelisa", 
	"kadri1914", "tomreinhoudt", "fionaosaurusrex", "robergd", "bbuecherl", "nicoleglynn", "hellofeverrrr", 
	"jasonkempers", "sterlingrules", "anysmechkar", "loresrockstar", "victorabrantes", "ilucasramos", "bartjo", 
	"motamarad", "deluzino", "jay_wilburn", "lpzilva", "migl40d", "_iamnyasha", "vitorleal", "edhenderson", 
	"akmalfikri"]


#Question  7- dir()
#I want you to create a list that contains only 'users' 
#that have the letter 'e' in their username

#Question 8 - dir()
#I want you to create a list that contains only 'users' 
#that doesn't have the letter 'e' in their username

#Question 9 - dir()
#I want you to create a list that contains only 'users' 
#that have two letter 'e' in their username

#Question 9 ---This one might be difficult for your level
#tips: There is many way you could resolve this. 
#Fizzbuzz this is a common question that a lot of programmer has to do (interview question).
#Can you try to do it
#
"""
"Write a program that prints the numbers from 1 to 100. But for multiples of 
three print "Fizz" instead of the number and for the multiples of five print "Buzz".
 For numbers which are multiples of both three and five print "FizzBuzz"."
"""

#Question 10 ---Yaozong
"""
Write a program that will only print the username if it contains at least two identical letters 
 i.e : 
 names = ['arnold', 'schwarzenegger']

 result => 'schwarzenegger'
 #because it contains at least two letter 'e'
"""