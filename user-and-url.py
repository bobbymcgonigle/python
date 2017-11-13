# Write a Python script named user-and-url.py which outputs only the user name and URL, one per line, and only for projects with a URL.


lines = ["agarwas2,shivi.agarwal2@mail.dcu.ie,?,?,No Supervisor",
"alkudar2,ruzana.alkudaywi2@mail.dcu.ie,?,?,No Supervisor"," brennok3,ken.brennock3@mail.dcu.ie,slittle,suzanne.little@dcu.ie,Dr Suzanne Little,https://docs.google.com/forms/d/1NZWZVkBFqTLq4bq51mcbS3DT4v-KeZcOj_iVxlGL2Dw/viewform",
"buckla34,amy.buckley34@mail.dcu.ie,?,?,No Supervisor,",
"chauhas2,sourabh.chauhan2@mail.dcu.ie,?,?,No Supervisor,"
"comptos2,stefan.compton2@mail.dcu.ie,?,?,No Supervisor,",
"dattav2,vinay.datta2@mail.dcu.ie,slittle,suzanne.little@dcu.ie,Dr Suzanne Little,https://docs.google.com/forms/d/1qsUF0v_BPQfMAXIPUx86t4Zoo0J8PK-3IPCGhoZAIrw/viewform",
"davidp2,priyanka.david2@mail.dcu.ie,?,?,No Supervisor,"
"dimrip2,prashant.dimri2@mail.dcu.ie,?,?,No Supervisor,"]


for currentLine in lines:
  parse = currentLine.split(",")
  if parse[4] != "No Supervisor":
    print parse[0] + " " + parse[5]  # If there's a name for supervisor, print the URL
