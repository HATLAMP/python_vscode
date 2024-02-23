class Ball:
    def __init__(self,colour, colour2):
        self.ballcolour = colour
        self.ballcolour2 = colour2

ball_1 = Ball("RED", "GREEN")
print(ball_1.ballcolour)
ball_1.ballcolour2 = "BLUE"
print(ball_1.ballcolour2)

# ball_list = [0 for i in range(10000)]
# for i in range(10000):
#     ball_list[i] = Ball("RED + fat", "GREENnd8*&$£^£)")
#     print(i)

# print(ball_list[0])
# print(ball_list[1])
# print(ball_list[2])

