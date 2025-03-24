class Contest:
    def __init__(self, names, task_count):
        self.s = {}
        self.u = {}
        t = range(1, task_count + 1)
        for n in names:
            self.s[n] = {x: 0 for x in t} 
            self.u[n] = 0
        self.c = 0

    def add_submission(self, name, task, score):
        self.c += 1
        if self.s[name][task] < score:
            self.s[name][task] = score
            self.u[name] = self.c

    def create_scoreboard(self):
        d = []
        for n in self.s:
            d.append((-sum(self.s[n].values()), self.u[n], n))
        d.sort()

        sb = []
        for ns, u, n in d:
            sb.append((n, -ns))
        return sb

if __name__ == "__main__":
    names = ["anna", "pekka", "kalle", "tiina", "eeva"]
    contest = Contest(names, 3)

    contest.add_submission("tiina", 2, 30)
    contest.add_submission("pekka", 1, 40)
    contest.add_submission("tiina", 1, 20)
    contest.add_submission("pekka", 1, 50)
    contest.add_submission("pekka", 2, 0)
    contest.add_submission("eeva", 3, 100)
    contest.add_submission("anna", 1, 0)
    contest.add_submission("eeva", 3, 80)
    contest.add_submission("tiina", 2, 30)

    scoreboard = contest.create_scoreboard()
    print(scoreboard)
    # [('eeva', 100), ('tiina', 50), ('pekka', 50), ('anna', 0), ('kalle', 0)]
