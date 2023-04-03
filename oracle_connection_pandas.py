#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cx_Oracle
con = cx_Oracle.connect('shashank/shashank@orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com:1521/ORCL')
print(con.version)


# In[2]:


import cx_Oracle
con = cx_Oracle.connect('team13_mercypriya/team13_mercypriya@orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com:1521/ORCL')
print(con.version)


# In[3]:


#create a table in oracle sql developer using python
try:
    con = cx_Oracle.connect('team13_mercypriya/team13_mercypriya@orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com:1521/ORCL')
    
    #now execute the sql cursor:
    cursor = con.cursor()
    #creating a table:
    cursor.execute("create table python_table1(empid integer primary key, name varchar(20), salary number(10,2))")
    print("table created successfully")
except cx_Oracle.DatabaseError as e:
    print("there is a problem with oracle",e)
#by writing FINALLY if any error occurs
#then also we can close all the database operation
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()


# In[ ]:




