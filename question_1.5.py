import numpy as np
import matplotlib.pyplot as plt


def func_f(x): return np.log(x)


def forward_approx(x, del_x): return (func_f(x+del_x) - func_f(x))/del_x


def backward_approx(x, del_x): return (func_f(x)-func_f(x-del_x))/del_x


def central_approx(x, del_x): return (func_f(x+del_x)-func_f(x-del_x))/(2*del_x)


def error(x, y): return np.abs(x-y)


def main():
    fig1, ax1 = plt.subplots()
    del_x = 0.1
    x = np.linspace(1, 3, 100)
    forward = forward_approx(x, del_x)
    backward = backward_approx(x, del_x)
    central = central_approx(x, del_x)
    ax1.plot(x, forward, color="red", label="forward")
    ax1.plot(x, backward, color="green", label="backward")
    ax1.plot(x, central, color="blue", label="central")
    # derivative of ln(x) = 1/x
    ax1.plot(x, 1/x, color="black", label="derivative")
    ax1.set_xlabel("x")
    ax1.set_ylabel("dx")
    ax1.set_title("derivatives")
    ax1.legend()

    # x-axis should be the step size
    fig2, ax2 = plt.subplots()
    ax2.loglog(x, error(1/x, forward), color="red")
    ax2.loglog(x, error(1/x, backward), color="green")
    ax2.loglog(x, error(1/x, central), color="blue")
    ax2.set_title("errors")

    plt.show()


if __name__ == "__main__":
    main()
