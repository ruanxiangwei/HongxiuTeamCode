class leg:

    def __init__(self, dog_leg = 4):
        self.dog_leg = dog_leg

    def put_log_num(self):
        print('leg num is ' + str(self.dog_leg))

    def get_range(self):
        if self.dog_leg > 4:
            print("is not dog")
        else:
            print("is dog")