# -- coding: utf-8 --
seconds = 86400
days = seconds / 86400
hours = (seconds-d*86400)//3600
minutes = (seconds-d*86400-h*3600)//60
s=seconds%60
print (days ,'дней:', hours ,'часов:', minutes ,'минут:', s ,'секунд')
