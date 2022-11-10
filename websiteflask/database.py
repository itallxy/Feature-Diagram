import sqlite3  



conn = sqlite3.connect('featureDiagram.db')

print ("Opened database successfully")
q2="SELECT * FROM FeatureDiagarm"
cursor=conn.cursor()
res=cursor.execute(q2)
res=res.fetchall()
print(res[0][1])
conn.close()
'''

conn.execute(CREATE TABLE if not exists FeatureDiagarm

         (ID            INT     NOT NULL,

         JSON_VALUE           TEXT    NOT NULL

         );)

print ("Table created successfully")

conn.close()

conn = sqlite3.connect('./featureDiagram.db')

print ("Opened database successfully")



conn.execute("INSERT INTO FeatureDiagarm (ID,JSON_VALUE) 

      VALUES (1, ' Paul  - - - - -- ' )")




conn.commit()

print ("Records created successfully")

conn.close()



conn = sqlite3.connect('featureDiagram.db')

print ("Opened database successfully")



cursor = conn.execute("SELECT * from FeatureDiagarm")

for row in cursor:

   print ("ID = ", row[0])

   print ("Value = ", row[1], "\n")



print ("Operation done successfully")


'''