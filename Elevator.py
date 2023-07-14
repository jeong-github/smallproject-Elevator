class Elevator:
    s_floor = 1
    d_floor = 0
    num = 0

    def gotofloor(self):
        self.d_floor = int(input("원하는 층을 입력하시오: "))
        self.num = int(input("인원을 정하시오: "))
    def info(self):
        result = [self.s_floor, self.d_floor, self.direction, self.num]
        print("출발 도착 방향 사람수")
        print(result)

    def check_floor(self):
        if self.d_floor > self.s_floor:
            self.direction = 'UP'
            return self.direction
        elif self.d_floor < self.s_floor:
            self.direction = 'DOWN'
            return self.direction
        elif self.d_floor == self.s_floor:
            self.direction = 'CONTINUE'
            return 'CONTINUE'
    def art(self):
        start = int(self.s_floor)
        end = int(self.d_floor)
        print("*" * 30)
        print("*                            *")
        print("*                            *")
        print("*============================*")
        print("* %s층에서-------------->%s층으로 *" %(start , end) )
        print("*============================*")
        print("*                            *")
        print("*                            *")
        print("*" * 30)

def main():
    import time
    e = Elevator()
    sec = 3
    while True:
        e.gotofloor()
        # 만석인 경우
        if e.num > 10:
            print("[ERROR]만석입니다 인원을 조정해주세요")
            continue
        e.check_floor()
        # 같은층을 입력한 경우
        if e.direction == 'CONTINUE':
            print("이미 도착했습니다!!! 다시 입력해주세요")
            continue
        print("이동중.........")
        e.info()
        e.art()
        time.sleep(sec)
        # 목적지 층 현재층으로 변환
        e.s_floor = e.d_floor
        print("도착 !!!현재 층", e.s_floor)
        print("*" * 30)


if __name__ == '__main__':
    main()

    '''
    def setData(self, s_floor, d_floor, direction, num):
        self.source_floor = s_floor
        self.dest_floor = d_floor
        self.direction = direction
        self.saram_nums = num
    '''