


import pandas

# data=pandas.read_csv("data.csv")
# data_dict=data.to_dict()
#colors=data_dict["Primary Fur Color"]
# gray=0
# red=0
# black=0
# print(colors)
# for color in colors:
#     if colors[color]=="Gray":
#         gray+=1
#     elif colors[color]=="Cinnamon":
#         red+=1
#     elif colors[color]=="Black":
#         black+=1
# print(gray)
# print(red)
# print(black)



# grey_count=len(data[data["Primary Fur Color"]=="Gray"])
# red_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
# black_count=len(data[data["Primary Fur Color"]=="Black"])
# 21
#
# data_dict={
#     "Fur Color":["Gray","Cinnamon","Black"],
#     "count":[grey_count,red_count,black_count]
#
# }


words="the of and to in a is was that for as with by on are from be or his were it an at not which have he had this has also their but one can its on the other been more they used first all two citation than into would only time who most may such some many when after between over these her about there use no them new him will out during made both then often so any being such as where number could main p. through system people known each while if called convert same later three because well work before the same under part very different became year did large example several city early until much government found own since she even form power do those around state including set high life against second century within world still end using small name what now usually American without however began like as well area make common the most water United States another way due must long less four death said film order due to back public does left based few become known as s given country major British place group considered among game point used to period support war music down million important systems control should took day family language last original result political line members case as well as see single just process along similar take following we although countries right either times areas published the other local include population never data home every various the time modern further development per how led possible military popular term though history generally you off rather men law developed German held human production body general the world light sometimes states late field based on having came above available book others York next created U.S. show himself out of wrote days died word play again great service age seen children level released works continued pp. the two five higher species energy required change means team January information theory New York produced making built design role addition included almost side position groups able de land total range July national space written social version Europe season force air allowed largest good type itself received women low throughout taken standard little least that is free cases size thus school especially old upon particular terms effect provide lower certain together present always short parts words third April described too up to established might played forces natural June once months rate European numbers six man rather than hand typically value England London October could be final the country September average France instead current December international program character increased a few surface across thought company followed best provided economic games significant named function building went return uses fact study below full source lost America person a number changes longer research individual languages strong structure party larger run open cause aircraft away far region need food forms increase outside started material cannot November half head market near record traditional special style all the sent story February player designed top at least themselves model returned band because of help types come points added events network limited services nature army former father close view allow won specific elements practice lines gave pressure introduced produce moved whether religious put official movement my Germany students trade method attack in order problems art eventually evidence referred results caused remained influence success meaning brought believed enough features give young white culture problem characters lead action according referred to conditions performance according to effects amount black business working better difficult temperature education real money smaller create located directly sound leading ground therefore get private formed particularly Chinese television subject south cities album class industry computer beginning community already complete go players associated related physical our town move complex interest rule speed commonly in order to rights living for example greater writing find growth killed court levels house against the office done shows Spanish needed saw central entire fire son books mostly access soon today earlier variety additional percent foreign ever recorded future widely title all of shown successful radio project construction changed king remains mass personal policy code includes involved Africa idea names separate base length rules key units likely makes release cost church films majority primary performed methods stated appear whole so that member allows decided Japanese reported sold capital science society rest stage event whose recent color legal highly career song frequently placed simple defined me mother appeared India schools turn simply relationship multiple nearly sense past relatively forced software attempt north William quickly companies programs products direct site sources previous technology battle front provides necessary served originally along with approach image seven experience Greek parts of text towards completed memory ability commercial UK health replaced worked yet start economy highest property behind knowledge test response largely sea reached president wide night operations supported act training reason Britain list issues occur loss the government reduced active functions remain lack to do clear gas island cells taking contains takes approximately exist basis distance independent intended elected product adopted actually wife ended born Christian keep potential course matter love issue objects things heavy oil center regular George the following divided eight date James summer direction laws numerous account income individuals concept plan announced Russian failed applied values northern proposed ships resulting estimated appears continue Canada red married object studies media engine passed Henry Australia machine quality founded hold say parties letter Japan expected treatment normal signal blood financial status video older carried compared know wanted accepted via read each other types of animals turned unit feature southern increasing met prevent songs applications require opened marriage contain equipment playing section remaining properties asked the case ten Charles activity whom ways buildings basic probably running materials stories edition location noted cell analysis Russia Rome removed becomes paper activities billion fall child cut operating degree ship occurs less than novel completely except inside Robert troops Jewish report call flow metal appointed offered told frequency initial campaign discovered definition historical models allowing operation police poor weight not have ancient here primarily agreed hit west heat security David claimed positive easily environment scientific going regions ISBN ball tradition reach requires St. extended charge female face serve equal Italy letters refused immediately believe supply effective internal versions cultural leave th mainly negative soldiers question spread suggested Paul"
words_list=words.split()

my_data_frame=pandas.DataFrame(words_list)
my_data_frame.to_csv('words.csv')
print(my_data_frame)