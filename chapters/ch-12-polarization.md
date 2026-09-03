---
title: "12. Polarization"
short_title: "Chapter 12"
label: ch-12-polarization
---

(ch-12)=

# 12. Polarization

In this chapter, we return to (9.46)-(9.48) and examine the consequences of Maxwell’s equations in a homogeneous material for a general traveling electromagnetic plane wave. The extra complication is polarization.

::::{admonition} Chapter Preview
:class: preview

Polarization is a general feature of transverse waves in three dimensions. The general electromagnetic plane wave has two polarization states, corresponding to the two directions that the electric field can point transverse to the direction of the wave’s motion. This gives rise to much interesting physics.

1. We introduce the idea of polarization in the transverse oscillations of a string.

2. We discuss the general form of electromagnetic waves and describe the polarization state in terms of a complex, two-component vector, $Z$. We compute the energy and momentum density as a function of $Z$ and discuss the Poynting vector. We describe the varieties of possible polarization states of a plane wave: linear, circular and elliptical.

3. We describe “unpolarized light,” and explain how to generate and manipulate polarized light with polarizers and wave plates. We discuss the rotation of the plane of linearly polarized light by optically active substances.

4. We analyze the reflection and transmission of polarized light at an angle on a boundary between dielectrics.
::::

## 12.1: The String in Three Dimensions

In most of our discussions of wave phenomena so far, we have assumed that the motion is taking place in a plane, so that we can draw pictures of the system on a sheet of paper. We have implicitly been restricting ourselves to two-dimensional waves. This is all right for longitudinal oscillations in three dimensions, because all the action is taking place along a single line. However, for transverse oscillations, going from two dimensions to three dimensions makes an enormous difference because there are two transverse directions in which the system can oscillate.

For example, consider a string in three dimensions, stretched in the $z$ direction. Each point on the string can oscillate in both the $x$ direction and the $y$ direction. If the system were not approximately linear, this could be a horrendous problem. Linearity allows us to solve the problem of oscillation in the $x$-$z$ plane separately from the problem of oscillation in the $y$-$z$ plane. We have already solved these two-dimensional problems in chapter 5. Then we can simply put the results together to get the most general motion of the three-dimensional system. In other words, we can treat the $x$ component of the transverse oscillation and the $y$ component as completely independent.

Suppose that there is a harmonic traveling wave in the +$z$ direction in the string. The displacement of the string at $z$ from its equilibrium position, $(0, 0, z)$, can be written as 
$$
\vec{\Psi}(z, t)=\operatorname{Re}\left[\left(\psi_{1} \hat{x}+\psi_{2} \hat{y}\right) e^{i(k z-\omega t)}\right] \tag{12.1} \label{eq-12-1}
$$

where $\hat{x}$ and $\hat{y}$ are unit vectors in the $x$ and $y$ direction and $\psi_{1}$ and $\psi_{2}$ are complex parameters describing the amplitude and phase of the oscillations in the $x$-$z$ plane and the $y$-$z$ plane, 
$$
\psi_{j}=A_{j} e^{i \phi_{j}} \text { for } j=1 \text { to } 2. \tag{12.2} \label{eq-12-2}
$$

It is convenient to arrange these parameters into a complex vector 
$$
Z=\left(\begin{array}{l}
\psi_{1} \\
\psi_{2}
\end{array} \tag{12.3} \label{eq-12-3}\right) ,
$$

which gives a complete description of the motion of the string.

### Polarization

:::{figure} ../images/lt-32886-clipboard_ec5b9c9bb8c0ae21e2fba16d99f112485.png
:label: fig-12-11
:enumerator: 12.11
:alt: Figure

:::12-1

“Polarization” refers to the nature of the motion of a point on the string (or other transverse oscillation). This motion is animated in program 12-1. You may want to read the discussion below with this program running.

If $\phi_{1}=\phi_{2}$, or $A_{1}$ or $A_{2}$ is zero, then [12.3](#eq-12-3) represent a linearly polarized string. Linear polarization is easy to understand. It means that each point on the string is oscillating back and forth in a fixed plane. For example, 
$$
u_{1}=\left(\begin{array}{l}
1 \\
0
\end{array} \tag{12.4} \label{eq-12-4}\right)
$$

$$
u_{2}=\left(\begin{array}{l}
0 \\
1
\end{array} \tag{12.5} \label{eq-12-5}\right)
$$

represent strings oscillating in the $x$-$z$ plane and the $y$-$z$ plane respectively. A string oscillating in a plane an angle $\theta$ from the positive $x$ axis (towards the positive $y$ axis) is represented by 
$$
u_{\theta}=\left(\begin{array}{l}
\cos \theta \\
\sin \theta
\end{array} \tag{12.6} \label{eq-12-6}\right) .
$$

This is shown in the $x$-$y$ plane in [Figure 12.1](#fig-12-1). The polarization vectors [12.4](#eq-12-4)-[12.6](#eq-12-6) can be multiplied by a phase factor, $e^{i \phi}$, without affecting the polarization state in any important way. This just corresponds to an overall resetting of the clock.

:::{figure} ../images/lt-32887-clipboard_e99b76e76bcac0c23aa0707a8d7400636.png
:label: fig-12-1
:enumerator: 12.1
:alt: u_{1}, u_{2} and u_{\theta}.

$u_{1}$, $u_{2}$ and $u_{\theta}$.
:::
More interesting is circular polarization. A circularly polarized wave in a string is represented by either 
$$
\left(\begin{array}{l}
1 \\
i
\end{array} \tag{12.7} \label{eq-12-7}\right)
$$

or 
$$
\left(\begin{array}{c}
1 \\
-i
\end{array} \tag{12.8} \label{eq-12-8}\right) .
$$

In [12.7](#eq-12-7), the $y$ component lags behind the $x$ component by $\pi / 2\left(=\phi_{2}\right)$. Thus, at any fixed point in space, the field rotates from $x$ to $y$, or in the counterclockwise direction viewed from the positive $z$ axis (with the wave coming at you), as shown in [Figure 12.2](#fig-12-2). This is called “left-circular polarization” because the string resembles a left-handed screw. Likewise, 
$$
\left(\begin{array}{c}
1 \\
-i
\end{array} \tag{12.9} \label{eq-12-9}\right) .
$$

represents clockwise rotation of the string. This is called “right-circular polarization.”

:::{figure} ../images/lt-32888-clipboard_e3b564d00a640b4bcbef1572031e5dd37.png
:label: fig-12-2
:enumerator: 12.2
:alt: Circular polarization.

Circular polarization.
:::
The vector 
$$
\left(\begin{array}{c}
A \\
i B
\end{array} \tag{12.10} \label{eq-12-10}\right)
$$

with $A > B > 0$ represents elliptical polarization. A point on the string traces out an ellipse with semi-major axis $A$ along the 1 axis and semi-minor axis $B$ along the 2 axis, with counterclockwise rotation, as shown in [Figure 12.3](#fig-12-3)

:::{figure} ../images/lt-32889-clipboard_e93d7f3eadef47dda249e0efa0263a893.png
:label: fig-12-3
:enumerator: 12.3
:alt: Elliptical polarization with long axis in the x direction.

Elliptical polarization with long axis in the $x$ direction.
:::
:::{figure} ../images/lt-32890-clipboard_e118e7e46306b91a5d90479d266959693.png
:label: fig-12-4
:enumerator: 12.4
:alt: General elliptical polarization.

General elliptical polarization.
:::
A completely general vector can be written in the following form: 
$$
\left(\begin{array}{l}
\psi_{1} \\
\psi_{2}
\end{array}\right)=e^{i \phi}\left(\begin{array}{c}
A \cos \theta-i B \sin \theta \\
A \sin \theta+i B \cos \theta
\end{array} \tag{12.11} \label{eq-12-11}\right)
$$

with $A \geq|B|$ and $0 \leq \theta<\pi$ and $\phi$ is real phase (which is not very relevant relevant to the physics but can be there to make the math look uglier). This represents elliptical polarization with semi-major axis $A$ at an angle $\theta$ with the 1 axis, as in 
$$
u_{\theta}=\left(\begin{array}{c}
\cos \theta \\
\sin \theta
\end{array} \tag{12.12} \label{eq-12-12}\right) .
$$

and semi-minor axis $B$ as shown in [Figure 12.4](#fig-12-4). If $B$ is positive (negative), the rotation is counterclockwise (clockwise). The physically interesting parameters $A$, $B$ and $\theta$ can be found from $\psi_{1}$ and $\psi_{2}$ as follows: 
$$
\begin{gathered}
A^{2}+B^{2}=\left|\psi_{1}\right|^{2}+\left|\psi_{2}\right|^{2} , \\
A B=-\operatorname{Im}\left(\psi_{1} \psi_{2}^{*}\right) .
 \tag{12.13} \label{eq-12-13}
\end{gathered}
$$

Thus, 
$$
A \pm B=\sqrt{\left|\psi_{1}\right|^{2}+\left|\psi_{2}\right|^{2} \mp 2 \operatorname{Im}\left(\psi_{1} \psi_{2}^{*}\right)} , \tag{12.14} \label{eq-12-14}
$$

gives $A$ and $B$. Then $\theta$ satisfies 
$$
\begin{aligned}
&\left(A^{2}-B^{2}\right) \cos 2 \theta=\left|\psi_{1}\right|^{2}-\left|\psi_{2}\right|^{2} , \\
&\left(A^{2}-B^{2}\right) \sin 2 \theta=2 \operatorname{Re}\left(\psi_{1} \psi_{2}^{*}\right) .
 \tag{12.15} \label{eq-12-15}
\end{aligned}
$$

Notice that the overall phase factor $e^{i \phi}$ cancels out in [12.11](#eq-12-11)-[12.13](#eq-12-13).

## 12.2: Electromagnetic Waves

### General Electromagnetic Plane Waves

![Figure](../images/lt-32891-clipboard_e6158ab7274d56dd646f1ae4175b430a7.png)12-1

We saw in chapters 8 and 9 that an electromagnetic plane wave traveling in the $+z$ direction looks like this, 
$$
E_{x}(z, t)=\varepsilon_{x} e^{i(k z-\omega t)}, \quad E_{y}(z, t)=\varepsilon_{y} e^{i(k z-\omega t)}, \tag{12.16} \label{eq-12-16}
$$

$$
B_{x}(z, t)=\beta_{x} e^{i(k z-\omega t)}, \quad B_{y}(z, t)=\beta_{y} e^{i(k z-\omega t)}, \tag{12.17} \label{eq-12-17}
$$

$$
E_{z}(z, t)=B_{z}(z, t)=0, \tag{12.18} \label{eq-12-18}
$$

where the $\beta$s are determined by Maxwell’s equations to be 
$$
\beta_{y}=\frac{n}{c} \varepsilon_{x}, \quad \beta_{x}=-\frac{n}{c} \varepsilon_{y} . \tag{12.19} \label{eq-12-19}
$$

As usual, we have written the wave with the irreducible time dependence, $e^{-i \omega t}$. To get the real electric and magnetic fields, we take the real part of [12.14](#eq-12-14)-[12.15](#eq-12-15). Note, in particular, that the constants $\varepsilon_{j}$ and $\beta_{j}$ for $j = x$ and $y$ may be complex.

The restriction to motion in the $z$ direction is not important. Because the physics of Maxwell’s equations is invariant under rotations in three-dimensional space, we can write down the form of a plane wave moving with an arbitrary $\vec{k}$ vector by extracting the features of [12.14](#eq-12-14)-[12.17](#eq-12-17) that do not depend on the direction. These are:

1. $\vec{k}$, $\vec{E}$ and $\vec{B}$ are mutually orthogonal vectors, 
$$
\vec{k} \cdot \vec{E}=\vec{k} \cdot \vec{B}=\vec{E} \cdot \vec{B}=0 ; \tag{12.20} \label{eq-12-20}
$$

2. $\vec{B}$ is determined by the cross product 
$$
\vec{B}=\frac{n}{c} \hat{k} \times \vec{E}=\frac{1}{\omega} \vec{k} \times \vec{E} , \tag{12.21} \label{eq-12-21}
$$

    where $\hat{k}$ is a unit vector in the direction of the $\vec{k}$ vector, the direction of propagation of the wave.

These two conditions imply that a general real electromagnetic plane wave can be written as 
$$
\begin{aligned}
&\vec{E}=\operatorname{Re}\left(\vec{e}(\vec{k}) e^{i \vec{k} \cdot \vec{r}-i \omega t}\right) \\
&\vec{B}=\operatorname{Re}\left(\vec{b}(\vec{k}) e^{i \vec{k} \cdot \vec{r}-i \omega t}\right)
 \tag{12.22} \label{eq-12-22}
\end{aligned}
$$

where the vectors, $\vec{e}$ and $\vec{b}$, are complex, in general, satisfying 
$$
\vec{b}(\vec{k})=\frac{1}{\omega} \vec{k} \times \vec{e}(\vec{k})=\frac{n}{c} \hat{k} \times \vec{e}(\vec{k}) \quad \text { and } \quad \hat{k} \cdot \vec{e}(\vec{k})=0 . \tag{12.23} \label{eq-12-23}
$$

There are two things to note about the relations, [12.21](#eq-12-21).

1. It is enough to specify the direction of the electric field, $\vec{e}(\vec{k})$. The magnetic field is then determined by [12.21](#eq-12-21). The vector, $\vec{e}$ is called the **“polarization”** of the electromagnetic wave.

2. Because of [12.21](#eq-12-21), the polarization is perpendicular to $\vec{k}$, and thus lives in a two-dimensional vector space.

In the two-dimensional space perpendicular to $\vec{k}$, we can choose a basis of real vectors, $\hat{e}_{1}$ and $\hat{e}_{2}$, where 
$$
\hat{e}_{1} \cdot \hat{k}=\hat{e}_{2} \cdot \hat{k}=\hat{e}_{1} \cdot \hat{e}_{2}=0, \quad \hat{e}_{1} \times \hat{e}_{2}=\hat{k}. \tag{12.24} \label{eq-12-24}
$$

For example, for a plane wave traveling in the $z$ direction, $\hat{k}=\hat{z}$, we could take $e_{1}=\hat{x}$ and $e_{2}=\hat{y}$. Then we can write 
$$
\vec{e}(\vec{k})=\psi_{1} \hat{e}_{1}+\psi_{2} \hat{e}_{2}. \tag{12.25} \label{eq-12-25}
$$

The components, $\psi_{1}$ and $\psi_{2}$ go into the the two-dimensional vector, [12.3](#eq-12-3), that describes the polarization state of the electromagnetic wave, just as it describes the polarization state of the string.[^12-2-1] We can always go back to the components of the electric field using [12.23](#eq-12-23) and [12.20](#eq-12-20) and then find the magnetic field using [12.21](#eq-12-21).

Now the entire discussion of transverse waves on a string from [12.4](#eq-12-4) to [12.13](#eq-12-13) can be taken over to describe polarized light. The direction of displacement of the string goes over directly into the direction of the electric field. Thus the animation in program 12-1 applies just as well to the electric field in a polarized wave as to polarization in a string.

### Energy and Intensity

The energy density in an electromagnetic field is 
$$
\mathcal{E}=\frac{1}{2}\left(\epsilon \vec{E}^{2}+\frac{1}{\mu} \vec{B}^{2}\right) . \tag{12.26} \label{eq-12-26}
$$

Because the energy density is a nonlinear function of the field strengths, we must use **real** fields in [12.24](#eq-12-24). The momentum density is 
$$
\overrightarrow{\mathcal{P}}=\epsilon \vec{E} \times \vec{B} . \tag{12.27} \label{eq-12-27}
$$

The Poynting vector, a measure of energy flow, is 
$$
\vec{S}=c^{2} \overrightarrow{\mathcal{P}} . \tag{12.28} \label{eq-12-28}
$$

These quantities satisfy 
$$
\frac{\partial}{\partial t} \mathcal{E}+\vec{\nabla} \cdot \vec{S}=0 . \tag{12.29} \label{eq-12-29}
$$

The Poynting vector is useful because it measures the intensity of the wave, the energy per unit time per unit area carried by the electromagnetic wave. The relation, [12.27](#eq-12-27), then expresses conservation of energy. The sum of the change in the energy density at any point plus the energy flowing away from it is zero.

To see what these quantities look like in terms of the vector, $Z$, let us compute the electric and magnetic fields explicitly using [12.20](#eq-12-20) and [12.21](#eq-12-21): 
$$
\begin{aligned}
&\vec{E}=\operatorname{Re}\left(\vec{e}(\vec{k}) e^{i \vec{k} \cdot \vec{r}-i \omega t}\right) \\
&\vec{B}=\operatorname{Re}\left(\vec{b}(\vec{k}) e^{i \vec{k} \cdot \vec{r}-i \omega t}\right)
 \tag{12.30} \label{eq-12-30}
\end{aligned}
$$

$$
\vec{b}(\vec{k})=\frac{1}{\omega} \vec{k} \times \vec{e}(\vec{k})=\frac{n}{c} \hat{k} \times \vec{e}(\vec{k}) \quad \text { and } \quad \hat{k} \cdot \vec{e}(\vec{k})=0 . \tag{12.31} \label{eq-12-31}
$$

The result is 
$$
\begin{gathered}
\vec{E}=A_{1} \hat{e}_{1} \cos \left(\vec{k} \cdot \vec{r}-\omega t+\phi_{1}\right)+A_{2} \hat{e}_{2} \cos \left(\vec{k} \cdot \vec{r}-\omega t+\phi_{2}\right) , \\
\vec{B}=\sqrt{\mu \epsilon}\left(A_{1} \hat{e}_{2} \cos \left(\vec{k} \cdot \vec{r}-\omega t+\phi_{1}\right)-A_{2} \hat{e}_{1} \cos \left(\vec{k} \cdot \vec{r}-\omega t+\phi_{2}\right)\right) .
 \tag{12.32} \label{eq-12-32}
\end{gathered}
$$

Putting this into [12.24](#eq-12-24) and [12.26](#eq-12-26) gives 
$$
\mathcal{E}=\frac{\epsilon}{4 \pi}\left(A_{1}^{2} \cos ^{2}\left(\vec{k} \cdot \vec{r}-\omega t+\phi_{1}\right)+A_{2}^{2} \cos ^{2}\left(\vec{k} \cdot \vec{r}-\omega t+\phi_{2}\right)\right), \tag{12.33} \label{eq-12-33}
$$

$$
\vec{S}=\hat{k} \sqrt{\frac{\epsilon}{\mu}} \frac{c}{4 \pi}\left(A_{1}^{2} \cos ^{2}\left(\vec{k} \cdot \vec{r}-\omega t+\phi_{1}\right)+A_{2}^{2} \cos ^{2}\left(\vec{k} \cdot \vec{r}-\omega t+\phi_{2}\right)\right) . \tag{12.34} \label{eq-12-34}
$$

You can check explicitly that [12.27](#eq-12-27) is satisfied. Because $\omega$ is very large for interesting electromagnetic waves, we are almost always interested in only the time averaged values of $\mathcal{E}$ and $\vec{S}$. These are 
$$
\langle\mathcal{E}\rangle=\frac{\epsilon}{8 \pi}\left(A_{1}^{2}+A_{2}^{2}\right), \tag{12.35} \label{eq-12-35}
$$

$$
\langle\vec{S}\rangle=\hat{k} \sqrt{\frac{\epsilon}{\mu}} \frac{c}{8 \pi}\left(A_{1}^{2}+A_{2}^{2}\right) . \tag{12.36} \label{eq-12-36}
$$

Note that the time averaged values depend only on the quantity 
$$
|Z|^{2} \equiv\left|\psi_{1}\right|^{2}+\left|\psi_{2}\right|^{2}=A_{1}^{2}+A_{2}^{2} . \tag{12.37} \label{eq-12-37}
$$

**The intensity of the light is proportional to** $|Z|^{2}$**.**

### Circular Polarization and Spin

Although linear polarization is more familiar and perhaps easier to understand, there is a sense in which circular polarization is the more fundamental. The plane electromagnetic wave in the $\hat{k}$ direction can be rotated around the $\hat{k}$ axis without changing anything but its polarization state. The rotation symmetry of the physics suggests that we ought to be able to find states that behave simply under such a rotation, and just get multiplied by a phase factor. These states are, in fact, the circular polarization states. The action of a rotation by an angle $\theta$ about the $\hat{k}$ axis on the polarization vector, $Z$, is represented by the matrix 
$$
R_{\theta}=\left(\begin{array}{cc}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{array} \tag{12.38} \label{eq-12-38}\right) .
$$

For example, $R_{\theta}$ acting on $u_{1}$, [12.4](#eq-12-4), gives $u_{\theta}$, [12.6](#eq-12-6): 
$$
R_{\theta}\left(\begin{array}{l}
1 \\
0
\end{array}\right)=\left(\begin{array}{l}
\cos \theta \\
\sin \theta
\end{array} \tag{12.39} \label{eq-12-39}\right) .
$$

But on the left- and right-circularly polarized states, 
$$
R_{\theta}\left(\begin{array}{l}
1 \\
i
\end{array}\right)=e^{-i \theta}\left(\begin{array}{l}
1 \\
i
\end{array}\right), \quad R_{\theta}\left(\begin{array}{c}
1 \\
-i
\end{array}\right)=e^{i \theta}\left(\begin{array}{c}
1 \\
-i
\end{array} \tag{12.40} \label{eq-12-40}\right) .
$$

This is related to the fact that the circularly polarized states carry the maximum angular momentum possible, which in turn is related to the quantum mechanical property of the spin of the photon.

__________________________

[^12-2-1]: This is sometimes called the Jones vector. See Hecht, page 323.

## 12.3: Wave Plates and Polarizers

One reason that polarization is important is that the polarization state of an electromagnetic wave can be easily manipulated. Two of the most important devices for such manipulation are polarizers and wave plates.

### Unpolarized Light

![Figure](../images/lt-32895-clipboard_e470f047f0b1d4bd4ecc91b7a748c5db6.png)12-2

In any beam of light, at any given point and time, the electric field points in a particular direction. Likewise, because any plane electromagnetic wave with a definite angular frequency can be described by [12.20](#eq-12-20) and [12.21](#eq-12-21), 
$$
\begin{aligned}
\vec{E} &=\operatorname{Re}\left(\vec{e}(\vec{k}) e^{i \vec{k} \cdot \vec{r}-i \omega t}\right) \\
\vec{B} &=\operatorname{Re}\left(\vec{b}(\vec{k}) e^{i \vec{k} \cdot \vec{r}-i \omega t}\right)
 \tag{12.41} \label{eq-12-41}
\end{aligned}
$$

$$
\vec{b}(\vec{k})=\frac{1}{\omega} \vec{k} \times \vec{e}(\vec{k})=\frac{n}{c} \hat{k} \times \vec{e}(\vec{k}) \quad \text { and } \quad \hat{k} \cdot \vec{e}(\vec{k})=0. \tag{12.42} \label{eq-12-42}
$$

every plane wave is polarized. However, in an “unpolarized” beam, the light wave consists of a range of angular frequencies with different polarizations. As a result of the interference of the different harmonic components of the wave, the polarization wanders more or less randomly as a function of time and space, and on the average, no particular polarization is picked out. A simple example of what this looks like is animated in program 12-2, where we plot an electric field of the form 
$$
\begin{aligned}
&E_{x}(t)=\cos \left(\omega_{1} t+\phi_{1}\right)+\cos \left(\omega_{2} t+\phi_{2}\right), \\
&E_{y}(t)=\cos \left(\omega_{3} t+\phi_{3}\right)+\cos \left(\omega_{4} t+\phi_{4}\right),
 \tag{12.43} \label{eq-12-43}
\end{aligned}
$$

where the phases are random and the frequencies are chosen at random in a small range around a central frequency. You can watch the $\vec{E}$ field wandering in the $x$-$y$ plane, eventually filling it up. The narrower the range of frequencies in the wave, the more slowly the polarization wanders. In the example in program 12-2, the range of frequencies is of the order of 10% of the central frequency, so the polarization wanders rapidly. But for a beam with a fairly well-defined frequency, the polarization will be nearly constant over many cycles of the wave. The time over which the polarization is approximately constant is called the coherence time of the wave. For a plane wave of definite frequency, the coherence time is infinite.

### Polarizers

A **“polarizer”** is a device that allows light polarized in a particular direction (the “easy transmission axis” of the polarizer) to pass through with very little absorption, but absorbs most of the light polarized in the perpendicular direction. Thus an unpolarized light beam, passing though the polarizer, emerges polarized along the easy axis.

For the transverse oscillations of a string, a polarizer is simply a slit that allows the string to oscillate in one transverse direction but not in the perpendicular direction.

For electromagnetic waves, the most familiar example of a polarizer, Polaroid, was invented by Edwin Land over 50 years ago, partly in experiments done in the attic of the Jefferson Physical Laboratory, where he worked as an undergraduate at Harvard. The idea of polaroid is to make material that conducts electricity (poorly) in one direction, but not in the other. Then the electric field in the conducting direction will be absorbed (the energy going to resistive loss), while the electric field in the nonconductive direction will be unaffected. One way of doing this is to make sheets of polymer (polyvinyl alcohol) stretched (to align the polymer molecules along a preferred axis) and doped with iodine (to allow conduction along the polymer molecules).[^12-3-2]

### Wave Plates

**“Wave plates”** are optical elements that change the relative phase of the two components of $Z$. Wave plates are possible because there are materials in which the index of refraction depends on the polarization. This property is called “birefringence.” It can happen in various ways.

For example, the transparent polymer material cellophane is made into thin sheets by stretching. Because of the stretching, the polymer strands tend to be oriented along the stretch direction. The dielectric constant in this material depends on the direction of the electric field. It is easier for charges to move along the polymer strands than across them. Thus the dielectric constant is larger for electric fields in the stretch direction.

The same effect may arise because of the inherent structure of a transparent crystal. An example is the naturally occurring mineral, calcite, a crystalline form of calcium carbonate, $CaCO_{3}$. Crystals of calcite have the fascinating property of splitting a beam of unpolarized light into its two polarization states. Birefringence can even be produced mechanically, by stressing a transparent material, squeezing the electronic structure in one direction.

However the birefringence is produced, we can make a wave plate by orienting the material so that the $x$ and $y$ directions correspond to different indices of refraction, $n_{x}$ and $n_{y}$, and then making a slice of the material in the form of a plate in the $x$-$y$ plane, with some thickness $\ell$ in the $z$ direction. Now an electromagnetic wave traveling in the $z$ direction through the plate has different $k$ values depending on its polarization: 
$$
k=\left\{\begin{array}{l}
\frac{n_{x}}{c} \omega \text { for polarization in the } x \text { direction } \\
\frac{n_{y}}{c} \omega \text { for polarization in the } y \text { direction }
\end{array} \tag{12.44} \label{eq-12-44}\right.
$$

In particular, the phase **difference**, between $x$ and $y$ polarized light in going through the plate is 
$$
\Delta \phi=\frac{n_{x}-n_{y}}{c} \omega \ell . \tag{12.45} \label{eq-12-45}
$$

Note that in general the phase difference, $\Delta \phi$, depends on the frequency of the light. Even if $n_{x}$ and $n_{y}$ depend on frequency, it would be a bizarre accident if that dependence canceled the $\omega$ dependence from the explicit factor of $\omega$ in [12.39](#eq-12-39).

:::{figure} ../images/lt-32897-clipboard_ea9f29a4476f3c806481001932674ef96.png
:label: fig-12-5
:enumerator: 12.5
:alt: Initially unpolarized light passing through a pair of crossed polarizers with a wave plate in between.

Initially unpolarized light passing through a pair of crossed polarizers with a wave plate in between.
:::
Consider, now, putting such a wave plate between two crossed polarizers, oriented at $\pm 45^{\circ}$, as shown in [Figure 12.5](#fig-12-5). Without the wave plate, no light would get through because the first polarizer transmits only light polarized at $45^{\circ}$, described by the $Z$ vector 
$$
Z=\left(\begin{array}{l}
1 / \sqrt{2} \\
1 / \sqrt{2}
\end{array} \tag{12.46} \label{eq-12-46}\right)
$$

and the second polarizer absorbs it.

Coming out of the first polarizer, the vector, $Z$, looks like [12.40](#eq-12-40) for all the frequency components in the white light. But when the wave plate is inserted in between, a frequency dependent phase difference is added, so that the $Z$ vector coming out of the wave plate (up to an irrelevant overall phase) looks like 
$$
Z=\left(\begin{array}{c}
1 / \sqrt{2} \\
e^{-i \Delta \phi} / \sqrt{2}
\end{array} \tag{12.47} \label{eq-12-47}\right) .
$$

For frequencies such that $e^{-i \Delta \phi}$ is −1, the light is polarized in the −$45^{\circ}$ direction, and gets $e^{-i \Delta \phi}$ through the second polarizer without further attenuation. But for frequencies such that e is 1, the light is still absorbed by the second polarizer. Intermediate frequencies are partially absorbed.

It is this frequency dependence that produces the interesting patterns of color that you see when you put cellophane or a stressed piece of plastic between polarizers.

### Matrices

The effects of wave plates and polarizers and the like can be summarized by multiplication of the $Z$ vector by 2×2 matrices. For example, a perfect polarizer with an axis at an angle $\theta$ from the 1 axis can be represented by 
$$
P_{\theta}=\left(\begin{array}{cc}
\cos ^{2} \theta & \cos \theta \sin \theta \\
\cos \theta \sin \theta & \sin ^{2} \theta
\end{array} \tag{12.48} \label{eq-12-48}\right) .
$$

The object $P_{\theta}$ is called a **“projection operator,”** because it projects the vector onto the direction parallel to $u_{\theta}$. It satisfies 
$$
P_{\theta} P_{\theta}=P_{\theta}, \tag{12.49} \label{eq-12-49}
$$

as it must, since the first polarizer produces polarized light and the second one transmits it perfectly. $P_{\theta}$ acting on a vector transmits the component in the $\theta$ direction. This is easiest to visualize if $\theta = 0$ or $\pi / 2$. The matrices 
$$
P_{0}=\left(\begin{array}{ll}
1 & 0 \\
0 & 0
\end{array}\right), \quad P_{\pi / 2}=\left(\begin{array}{ll}
0 & 0 \\
0 & 1
\end{array} \tag{12.50} \label{eq-12-50}\right) ,
$$

represent polarizers along the 1 and 2 axes respectively.

A wave plate in which the phase difference is $\pi / 2$ is called a “quarter wave plate.” For a wave plate in which the phase difference is between 0 and $\pi$, it is conventional to call the axis with the smaller phase the “fast axis.” A quarter wave plate with fast axis along the 1 axis is represented by 
$$
Q_{0}=\left(\begin{array}{ll}
1 & 0 \\
0 & i
\end{array} \tag{12.51} \label{eq-12-51}\right) .
$$

Notice that we can write 
$$
Q_{0}=P_{0}+i P_{\pi / 2} . \tag{12.52} \label{eq-12-52}
$$

This should convince you that in general if the fast axis is in the $\theta$ direction, the quarter wave plate looks like 
$$
Q_{\theta}=P_{\theta}+i P_{\theta+\pi / 2} . \tag{12.53} \label{eq-12-53}
$$

The discussion of [12.39](#eq-12-39) shows that in general, a wave plate will only be a quarter wave plate for light of a definite frequency.

A wave plate in which the phase difference is $\pi$ is called a “half wave plate.” A half wave plate is obtained by replacing the $i$ in [12.45](#eq-12-45)-[12.47](#eq-12-47) by -1. Thus, 
$$
H_{\theta}=P_{\theta}-P_{\theta+\pi / 2} . \tag{12.54} \label{eq-12-54}
$$

Notice that 
$$
H_{\theta}=Q_{\theta} Q_{\theta}; \tag{12.55} \label{eq-12-55}
$$

two quarter wave plates make a half wave plate.

:::{figure} ../images/lt-32912-clipboard_e1cf9c3ec8155ebbccffeb8e82935701d.png
:label: fig-12-6
:enumerator: 12.6
:alt: Producing circularly polarized light.

Producing circularly polarized light.
:::
Here are two amusing devices that you can make with these optical elements (or matrices). Consider the combination of first a polarizer at $45^{\circ}$ and then a quarter wave plate, as shown in [Figure 12.6](#fig-12-6). By forming the matrix product, $Q_{0} P_{\pi / 4}$, you can see that this produces counterclockwise circularly polarized light from anything with a component of polarization in the $\pi / 4$ direction. The argument goes like this. The product is 
$$
Q_{0} P_{\pi / 4}=\left(\begin{array}{cc}
1 & 0 \\
0 & i
\end{array}\right)\left(\begin{array}{cc}
1 / 2 & 1 / 2 \\
1 / 2 & 1 / 2
\end{array}\right)=\left(\begin{array}{cc}
1 / 2 & 1 / 2 \\
i / 2 & i / 2
\end{array} \tag{12.56} \label{eq-12-56}\right) .
$$

When this acts on an arbitrary vector you get circularly polarization unless the vector is annihilated by $P_{\pi / 4}$. 
$$
Q_{0} P_{\pi / 4}\left(\begin{array}{l}
\psi_{1} \\
\psi_{2}
\end{array}\right)=\frac{\psi_{1}+\psi_{2}}{2}\left(\begin{array}{l}
1 \\
i
\end{array} \tag{12.57} \label{eq-12-57}\right) .
$$

In the opposite order, $P_{\pi / 4} Q_{0}$ is an analyzer for circularly polarized light. It annihilates counterclockwise light and converts clockwise polarized light to light linearly polarized in the $\pi / 4$ direction.

### Optical Activity

**“Optical activity”** is a property of many organic and some inorganic compounds. An optically active material rotates the polarization of light without absorbing either component of the polarization. A familiar example of such a material is corn syrup, a thick aqueous solution of sugar that you probably have in your kitchen. If you put a rectangular container of corn syrup between polarizers, as shown in [Figure 12.7](#fig-12-7), and rotate the second polarizer until the intensity of the light getting through is a maximum, you will find that direction of the second polarizer is not the same as that of the first. The plane of the polarization has been rotated by some angle $\theta$. The rotation angle, $\theta$, is proportional to the thickness of the container, the length of the region of syrup that the light goes through.

:::{figure} ../images/lt-32916-clipboard_ea84e5904663a7c05e42f10b19dc2b6e2.png
:label: fig-12-7
:enumerator: 12.7
:alt: A rectangular container of corn syrup between polarizers.

A rectangular container of corn syrup between polarizers.
:::
Clearly, the optical activity of corn syrup cannot depend on crystal structure, because the stuff is a perfectly uniform liquid, completely invariant under rotations in three-dimensional space. It can have no special axes, or any such thing. Optical activity must work very differently from birefringence.

You can find a clue to the nature of optical activity by considering what it looks like if you look at it in a mirror. If you reflect the system illustrated in [Figure 12.7](#fig-12-7) in the $x$-$z$ plane, by changing the sign of all the $y$ coordinates, the angle $\theta$ changes to −$\theta$. Thus the corn syrup that you see in a mirror must be fundamentally different from the corn syrup in your kitchen. This is not so strange. After all, your right hand looks like a left hand when you look at it in a mirror. The corn syrup must have the same property and have a definite “handedness.” In fact, because of the tetrahedral bonding of the carbon atoms of which they are built, the sugar molecules in the corn syrup can and do have such a handedness.

Because of the handedness of the sugar molecules, the index of refraction of the corn syrup actually depends on the handedness of the light. It is slightly different for left- and right-circularly polarized light. This happens because the $\vec{E}$ field of a circularly polarized beam twists slightly as it traverses each sugar molecule and sees a slightly different electronic structure depending on the direction of the twist. Then, because the indices of refraction are slightly different, the left- and right-circularly polarized components of the light get different phase factors ($k \ell$) in passing through a thickness, $\ell$, of the syrup.

We can now use our matrix language to see how this leads to optical activity. Up to an irrelevant overall phase, we can choose the phase produced on the left-circularly polarized light to be −$\theta$ and that on the right-circularly polarized light to be $\theta$. Then we can represent the action of the syrup on an arbitrary wave by the matrix 
$$
e^{-i \theta} P_{+}+e^{i \theta} P_{-} , \tag{12.58} \label{eq-12-58}
$$

where $P_{\pm}$ are matrices that pick out the left- and right-circularly polarized components, respectively. They satisfy 
$$
P_{\pm}\left(\begin{array}{c}
1 \\
\pm i
\end{array}\right)=\left(\begin{array}{c}
1 \\
\pm i
\end{array}\right), \quad P_{\pm}\left(\begin{array}{c}
1 \\
\mp i
\end{array} \tag{12.59} \label{eq-12-59}\right)=0 .
$$

You can check that the matrices are 
$$
P_{\pm}=\frac{1}{2}\left(\begin{array}{cc}
1 & \mp i \\
\pm i & 1
\end{array} \tag{12.60} \label{eq-12-60}\right) .
$$

Then [12.52](#eq-12-52) becomes 
$$
e^{-i \theta} \frac{1}{2}\left(\begin{array}{cc}
1 & -i \\
i & 1
\end{array}\right)+e^{i \theta} \frac{1}{2}\left(\begin{array}{cc}
1 & i \\
-i & 1
\end{array}\right)=\left(\begin{array}{cc}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{array} \tag{12.61} \label{eq-12-61}\right) .
$$

This is just the rotation matrix $R_{\theta}$, of [12.34](#eq-12-34)! $R_{\theta}$ rotates both components of any light by an angle $\theta$.

One might wonder about the reason for the handedness of the sugar molecules. In fact, there are physical processes, the weak interactions that give rise to $\beta$-radioactivity, that look different when reflected in a mirror[^12-3-3] and thus in principle could distinguish between left-handed and right-handed molecules. However, these interactions are most likely irrelevant to the handedness of corn syrup. Probably, the reason is biology rather than physics. Long ago, when the beginnings of life emerged from the primordial soup, **purely by accident**, the right-handed sugars were used. From then on, the handedness was maintained by the processes of reproduction.

:::{figure} ../images/lt-32926-clipboard_e3bcaff081cc87d3d744290e420d01d4b.png
:label: fig-12-8
:enumerator: 12.8
:alt: Initially unpolarized light passing through a pair of crossed polarizers.

Initially unpolarized light passing through a pair of crossed polarizers.
:::
### Crossed Polarizers and Quantum Mechanics

Polarization offers many opportunities to get confused when you think of the light wave in terms of photons. Let us imagine turning down the intensity of the light to the point where one photon at a time is going through the polarizers and consider first the deceptively simple situation of light moving in the $z$ direction through crossed polarizers in the $x$-$y$ plane. Suppose that the first polarizer transmits light polarized in the $x$ direction, and the second transmits light polarized in the $y$ direction. This is deceptively simple because it seems that we can interpret what is going on simply in terms of photons. The situation is depicted in [Figure 12.8](#fig-12-8). This seems simple enough to interpret in terms of photons. The unpolarized light in region $I$ is composed equally of photons polarized in the $x$ direction and in the $y$ direction (goes the wrong “classical” argument). Those polarized in the $x$ direction get through the first polarizer, so half the photons are still around in region $II$, where the intensity is reduced by half. Then none of these get through the second polarizer, so that the intensity in region $III$ is zero.

But compare this with the apparently similar situation in which the second polarizer transmits light polarized at $45^{\circ}$ in the $x$-$y$ plane, as shown in [Figure 12.9](#fig-12-9). Now the wave description tells us that the intensity in region $III$ is reduced by another factor of 2 from that in region $II$. This is impossible to interpret in terms of classical particles. To see this, it is only necessary to turn down the intensity so that only one photon comes through at a time. Then the first polarizer is OK. As before, if the photon is polarized in the $x$ direction, it get through. But now what happens at the second polarizer. The photon cannot split up. Either it gets through or it doesn’t. To be consistent with the wave description, in which the intensity is reduced by another factor of two, the transmission at the second polarizer must be a probabilistic event. Half the time the photon gets through. Half the time it is absorbed. There is no way for the

:::{figure} ../images/lt-32933-clipboard_e063bd818d6043f115d59603beacd8dfb.png
:label: fig-12-9
:enumerator: 12.9
:alt: Initially unpolarized light passing through a pair of polarizers at with axes at 45^{\circ}.

Initially unpolarized light passing through a pair of polarizers at with axes at $45^{\circ}$.
:::
photon in region $II$ to tell whether it is going to make it! It is random. God plays dice.

__________________________

[^12-3-2]: See Sears, Zemansky and Young, page 813.

[^12-3-3]: They violate what is called “parity” symmetry.

## 12.4: Boundary between Dielectrics

Let us return to the infinite plane boundary between two dielectrics that we discussed in chapter 9, but now consider an electromagnetic wave coming in at an arbitrary angle. As in chapter 5, we will assume that the boundary is the $z = 0$ plane, and that for $z < 0$ we have dielectric constant $\epsilon$, while for $z > 0$, dielectric constant $\epsilon^{\prime}$. We assume $\mu=1$ everywhere.

On the general grounds of translation invariance and local interactions discussed in the previous chapter, all the components of the electric and magnetic fields will have the general form 
$$
\begin{array}{cl}
\psi(r, t) \propto e^{i \vec{k} \cdot \vec{r}}+R e^{i \vec{k} \cdot \vec{r}} & \text { for } z \leq 0 \\
\psi(r, t) \propto \tau e^{i \vec{k}^{\prime} \cdot \vec{r}} & \text { for } z \geq 0
\end{array} \tag{12.62} \label{eq-12-62}
$$

where 
$$
\tilde{k}_{x}=k_{x}, \quad k_{x}^{\prime}=k_{x} , \tag{12.63} \label{eq-12-63}
$$

and 
$$
\begin{gathered}
\tilde{k}_{z}=-\sqrt{\omega^{2} / v^{2}-k_{x}^{2}}=-k_{z} \\
k_{z}^{\prime}=\sqrt{\omega^{2} / v^{\prime 2}-k_{x}^{2}}
 \tag{12.64} \label{eq-12-64}
\end{gathered} .
$$

Thus Snell’s law is satisfied, with $\theta$ and $\theta^{\prime}$ defined as shown in [Figure 12.10](#fig-12-10). 
$$
\begin{aligned}
&k \cdot \sin \theta=k^{\prime} \sin \theta^{\prime} . \\
&|\vec{k}|=\sqrt{\mu \epsilon} \frac{\omega}{c}=n \frac{\omega}{c} \\
&n \sin \theta=n^{\prime} \sin \theta^{\prime} .
 \tag{12.65} \label{eq-12-65}
\end{aligned}
$$

:::{figure} ../images/lt-32940-clipboard_e10e7a8b98a69e568cfd8daa0f3d62fc6.png
:label: fig-12-10
:enumerator: 12.10
:alt: Scattering of plane waves from a plane boundary.

Scattering of plane waves from a plane boundary.
:::
The details of the scattering will depend on the polarization. It is clear (by symmetry as usual) that the two cases will be polarization in the $x$-$z$ plane and polarization perpendicular to the $x$-$z$ plane. Of course, we lose nothing by considering these two separately, because of linearity. Any polarization for the incoming wave can be dealt with by forming a linear combination of the parallel and perpendicular solutions.

### Polarization Perpendicular to the Scattering Plane

Let us first consider perpendicular polarization. This means that the electric field is in the $y$ direction (out of the plane of the paper), while the magnetic field is the $x$-$z$ plane:<sup>4 </sup>
$$
\begin{gathered}
E_{y}(r, t)=A e^{i(\vec{k} \vec{r}-\omega t)}+R_{\perp} A e^{i(\tilde{k} \cdot \vec{r}-\omega t)} \quad \text { for } z \leq 0 \\
E_{y}(r, t)=\tau_{\perp} A e^{i\left(\vec{k}^{\prime} \cdot \vec{r}-\omega t\right)} \quad \text { for } z \geq 0 \\
E_{z}=E_{x}=0
 \tag{12.66} \label{eq-12-66}
\end{gathered}
$$

Using [12.19](#eq-12-19)) 
$$
\vec{B}=\frac{n}{c} \hat{k} \times \vec{E}=\frac{1}{\omega} \vec{k} \times \vec{E} , \tag{12.67} \label{eq-12-67}
$$

we can write 
$$
\begin{array}{rlr}
B_{x}(r, t)=-\frac{n}{c} A \cos \theta e^{i(\vec{k} \cdot \vec{r}-\omega t)}+\frac{n}{c} \cos \theta R_{\perp} A e^{i(\vec{k} \cdot \vec{r}-\omega t)} & \text { for } z \leq 0 \\
B_{x}(r, t)--\frac{n^{\prime}}{c} \cos \theta^{\prime} \tau_{\perp} A e^{i\left(\vec{k}^{\prime} \cdot \vec{r}-\omega t\right)} & & \text { for } z \geq 0 \\
B_{z}(r, t)=\frac{n}{c} \sin \theta A e^{i(\vec{k} \cdot \vec{r}-\omega t)}+\frac{n}{c} \sin \theta R_{\perp} A e^{i(\vec{k} \cdot \vec{r}-\omega t)} & & \text { for } z \leq 0 \\
B_{z}(r, t)=\frac{n^{\prime}}{c} \sin \theta^{\prime} \tau_{\perp} A e^{i\left(\vec{k}^{\prime} \cdot \vec{r}-\omega t\right)} & & \text { for } z \geq 0 \\
B_{y}=0 &
\end{array} \tag{12.68} \label{eq-12-68}
$$

The system is shown in [Figure 12.11](#fig-12-11). This figure shows the directions of the magnetic fields of the incoming ($\vec{B}_{i}$), reflected ($\vec{B}_{r}$), and transmitted ($\vec{B}_{t}$) component waves in scattering of an electromagnetic plane wave polarized parallel to a plane dielectric boundary. The $\vec{k}$ vectors are shown directly beneath the magnetic fields. The nontrivial boundary conditions are that $E_{y}$ and $B_{x}$ are continuous (the latter because we have assumed $\mu=1$ so there is no sheet of bound current on the boundary). $B_{z}$ is also continuous, but that provides no new information. Thus 
$$
1+R_{\perp}=\tau_{\perp} \tag{12.69} \label{eq-12-69}
$$

where 
$$
\xi_{\perp}=\frac{k_{z}^{\prime}}{k_{z}} . \tag{12.70} \label{eq-12-70}
$$

### Polarization in the Scattering Plane

Polarization in the $x$-$z$ plane looks like 
$$
\begin{array}{cl}
B_{y}(r, t)=A e^{i(\vec{k} \cdot \vec{r}-\omega t)}+R_{\|} A e^{i(\vec{k} \cdot \vec{r}-\omega t)} & \text { for } z \leq 0 \\
B_{y}(r, t)=\tau_{\|} A e^{i\left(\vec{k}^{\prime} \cdot \vec{r}-\omega t\right)} & \text { for } z \geq 0 \\
B_{z}=B_{x}=0, &
\end{array} \tag{12.71} \label{eq-12-71}
$$

where, for convenience, we have defined the reflection and transmission coefficients in terms of the magnetic fields, and 
$$
\begin{array}{rlr}
E_{x}(r, t)=\frac{c}{n} \cos \theta A e^{i(\vec{k} \cdot \vec{r}-\omega t)}-\frac{c}{n} \cos \theta R_{\|} A e^{i(-\overrightarrow{\vec{k}} \cdot \vec{r}-\omega t)} & \text { for } z \leq 0 \\
E_{x}(r, t)=\frac{c}{n^{\prime}} \cos \theta^{\prime} \tau_{\|} A e^{i\left(\vec{k}^{\prime} \cdot \vec{r}-\omega t\right)} & & \text { for } z \geq 0 \\
E_{z}(r, t)=-\frac{c}{n} \sin \theta A e^{i(\vec{k} \cdot \vec{r}-\omega t)}-\frac{c}{n} \sin \theta R_{\|} A e^{i(-\tilde{\vec{k}} \cdot \vec{r}-\omega t)} & & \text { for } z \leq 0 \\
E_{z}(r, t)=-\frac{c}{n^{\prime}} \sin \theta^{\prime} \tau_{\|} A e^{i\left(\vec{k}^{\prime} \cdot \vec{r}-\omega t\right)} & & \text { for } z \geq 0 \\
E_{z}=0 . &
\end{array} \tag{12.72} \label{eq-12-72}
$$

Now the nontrivial boundary conditions are the continuity of $B_{y}$ and $E_{x}$. $E_{z}$ is not continuous because a surface bound charge density builds up on the dielectric boundary. The boundary conditions yield 
$$
1+R_{\|}=\tau_{\|} \tag{12.73} \label{eq-12-73}
$$

$$
\frac{\cos \theta}{n}\left(1-R_{\|}\right)=\frac{\cos \theta^{\prime}}{n^{\prime}} \tau_{\|} \tag{12.74} \label{eq-12-74}
$$

or 
$$
\tau_{\|}=\frac{2}{1+\xi_{\|}} \tag{12.75} \label{eq-12-75}
$$

$$
R_{\|}=\frac{1-\xi \|}{1+\xi_{\|}} \tag{12.76} \label{eq-12-76}
$$

where 
$$
\xi_{\|}=\frac{\cos \theta^{\prime} / n^{\prime}}{\cos \theta / n}=\frac{n^{2} k_{z}^{\prime}}{n^{\prime 2} k_{z}} . \tag{12.77} \label{eq-12-77}
$$

One of the interesting things about [12.74](#eq-12-74) is that when 
$$
\frac{n^{2} k_{z}^{\prime}}{n^{\prime 2} k_{z}}-1 \tag{12.78} \label{eq-12-78}
$$

there is no reflection. This condition is satisfied for a special angle of incidence called Brewster’s angle. We can understand the significance of Brewster’s angle as follows: 
$$
\text { from Snell's law, } \frac{n^{2}}{n^{\prime 2}}-\frac{\sin ^{2} \theta^{\prime}}{\sin ^{2} \theta} \tag{12.79} \label{eq-12-79}
$$

$$
\frac{k_{z}^{\prime}}{k_{z}}=\frac{k_{x} / k_{z}}{k_{x}^{\prime} / k_{z}^{\prime}}=\frac{\tan \theta}{\tan \theta^{\prime}} \tag{12.80} \label{eq-12-80}
$$

$$
\frac{n^{2} k_{z}^{\prime}}{n^{\prime 2} k_{z}}=\frac{\sin \theta^{\prime} \cos \theta^{\prime}}{\sin \theta \cos \theta}=1 . \tag{12.81} \label{eq-12-81}
$$

Thus $\sin 2 \theta=\sin 2 \theta^{\prime}$. Because $\theta \neq \theta^{\prime}$ (that would be the trivial situation with no boundary), this means that 
$$
\theta=\pi / 2-\theta^{\prime} . \tag{12.82} \label{eq-12-82}
$$

In other words, Brewster’s angle is defined by the condition that the reflected and transmitted plane waves are perpendicular, as shown in the diagram in [Figure 12.12](#fig-12-12). The relevance of this condition is that the reflected wave can be thought of as being produced by the motion of the charges on the boundary. But if these are moving in a direction perpendicular to the electric field in the would-be reflected wave, then the wave cannot be produced.

:::{figure} ../images/lt-32978-clipboard_ec4edb728c7d10c58c3ae72eda8973464.png
:label: fig-12-12
:enumerator: 12.12
:alt: Brewster's angel.

Brewster's angel.
:::
_____________________

<sup>4</sup> The quantities, $R_{\perp}$ and $\tau_{\perp}$ in this section and $R_{\|}$ and $\tau_{\|}$ in the next are conventionally called “Fresnel coefficients.” See Hecht, page 97.

## 12.5: Radiation

In this section, we write down the electric and magnetic fields associated with changing charge and current densities.

### Fields of moving charges

Because Maxwell’s equations are partial differential equations, lots of initial conditions or boundary conditions must be specified to determine the solutions. For example, a constant electric field everywhere is a solution to the free-space Maxwell’s equations, and therefore you can add a constant field to any solution and it will still be a solution. Such things must be determined by physical initial conditions or boundary conditions. One set of conditions that is frequently interesting is an analog of the boundary condition at infinity that we discussed for one-dimensional waves. Suppose that you have a universe which is initially stationary, with no electric currents, no magnetic fields, and only electric fields due to stationary charges (which you know how to compute from Physics 15b). At some time, you begin to move charges around in some finite region of space. What are the electric and magnetic fields produced in this way? This question has a relatively simple answer that is a nice intuitive generalization of the relations you learned in 15b for the electric and vector potentials from stationary charge and current distributions. These relations were 
$$
\phi(\vec{r})=\int d^{3} r^{\prime} \frac{\rho\left(\vec{r}^{\prime}\right)}{\left|\vec{r}-\overrightarrow{r^{\prime}}\right|} \tag{12.83} \label{eq-12-83}
$$

$$
\vec{A}(\vec{r})=\frac{1}{c} \int d^{3} r^{\prime} \frac{\overrightarrow{\mathcal{J}}\left(\vec{r}^{\prime}\right)}{\left|\vec{r}-\overrightarrow{r^{\prime}}\right|} \tag{12.84} \label{eq-12-84}
$$

The generalizations are 
$$
\phi(\vec{r}, t)=\int d^{3} r^{\prime} \frac{\rho\left(\overrightarrow{r^{\prime}}, t-\left|\vec{r}-\vec{r}^{\prime}\right| / c\right)}{\left|\vec{r}-\vec{r}^{\prime}\right|} \tag{12.85} \label{eq-12-85}
$$

$$
\vec{A}(\vec{r}, t)=\frac{1}{c} \int d^{3} r^{\prime} \frac{\overrightarrow{\mathcal{J}}\left(\overrightarrow{r^{\prime}}, t-|\vec{r}-\vec{r}| / c\right)}{\left|\vec{r}-\overrightarrow{r^{\prime}}\right|} \tag{12.86} \label{eq-12-86}
$$

It is a straightforward, but tedious, exercise in vector calculus to show these satisfy Maxwell’s equations. I am not going to talk about this (I’ll write down the derivation in an appendix for those of you who are interested), but it is worth trying to understand what these relations mean physically. The important physical point that these relations imply is that if the charge and current distributions depend on time, and if they are producing the fields, then what determines what the field is at some point $\vec{r}$ is the values of the charge and current distributions at earlier times. The farther away the charge is, the earlier the time has to be. That is what the factor of $t-\left|\vec{r}-\vec{r}^{\prime}\right| / c$ is telling us. The appearance of this factor is a kind of boundary condition at infinity. It is consistent with the relativistic version of the principle of causality. Because information cannot be transferred faster than light, a charge distribution at a space-time point $\left(\vec{r}^{\prime}, t^{\prime}\right)$ can effect the fields at the space-time point $(\vec{r}, t)$, only if $t \geq t^{\prime}$ and 
$$
\frac{\left|\vec{r}-\vec{r}^{\prime}\right|}{t-t^{\prime}} \leq c \tag{12.87} \label{eq-12-87}
$$

In these relations, [12.82](#eq-12-82) and [12.83](#eq-12-83), however, the condition is even stronger — a charge distribution at a space time point $\left(\vec{r}^{\prime}, t^{\prime}\right)$ can effect the fields at the space time point $(\vec{r}, t)$ only if light can travel directly from $\left(\vec{r}^{\prime}, t^{\prime}\right)$ to $(\vec{r}, t)$ — that is if$t \geq t^{\prime}$ and 
$$
\text { ck } \tag{12.88} \label{eq-12-88}
$$

or 
$$
t-t^{\prime}=\left|\vec{r}-\overrightarrow{r^{\prime}}\right| / c \tag{12.89} \label{eq-12-89}
$$

or 
$$
t^{\prime}=t-\left|\vec{r}-\vec{r}^{\prime}\right| / c \tag{12.90} \label{eq-12-90}
$$

These are just words. We have not derived this! The real justification of this discussion comes when you check that the relations actually satisfy Maxwell’s equations. That can wait for Physics 153 or 232 (or the appendix if you are in a hurry). However, I hope that this discussion at least makes the result reasonable. In fact you have already seen the result in action in 15b in Purcell’s discussion of the electric field from a charge that starts and stops. Look at the ANIMATIONS - PURCELL - the field from a charge that suddenly accelerates. This is an animation of a famous figure in Purcell’s book. The interesting thing about the animation is the kink in the electric field that propagates out from the acceleration event at the velocity of light — because it is light. Inside the kink, the fields are those of the moving charge. Outside the kind, the fields are those of the stationary charge. The kink — the electromagnetic way — is what connects the two asymptotic regions together. It is also fun to compare with PURCELL2 which illustrates what happens if an initially moving charge stops suddenly.

Now let’s see at what the electric and magnetic fields look like in an important limit. The connection between the potentials and the fields is the following: 
$$
\vec{E}=-\vec{\nabla} \phi-\frac{1}{c} \frac{\partial}{\partial t} \vec{A} \tag{12.91} \label{eq-12-91}
$$

$$
\vec{B}=\vec{\nabla} \times \vec{A} \tag{12.92} \label{eq-12-92}
$$

These relations are completely general. The special limit that I want to consider is one in which the charges and currents are confined to a small region around $\vec{r} = 0$. Then we will look at the electric and magnetic fields produced by the moving charges far away, for large $|\vec{r}|$. It is actually easiest to look at the magnetic field: 
$$
\vec{B}=\vec{\nabla} \times \vec{A}=\vec{\nabla} \times \frac{1}{c} \int d^{3} r^{\prime} \frac{\overrightarrow{\mathcal{J}}\left(\overrightarrow{r^{\prime}}, t-\left|\vec{r}-\vec{r}^{\prime}\right| / c\right)}{\left|\vec{r}-\vec{r}^{\prime}\right|} \tag{12.93} \label{eq-12-93}
$$

The point is that the curl $(\vec{\nabla} \times)$ can operate in two different places, either on the $1 /\left|\vec{r}-\overrightarrow{r^{\prime}}\right|$ or on the $-\left|\vec{r}-\overrightarrow{r^{\prime}}\right| / c$ in the time dependence of $\mathcal{J}$. The first gives a contribution that drops of like $1 / r^{2}$ for large $r$, just like the magnetic field from a time-independent distribution of currents. But the second gives a contribution that only falls off like $1/r$. Thus this contribution dominates for large $r$. Explicitly (using the chain rule), it is 
$$
\vec{B}=-\frac{1}{c^{2}} \int d^{3} r^{\prime} \frac{\vec{r}-\vec{r}^{\prime}}{\left|\vec{r}-\vec{r}^{\prime}\right|^{2}} \times \frac{d}{d t} \overrightarrow{\mathcal{J}}\left(\vec{r}^{\prime}, t-\left|\vec{r}-\vec{r}^{\prime}\right| / c\right) \tag{12.94} \label{eq-12-94}
$$

$$
\rightarrow-\frac{1}{c^{2}} \frac{1}{r} \int d^{3} r^{\prime} \hat{r} \times \frac{d}{d t} \overrightarrow{\mathcal{J}}\left(\overrightarrow{r^{\prime}}, t-\left|\vec{r}-\vec{r}^{\prime}\right| / c\right) \tag{12.95} \label{eq-12-95}
$$

where in [12.92](#eq-12-92) we have dropped a $\overrightarrow{r^{\prime}}$ in the numerator because this term falls like $1 / r^{2}$ for large $r$.

This is the magnetic field of an electromagnetic wave. Notice that it is perpendicular to the direction of motion $(\hat{r})$. The $1/r$ fall-off is what we expect for an electromagnetic wave, because the energy density goes like the square of the field, and falls off like $1 / r^{2}$ as the wave spreads.

The electric field can be computed in a similar way, although you also need to use the conservation of electric charge. 
$$
\frac{\partial}{\partial t} \rho+\vec{\nabla} \cdot \overrightarrow{\mathcal{J}}=0 \tag{12.96} \label{eq-12-96}
$$

As you would expect, the result is that the electric field has the same magnitude as the magnetic field and is perpendicular to both direction of motion and to the magnetic field. The piece that corresponds to a traveling electromagnetic wave can be written as 
$$
\vec{E} \rightarrow-\frac{1}{c^{2}} \int d^{3} r^{\prime} \frac{\vec{r}-\overrightarrow{r^{\prime}}}{\left|\vec{r}-\overrightarrow{r^{\prime}}\right|} \times\left(\frac{\vec{r}-\overrightarrow{r^{\prime}}}{\left|\vec{r}-\overrightarrow{r^{\prime}}\right|^{2}} \times \frac{d}{d t} \overrightarrow{\mathcal{J}}\left(\overrightarrow{r^{\prime}}, t-\left|\vec{r}-\vec{r}^{\prime}\right| / c\right)\right) \tag{12.97} \label{eq-12-97}
$$

$$
\rightarrow \frac{1}{c^{2}} \frac{1}{r} \int d^{3} r^{\prime} \hat{r} \times\left(\hat{r} \times \frac{d}{d t} \overrightarrow{\mathcal{J}}\left(\overrightarrow{r^{\prime}}, t-\left|\vec{r}-\vec{r}^{\prime}\right| / c\right)\right) \tag{12.98} \label{eq-12-98}
$$

To lowest order in $1/r$ for charges moving with velocities much smaller than $c$, we can simplify the electric field in [12.95](#eq-12-95) by substituting 
$$
|\vec{r}-\vec{r}| \rightarrow r \tag{12.99} \label{eq-12-99}
$$

and write the result as 
$$
\vec{E}(\vec{r}, t) \approx \frac{1}{c^{2}} \frac{1}{r} \int d^{3} r^{\prime} \hat{r} \times\left(\hat{r} \times \frac{d}{d t} \overrightarrow{\mathcal{J}}\left(\overrightarrow{r^{\prime}}, t-r / c\right)\right) \tag{12.100} \label{eq-12-100}
$$

The reason for the restriction to nonrelativistic motion of charges is that if a charged particle is moving at a speed close to the velocity of light, then we cannot neglect its position, $\overrightarrow{r^{\prime}}$, when it is moving towards $\vec{r}$. To see this, consider the impossible limit in which the charge is moving towards the point $\vec{r}$ at the speed of light. Then if the charge contributes to the electric field at $\vec{r}$ at one time, then it also contributes at later times because the particle keeps up with the moving light wave. While $v = c$ is impossible, for $v \approx c$, the $\overrightarrow{r^{\prime}}$ dependence cannot be ignored because it leads to very rapid time dependence of the potentials, and hence to large fields. What happens is that the contribution of charges moving relativistically to the electric fields in front of them get enhanced by factors of $\frac{c}{c-v}$. This effect is widely used today to produce intense “light” from particle accelerators — so called synchrotron radiation. You can see this effect in the ANIMATIONS if you make $v$ close to 1.

A particularly important and instructive case of [12.97](#eq-12-97) is the nonrelativistic motion of a single charge, $Q$, moving along a trajectory $\vec{R}(t)$. For this system,<sup>5 </sup>
$$
\overrightarrow{\mathcal{J}}(\vec{r}, t)=Q \vec{v}(t) \delta^{3}(\vec{r}-\vec{R}(t))=Q \frac{d \vec{R}(t)}{d t} \delta^{3}(\vec{r}-\vec{R}(t)) \tag{12.101} \label{eq-12-101}
$$

Then the integration over $d^{3} r^{\prime}$ in $(a)$ eliminates the $\delta$-function, and the electric field of the outgoing electromagnetic wave is proportional to the acceleration, 
$$
\vec{E}(\vec{r}, t) \approx \frac{1}{c^{2}} \frac{1}{r} Q \hat{r} \times(\hat{r} \times \vec{a}(t-r / c)) \tag{12.102} \label{eq-12-102}
$$

where 
$$
\vec{a}(t)=\frac{d^{2} \vec{R}(l)}{d t^{2}} \tag{12.103} \label{eq-12-103}
$$

All that the cross products with $\hat{r}$ do is to pick out minus the component of $\vec{a}(l-r / c)$ that is perpendicular to $\vec{r}$. It follows from the famous “bac-cab” identity, 
$$
\vec{a} \times(\vec{b} \times \vec{c})=\vec{b}(\vec{a} \cdot \vec{c})-\vec{c}(\vec{a} \cdot \vec{b}), \tag{12.104} \label{eq-12-104}
$$

that 
$$
\vec{E}(\vec{r}, t) \approx-\frac{1}{c^{2}} \frac{1}{r} Q(\vec{a}(t-r / c)-\hat{r}(\hat{r} \cdot \vec{a}(t-r / c))) . \tag{12.105} \label{eq-12-105}
$$

This had to happen because the electric field of an electromagnetic wave is perpendicular to its direction of motion. In this case, for large $r$, the wave is nearly a plane wave moving in direction $\vec{r}$.

### Antenna Pattern

Let us do an even more explicit example by considering a charge that oscillates harmonically along the $z$ axis, 
$$
\vec{R}(t)=\ell \hat{z} \cos \omega t . \tag{12.106} \label{eq-12-106}
$$

so that 
$$
\vec{a}(t)=-\ell \omega^{2} \hat{z} \cos \omega t . \tag{12.107} \label{eq-12-107}
$$

$$
\vec{E}(\vec{r}, t) \approx \frac{\ell \omega^{2}}{c^{2}} \frac{1}{r} Q(\hat{z}-\hat{r}(\hat{r} \cdot \hat{z})) \cos [\omega(t-r / c)] . \tag{12.108} \label{eq-12-108}
$$

The vector $\hat{z}-\hat{r}(\hat{r} \cdot \hat{z})$ is the component of $\hat{z}$ perpendicular to $\vec{r}$, as illustrated in [Figure 12.13](#fig-12-13).

:::{figure} ../images/lt-32979-clipboard_e722a88257bc70109f6be0999c93c93c4.png
:label: fig-12-13
:enumerator: 12.13
:alt: Evidently, the magnitude of \hat{z}-\hat{r}(\hat{r} \cdot \hat{z}) is \sin \theta. This means that the intensity of the electromagnetic wave at an angle \theta from the z axis is proportional to \sin ^{2} \theta. The intensity pattern can be conveniently represented in polar coordinates, where we…

Evidently, the magnitude of $\hat{z}-\hat{r}(\hat{r} \cdot \hat{z})$ is $\sin \theta$. This means that the intensity of the electromagnetic wave at an angle $\theta$ from the $z$ axis is proportional to $\sin ^{2} \theta$. The intensity pattern can be conveniently represented in polar coordinates, where we plot the intensity as a function of $\theta$. The result is shown below. This is the “antenna pattern” for the oscillating
:::
:::{figure} ../images/lt-32980-clipboard_e1e28f92c777a75cd4c8901e4eb85e009.png
:label: fig-12-14
:enumerator: 12.14
:alt: dipole in the z direction. It is shown in [Figure 12.14](#fig-12-14). The two lobes of the pattern arise because the field is highest in the x-y plane, for \theta=\pi / 2, and drops to zero as we approach the z axis, \theta = 0 or \theta = \pi.

dipole in the $z$ direction. It is shown in [Figure 12.14](#fig-12-14). The two lobes of the pattern arise because the field is highest in the $x$-$y$ plane, for $\theta=\pi / 2$, and drops to zero as we approach the $z$ axis, $\theta = 0$ or $\theta = \pi$.
:::
### Checking Maxwell’s equations

These things are called retarded potentials. This is a confusing name, since there is really nothing special about the potentials themselves. What is special is the assumption of a particular relation between the potentials and the charges and currents — that the fields are being produced entirely by the charges and currents. Here I show that they satisfy Maxwell’s equations. I call this an appendix because you are NOT responsible for knowing the details. I include it for your general education.

Some mathematical things to notice about the solution: 
$$
\frac{\partial}{\partial t} \rho+\vec{\nabla} \cdot \overrightarrow{\mathcal{J}}=0 \tag{12.109} \label{eq-12-109}
$$

implies 
$$
\frac{\partial}{\partial t} \rho+\vec{\nabla} \cdot \overrightarrow{\mathcal{J}}=0 \tag{12.110} \label{eq-12-110}
$$

This is called the Lorentz gauge condition. 
$$
\vec{\nabla} \cdot \vec{E}=-\nabla^{2} \phi-\frac{1}{c} \frac{\partial}{\partial t} \vec{\nabla} \cdot \vec{A} \tag{12.111} \label{eq-12-111}
$$

$$
=\left(-\nabla^{2}+\frac{1}{c^{2}} \frac{\partial^{2}}{\partial t^{2}}\right) \phi \tag{12.112} \label{eq-12-112}
$$

$$
=\int d^{3} r^{\prime}\left(\rho\left(\overrightarrow{r^{\prime}}, t-\left|\vec{r}-\vec{r}^{\prime}\right| / c\right)\left(-\nabla^{2}\right) \frac{1}{\left|\vec{r}-\overrightarrow{r^{\prime}}\right|}\right. \tag{12.113} \label{eq-12-113}
$$

$$
+\frac{1}{\left|\vec{r}-\vec{r}^{\prime}\right|}\left(-\nabla^{2}+\frac{1}{c^{2}} \frac{\partial^{2}}{\partial t^{2}}\right) \rho\left(\overrightarrow{r^{\prime}}, t-\left|\vec{r}-\vec{r}^{\prime}\right| / c\right) \tag{12.114} \label{eq-12-114}
$$

$$
\left.-2\left(\vec{\nabla} \rho\left(\overrightarrow{r^{\prime}}, t-\left|\vec{r}-\vec{r}^{\prime}\right| / c\right)\right) \cdot\left(\vec{\nabla} \frac{1}{\left|\vec{r}-\overrightarrow{r^{\prime}}\right|}\right)\right) \tag{12.115} \label{eq-12-115}
$$

The first term is the one we want. It is 
$$
=\int d^{3} r^{\prime} \rho\left(\vec{r}^{\prime}, t-\left|\vec{r}-\vec{r}^{\prime}\right| / c\right) 4 \pi \delta^{3}\left(\vec{r}-\vec{r}^{\prime}\right) \tag{12.116} \label{eq-12-116}
$$

$$
=4 \pi \rho(\vec{r}, t) \tag{12.117} \label{eq-12-117}
$$

The other two terms cancel because of the special form of the variable $t-\left|\vec{r}-\overrightarrow{r^{\prime}}\right| / c$. 
$$
\frac{1}{\left|\vec{r}-\overrightarrow{r^{\prime}}\right|}\left(-\nabla^{2}+\frac{1}{c^{2}} \frac{\partial^{2}}{\partial t^{2}}\right) \rho\left(\vec{r}^{\prime}, t-\left|\vec{r}-\vec{r}^{\prime}\right| / c\right) \tag{12.118} \label{eq-12-118}
$$

$$
-2\left(\vec{\nabla} \rho\left(\overrightarrow{r^{\prime}}, t-\left|\vec{r}-\vec{r}^{\prime}\right| / c\right)\right) \cdot\left(\vec{\nabla} \frac{1}{\left|\vec{r}-\vec{r}^{\prime}\right|}\right) \tag{12.119} \label{eq-12-119}
$$

$$
=\frac{1}{\left|\vec{r}-\vec{r}^{\prime}\right|} \frac{1}{c^{2}} \ddot{\rho}\left(\vec{r}^{\prime}, t-\left|\vec{r}-\vec{r}^{\prime}\right| / c\right) \tag{12.120} \label{eq-12-120}
$$

$$
+\frac{1}{\left|\vec{r}-\vec{r}^{\prime}\right|} \frac{1}{c} \vec{\nabla} \cdot \frac{\vec{r}-\vec{r}^{\prime}}{\left|\vec{r}-\vec{r}^{\prime}\right|} \dot{\rho}\left(\overrightarrow{r^{\prime}}, t-\left|\vec{r}-\vec{r}^{\prime}\right| / c\right) \tag{12.121} \label{eq-12-121}
$$

$$
-2 \frac{1}{c} \frac{1}{\left|\vec{r}-\vec{r}^{\prime}\right|} \dot{\rho}\left(\vec{r}^{\prime}, t-\left|\vec{r}-\vec{r}^{\prime}\right| / c\right) \tag{12.122} \label{eq-12-122}
$$

where $*$ means differentiation with respect to the time variable: 
$$
\left.\dot{\rho}\left(\overrightarrow{r^{\prime}}, t-\left|\vec{r}-\vec{r}^{\prime}\right| / c\right) \equiv \frac{\partial}{\partial t^{\prime}} \rho\left(\overrightarrow{r^{\prime}}, t^{\prime}\right)\right|_{t^{\prime}=t-\left|\vec{r}-\vec{r}^{\prime}\right| / c} \tag{12.123} \label{eq-12-123}
$$

$i$ and $ii$ come from $a$ (from the $\frac{\partial^{2}}{\partial t^{2}}$ and $−\nabla^{2}$ terms respectively) and $iii$ comes from $b$. Now the $\vec{\nabla}$ in $ii$ gives two terms — acting on $\dot{\rho}$ cancels $i$ and acting on cancels $iii$. Thus 
$$
\vec{\nabla} \cdot \vec{E}=4 \pi \rho . \tag{12.124} \label{eq-12-124}
$$

Likewise, 
$$
\vec{\nabla} \times \vec{B}-\frac{1}{c} \frac{\partial}{\partial t} \vec{E} \tag{12.125} \label{eq-12-125}
$$

$$
=\vec{\nabla} \times(\vec{\nabla} \times \vec{A})-\frac{1}{c} \frac{\partial}{\partial t}\left(-\vec{\nabla} \phi-\frac{1}{c} \frac{\partial}{\partial t} \vec{A}\right) \tag{12.126} \label{eq-12-126}
$$

$$
=\vec{\nabla}(\vec{\nabla} \cdot \vec{A})-\nabla^{2} \vec{A}-\vec{\nabla}\left(\frac{1}{c} \frac{\partial}{\partial t} \phi\right)+\frac{1}{c^{2}} \frac{\partial^{2}}{\partial t^{2}} \vec{A}
$$

or using the Lorentz gauge condition, 
$$
=\left(-\nabla^{2}+\frac{1}{c^{2}} \frac{\partial^{2}}{\partial t^{2}}\right) \vec{A}
$$

Form here on, the derivation is the same as for $\vec{\nabla} \cdot \vec{E}$, and we find 
$$
\vec{\nabla} \times \vec{B}-\frac{1}{c} \frac{\partial}{\partial t} \vec{E}=\frac{4 \pi}{c} \overrightarrow{\mathcal{J}}
$$

QED.

__________________

<sup>5</sup> This equation makes use of δ-function notation. To a physicist, a δ-function δ(x) is just a function that has area 1 and is so sharply peaked around x = 0 that we don’t care exactly what it looks like. All that matters is the area and where the peak is. The δ3 ~ ¡ ~r − R(t) ¢ in the equation is actually the product of three delta functions, for the x, y and z components, and just tells you that ~r = (x, y, z) = R~(t) = ¡ X(t), Y (t), Z(t) ¢ — that is that the particle is moving along the trajectory R~(t). For a mathematical discussion of the δ-function you can look at [http://mathworld.wolfram.com/DeltaFunction.html](http://mathworld.wolfram.com/DeltaFunction.html). But don’t be frightened. It is just a simple device for ignoring small details that we don’t care about. If you translate the integral into words or pictures, it may help.

::::{admonition} Chapter Checklist
:class: checklist

You should now be able to:

1. Describe polarization on a beaded or continuous string;

2. Write down the general form of an electromagnetic plane wave and relate it to the two-dimensional vector, $Z$;

3. Find the energy and momentum density of a plane electromagnetic wave;

4. Understand the possible polarization states of a plane wave;

5. Analyze systems of polarizers and wave plates using matrix multiplication;

6. Understand the connection between optical activity and handedness;

7. Calculate the reflection and transmission of a plane electromagnetic wave from a plane boundary between dielectric for any angle and find and explain Brewster's angle.
::::

## Problems

::::{exercise}
:label: prb-12-1
:enumerator: 12.1*

A pane of glass with index of refraction $n = 2$ sits in the $x$-$y$ plane, from $z = 0$ to $z = \ell$. A plane wave with wave number $k$ (outside the glass) comes at the pane at an angle $\theta$ from the perpendicular in the $x$-$y$ plane, with $k_{z}=k \cos \theta$ and $k_{x}=k \sin \theta$.

For each of the two polarization states (in the $y$ direction, and in the $x$-$z$ plane), some fraction of the intensity is reflected as a function of $\theta$ and $k$. In this problem, we will use the method of transfer matrices, discussed in Chapter 9 to find it. We will work out the case of polarization perpendicular to the $x$-$z$ scattering plane in detail. Then your job will be to repeat the calculation for polarization in the $x$-$z$ plane. To do it, we must generalize the analysis of [12.62](#eq-12-62)-[12.63](#eq-12-63) and [12.70](#eq-12-70)-[12.71](#eq-12-71) to a situation with arbitrary incoming and outgoing waves on both sides and to a boundary at arbitrary $z$ (rather than $y$ for this problem). For the perpendicular polarization state, the boundary conditions look like: 
$$
\begin{gathered}
e^{i k_{z} z} T_{\perp}^{1}+e^{-i k_{z} z} R_{\perp}^{1}=e^{i k_{z}^{\prime} z} T_{\perp}^{2}+e^{-i k_{z}^{\prime} z} R_{\perp}^{2} \\
n \cos \theta\left(e^{i k_{z} z} T_{\perp}^{1}-e^{-i k_{z} z} R_{\perp}^{1}\right)=n^{\prime} \cos \theta^{\prime}\left(e^{i k_{z}^{\prime} z} T_{\perp}^{2}+e^{-i k_{z}^{\prime} z} R_{\perp}^{2}\right)
\end{gathered}
$$

which gives 
$$
\left(\begin{array}{l}
T_{\perp}^{1} \\
R_{\perp}^{1}
\end{array}\right)=d(z)\left(\begin{array}{l}
T_{\perp}^{2} \\
R_{\perp}^{2}
\end{array}\right)
$$

where the transfer matrix, $d(z)$ is 
$$
\frac{1}{2}\left(\begin{array}{cc}
e^{-i k_{z} z} & 0 \\
0 & e^{i k_{z} z}
\end{array}\right)\left(\begin{array}{cc}
1+h_{\perp} & 1-h_{\perp} \\
1-h_{\perp} & 1+h_{\perp}
\end{array}\right)\left(\begin{array}{cc}
e^{i k_{z}^{\prime} z} & 0 \\
0 & e^{-i k_{z}^{\prime} z}
\end{array}\right)
$$

with 
$$
h_{\perp}=\frac{n \cos \theta}{n^{\prime} \cos \theta^{\prime}} .
$$

Going from index $n^{\prime}$ to index $n$ at $z$ gives a transfer matrix that is the inverse of $d(z)$. Applying this to the present problem, if $R_{\perp}$ and $\tau_{\perp}$ are the reflection and transmission coefficients from the pane of glass, we have 
$$
\left(\begin{array}{c}
1 \\
R_{\perp}
\end{array}\right)=d(0) d(\ell)^{-1}\left(\begin{array}{c}
0 \\
\tau_{\perp}
\end{array}\right)
$$

which implies 
$$
\begin{aligned}
\tau_{\perp} &=\frac{2 h_{\perp} e^{i k_{z} \ell}}{2 h_{\perp} \cos k_{z}^{\prime} \ell-i\left(1+h_{\perp}^{2}\right) \sin k_{z}^{\prime} \ell} \\
R_{\perp} &=\frac{-i\left(1-h_{\perp}^{2}\right) \sin k_{z}^{\prime} \ell}{2 h_{\perp} \cos k_{z}^{\prime} \ell-i\left(1+h_{\perp}^{2}\right) \sin k_{z}^{\prime} \ell}
\end{aligned}
$$

The fraction of the reflected intensity is 
$$
\left|R_{\perp}\right|^{2}=\frac{\left(1-h_{\perp}^{2}\right)^{2} \sin ^{2} k_{z}^{\prime} \ell}{4 h_{\perp}^{2} \cos ^{2} k_{z}^{\prime} \ell+\left(1+h_{\perp}^{2}\right)^{2} \sin ^{2} k_{z}^{\prime} \ell}
$$

Now, do the same analysis for the polarization in the $x$-$z$ plane. Find $\left|R_{\|}\right|^{2}$. What happens at Brewster’s angle?

::::

::::{exercise}
:label: prb-12-2
:enumerator: 12.2

Consider a boundary at $x = 0$ between two regions of empty space. On the boundary surface at $x = 0$, there is a thin layer of stuff with surface conductivity $\sigma$. That means that an electric field, $\vec{E}$, with a component parallel to the surface (in the $y$-$z$ plane) produces a surface current density in the boundary layer:

$$
\overrightarrow{\mathcal{J}}(y, z)=\left(0, \sigma E_{y}(0, y, z), \sigma E_{z}(0, y, z)\right) .
$$

In this system, there is an electric field of the form shown below: 
$$
E_{z}(x, y, t)=A e^{i(k x \cos \theta+k y \sin \theta-\omega t)}+R A e^{i\left(-k^{\prime} x \cos \theta^{\prime}+k^{\prime} y \sin \theta^{\prime}-\omega t\right)}
$$

for $x < 0$, and 
$$
E_{z}(x, y, t)=T A e^{i\left(k^{\prime \prime} x \cos \theta^{\prime \prime}+k^{\prime \prime} y \sin \theta^{\prime \prime}-\omega t\right)}
$$

for $x > 0$. $E_{x}$ and $E_{y}$ vanish everywhere.

Find $k^{\prime}$, $k^{\prime \prime}$, $\theta^{\prime}$ and $\theta^{\prime \prime}$. Find $T$ in terms of $R$. Find the current density on the boundary, $\overrightarrow{\mathcal{J}}(y, z)$. Find the magnetic field everywhere. Find $R$.

Check your result for $R$ by explaining the limit $\sigma \rightarrow \infty$, a superconducting surface. What happens to $R$ in this limit and why?

**Hint:** Use Maxwell’s equations to find $\vec{B}$ and then look at the discontinuity of the magnetic field across the surface current.

::::

::::{exercise}
:label: prb-12-3
:enumerator: 12.3

Suppose that on the planes $z = 0$ and $z = a$ for $x \geq 0$, there are two flat semi-infinite conducting planes. Suppose, further, that the oscillation of the system is forced by some device that produces an electric field in the $x = 0$ plane for $0 \leq z \leq a$ with the following properties: $\vec{E}$ points in the $y$ direction but its $y$-component is independent of $y$ and equal to $E_{0} \sin (3 \pi z / a) \cos (\omega t)$, where $\omega>3 \pi c / a$ and $c$ is the speed of light in vacuum. If this produces a traveling wave in the $+x$ direction, find the form of the electric field everywhere between the plates. If this traveling wave is used as a carrier wave for amplitude modulated signals, with what speed does the signal travel?

::::

::::{exercise}
:label: prb-12-4
:enumerator: 12.4

Consider the standing electromagnetic waves in a cubical evacuated box with **perfectly conducting** sides at $x = 0$, $x = L$, $y = 0$, $y = L$, $z = 0$ and $z = L$. There exist modes in which the electric and magnetic fields vanish outside the box, and inside take the following form:

$$
\begin{gathered}
E_{z}(x, y, z, t)=A \omega \sin k_{x} x \sin k_{y} y \cos \omega t \\
B_{x}(x, y, z, t)=-A k_{y} \sin k_{x} x \cos k_{y} y \sin \omega t \\
B_{y}(x, y, z, t)=A k_{x} \cos k_{x} x \sin k_{y} y \sin \omega t \\
E_{x}=E_{y}=B_{z}=0 .
\end{gathered}
$$

You can check that inside the box and for properly chosen $\omega$, these satisfy Maxwell’s equations, 
$$
\begin{array}{r}
\vec{\nabla} \times \vec{E}=-\frac{\partial \vec{B}}{\partial t} , \\
\vec{\nabla} \times \vec{B}=\mu_{0} \epsilon_{0} \frac{\partial \vec{E}}{\partial t}+\mu_{0} \vec{J} , \\
\vec{\nabla} \cdot \vec{E}=\rho, \quad \vec{\nabla} \cdot \vec{B}=0 .
\end{array}
$$

Find $\omega$ as a function of $k_{x}$ and $k_{y}$.

There are no charges or currents inside the box, but there will be charges and currents built up on the boundary to confine the electric and magnetic fields inside the box. For example, a nonzero surface charge density appears on the top ($z = L$) and bottom ($z = 0$). The charges oscillate back and forth from top to bottom while nonzero surface current densities appear on all sides. The form above is constructed to satisfy appropriate boundary conditions on the four sides $x = 0$, $y = 0$, $z = 0$ and $z = L$.

Explain the physics of the boundary conditions for the $\vec{E}$ field on the sides $x = L$ and $y = L$ and find the allowed values of $k_{x}$ and $k_{y}$. Then explain the physics of the boundary conditions for the $\vec{E}$ field on the sides $x = L$ and $y = L$ and draw a diagram to explain what is going on for the lowest possible values of $k_{x}$ and $k_{y}$. **Hint:** Remember that the magnetic field vanishes outside the box.

::::

::::{exercise}
:label: prb-12-5
:enumerator: 12.5

A plane wave of light traveling in the $+z$ direction is polarized at an angle $\theta$ from the $x$ axis in the $x$ − $y$ plane. When it encounters a sheet of polaroid in the $z = L$ plane that transmits only light polarized and an angle $\theta+\frac{\pi}{2}$, the wave is completely absorbed. However, if the plane wave first passes through a sheet of cellophane in the $z = 0$ plane with the “fast axis” along $x$ axis, some of the light gets through. Suppose that the cellophane introduces a phase difference of $\phi$ between the component of the light wave polarized along the fast $(x)$ axis and the component polarized along the slow $(y)$ axis. Find the ratio of the intensity of the transmitted wave beyond the polaroid to the incoming wave intensity as a function of $\theta$ and $\phi$. **Hint:** Does your answer go to zero as $\phi \rightarrow 0$? What happens as $\theta \rightarrow 0$?

::::

::::{exercise}
:label: prb-12-6
:enumerator: 12.6

A plane wave of light traveling in the $+z$ direction is polarized in the $x$ direction. When it encounters a sheet of polaroid in the $z = L$ plane that transmits only $y$ polarized light, the wave is completely absorbed. However, if the plane wave first passes through a sheet of cellophane in the $z = 0$ plane with the “fast axis” at an angle $\theta$ with the $x$ axis, some of the light get through. Suppose that the cellophane introduces a phase difference of $\phi$ between a wave polarized along the fast axis and one polarized along the slow axis. Find the ratio of the intensity of the transmitted wave beyond the polaroid to the incoming wave intensity as a function of $\theta$ and $\phi$.

Compare the result with the previous problem and explain what is going on.

::::

::::{exercise}
:label: prb-12-7
:enumerator: 12.7

Suppose that a charge $Q$ is stationary at the origin until $t = 0$. From time $t = 0$ to $t=\Delta t$, the charge experiences uniform acceleration $a \hat{x}$.

1. Use [12.102](#eq-12-102) to find an approximate expression for the electric field at a large distance $r \gg a \Delta t^{2}$ from the origin.

2. How does this compare with what you see in the animation PURCELL?

::::
