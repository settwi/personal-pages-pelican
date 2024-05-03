Title: Coplanar waveguides with shielding vias
Status: draft
Date: 2024-04-27 11:00
Slug: coplanar-waveguides-with-vias
Summary: Discussion on how to design coplanar waveguides with shielding vias, something which seems to be lacking online.

## Intro
### If you want to get equations for impedance, skip ahead to the [impedance equations](#impedance-equations).
### A Python script for computing impedances given different geometries can be found at [this GitHub gist]().

**Why you should care:** stitching vias impose Dirichlet boundary conditions on the electric fields of electromagnetic waves traveling through the coplanar waveguide so you can't just ignore them!

Here we report some equations which can be used to compute the characteristic impedance of coplanar
    waveguides (CPW) with vias stitched around them.
Different people use different terms to refer to these things;
    I'm gonna call them "stitched CPWs" or SCPW.
I haven't found a post online that communicates these effectively;
    most just say "use a full-wave simulation to figure it out."
The impedance seems pretty elementary to compute using (for example)
    [quasistatic conformal mapping techniques](https://doi.org/10.1080/00207219008921226).

<img src="{attach}static/images/shielded-cpw.svg" alt="shielded-cpw" width="80%"/>

*Coplanar waveguide with vias stitched around it. Stolen from [Altair Engineering docs](https://altair.com/).*

Anyway--there **are** closed form expressions to compute the impedance of such a waveguide,
    taking into account the effect of the boundary conditions imposed by the stitching vias.
So we'll report those here and give an example application.

I am ripping most of this content from Chapter 3 of a very nice book
    by Rainee Simons,
    *[Coplanar Waveguide Circuits, Components, and Systems](https://onlinelibrary.wiley.com/doi/book/10.1002/0471224758)*.
If you are curious about things like the effect of finite conductivity or finite conductor thickness,
    which you ought to be if you're here,
    I suggest getting the book and perusing Chapter 3.

## Why can't I find these damn equations anywhere?!?
Across the internet there seems to be a consensus that,

- Coplanar waveguides are [superior to microstriplines at high-frequency](
    https://www.microwavejournal.com/blogs/1-rog-blog/post/24374-comparing-microstrip-and-grounded-coplanar-waveguide#understanding-coplanar-waveguide-with-ground),
    but [can excite parallel-plate modes without via stitching around them](https://ieeexplore.ieee.org/document/6101804)
- There [are not closed-form expressions](
    https://resources.altium.com/p/coplanar-waveguide-with-ground)
    for computing the characteristic impedance
    of coplanar waveguides with "via stitching" surrounding them.

As I alluded to in the intro, **there are closed forms!**
They do not apply in all geometries as mentioned in other blog posts.
However, for many geometries they are useful.
The equations presented here are good (<2% deviation) approximations
    of quasistatic solutions to Laplace's equation.

Of course,
    for the most accurate results,
    using a full-wave simulation is the way to go.
However for prototyping on a budget,
    or for designs which aren't as sensitive,
    the closed-form expressions here can be of use.

## Idealized problem: conducting walls instead of vias
### Overview
In Chapter 3 of Simmons's book,
    equations are presented for an approximate form of the stitched CPW,
    that where the ground plane below the waveguide strip
    is connected to semi-infinite conducting lateral walls.

**IMPORTANT:** The spacing $g$ is assumed to be $g = S/2 + W$.
This is a limitation of the model but we get nice closed-form expressions.
Also note that if your waveguide is shaped with a "bad" aspect ratio
    and your stripline-to-ground plane spacing is too small,
    the dielectric-filled rectangular modes may be excited.
See [*Microwave Engineering*, (Pozar 2012)](https://www.wiley.com/en-us/Microwave+Engineering,+4th+Edition-p-9780470631553) for equations.

<img src="{attach}static/images/semi-inf-cpw.png" alt="semi-infinite walls" width="80%"/>

*Semi-infinite conducting lateral walls around a conductor-backed coplanar waveguide.*
*Stolen from Simmons.*

We can fabricate a structure like the one above using closely-stitched vias, say $d < \lambda / 10$
    for the wavelength of interest.

### Impedance equations {#impedance-equations}
#### *A note on the quasistatic approximation*
*In this case typical dimensions $L$ are 1mm and typical timescales $\tau$ are 1ns to 50ps.*
*The quasistatic approximation is valid when $L / \tau \ll v_g$ i.e. the wave group velocity.*
*For TEM and quasi-TEM modes the group velocity is just $v_g = c \cdot \varepsilon_r^{-1/2}$.*
*For FR-4 $\varepsilon_r \sim 4$ and so we must satisfy*
$$ \frac{L}{\tau} = [10^6, 10^7]\text{ m/s} << v_g = 2\times10^8\text{ m/s}$$

_**So for signals of frequency 1 GHz the quasistatic approximation is definitely valid.
At 20 GHz (i.e. $\tau = 50 ps$) there may be significant deviations.**_

#### Results collected from Simmons
These are a mouthful but are adapted by Simmons from [Rowe & Lao 1983](https://ieeexplore.ieee.org/document/1131631) and
    other publications mentioned in the textbook.
Empirical expressions are derived from their quasistatic solutions to Laplace's equation.

**The characteristic impedance $Z_0$** of the above waveguide is
$$ \frac{1}{Z_0} = 
    \frac{5q}{1 + 5q} \cdot \frac{1}{Z_m} +
    \frac{1}{1 + q} \cdot \frac{1}{Z_c},
$$

where

$$ q =
    \frac{S}{h}
    \left( \frac{S + 2W}{S} - 1\right)
    \left( 3.6 - 2 \exp\left[-\frac{\varepsilon_r + 1}{4}\right]
    \right).
$$

We may use approximations for the terms $Z_m$ and $Z_c$, correct to within 2% of the exact solutions.

For $S/h \le 1$ we have: $$ Z_m = \frac{\eta}{2 \pi \sqrt{\varepsilon_\text{effm}}} \ln \left[\frac{8h}{S} + \frac{S}{4h} \right].$$

Then for for $S/h \ge 1$:
$$ Z_m =
    \frac{\eta}{\sqrt{\varepsilon_\text{effm}}}\left(
        \frac{S}{h} + 1.393 + 0.667 \ln\left[\frac{S}{h} + 1.444\right]
    \right)^{-1}
$$

Above $\eta = 377 \Omega$ is the impedance of free space, and the effective *m* dielectric constant is:
$$
\varepsilon_\text{effm} =
    \frac{\varepsilon_r + 1}{2} + \frac{\varepsilon_r - 1}{2} \left(1 + \frac{10h}{S}\right)^{-1/2}.
$$


The $Z_c$ term has similar approximations:

$$ Z_c = \frac{30 \pi}{\sqrt{\varepsilon_\text{effc}}} \frac{K\left(\sqrt{1 - k^2}\right)}{K(k)}. $$

In this expression the $K$ function is the
    [complete elliptic integral of the first kind](https://mathworld.wolfram.com/CompleteEllipticIntegraloftheFirstKind.html),
    and $k$ and $\varepsilon_\text{effc}$ are defined as follows:
$$ k = \frac{S}{S + 2W} $$
$$
\varepsilon_\text{effc} = 
    \frac{\varepsilon_r + 1}{2} \varepsilon^\star
$$
$$
\varepsilon^\star = 
    \tan\left[0.775\ln\frac{h}{W} + 1.75\right] + 
    \frac{kW}{h}\left\{
        0.04 - 0.7k + (1 - \varepsilon_r/10)(1 + 4k) / 400
    \right\}
$$

Those are the equations you need to compute the impedances.
There are other cases considered in Simmons chapter 3,
    such as the effect of conductors of finite size,
    lossy dielectrics,
    and modified geometries.

A calculator for various geometries with variables you can modify is given in [this GitHub gist]().

## Example application: multi-SiPM readout for scintillation detectors
### Setup
We are using [silicon photomultipliers (SiPMs)](https://en.wikipedia.org/wiki/Silicon_photomultiplier)
    to read out scintillation photons in an X-ray detector.
The typical rise times of our signals are ~1ns to ~100ns,
    so RF techniques apply.
Each scintillation crystal couples to six SiPM and we read them out as a combined unit.

After pre-amplifying the SiPM pulses immediately at the output using a
    ["transimpedance amplifier"](https://en.wikipedia.org/wiki/Transimpedance_amplifier)
    (current to voltage converter),
    we need to sum the voltages into a single signal.

These pulses have frequency components at least in the ~100MHz to 1 GHz regime.
Due to physical constraints of the crystal the propagation length along the PCB is on the order of
    $\lambda / 10$ for the fastest components.
So we need to use waveguides to move the electromagnetic energy.
We also want:

- Low energy loss due to spurious mode excitation
- Ease of manufacturing
- Small form factor
- Good isolation between physical channels, which can be some millimeters apart

<img src="{attach}static/images/rf-layout-example-crop.png" alt="layout example" width="80%"/>

_Example layout of **unshielded** CPW on a prototype SiPM readout PCB._
_The spacing between readout channels is approaching $\lambda / 10$ for $\tau = 1\text{ns}$._

Stitched coplanar waveguides fit the bill here.
We can use the calculator given in the gist to figure out what we need.

### How to compute an impedance
We want a characteristic impedance $Z_0 = 50\ \Omega$.
Let's set the microstrip-to-ground plane spacing 
    $h = 0.994$mm and the dielectric constant
    $\varepsilon_r = 4.1$.
These values happen to line up with a controlled impedance setup on
    [JLC PCB](https://jlcpcb.com/impedance).
The equations form a nonlinear system,
    subject to the constraint $g = S/2 + W$,
    where $g$ is the via wall-to-microstrip center distance as defined in the above figure.

We can easily use numerics to solve the equation for $S$ given a $W$,
    or $W$ given an $S$.
For this computation let's take $W = 0.2$mm and go from there.
Using the gist calculator, we find:
- $S = $mm
- $g = $mm, i.e. the spacing of vias from microstrip center.
