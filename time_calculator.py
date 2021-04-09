def add_time(start, duration, day=''): 
  dia = day
  dia = day.title()

  weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',]
  hora  = start.split()
  modt = hora[1].upper()
  ihora = hora[0].split(':')
  dhora = duration.split(':')

  if modt  == 'PM':
    dic = {12:'12',1:'13',2:'14', 3:'15', 4:'16', 5:'17', 6:'18', 7:'19', 8:'20', 9:'21', 10:'22', 11:'23'}
    hora1 = dic.get(int(ihora[0]))
  else:
    hora1 = ihora[0]

  sumatoria = int(hora1)*60 + int(ihora[1]) + int(dhora[0])*60 + int(dhora[1])
  dias = None


  if sumatoria >= 1440:
    dias = sumatoria//1440
    horas = (sumatoria % 1440)//60
    mins = (sumatoria % 1440)%60
  else:
    horas = (sumatoria % 1440)//60
    mins = (sumatoria % 1440)%60

  if horas > 11:
    dic = {12:12, 13:1, 14:2, 15:3, 16:4, 17:5, 18:6, 19:7, 20:8, 21:9, 22:10, 23:11}
    horas = dic.get(horas)
    modt = 'PM'
  elif horas == 0:
    horas = 12
    modt = 'AM'
  else:
    modt = 'AM'
  if mins<10:
    dicti = {1:'01',2:'02', 3:'03', 4:'04', 5:'05', 6:'06', 7:'07', 8:'08', 9:'09'}
    mins = dicti.get(mins)

  if dia != '':
    if (sumatoria//1440 == 0):
      new_time = f'{horas}:{mins} {modt}, {dia}'
    elif ((sumatoria//1440 > 0) and (sumatoria//1440 <2)):
      weekday = weekdays.index(dia)
      weekday_new =(weekday+(dias))%7
      new_time = f'{horas}:{mins} {modt}, {weekdays[weekday_new]} (next day)'
    else:
      weekday = weekdays.index(dia)
      weekday_new =(weekday+(dias))%7
      new_time = f'{horas}:{mins} {modt}, {weekdays[weekday_new]} ({dias} days later)'
  elif ((sumatoria//1440 > 0) and (sumatoria//1440<=1)):
    new_time = f'{horas}:{mins} {modt} (next day)'
  elif sumatoria//1440 >= 2:
    new_time = f'{horas}:{mins} {modt} ({dias} days later)'
  else:
    new_time = f'{horas}:{mins} {modt}'
    
  return new_time