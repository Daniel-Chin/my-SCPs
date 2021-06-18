from matplotlib import pyplot as plt

def sim(T, dt = .001):
    d = 0.01928
    v = 0
    t = 0
    tt = []
    vv = []
    dd = []

    while t < T:
        f = (d ** 2) * 426.7998
        a = f / .0340611534
        v += a * dt
        d += 2 * v * dt
        t += dt
        tt.append(t)
        vv.append(v)
        dd.append(d)
    print('terminal:', t, v, d)
    
    plt.plot(tt, vv)
    plt.xlabel('time (s)')
    plt.ylabel('velocity (m/s)')
    plt.show()
    plt.plot(tt, dd)
    plt.xlabel('time (s)')
    plt.ylabel('distance (m)')
    plt.show()

sim(.136, .0001)
# sim(.1, .0001)
