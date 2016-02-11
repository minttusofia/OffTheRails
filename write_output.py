class Output:
    def __init__(self):
        self._q = 0
        self._w_list = []

    def finish(self):
        with open('output.dat', 'w+') as f:
            f.write(str(self._q) + '\n')
            for string in self._w_list:
                f.write(string)

    def write_command(self, d_id, c_tag, t_id, p_id, n_items):
        string = " ".join([str(d_id), c_tag, str(t_id), str(p_id),
                str(n_items), '\n'])
        self._w_list.append(string)
        self.inc_q()

    def write_wait(self, d_id, c_tag, n_wait):
        string = " ".join([str(d_id), "W", str(n_wait), '\n'])
        self._w_list.append(string)
        self.inc_q()

    def load(self, d_id, w_id, p_id, n_prod):
        self.write_command(d_id, "L", w_id, p_id, n_prod)

    def unload(self, d_id, w_id, p_id, n_prod):
        self.write_command(d_id, "U", w_id, p_id, n_prod)

    def deliver(self, d_id, c_id, p_id, n_prod):
        self.write_command(d_id, "D", c_id, p_id, n_prod)

    def wait(self, d_id, n_turns):
        self.write_wait(d_id, "W", n_turns)

    def inc_q(self):
        self._q += 1
