





import numpy as np



class IndexCalculation:

    def __init__(self, red=None, green=None, blue=None, red_edge=None, nir=None):
        self.set_matricies(red=red, green=green, blue=blue, red_edge=red_edge, nir=nir)

    def set_matricies(self, red=None, green=None, blue=None, red_edge=None, nir=None):
        if red is not None:
            self.red = red
        if green is not None:
            self.green = green
        if blue is not None:
            self.blue = blue
        if red_edge is not None:
            self.redEdge = red_edge
        if nir is not None:
            self.nir = nir
        return True

    def calculation(
        self, index="", red=None, green=None, blue=None, red_edge=None, nir=None
    ):
        self.set_matricies(red=red, green=green, blue=blue, red_edge=red_edge, nir=nir)
        funcs = {
            "ARVI2": self.arv12,
            "CCCI": self.ccci,
            "CVI": self.cvi,
            "GLI": self.gli,
            "NDVI": self.ndvi,
            "BNDVI": self.bndvi,
            "redEdgeNDVI": self.red_edge_ndvi,
            "GNDVI": self.gndvi,
            "GBNDVI": self.gbndvi,
            "GRNDVI": self.grndvi,
            "RBNDVI": self.rbndvi,
            "PNDVI": self.pndvi,
            "ATSAVI": self.atsavi,
            "BWDRVI": self.bwdrvi,
            "CIgreen": self.ci_green,
            "CIrededge": self.ci_rededge,
            "CI": self.ci,
            "CTVI": self.ctvi,
            "GDVI": self.gdvi,
            "EVI": self.evi,
            "GEMI": self.gemi,
            "GOSAVI": self.gosavi,
            "GSAVI": self.gsavi,
            "Hue": self.hue,
            "IVI": self.ivi,
            "IPVI": self.ipvi,
            "I": self.i,
            "RVI": self.rvi,
            "MRVI": self.mrvi,
            "MSAVI": self.m_savi,
            "NormG": self.norm_g,
            "NormNIR": self.norm_nir,
            "NormR": self.norm_r,
            "NGRDI": self.ngrdi,
            "RI": self.ri,
            "S": self.s,
            "IF": self._if,
            "DVI": self.dvi,
            "TVI": self.tvi,
            "NDRE": self.ndre,
        }

        try:
            return funcs[index]()
        except KeyError:
            print("Index not in the list!")
            return False

    def arv12(self):
        return -0.18 + (1.17 * ((self.nir - self.red) / (self.nir + self.red)))

    def ccci(self):
        return ((self.nir - self.redEdge) / (self.nir + self.redEdge)) / (
            (self.nir - self.red) / (self.nir + self.red)
        )

    def cvi(self):
        return self.nir * (self.red / (self.green**2))

    def gli(self):
        return (2 * self.green - self.red - self.blue) / (
            2 * self.green + self.red + self.blue
        )

    def ndvi(self):
        return (self.nir - self.red) / (self.nir + self.red)

    def bndvi(self):
        return (self.nir - self.blue) / (self.nir + self.blue)

    def red_edge_ndvi(self):
        return (self.redEdge - self.red) / (self.redEdge + self.red)

    def gndvi(self):
        return (self.nir - self.green) / (self.nir + self.green)

    def gbndvi(self):
        return (self.nir - (self.green + self.blue)) / (
            self.nir + (self.green + self.blue)
        )

    def grndvi(self):
        return (self.nir - (self.green + self.red)) / (
            self.nir + (self.green + self.red)
        )

    def rbndvi(self):
        return (self.nir - (self.blue + self.red)) / (self.nir + (self.blue + self.red))

    def pndvi(self):
        return (self.nir - (self.green + self.red + self.blue)) / (
            self.nir + (self.green + self.red + self.blue)
        )

    def atsavi(self, x=0.08, a=1.22, b=0.03):
        return a * (
            (self.nir - a * self.red - b)
            / (a * self.nir + self.red - a * b + x * (1 + a**2))
        )

    def bwdrvi(self):
        return (0.1 * self.nir - self.blue) / (0.1 * self.nir + self.blue)

    def ci_green(self):
        return (self.nir / self.green) - 1

    def ci_rededge(self):
        return (self.nir / self.redEdge) - 1

    def ci(self):
        return (self.red - self.blue) / self.red

    def ctvi(self):
        ndvi = self.ndvi()
        return ((ndvi + 0.5) / (abs(ndvi + 0.5))) * (abs(ndvi + 0.5) ** (1 / 2))

    def gdvi(self):
        return self.nir - self.green

    def evi(self):
        return 2.5 * (
            (self.nir - self.red) / (self.nir + 6 * self.red - 7.5 * self.blue + 1)
        )

    def gemi(self):
        n = (2 * (self.nir**2 - self.red**2) + 1.5 * self.nir + 0.5 * self.red) / (
            self.nir + self.red + 0.5
        )
        return n * (1 - 0.25 * n) - (self.red - 0.125) / (1 - self.red)

    def gosavi(self, y=0.16):
        return (self.nir - self.green) / (self.nir + self.green + y)

    def gsavi(self, n=0.5):
        return ((self.nir - self.green) / (self.nir + self.green + n)) * (1 + n)

    def hue(self):
        return np.arctan(
            ((2 * self.red - self.green - self.blue) / 30.5) * (self.green - self.blue)
        )

    def ivi(self, a=None, b=None):
        return (self.nir - b) / (a * self.red)

    def ipvi(self):
        return (self.nir / ((self.nir + self.red) / 2)) * (self.ndvi() + 1)

    def i(self):
        return (self.red + self.green + self.blue) / 30.5

    def rvi(self):
        return self.nir / self.red

    def mrvi(self):
        return (self.rvi() - 1) / (self.rvi() + 1)

    def m_savi(self):
        return (
            (2 * self.nir + 1)
            - ((2 * self.nir + 1) ** 2 - 8 * (self.nir - self.red)) ** (1 / 2)
        ) / 2

    def norm_g(self):
        return self.green / (self.nir + self.red + self.green)

    def norm_nir(self):
        return self.nir / (self.nir + self.red + self.green)

    def norm_r(self):
        return self.red / (self.nir + self.red + self.green)

    def ngrdi(self):
        return (self.green - self.red) / (self.green + self.red)

    def ri(self):
        return (self.red - self.green) / (self.red + self.green)

    def s(self):
        max_value = np.max([np.max(self.red), np.max(self.green), np.max(self.blue)])
        min_value = np.min([np.min(self.red), np.min(self.green), np.min(self.blue)])
        return (max_value - min_value) / max_value

    def _if(self):
        return (2 * self.red - self.green - self.blue) / (self.green - self.blue)

    def dvi(self):
        return self.nir / self.red

    def tvi(self):
        return (self.ndvi() + 0.5) ** (1 / 2)

    def ndre(self):
        return (self.nir - self.redEdge) / (self.nir + self.redEdge)
