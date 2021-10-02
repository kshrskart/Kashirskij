# -- coding: utf-8 --
seconds = 86400
days = seconds / 86400
hours = (second-d*86400)//3600
minutes = (second-d*86400-h*3600)//60
s=second%60
print (days ,'дней:', hours ,'часов:', minutes ,'минут:', s ,'секунд')
