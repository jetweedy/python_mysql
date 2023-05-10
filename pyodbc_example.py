import pyodbc 

conn = pyodbc.connect('Driver={'+cfg['db']['driver']+'};'
                        'Server='+cfg['db']['server']+';'
                        'Database='+database+';'
                        'Trusted_Connection=yes;')
cursor = conn.cursor() 