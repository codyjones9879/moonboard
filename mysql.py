import pymysql
import pymysql.cursors


#TEST DATA
name = 'ROUTE1'
name2 = '%25%FC'
setter = 'Cody Jones'
grading = '7C+'
rating = 4
numMoves = 12
repeaters = 10
start1 = 'A13'
start2 = 'C14'
in1 = 'E12'
in2 = 'C10'
in3 = 'G12'
fin1 = 'D18'


args = (name2, setter, grading, rating, numMoves, repeaters, start1, start2, in1, in2, in3, fin1)
query = "INSERT INTO Moonboard (Name, Author, Grade, Stars, Moves, Repeats, StartHold1, StartHold2, IntermediateHold1, IntermediateHold2, IntermediateHold3, FinishHold1) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE Repeats = VALUES(Repeats), Stars = VALUES(Stars)"
conn = pymysql.connect(host='ClimbingHoldsApe.db.8216949.hostedresource.com', user='ClimbingHoldsApe', password='Comply9879!', db='ClimbingHoldsApe', charset='utf8')
cur = conn.cursor()
#cur.execute("INSERT INTO Moonboard (Name, Author, Grade, Stars, Moves, Repeats, StartHold1, StartHold2, IntermediateHold1, IntermediateHold2, IntermediateHold3, FinishHold1) VALUES ('ROUTE1', 'Cody Jones', '7C+', 3, 12, 5, 'A13', 'C14', 'E12', 'C10', 'G12', 'D18')")
cur.execute(query, args)

cur.close()
conn.close()