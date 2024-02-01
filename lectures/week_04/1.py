trains = """350 Wolverine eastbound CHI ARB 6:45a 12:26a
351 Wolverine westbound ARB CHI 7:14a 10:32a
352 Wolverine eastbound CHI ARB 2:15p 7:31p
353 Wolverine westbound ARB CHI 10:23a 2:02p
354 Wolverine eastbound CHI ARB 5:50p 11:04p
355 Wolverine westbound ARB CHI 7:00p 10:40p
364 Bluewater eastbound CHI LNS 4:00p 8:55p
365 Bluewater westbound LNS CHI 8:54a 11:45a
370 Pere_Marquette eastbound CHI GRR 6:30p 11:34p
371 Pere_Marquette westbound GRR CHI 6:00a 9:08a
"""

data = trains.splitlines()

westbound = data[1::2]
del(westbound[-2:])
westbound