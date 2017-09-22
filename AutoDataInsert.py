import pymysql
import time
import random



total = 0b111110000000000000000
current1 = 0b11111
current2 = 0b11111
current3 = 0b11111

while(True) :
    conn = pymysql.connect(host='210.125.31.23', port=3306, user='admin', password='admin', db='cnc_mc')
    curs = conn.cursor()

    if(current1 < 0b10):
        current1 = total >> 16
    if (current2 < 0b10):
        current2 = total >> 16
    if (current3 < 0b10):
        current3 = total >> 16

    current1 = current1 - (random.randrange(0b1, 0b11))
    current2 = current2 - (random.randrange(0b1, 0b100))
    current3 = current3 - (random.randrange(0b1, 0b10))
    sql = "INSERT into data (id, lubricant_machine, lubricant_saw, pressure_air_main, pressure_oil_hydraulic, servo_cut, servo_transfer, spindle, safety_door, depletion, workload, timestamp) " +\
          " VALUES (1, "\
          +str(random.randrange(0,2))+", "\
          +str(random.randrange(0,2))+", "\
          +str(random.randrange(0,2))+", "\
          +str(random.randrange(0,2))+", "\
          +str(random.randrange(0,2))+", "\
          +str(random.randrange(0,2))+", "\
          +str(random.randrange(0,2))+", "\
          +str(random.randrange(0,2))+", "\
          +str(random.randrange(0,2))+", "\
          +str(current1 + total)+", "\
          +str(int(time.time()))+")"
    curs.execute(sql)
    conn.commit()

    sql = "INSERT into data (id, lubricant_machine, lubricant_saw, pressure_air_main, pressure_oil_hydraulic, servo_cut, servo_transfer, spindle, safety_door, depletion, workload, timestamp) " + \
          " VALUES (2, " \
          + str(random.randrange(0, 2)) + ", " \
          + str(random.randrange(0, 2)) + ", " \
          + str(random.randrange(0, 2)) + ", " \
          + str(random.randrange(0, 2)) + ", " \
          + str(random.randrange(0, 2)) + ", " \
          + str(random.randrange(0, 2)) + ", " \
          + str(random.randrange(0, 2)) + ", " \
          + str(random.randrange(0, 2)) + ", " \
          + str(random.randrange(0, 2)) + ", " \
          + str(current2 + total) + ", " \
          + str(int(time.time())) + ")"
    curs.execute(sql)
    conn.commit()

    sql = "INSERT into data (id, lubricant_machine, lubricant_saw, pressure_air_main, pressure_oil_hydraulic, servo_cut, servo_transfer, spindle, safety_door, depletion, workload, timestamp) " + \
          " VALUES (3, " \
          + str(random.randrange(0, 2)) + ", " \
          + str(random.randrange(0, 2)) + ", " \
          + str(random.randrange(0, 2)) + ", " \
          + str(random.randrange(0, 2)) + ", " \
          + str(random.randrange(0, 2)) + ", " \
          + str(random.randrange(0, 2)) + ", " \
          + str(random.randrange(0, 2)) + ", " \
          + str(random.randrange(0, 2)) + ", " \
          + str(random.randrange(0, 2)) + ", " \
          + str(current3 + total) + ", " \
          + str(int(time.time())) + ")"
    curs.execute(sql)
    conn.commit()


    #rows = curs.fetchall()
    print(sql)

    time.sleep(5)
    conn.close()
