from datetime import date

s_date=date(2016,9,30)
e_date=date(2016,11,20)
delta=e_date-s_date
print('there are {} days between {} and {}'.format(delta.days,"2016-09-30","2016-11-20"))
