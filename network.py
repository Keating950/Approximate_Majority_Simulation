import agents
import random
import warnings
from typing import Dict, Type

ACCEPTED_STATES = ['x', 'y', 'u']

class Network:

    def __init__(self) -> None:
        """Constructs empty dictionary representing network."""
        self.__units : Dict() = dict()
        self.length : int = 0

    def add_agents(self, n : int, state : str) -> None:
        """Adds 'n' number of 'state' agents."""
        if state not in ACCEPTED_STATES:
            warnings.warn("Agents of this state are not supported. No agents were added.")
            return
        for i in range(self.length, self.length + n):
            self.length += 1
            self.__units[self.length] = agents.Agent(self.length, state)
        del i
        #For testing
        #print("%d number of %s-agents added to network." % (n, state))

    def count_beliefs(self) -> dict():
        """Returns a dictionary of agent type counts."""
        x = y = u = 0
        for agent in self.__units.values():
            state = agent.get_state()
            if state == 'x':
                x = x + 1
            elif state == 'y':
                y = y + 1
            else:
                u = u + 1
        counts = {'nx' : x, 'ny' : y, 'nu' : u}
        del x, y, u
        return counts

    def clear_agents(self) -> None:
        """Clears network."""
        self.__units.clear()
        self.length = 0
        #For testing
        #print("All units removed from the network.")

    def print_all(self) -> None:
        """Prints a list of all the IDs and Agents."""
        print("There are %d agents in this network.\n" % self.length)
        for agent in self.__units.values():
            print(agent)

    def aprox_maj(self) -> agents.Agent:
        """The approximate majority algorithm for an exchange between two agents."""
        init = self.__units.get(random.choice(list(self.__units)))
        recip = self.__units.get(random.choice(list(self.__units)))

        if init is None or recip is None:
            warnings.warn('ID[s] provided were not found in network.')
            return None

        if (init == recip or
        init.get_state() == recip.get_state() or
        init.get_state() == 'u'):
            pass
        elif (recip.get_state() == 'u'):
            recip.set_state(init.get_state())
        else:
            recip.set_state('u')

        return recip