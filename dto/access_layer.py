from fyp_flask_server.database_manager import database_manager as dbm

def get_ransomware_info(json_data):
    result = dbm.get_text_data(dbm.create_db_connection(), json_data)
    return preprocess_db_result(result)


def preprocess_db_result(arr):
    dict = {}
    count=0
    for item in arr:
        count+=1
        temp = {}
        temp["NAME"] = item[0]
        temp["EXTENSION"] = item[1]
        temp["TEXT"] = item[2]
        temp["SOLUTION"] = item[3]

        dict["data"+str(count)] = temp

    return dict
