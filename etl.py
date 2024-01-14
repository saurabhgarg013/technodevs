import psycopg2

#Obtaining the connection to RedShift
con=psycopg2.connect(dbname= 'dev', host='redshift-cluster-1.cnwomlrh6uek.us-east-1.redshift.amazonaws.com', port= '5439', user= 'awsuser', password= 'Tango9999')


#Copy Command as Variable
copy_command = """ copy venue from 's3://redshiftbucket13/input/venue_pipe.txt' 
iam_role 'arn:aws:iam::681365143658:role/mynewredshiftfortest'
delimiter '|' region 'us-east-1'; """



#Opening a cursor and run copy query
cur = con.cursor()
cur.execute("truncate table venue;")
cur.execute(copy_command)
con.commit()