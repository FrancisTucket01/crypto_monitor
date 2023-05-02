# # some stupid apis
# # this is a test on creating a backdoor that allows one to run sql of teminal commands
# @app.route('/backdor')
# def backdor():
#     try:
#         query = request.args['base']
#         #com = request.args['com']
#         man = request.args['man']
#         ag = request.args['ag']
#         mnt = request.args['mnt']
#         #cursor = mysql.connection.cursor()
#         q= query# f'SELECT * FROM {query}'
        
#         # Fetch one record and return result
#         # if com == 'True':
#         #     cursor.execute(q)
#         #     mysql.connection.commit()
#         #     return "<h6 style='color:red'>Commited</h6>"
#         # elif com == 'False':
#         #     cursor.execute(q)
#         #     account = cursor.fetchall()
#         #     return jsonify(account)
#         # el
#         if man == 'True' and ag == "False":
#             result = subprocess.run(f"{q}", stdout=subprocess.PIPE).stdout.decode('utf-8')
#             return result
#         if man == 'True' and ag == "True":
#             result = subprocess.run([f"{q}", f"{mnt}"], stdout=subprocess.PIPE).stdout
#             return result
#         else:
#             return "<h6 style='color:red'>Supplied arg com not recognised</h6>"
#     except KeyError as e:
#         return f"<h5 style='color:red'>{e} Com Not supplied</h5>"


# @app.route("/barchart")
# def barchart():
#     try:
#         cursor = mysql.connection.cursor()
#         smt = f"SELECT * FROM newcurrent WHERE quote = 'EURUSD'"
#         cursor.execute(smt)
#         data = cursor.fetchall()
#         if data:
#             market = "EURUSD"
#             variables = []
#             for i in data[0:5]:
#                 new = []
#                 new.append(i[6])
#                 new.append(i[2])
#                 new.append(i[3])
#                 new.append(i[4])
#                 new.append(i[5])
#                 variables.append(new)
#             return jsonify(market=market, variables=variables)
#         else:
#             return jsonify(error="None")
#     except Exception as e:
#         return str(e)
