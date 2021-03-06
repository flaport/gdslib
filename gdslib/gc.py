import pp

from gdslib.config import CONFIG
from gdslib.load import load


@pp.autoname
def gc1550te(filepath=CONFIG["sp"] / "gc2dte" / "gc1550.dat", numports=2):
    m = load(filepath=filepath, numports=numports)
    return m


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    wav = np.linspace(1520, 1570, 1024) * 1e-9
    f = 3e8 / wav
    c = gc1550te()
    s = c.s_parameters(freq=f)

    plt.plot(wav, np.abs(s[:, 1] ** 2))
    print(c.pins)
    plt.show()
