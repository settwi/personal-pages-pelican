Title: How much power does a WiFi router deliver to a human body?
Date: 2024-05-03 11:00
Slug: wifi-microwaves-sunlight
Summary: Discussion on power radiated by WiFi routers vs. microwaves vs. sunlight.
Status: published

This post started out as a fun calculation to compare the power output by microwave ovens and by WiFi routers.
That's still what it is, but it is also a nice surface-level summary of the physics of antennas, sunlight, estimation, and the FCC.
Well, not the physics of the FCC, but I did learn why we hire professionals to read the regulations.

**The big takeaway is that, while it takes your microwave oven only about a minute to heat up a cup of coffee, it would take your WiFi router over ten thousand years to do the same!**

## How much energy do microwaves actually put into your food?
Microwave ovens use [magnetrons](https://en.wikipedia.org/wiki/Cavity_magnetron) to generate microwave radiation.
Generally they operate at ~2 GHz, the same frequency as WiFi.
We can compute how much power gets injected into the microwave oven "cavity",
    i.e. the part where you cook your food,
    and from that determine the energy flux into food.
The water molecules in the food absorb the microwaves and vibrate harder (turn the microwaves into heat).
I'm gonna use the example of a coffee cup here because that's what I'm drinking right now.

<img src="{attach}static/images/coffee.jpg" alt="coffee in a microwave" width="75%"/>

_Yes, that's my own coffee, in my own microwave._

The power injected into the microwave cavity is $P_\text{inj} = \epsilon \cdot P_\text{in}$,
    where $\epsilon$ is the efficiency of the microwave oven and varies from 0.5 to 0.9 based on Googling for efficiencies.

For a typical microwave,
    $P_\text{in} = 1 \text{ kW}$.
Assuming poor efficiency,
    the power that gets injected into the microwave box is about 500 W.

A typical microwave box is about $V = 2\text{ ft}^3 = 0.06 \text{m}^3$

If we assume the energy is flows uniformly from the top to the bottom of the microwave,
    ([which isn't a perfect assumption](https://www.youtube.com/watch?v=qhXbAoqWCwY) but should be good enough,)
    we can compute a power flux (irradiance):
$$I_\text{microwave} \approx
P_\text{inj} \cdot V^{-2/3}
= 3300 \text{ W/m}^2.$$
This calculation assumes that a typical microwave is a cube which is inaccurate but the number is close enough.

### How much energy goes into heating a cup of coffee?
A typical microwave (~3 kW/m$^2$ equivalent irradiance) can heat up a cup of coffee in about a minute. If the coffee is 8 US fl. oz. and the cup has a circular diameter of three inches, then the incident power is 
$$P_\text{inc} = \pi r_\text{cup}^2 \cdot I_\text{microwave} = 15\text{ W}$$
Across one minute the microwave delivers a total energy of 
$$\begin{aligned}
    E_\text{delivered} &= P_\text{inc} \cdot 1\text{ minute} \\
                       &= 900\text{ J} = 220 \text{ calories}
\end{aligned}
$$
Computing the same number from heat capacity, it would take about 700 J of energy to heat a coffee cup from room temperature to boiling. So this estimate is decent, within 30%.
#### Implication: in a minute the microwave heats up the coffee by about 200 calories. A minute in the microwave is like eating four Oreo cookies. I could go on...

## How much power does a WiFi router produce?
Now let's compute similar quantities for a WiFi router.
Routers broadcast their energy using antennas rather than magnetrons like in microwave ovens.

[Title 47, Chapter 1, Section 15.209](https://www.ecfr.gov/current/title-47/section-15.209) of the Code of Federal Regulations limits the electric field strength which may be radiated from a given non-broadcast antenna (or "[intentional radiator](https://www.ecfr.gov/current/title-47/part-15#p-15.3(o))" as they call it). For WiFi antennas the electric field strength may not exceed $500\ \mu\mathrm{V}/\mathrm{m}$ measured at a distance of 3 meters away. We need to jump through some hoops to convert that field strength into irradiance but it is straightforward if you know the right equations.

There's a complication: the radiation pattern for a given antenna is not uniform. The most simple dipole antennas have a radiation pattern which is axially symmetric but varies along the other directions like a donut.

<img src="{attach}static/images/dipole.jpg" alt="dipole radiation pattern"/>

_Radiation pattern of a dipole antenna of length $L = \lambda$, i.e. a single wavelength.
WiFi antennas are generally more like $L = \lambda / 10$ in length so the radiation pattern is different.
Credit: [antenna-theory.com](https://www.antenna-theory.com/antennas/dipole.php)_

For the sake of argument let's just assume that the WiFi antenna radiates isotropically with the maximum allowed electric field strength at 10 meters.
This would not be a practical antenna design,
    but it is a worst-case scenario which we can use to determine how much energy could be dumped into an object at the FCC limits.

First we need to convert the electric field strength measured at 3 meters to a power flux.
The energy density of an electric field can be derived by analyzing the potential energy equations for electrostatics,
    as in [Jackson](https://en.wikipedia.org/wiki/Classical_Electrodynamics_(book)) Chapter 1.11.
The result is that the energy density $w$ is given as
$$ w = \frac{\epsilon}{2} \mathbf{E} \cdot \mathbf{E}.$$

The power flux is the energy density multiplied by how fast it moves through space,
    which is the speed of light,
    at least in this case of an isotropic radiator.
For air the dielectric constant $\epsilon \approx \epsilon_0$ and the speed of light is approximately that of vacuum.
Thus the irradiance from a given electric field strength is
$$
\begin{aligned}
    I_\text{antenna} &= w \cdot c \\
                     &= c \frac{\epsilon_0}{2} E^2 \\
                     &= \frac{E^2}{2 Z_0} \\
                     &= 0.33 \text{ nW/m}^2 \\
                     &= \frac{I_\text{microwave}}{10000000000000},
\end{aligned}
$$
Where we have used that the speed of light
    $c = (\epsilon_0 \mu_0)^{-1/2}$ and $Z_0 = \sqrt{\mu_0 / \epsilon_0} \approx 377\ \Omega$ is the impedance of free space.
Already we can see that the WiFi router irradiance is very tiny compared to that of the microwave.

Now we can put in some numbers.
Standing three meters away from a typical WiFi antenna,
    and assuming the human body has a cross section of about
    $A = 2 \times 0.6 = 1.2$ m$^2$,
    the absolute maximum power a person could receive from its radiated power would be:
$$
\begin{aligned}
P_\text{max, human}(10\text{ meters}) &= I_\text{antenna} \cdot A \\
                                      & = \frac{(500\ \mu\text{V}/\text{m})^2}{2 \cdot 377\ \Omega} \cdot 1.2\text{ m}^2\\
&= 0.4 \text{ nW (!)}
\end{aligned}
$$
**So standing 30ft away from a WiFi antenna you'd get hit with about a nanowatt of power.**
The power in a loud fart is more than that.

Of course the power increases as you get closer,
    inversely proportional to the distance.
Say you are only one foot away. Then the incident power would be (noting 33 ft = 10 m):
$$
\begin{aligned}
P_\text{max, human}(1\text{ ft}) &= P_\text{max, human}(10\text{ m}) \cdot \frac{33^2}{1^2} \\
                                 &= 400 \text{nW}
\end{aligned}$$
Clearly 400 nW is more than 0.4 nW.
Still, this is a tiny, TINY amount of power.

### How long would it take the WiFi router to heat a cup of coffee?
Let's do the same analysis for the coffee cup. This time assume it's side-on with a height of three inches and the same diameter of three inches. We can scale the power delivered to the human by the ratio of areas to compute this. The incident power (calculated as in the case of the human body) is 
$$\begin{aligned}
    P_\text{max, coffee}(1\text{ ft}) &= \\
                                      &= P_\text{max, human}(1\text{ ft}) \\
                                      & \quad \times \frac{\text{cross section of coffee}}{\text{cross section of a human}} \\
                                      &= 2\text{ nW}
\end{aligned}$$
The power delivered to the coffee cup 1 foot away from the antenna is about 2 nanowatts.

From before we know it takes about four Oreo cookies (200 calories, or 900 Joules) to heat the coffee cup up in the microwave. At a power delivered of two nanowatts, this would take 
$$ t = \frac{900\text{ J}}{2\text{ nW}} = 13000\text{ years}$$
This is neglecting the cooling of the coffee cup due to thermal conduction.
Setting it out in the sunlight would do a better job of warming it up.

#### Takeaway: heating up a cup of coffee with a WiFi router would take 13,000 years assuming it doesn't conduct any heat away.

## Why does the FCC even bother regulating the power output of antennas if it's so small?
Because all radio equipment is sensitive to broadband contamination.
The primary purpose of the regulations isn't to protect _people_,
    although the regulations do a good job of that.
The regulations are to protect communications equipment and keep it functioning.

## How does a WiFi router compare to the power received on a sunny day?
With no cloud cover,
    the irradiance from the sun is about 1000 W/m$^2$.
That's about one-third of the microwave irradiance,
    **but about a million billion times that of the router!**
The radiation doesn't penetrate as deeply because it is shorter wavelength.
But, we still need to wear sunscreen because ultraviolet light is what gives you skin cancer.

**Sunlight is many times more dangerous than radiation from WiFi routers.**

<img src="{attach}static/images/sunlight-wifi.jpeg" alt="sunlight shining on wifi" style="max-width: 60%"/>

_Generated using [deep ai](https://deepai.org/machine-learning-model/text2img)_
