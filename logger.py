import os
import csv
from datetime import datetime


def logger(path_name, file_name):
    def dec(some_func):
        def inner_func(*args):
            path = os.path.join(path_name,file_name)
            #path = os.path.join(f'{input("input path name: ")}',f'{input("input csv name: ")}.csv')
            #path = os.path.join(r'logpath\logs_file.csv') #variant 2 for variable 'path'
            result = some_func(*args)
            if isinstance(result, dict):
                result = list(some_func(*args).values())
                result.insert(0,str(datetime.date(datetime.now())))
                result.insert(1,str(datetime.now().time())[0:8])
                result.insert(2, some_func.__name__)
                writer(path,result)
            else:
                writer(path,[str(datetime.date(datetime.now())), str(datetime.now().time())[0:8], result])

            return result
        return inner_func
    return dec


def writer(path,data):
    if os.path.exists(str(path.split('\\')[0])) == False:
        os.mkdir(str(path.split('\\')[0]))
    with open(path,"a",newline="\n") as f:
      writer = csv.writer(f,delimiter = ',',lineterminator="\r")
      if os.stat(path).st_size == 0:
          writer.writerow(['date','time','func_name','city','temp', 'desc'])
      writer.writerow(data)