from datetime import datetime

import pandas as pd


class SimulationLog:

    def __init__(self) -> None:
        self._file = pd.DataFrame()
        self._trial = 1

    def inc_trial(self) -> None:
        self._trial = self._trial + 1

    def add_row(self, cycle: int, counts: {}) -> None:
        to_add = pd.DataFrame({'CYCLE': cycle, 'N_X': counts.get('nx'),
                               'N_Y': counts.get('ny'), 'N_XY': counts.get('nxy'), 'N_S': counts.get('ns')},
                              index=[self._trial])
        self._file = self._file.append(to_add)

    def get_file(self) -> pd.DataFrame:
        return self._file

    def save_file(self) -> None:
        """Save log file with current date and time."""
        today = datetime.now()
        file_name = str("./Data/SIMULATION_%s.csv" % today.strftime("%d_%m_%Y_%H%M"))
        self._file.index.name = 'TRIAL'
        # print(self._file.head(10))
        self._file.to_csv(file_name)
        print('File Printed to %s' % file_name)