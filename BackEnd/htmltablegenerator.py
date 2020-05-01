import csv

# Open CSV and create a list
f = open(r"C:\Users\Jonathan McAwesome\Dropbox\Projects\DieVleisHuisPrysLys\BackEnd\Pricelist.csv","r").read()
itemlist = f.replace("\n",",").split(",")

#Use above list and create a paired matrix
cc = 0 
combo_list = []
while cc < len(itemlist[:-1]):
    combo_list.append([itemlist[cc],itemlist[cc+1]])

    cc = cc+3


# Writing HTML file

writing_session =  open(r"C:\Users\Jonathan McAwesome\Dropbox\Projects\DieVleisHuisPrysLys\index.html","w")


writing_session.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./FrontEnd/CSS/main.css">
    <title>VleisHuisPrysLys</title>
</head>
<body>
    <h1 class="maint">Die Vleishuis</h1>
    <div class="buttoncontainer">
    <button type="button" class="collapsible">Promosie</button>
    
    <div class="content">
    Koop R400 of meer kry gratis Kookvleis by!<br><br>
    Skaapstertjies beperkte tyd beskikbaar!
    </div>
    </div>
    </div>
    <h2>Pryslys</h2>
""")

# Price List Table
writing_session.write('<div class="table-center">\n')
writing_session.write("\t<table>\n")
writing_session.write("\t\t<tr><th>"+combo_list[0][0]+"</th><th>"+combo_list[0][1]+"</th></tr>\n")
for i in combo_list[1:]:
    writing_session.write("\t\t<tr>")
    #Food Cells
    writing_session.write("<td class=foody>"+i[0]+"</td>")
    #Money Cells
    writing_session.write("<td class='money-cell'>"+i[1]+"</td>")

    writing_session.write("</td>\n")
writing_session.write("\n")
writing_session.write("\t</table>")
writing_session.write("</div>")

#Closing Tags
writing_session.write(""" 
<script src="./FrontEnd/JS/collapsebutton.js"></script>
</body>
</html>
""")
