"""
CORDIC Algorithm implementation
Authors:
--  Robert Alexander Limas Sierra
--  Wilson Javier Perez Holguin
Year: 2020
"""
from CORDIC import Cordic
from utils import deg_to_rad
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


matplotlib.rcParams.update({
    'font.size': 18,
    "grid.color": "0.5",
    "grid.linestyle": "-",
})


def convergence_test_linear():
    # Linear Coordinate System
    # Rotation mode: CORDIC algorithm compute x * z when |z| < 2
    # Vectoring mode: CORDIC algorithm compute y / x when |quotient| < 2
    x = 2
    z = np.arange(-3, 3, 0.01)
    products, quotients = [], []
    cordic = Cordic()
    for i in z:
        products.append(cordic.product(x, i))
    fig, axes = plt.subplots(1, 2)
    axes[0].plot(z, products, 'b-')
    axes[0].set_title('Rotation Mode')
    axes[0].set_ylabel('Products')
    axes[0].set_xlabel('Z Values')
    axes[0].grid()
    z = np.arange(-5, 5, 0.01)
    for i in z:
        quotients.append(cordic.division(x, i))
    axes[1].plot(z, quotients, 'b-')
    axes[1].set_title('Vectoring Mode')
    axes[1].set_ylabel('Quotients')
    axes[1].set_xlabel('Y Values')
    axes[1].grid()
    plt.show()


def convergence_test_circular():
    # Circular Coordinate System
    # Rotation mode: CORDIC algorithm compute when |angle| < 99.9°
    # Vectoring mode: CORDIC algorithm when |result| < 99.9°
    z = np.arange(-120, 120, 0.01)
    cos, arctan = [], []
    cordic = Cordic()
    for i in z:
        cos_cordic, _ = cordic.cos_sin(i)
        cos.append(cos_cordic)
    fig, axes = plt.subplots(1, 2)
    axes[0].plot(z, cos, 'b-')
    axes[0].set_title('Rotation Mode')
    axes[0].set_ylabel('Magnitude')
    axes[0].set_xlabel('Angle')
    axes[0].grid()
    for i in z:
        x = np.cos(deg_to_rad(i))
        y = np.sin(deg_to_rad(i))
        arctan_cordic = cordic.artan(x, y)
        arctan.append(arctan_cordic)
    axes[1].plot(z, arctan, 'b-')
    axes[1].set_title('Vectoring Mode')
    axes[1].set_ylabel('Angle')
    axes[1].set_xlabel('Angle')
    axes[1].grid()
    plt.show()


def convergence_test_hyperbolic():
    # Circular Coordinate System
    # Rotation mode: CORDIC algorithm compute when |angle| < 64°
    # Vectoring mode: CORDIC algorithm when |result| < 64°
    z = np.arange(-70, 70, 0.01)
    cosh, arctanh = [], []
    cordic = Cordic()
    for i in z:
        cosh_cordic, _ = cordic.cosh_sinh(i)
        cosh.append(cosh_cordic)
    fig, axes = plt.subplots(1, 2)
    axes[0].plot(z, cosh, 'b-')
    axes[0].set_title('Rotation Mode')
    axes[0].set_ylabel('Magnitude')
    axes[0].set_xlabel('Angle')
    axes[0].grid()
    for i in z:
        x = np.cos(deg_to_rad(i))
        y = np.sin(deg_to_rad(i))
        arctanh_cordic = cordic.artanh(x, y)
        arctanh.append(arctanh_cordic)
    axes[1].plot(z, arctanh, 'b-')
    axes[1].set_title('Vectoring Mode')
    axes[1].set_ylabel('Angle')
    axes[1].set_xlabel('Angle')
    axes[1].grid()
    plt.show()
    

def convergence_test():
    convergence_test_hyperbolic()
    convergence_test_circular()
    convergence_test_linear()


def test():
    convergence_test()