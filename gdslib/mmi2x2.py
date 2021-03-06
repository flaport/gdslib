import pp

from gdslib.load import load


@pp.autoname
def mmi2x2(c=pp.c.mmi2x2, **kwargs):
    """ mmi1x2 Sparameter model

    .. code::
                 ____
            W1 _|   |_ E1
            W0 _|   |_ E0
                |___|

    .. plot::
        :include-source:

        import gdslib as gl

        c = gl.mmi2x2()
        gl.plot_sparameters(c)
    """
    m = load(c)
    return m


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    wav = np.linspace(1520, 1570, 1024) * 1e-9
    f = 3e8 / wav
    c = mmi2x2()
    s = c.s_parameters(freq=f)

    plt.plot(wav, np.abs(s[:, 1] ** 2))
    print(c.pins)
    plt.show()
