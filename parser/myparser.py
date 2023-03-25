def generate_sql(tagged_query):
    select_clause = "SELECT "
    from_clause = "FROM " 
    where_clause = "WHERE "
    val = {}
    select = ""
    From = ""
    where = ""
    join_clause = ""
    
    for token in tagged_query:
        # if token[1] == "ATTR" or token[1] == "ATTRREF":
        #     select += token[2]
        if token[1] == "TABLE" or token[1] == "TABLEREF":
            From += token[2] + " "
        if token[1] == "ATTR" or token[1] == "ATTRREF":
            select += token[2] + " "
        if token[1] == "VALUE":
            if token[2] not in val:
                val[token[2]] = ""
            val[token[2]]+=token[0]+" "

    for key in val:
        where += key + " = " + val[key]
    
    sql_query = ""
    
    if select != "":
        sql_query += select_clause + select
    else :
        sql_query += select_clause + "* "
    
    if From != "":
        sql_query += " " + from_clause + From
    
    if join_clause != "":
        sql_query += " " + join_clause
    
    if where != "":
        sql_query += " " + where_clause + where
        
    return sql_query





# def generate_sql(tagged_query):
#     select_clause = "SELECT "
#     from_clause = "FROM " 
#     join_clause = "JOIN "
#     where_clause = "WHERE "
#     val={}
#     table = None
#     join_table = None
#     for token in tagged_query:
#         if token[1] == "TABLE":
#             table = token[2]
#         if token[1] == "TABLEREF":
#             join_table = token[2]
#         if token[1] == "ATTR":
#             select_clause += token[2]
#         if token[1] == "ATTRREF":
#             join_clause += "ON " + table + "." + token[2] + " = " + join_table + "." + token[2]
#         if token[1] == "VALUE":
#             val[token[2]]=token[0]
    
#     for key in val:
#         where_clause += key + " = " + val[key]
    
#     sql_query = select_clause + " " + from_clause + " " + table + " " + join_clause + " " + join_table + " " + where_clause
#     return sql_query

# tagged_query = [("Find", "OTHER", "OTHER"), ("all", "OTHER", "OTHER"), ("movies", "TABLE", "movie"), ("featuring", "TABLEREF", "cast"), ("Kevin", "VALUE", "person.name"), ("Spacey", "VALUE", "person.name")]
# sql_query = generate_sql(tagged_query)
# print(sql_query)


#tagged_query = [("Find", "OTHER", "OTHER"), ("all", "OTHER", "OTHER"), ("movies", "TABLE", "movie"), ("featuring", "TABLEREF", "cast"), ("Kevin", "VALUE", "person.name"), ("Spacey", "VALUE", "person.name")]
#tagged_query = [("List", "TABLE", "OTHER"), ("James", "VALUE", "movie.title"), ("Bond", "VALUE", "movie.title"), ("Director", "TABLE", "director")]
tagged_query = [("Find", "OTHER", "OTHER"), ("all", "OTHER", "OTHER"), ("actors","TABLE", "actor"),  ("born", "OTHER", "OTHER"), ("in", "COND", "COND"), ("Los", "VALUE", "person.birthplace"), ("Angeles", "VALUE", "person.birthplace")]
#tagged_query = [("Find", "OTHER", "OTHER"), ("all", "OTHER", "OTHER") actors/actor/ from/COND/ Austin/person.birth_city/ born/O/ after/COND/ 1980/person.birth_year/]
sql_query = generate_sql(tagged_query)
print(sql_query)