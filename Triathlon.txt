import random


class triathlon:

    def __init__(self):
        self.limit = 10000
        self.piece = {}
        for pos in range(self.limit):
            if pos <= 100:
                self.piece[pos] = "Swimming"
            elif pos <= 9000:
                self.piece[pos] = "Biking"
            else:
                self.piece[pos] = "Running"

    def get_limit(self):
        return self.limit

    def get_piece(self,pos):
        return self.piece[pos]


count = 0
total = []


class motion:

    def __init__(self):
        self.position = 0
        self.swim_time = 0
        self.bike_time = 0
        self.run_time = 0

    def move(self,env):
        if self.position < env.get_limit():
            if env.get_piece(self.position) == "Swimming":
                self.position += random.randint(0,2)
                self.swim_time += 1
            elif env.get_piece(self.position) == "Biking":
                self.position += random.randint(0,10)
                self.bike_time += 1
            else:
                self.position += random.randint(0,6)
                self.run_time += 1
            return True
        else:
            self.player_info()
            return False

    def player_info(self):
        global count
        count = count + 1
        tot = self.swim_time + self.bike_time + self.run_time

        sh, sm, ss = int(self.swim_time/3600), int((self.swim_time % 3600)/60), self.swim_time % 60
        bh, bm, bs = int(self.bike_time/3600), int((self.bike_time % 3600)/60), self.bike_time % 60
        rh, rm, rs = int(self.run_time/3600), int((self.run_time % 3600)/60), self.run_time % 60
        th, tm, ts = int(tot/3600), int((tot % 3600)/60), tot % 60

        print("Player {}\t\t{}h {}m {}s\t\t{}h {}m {}s\t\t{}h {}m {}s\t\t{}h {}m {}s".format(count, th, tm, ts, sh, sm, ss, bh, bm, bs, rh, rm, rs))
        total.append([count, self.swim_time, self.bike_time, self.run_time, tot])


# Driver Code
print("Event: Triathlon")

n = int(input("Enter number of players: "))
players = []

print("\nRESULTS OF TRIATHLON\n")
print("Player No.\t\tTotal Time\t\tSwim Time\t\tBike Time\t\tRun Time")
for i in range(n):
    environment = triathlon()
    player = motion()
    status = True
    while(status):
        status = player.move(environment)

for i in total:
    if i[4] == min(j[4] for j in total):
        winner = i[0]
    if i[1] == min(j[1] for j in total):
        swim_winner = i[0]
    if i[2] == min(j[2] for j in total):
        bike_winner = i[0]
    if i[3] == min(j[3] for j in total):
        run_winner = i[0]

print("\nSTATS")
print("Winner: Player", winner)
print("Fastest swimmer: Player", swim_winner)
print("Fastest biker: Player", bike_winner)
print("Fastest runner: Player", run_winner)

