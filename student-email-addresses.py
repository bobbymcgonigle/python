lines = ["agarwas2,shivi.agarwal2@mail.dcu.ie,?,?,No Supervisor",
"alkudar2,ruzana.alkudaywi2@mail.dcu.ie,?,?,No Supervisor"," brennok3,ken.brennock3@mail.dcu.ie,slittle,suzanne.little@dcu.ie,Dr Suzanne Little,https://docs.google.com/forms/d/1NZWZVkBFqTLq4bq51mcbS3DT4v-KeZcOj_iVxlGL2Dw/viewform",
"buckla34,amy.buckley34@mail.dcu.ie,?,?,No Supervisor,",
"chauhas2,sourabh.chauhan2@mail.dcu.ie,?,?,No Supervisor,"
"comptos2,stefan.compton2@mail.dcu.ie,?,?,No Supervisor,"]


for currentLine in lines:
  parse = currentLine.split(",")
  print parse[1]          # Input given in defined form E.g CSV File
