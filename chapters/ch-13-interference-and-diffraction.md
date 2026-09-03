---
title: "13. Interference and Diffraction"
short_title: "Chapter 13"
label: ch-13-interference-and-diffraction
---

(ch-13)=

# 13. Interference and Diffraction

A “beam” of light is very familiar. A laser pointer, for example, produces a pattern of light that is almost like a transverse section of a plane wave. But not quite. The laser beam spreads as it travels. You might think that this is simply due to the imperfections in the laser. But, in fact, no matter how hard you try to perfect your laser, you cannot avoid some spreading. The problem is “diffraction.”

Interference is a crucial part of the physics of diffraction. We have seen it already in one-dimensional situations such as interferometers and reflection from thin films. Here we begin to see what amazing things it does in more than one dimension.

::::{admonition} Chapter Preview
:class: preview

In this chapter, we show how the phenomena of interference and diffraction arise from the physics of the forced oscillation problem and the mathematics of Fourier transformation.

1. We begin by discussing interference from a double slit. This is the classic example of interference. We give a heuristic discussion of the physics, and generalize it to get the fundamental result of Fourier optics.

2. We then continue our quantitative analysis of interference and diffraction by discussing the general problem again as a forced oscillation problem. We show the connection with making a beam. We find the relevant boundary condition at infinity and express the solution in the form of an integral.

3. We show how the integral simplifies in two extreme regions — very close to the source of the beam, where it really looks like a beam — and very far away, where diffraction takes over and the intensity of the wave is related to a Fourier transform of the wave pattern at the source, the same result that we found in our heuristic discussion of interference.

4. We apply these techniques to examples involving beams made with one or more slits and rectangular regions.

5. We prove a useful result, the convolution theorem, for combining Fourier transforms.

6. We show how periodic patterns lead to sharp diffraction patterns, and discuss the example of the diffraction grating in detail.

7. We apply the same ideas to the three-dimensional example of x-ray diffraction from crystals.

8. We describe a hologram as a rather complicated diffraction pattern.

9. We discuss interference fringes and zone plates.
::::

## 13.1: Interference

### Double Slit

The classic arrangement of the double slit experiment is illustrated in [Figure 13.1](#fig-13-1). There is an opaque screen with two narrow slits in it in the $z = 0$ plane (shown in cross section in the $x-z$ plane — the slits come out of the paper in the $y$ direction) a small distance $s$ apart. The opaque screen is illuminated by a “point” source of light. For example, this could be a light with a clear glass bulb and a colored filter to pick out a narrow frequency range, far away in the −$z$ direction. A laser beam spread out with a lens would serve just as well. The important thing is to produce illumination at the opaque screen in which the frequency is in a narrow range and the phase of the light reaching the two slits is correlated. This will certainly be true if the illumination for $z < 0$ is nearly a plane wave.

:::{figure} ../images/lt-32771-clipboard_e34010b4a7e0c3eb59341b82e65477d20.png
:label: fig-13-1
:enumerator: 13.1
:alt: The double slit experiment.

The double slit experiment.
:::
Now an interesting thing happens at the second screen, at $z = Z$. This “screen” could be a photographic plate, a translucent screen, or even your retina. What appears on this screen is a series of parallel lines of brightness in the $y$ direction (parallel to the slits). If one of the slits is covered up, the lines disappear.

What is going on is interference between the two possible straight-line paths by which the light can reach the screen. We will give a heuristic, physical discussion of the interference in this section. Then in the next section, we will derive the same result using the kind of forced oscillation and boundary condition arguments that you know from our study of one-dimensional waves.

The physical picture is this. The electric field at $z = Z$ is a sum of the fields that come from the two slits. At $x = 0$, in the symmetrical arrangement shown in [Figure 13.1](#fig-13-1), the two possible paths for the light have the same length. Therefore, the two components of the field have the same phase. Therefore they interfere “constructively” and there is a bright line at $x = 0$. As x changes, at $z = Z$, the relative length of the two paths changes. We will then get alternating positions of constructive and destructive interference. This gives rise to the bright lines.

We can understand the effect quantitatively by computing the path length explicitly. Consider a point on the screen at $x = X$. This is shown in [Figure 13.2](#fig-13-2).

The length of the dotted line in [Figure 13.2](#fig-13-2) is 
$$
\sqrt{X^{2}+Z^{2}}. \tag{13.1} \label{eq-13-1}
$$

For the upper and lower slits, the path lengths are slightly shorter and longer respectively. The total difference in path length is 
$$
\Delta \ell=\sqrt{(X+s / 2)^{2}+Z^{2}}-\sqrt{(X-s / 2)^{2}+Z^{2}}. \tag{13.2} \label{eq-13-2}
$$

For $Z \gg s$, we can expand $\Delta \ell$ in [13.2](#eq-13-2) in a Taylor series, 
$$
\Delta \ell \approx \frac{s X}{\sqrt{X^{2}+Z^{2}}}. \tag{13.3} \label{eq-13-3}
$$

:::{figure} ../images/lt-32772-clipboard_ed9620034248b782bd992fc4be25e1ae1.png
:label: fig-13-2
:enumerator: 13.2
:alt: Path lengths.

Path lengths.
:::
Therefore if the angular wave number of the light is k, the **phase difference** between the two paths is
$$
\frac{k s X}{\sqrt{X^{2}+Z^{2}}}. \tag{13.4} \label{eq-13-4}
$$

We get an intensity maximum every time the phase is a multiple of $2 \pi$, when 
$$
\frac{k s X}{\sqrt{X^{2}+Z^{2}}}=2 n \pi \tag{13.5} \label{eq-13-5}
$$

In terms of the wavelength, $\lambda=2 \pi / k$, this is 
$$
\frac{X}{\sqrt{X^{2}+Z^{2}}}=n \frac{\lambda}{s}. \tag{13.6} \label{eq-13-6}
$$

### Fourier Optics

Suppose that instead of a simple pattern of two slits, there is some more complicated pattern on the opaque screen. In general, we can describe the wave disturbance in the $z = 0$ plane by some function of $x$ and $y,^{1}$ 
$$
f(x, y). \tag{13.7} \label{eq-13-7}
$$

Our strategy will be to think of the wave produced for $z > 0$ by this general function as a sum of the effects of tiny holes at all the values of $x$ and $y$ for which $f(x, y)$ is nonzero. For each little piece of the function, we can compute the path length to some point on the screen at $z = Z$. Then we can add up all the pieces.

Suppose, for simplicity, that $f(x, y)$ is only nonzero in some small region around the origin, so that $x$ and $y$ will be small 
$$
x, y \ll Z \tag{13.8} \label{eq-13-8}
$$

for all relevant values of $x$ and $y$. Now the path length from the point $(x, y, 0)$ on the screen at $z = 0$ to the point $(X, Y,Z)$ on the screen at $z = Z$ is 
$$
\sqrt{(X-x)^{2}+(Y-y)^{2}+Z^{2}}. \tag{13.9} \label{eq-13-9}
$$

Using [13.8](#eq-13-8), we can expand this as follows: 
$$
R+\Delta \ell(x, y)+\cdots , \tag{13.10} \label{eq-13-10}
$$

where 
$$
R=\sqrt{X^{2}+Y^{2}+Z^{2}} \tag{13.11} \label{eq-13-11}
$$

and 
$$
\Delta \ell(x, y)=-\frac{x X+y Y}{R} \tag{13.12} \label{eq-13-12}
$$

Thus the wave on the path from $(x, y, 0)$ to $(X, Y,Z)$ gets a phase of approximately 
$$
e^{i k(R+\Delta \ell)}. \tag{13.13} \label{eq-13-13}
$$

Now we can put the pieces of the wave back together to see how the interference works at the point $(X, Y,Z)$. We just sum over all values of $x$ and $y$, with a factor of the phase and the function, $f(x, y)$. Because $x$ and $y$ are continuous variables, the sum is actually an integral, 
$$
\int d x \int d y f(x, y) e^{i k(R+\Delta \ell)}=e^{i k R} \int d x \int d y f(x, y) e^{-i(x X+y Y) k / R}. \tag{13.14} \label{eq-13-14}
$$

As we will see in more detail below, this is a two-dimensional Fourier transform of the function, $f(x, y)$.

The equation, [13.14](#eq-13-14), is the fundamental result of Fourier optics. It contains much of the physics of diffraction. We have made a number of assumptions in deriving it that need further discussion. In the next section, we will derive it in a different way, treating the wave for $z > 0$ as the result of a forced oscillation, produced by the wave in the $z = 0$ plane. This will give us an alternative physical description of diffraction. But it will be useful to keep the simple picture of adding up all the possible paths in mind as we get deeper into the phenomena of interference and diffraction.

_________________________________

<sup>1</sup>We are ignoring polarization.

## 13.2: Beams

### Making a Beam

Consider a system with an opaque barrier in the $z = 0$ plane. If it is illuminated by a plane wave traveling in the +$z$ direction, the barrier absorbs the wave completely. Now cut a hole in the barrier. You might think that this would produce a beam of light traveling in the direction of the initial plane wave. But it is not that simple. This is actually the same problem that we considered in the previous section, [13.7](#eq-13-7)-[13.14](#eq-13-14), with the function, $f(x, y)$, given by 
$$
f(x, y) e^{-i \omega t} \tag{13.15} \label{eq-13-15}
$$

where 
$$
f(x, y)=\left\{\begin{array}{l}
1 \text { inside the opening } \\
0 \text { outside the opening }
\end{array}\right. \tag{13.16} \label{eq-13-16}
$$

In fact, it will be useful to think about the more general problem, because the the function, [13.16](#eq-13-16), is discontinuous. As we will see later, this leads to more complicated diffraction phenomena than we see with a smooth function. In particular, we will assume that $f(x, y)$ is signifigantly different from zero only for small x and y and goes to zero for large $x$ and $y$. Then we can talk about the position of the “opening” that produces the beam, near $x = y = 0$.

We can think of this problem as a forced oscillation problem. It is much easier to analyze the physics if we ignore polarization, so we will discuss scalar waves. For example, we could consider the transverse waves on a flexible membrane or pressure waves in a gas. Equivalently, we could consider light waves that depend only on two dimensions, $x$ and $z$, and polarized in the $y$ direction. We will not worry about these niceties too much, because as usual, the basic properties of the wave phenomena will be determined by translation invariance properties that are independent of what it is that is waving!

### Caveats

It is worth noting that there are other approaches to the diffraction problem besides the ones we discuss here. The physical setup we are considering is slightly different from the standard setup of Huygens-Fresnel-Kirchhoff diffraction, because we are studying a different problem. In Huygens-Fresnel-Kirchhoff diffraction,[^13-2-2] you consider the diffraction of a plane wave from a finite object, whereas, our opaque screen is infinite in the $x$-$y$ plane. In the Huygens-Fresnel case, the appropriate boundary condition is that there are no incoming **spherical waves** coming back in from infinity toward the object that is doing the diffracting. The diffraction produces outgoing spherical waves only. We will not discuss this alternative physical setup in detail because it leads deeper into Bessel functions[^13-2-3] than we (and probably the reader as well) are eager to go. The advantage of our formulation is that we can set it up entirely with the plane wave solutions that we have already discussed. We will simply indicate the differences between our treatment and Huygens-Fresnel diffraction. For diffraction in the forward region, at large z and not very far from the z axis, the diffraction is the same in the two cases.

The reader should also notice that we have not explained exactly how the oscillation, [13.15](#eq-13-15), 
$$
f(x, y) e^{-i \omega t} \tag{13.17} \label{eq-13-17}
$$

in the $z = 0$ plane is produced. This is by no means a trivial problem, but we will not discuss it in detail. We are concentrating on the physics for $z > 0$. This will be quite interesting enough.

#### Boundary at $\infty$

To determine the form of the waves in the region $z > 0$ (beyond the barrier), we need boundary conditions both at $z = 0$ and at $z=\infty$. At $z = 0$, there is an oscillating amplitude given by [13.15](#eq-13-15).[^13-2-4] At $z=\infty$, we must impose the condition that there are no waves traveling in the −$z$ direction (back toward the barrier) and that the sodwlutions are well behaved at $\infty$.

The normal modes have the form 
$$
e^{i \vec{k} \cdot \vec{r}-i \omega t} \tag{13.18} \label{eq-13-18}
$$

where $\vec{k}$ satisfies the dispersion relation 
$$
\omega^{2}=v^{2} \vec{k}^{2}. \tag{13.19} \label{eq-13-19}
$$

Thus given two components of $\vec{k}$, we can find the third using [13.18](#eq-13-18). So we can write the solution as 
$$
\psi(\vec{r}, t)=\int d k_{x} d k_{y} C\left(k_{x}, k_{y}\right) e^{i \vec{k} \cdot \vec{r}-i \omega t} \text { for } z>0 \tag{13.20} \label{eq-13-20}
$$

where 
$$
k_{z}=\sqrt{\omega^{2} / v^{2}-k_{x}^{2}-k_{y}^{2}}. \tag{13.21} \label{eq-13-21}
$$

Note that [13.20](#eq-13-20) does not determine the sign of $k_{2}$. But the boundary condition at $\infty$ does. If $k_{z}$ is real, it must be positive in order to describe a wave traveling to the right, away from the barrier. If $k_{z}$ is complex, its imaginary part must be positive, otherwise $e^{i \vec{k} \cdot \vec{r}}$ would blow up as $z$ goes to $\infty$. Thus, 
$$
\text { if } \operatorname{Im} k_{z}=0, \text { then } \operatorname{Re} k_{z}>0 \text { ; otherwise } \operatorname{Im} k_{z}>0 \text { . } \tag{13.22} \label{eq-13-22}
$$

We discussed the physical signifigance of the boundary condition, [13.21](#eq-13-21), in our discussion of tunneling starting on page 274. There is real physics in the boundary condition at infinity. For example, consider the relation between this analysis and the discussion of path lengths in the previous section. In the language of the last chapter, we cannot describe the effects of the waves with imaginary $k_{z}$. However, the boundary condition, [13.21](#eq-13-21), ensures that these components of the wave will go to zero rapidly for large $z$.

### Boundary at $z=0$

All we need to do to determine the form of the wave for $z > 0$ is to find $C(k_{x}, k_{y})$. To do that, we implement the boundary condition at $z = 0$ by using [13.19](#eq-13-19) 
$$
\psi(\vec{r}, t)=\int d k_{x} d k_{y} C\left(k_{x}, k_{y}\right) e^{i \vec{k} \cdot \vec{r}-i \omega t} \text { for } z>0 \tag{13.23} \label{eq-13-23}
$$

and setting 
$$
\left.\psi(\vec{r}, t)\right|_{z=0}=f(x, y) e^{-i \omega t} \tag{13.24} \label{eq-13-24}
$$

to get [13.15](#eq-13-15). Taking out the common factor of $e^{-i \omega t}$, this condition is 
$$
f(x, y)=\int d k_{x} d k_{y} C\left(k_{x}, k_{y}\right) e^{i\left(k_{x} x+k_{y} y\right)}. \tag{13.25} \label{eq-13-25}
$$

If $f(x, y)$ is well behaved at infinity (as it certainly is if, as we have assumed, it goes to zero for large $x$ and $y$), then only real $k_{x}$ and $k_{y}$ can contribute in [13.23](#eq-13-23). A complex $k_{x}$ would produce a contribution that blows up either for $x \rightarrow+\infty$ or $x \rightarrow-\infty$. Thus the integrals in [13.23](#eq-13-23) run over real k from −$\infty$ to $\infty$.

[13.23](#eq-13-23) is just a two-dimensional Fourier transform. Using arguments analogous to those we used in our discussion of signals, we can invert it to find $C$. 
$$
C\left(k_{x}, k_{y}\right)=\frac{1}{4 \pi^{2}} \int d x d y f(x, y) e^{-i\left(k_{x} x+k_{y} y\right)} \tag{13.26} \label{eq-13-26}
$$

Inserting [13.24](#eq-13-24) into [13.19](#eq-13-19) with [13.20](#eq-13-20) and [13.21](#eq-13-21) 
$$
k_{z}=\sqrt{\omega^{2} / v^{2}-k_{x}^{2}-k_{y}^{2}} \tag{13.27} \label{eq-13-27}
$$

$$
\text { if } \operatorname{Im} k_{z}=0 \text { , then } \operatorname{Re} k_{z}>0 \text { ; otherwise } \operatorname{Im} k_{z}>0 \tag{13.28} \label{eq-13-28}
$$

gives the result for the wave, $\psi(\vec{r}, t)$, for $z > 0$. This result is really very general. It holds for any reasonable $f(x, y)$.

____________________________

[^13-2-2]: For example, see Hecht, chapter 10.

[^13-2-3]: See the discussion starting on page 314.

[^13-2-4]: Note that in a real physical situation, the boundary conditions are often much more complicated than [13.16](#eq-13-16), because the physics of the boundary matters. However, this often means that diffraction in a real situation is even larger.

## 13.3: Small and Large z

But what do we do with it? The integral in [13.19](#eq-13-19) is too complicated to do analytically. Below, we will give some examples of how it works by doing the integral numerically. However, for small $z$ and for large $z$, the integral simplifies in different ways.

### Small $z$

For sufficiently small $z$, we would expect on physical grounds that we really have produced a beam and projected an image of the function, $f(x, y)$. To see this explicitly, we will use the fact that for a particular (well behaved) $f(x, y)$, the Fourier transform $C(k_{x}, k_{y})$ is a function that goes to zero for 
$$
k \equiv \sqrt{k_{x}^{2}+k_{y}^{2}} \gg 1 / L \tag{13.29} \label{eq-13-29}
$$

for some $L$ much larger than the wavelength. The distance $L$ is determined by the smoothness of $f(x, y)$. Typically, $L$ is the size of the smallest important feature in $f(x, y)$, the smallest distance over which $f(x, y)$ changes appreciably. We saw this in our discussion of Fourier transforms in connection with signals in Chapter 10. We will see more examples below. We can expand $k_{z}z$ in the exponential in a Taylor expansion, 
$$
\begin{aligned}
&k_{z} z=z \sqrt{\omega^{2} / v^{2}-k_{x}^{2}-k_{y}^{2}} \\
&=\frac{z \omega}{v} \sqrt{1-\frac{v^{2}\left(k_{x}^{2}+k_{y}^{2}\right)}{\omega^{2}}} \\
&\approx \frac{z \omega}{v}-\frac{z v\left(k_{x}^{2}+k_{y}^{2}\right)}{2 \omega}
 \tag{13.30} \label{eq-13-30}
\end{aligned}
$$

Because of [13.25](#eq-13-25), the largest value of $\sqrt{k_{x}^{2}+k_{y}^{2}}$ that we need in the integral, [13.19](#eq-13-19) 
$$
\psi(\vec{r}, t)=\int d k_{x} d k_{y} C\left(k_{x}, k_{y}\right) e^{i \vec{k} \cdot \vec{r}-i \omega t} \text { for } z>0 \tag{13.31} \label{eq-13-31}
$$

is of order $1/L$. For much larger values, the integrand is zero. Thus the largest possible value of the second term in the expansion [13.26](#eq-13-26) that matters in the integral, [13.19](#eq-13-19) is of the order of 
$$
\frac{z v}{2 \omega L^{2}}. \tag{13.32} \label{eq-13-32}
$$

Therefore, if $L$ is finite and $z$ is small $\left(\ll \omega L^{2} / v\right)$, the second term is small and we can keep only the first term, $z \omega / v$. Then putting this back into the integral, [13.19](#eq-13-19), we have 
$$
\begin{gathered}
\psi(\vec{r}, t)=\int d k_{x} d k_{y} C\left(k_{x}, k_{y}\right) e^{i \vec{k} \cdot \vec{r}-i \omega t} \\
\approx \int d k_{x} d k_{y} C\left(k_{x}, k_{y}\right) e^{i\left(k_{x} x+k_{y} y+z \omega / v-\omega t\right)} \\
\approx \int d k_{x} d k_{y} C\left(k_{x}, k_{y}\right) e^{i\left(k_{x} x+k_{y} y\right)} e^{i(z \omega / v-\omega t)} \approx f(x, y) e^{i \omega(z-v t) / v}
 \tag{13.33} \label{eq-13-33}
\end{gathered}
$$

This is just what we expect — a beam with the shape of the original function, propagating in the $z$ direction with velocity $v$.

The result [13.28](#eq-13-28) begins to break down when the next term in the Taylor series, [13.26](#eq-13-26), becomes important. That is when 
$$
\frac{z v\left(k_{x}^{2}+k_{y}^{2}\right)}{\omega} \approx 1 \tag{13.34} \label{eq-13-34}
$$

Thus 
$$
z \approx \frac{\omega L^{2}}{v}=\frac{2 \pi L^{2}}{\lambda} \tag{13.35} \label{eq-13-35}
$$

marks the transition from a simple beam to the onset of important diffraction effects.

If $L = 0$, which is the situtation in the example of a single slit of width $2a$, that we will analyze in detail later, important diffraction effects start immediately because the slit has sharp edges. However, the beam maintains some semblance of its original size until $z \approx a^{2} / \lambda$.

For z larger than $\omega L^{2} / v$, the $k_{x}$ and $k_{y}$ dependence from the $e^{i k_{z} z}$ factor cannot be ignored. In general, the evaluation of the integral, [13.19](#eq-13-19), is very hard. However, for very large $z, z \gg L$, we can use a physical argument to find the result of the integral, [13.19](#eq-13-19).

### Large $z$

Suppose that you are very far away, at a point $\vec{R}=(X, Y, Z)$, 
$$
(x, y, z)=(X, Y, Z) \text { for } Z \gg \omega L^{2} / v. \tag{13.36} \label{eq-13-36}
$$

Then you cannot see the details of the shape of the opening or other details of $f(x, y)$, only its position. The wave you detect at some far-away point must have come from the opening and if you are far enough away, it is almost a plane wave. This is called “Fraunhofer” or “far-field” diffraction. If this condition is not satisfied, the problem is called “Fresnel” or “near-field” diffraction. For the light to actually reach your eye in the far-field situation, the propagation vector must point from the opening to you. The situation is depicted in the diagram in [Figure 13.3](#fig-13-3). In the near-field region, the spreading due to diffraction is of the same order as the size of the opening. For much larger $Z$, in the far-field region, the $\vec{k}$ vector must point back to the opening.

Thus the only contribution to the integral, [13.19](#eq-13-19), 
$$
\psi(\vec{r}, t)=\int d k_{x} d k_{y} C\left(k_{x}, k_{y}\right) e^{i \vec{k} \cdot \vec{r}-i \omega t} \text { for } z>0 \tag{13.37} \label{eq-13-37}
$$

that counts is that proportional to $e^{i \vec{k} \cdot \vec{R}}$ where $\vec{k}$ points from the opening to your eye. **Because the integrand in [13.19](#eq-13-19) has a factor of**$C(k_{x}, k_{y})$**, the amplitude of the wave is proportional to** $C(k_{x}, k_{y})$ **where**
$$
\left(k_{x}, k_{y}, k_{z}\right)=\left(k_{x}, k_{y}, \sqrt{\omega^{2} / v^{2}-k^{2}}\right) \propto(X, Y, Z). \tag{13.38} \label{eq-13-38}
$$

:::{figure} ../images/lt-32774-clipboard_e66bcbdad6ae313f1c2d1ca133c7f6691.png
:label: fig-13-3
:enumerator: 13.3
:alt: The basic diffraction problem — making a beam.

The basic diffraction problem — making a beam.
:::
The amplitude is also inversely proportional to 
$$
R=\sqrt{X^{2}+Y^{2}+Z^{2}}, \tag{13.39} \label{eq-13-39}
$$

because the intensity must fall off as $R^{−2}$, as in a spherical wave, by energy conservation.

There are other factors that contribute to the variation of the amplitude besides $C(k_{x}, k_{y})$ (we will see one below). However, typically, all the other factors are very slowly varying and can be ignored. Thus we expect that the intensity for large $Z$ is approximately 
$$
\frac{\left|C\left(k_{x}, k_{y}\right)\right|^{2}}{R^{2}}, \tag{13.40} \label{eq-13-40}
$$

where $\vec{k}$ and $\vec{R}$ are related by [13.32](#eq-13-32). 
$$
\left(k_{x}, k_{y}, k_{z}\right)=\left(k_{x}, k_{y}, \sqrt{\omega^{2} / v^{2}-k^{2}}\right) \propto(X, Y, Z) \tag{13.41} \label{eq-13-41}
$$

which implies 
$$
\frac{k_{x}}{X}=\frac{k_{y}}{Y}=\frac{k_{z}}{Z}=\frac{k}{R}=\frac{\omega / v}{R}, \tag{13.42} \label{eq-13-42}
$$

or 
$$
k_{x}=\frac{k X}{R}, \quad k_{y}=\frac{k Y}{R}. \tag{13.43} \label{eq-13-43}
$$

**Now here is the point!** Inserting [13.36](#eq-13-36) into [13.24](#eq-13-24) 
$$
C\left(k_{x}, k_{y}\right)=\frac{1}{4 \pi^{2}} \int d x d y f(x, y) e^{-i\left(k_{x} x+k_{y} y\right)} \tag{13.44} \label{eq-13-44}
$$

gives the integral in [13.14](#eq-13-14) that came from our physical argument about interference! 
$$
\int d x \int d y f(x, y) e^{i k(R+\Delta \ell)}=e^{i k R} \int d x \int d y f(x, y) e^{-i(x X+y Y) k / R} \tag{13.45} \label{eq-13-45}
$$

Thus our description of the wave for $z > 0$ as a forced oscillation problem contains the same factor that describes the interference of all the paths that the wave can take from the opening to $\vec{R}$. The advantage of our present approach is that it is a real derivation.

We can also write this result in terms of angles: 
$$
\sin \theta_{x}=\frac{X}{R}=\frac{k_{x} v}{\omega}, \sin \theta_{y}=\frac{Y}{R}=\frac{k_{y} v}{\omega} \tag{13.46} \label{eq-13-46}
$$

where $\theta_{x}$ and $\theta_{y}$ are the angles of the vector $\vec{r}$ from the $X = y = 0$ line in the $x$ and $y$ directions. Or equivalently, 
$$
X=\frac{Z k_{x}}{\sqrt{\omega^{2} / v^{2}-k_{x}^{2}-k_{y}^{2}}}, \quad y=\frac{Z k_{y}}{\sqrt{\omega^{2} / v^{2}-k_{x}^{2}-k_{y}^{2}}} \tag{13.47} \label{eq-13-47}
$$

This is illustrated in the diagram in [Figure 13.4](#fig-13-4).

### Stationary Phase

Mathematically, [13.32](#eq-13-32) 
$$
\left(k_{x}, k_{y}, k_{z}\right)=\left(k_{x}, k_{y}, \sqrt{\omega^{2} / v^{2}-k^{2}}\right) \propto(X, Y, Z) \tag{13.48} \label{eq-13-48}
$$

arises for large $Z$ becasue the phase of the exponential in [13.19](#eq-13-19) 
$$
\psi(\vec{r}, t)=\int d k_{x} d k_{y} C\left(k_{x}, k_{y}\right) e^{i \vec{k} \cdot \vec{r}-i \omega t} \text { for } z>0 \tag{13.49} \label{eq-13-49}
$$

is very rapidly varying as a function of $k_{x}$ and $k_{y}$ **except for special values of** $k_{x}$ **and** $k_{y}$ **where the derivatives of the phase with respect to** $k_{x}$ **and** $k_{y}$ **vanish.** If the function is centered at $x = y = 0$ and is smooth,[^13-3-5] the $k$ derivatives of $C(k_{x}, k_{y})$ are of order $L$ and are

:::{figure} ../images/lt-32775-clipboard_ea18f1b1113c21956dbc2932571da305a.png
:label: fig-13-4
:enumerator: 13.4
:alt: irrelevant. Thus the contribution comes from k_{x}, k_{y} such that

irrelevant. Thus the contribution comes from $k_{x}$, $k_{y}$ such that
:::
$$
\begin{aligned}
\frac{\partial}{\partial k_{x}}\left(X k_{x}+Y k_{y}+Z \sqrt{\omega^{2} / v^{2}-k_{x}^{2}-k_{y}^{2}}\right) &=X-\frac{Z k_{x}}{\sqrt{\omega^{2} / v^{2}-k_{x}^{2}-k_{y}^{2}}}=0, \\
\frac{\partial}{\partial k_{y}}\left(X k_{x}+Y k_{y}+Z \sqrt{\omega^{2} / v^{2}-k_{x}^{2}-k_{y}^{2}}\right) &=Y-\frac{Z k_{y}}{\sqrt{\omega^{2} / v^{2}-k_{x}^{2}-k_{y}^{2}}}=0,
 \tag{13.50} \label{eq-13-50}
\end{aligned}
$$

which is equivalent to [13.38](#eq-13-38). A careful evaluation of the integral, taking account of the $k_{x}$ and $k_{y}$ dependence in the neighborhood of the critical value determined by [13.38](#eq-13-38) yields an additional factor in the amplitude of the wave of 
$$
\frac{Z}{r^{2}}=\frac{\cos \theta}{r} \tag{13.51} \label{eq-13-51}
$$

where $\theta$ is the angle of the vector $\vec{r}$ to the $z$ axis. We expected the $/r$ factor because of the spreading of the diffracted wave with distance. The factor of $\cos \theta$ is actually the only place where the details of the boundary condition at infinity, [13.21](#eq-13-21), enter into our expression for the diffracted wave. This factor guarantees that the diffracted wave vanishes as we go to the surface of the opaque screen far from the opening. This is analogous to the “obliquity” factor $(1+\cos \theta) / 2$, in the Fresnel-Kirchhoff diffraction theory. The difference between the two is due to the different boundary conditions (our infinite flat barrier versus the lack of incoming spherical waves). We will usually ignore this factor, and indeed it generally does not make much difference where diffraction is important in the forward direction. The important thing is that everything else about the diffraction in the far-field region is determined just by linearity, translation invariance and local interactions.

### Spot Size

A useful way to think about the transition from near-field (Fresnel) to far-field (Fraunhofer) diffraction is to consider the size of the spot formed by the beam of [Figure 13.3](#fig-13-3) as a function of $z$. This is a competition between two effects. Increasing the size of the opening makes the spot size larger at small $z$. However, decreasing the size of the opening increases the spread in $k_{x}$, thus increasing the diffraction, and making the spot size larger at large $z$. For a given $z$, the best you can do is to choose the size of your opening so that these two effects are of the same order of magnitude. Suppose that the size of your opening is $\ell$. Then the spread in $k_{x}$ is of order $2 \pi / \ell$. At large $z$, the beam spreads into a cone with an opening angle of order 
$$
\theta \approx \frac{\lambda}{\ell}. \tag{13.52} \label{eq-13-52}
$$

Thus when 
$$
\frac{\lambda}{\ell} \approx \frac{\ell}{z}, \tag{13.53} \label{eq-13-53}
$$

the spreading of the spot due to diffraction is of the same order of magnitude as the size of the opening. We conclude that to minimize the spot size for a given $z$, you should choose an opening of size 
$$
\ell \approx \sqrt{\lambda z}. \tag{13.54} \label{eq-13-54}
$$

The relation, [13.41](#eq-13-41), up to factors of $\pi$, is what defines the region of Fresnel diffraction in [Figure 13.3](#fig-13-3). Another way of summarizing the result of this discussion is that for 
$$
z \gg \frac{\ell^{2}}{\lambda}, \tag{13.55} \label{eq-13-55}
$$

the spreading due to diffraction is much larger than the spreading due to the size of the opening. This defines the region of far-field, or Fraunhofer diffraction.

### Angles

What happens if the plane wave in [13.15](#eq-13-15) is coming in toward the opaque barrier at an angle, rather than head on? To be specific, suppose that the $\vec{k}$ vector of the wave makes an angle $\theta$ with the perpendicular in the $x$-$z$ plane, so that 
$$
k_{z}=k \cos \theta, \quad k_{x}=k \sin \theta. \tag{13.56} \label{eq-13-56}
$$

Then it is reasonable to assume that the analog of [13.15](#eq-13-15), the amplitude of the wave in the $z = 0$ plane, is<sup>6 </sup>
$$
f_{\theta}(x, y)=f(x, y) e^{i x k \sin \theta} \tag{13.57} \label{eq-13-57}
$$

where the additional $x$ dependence has simply been inherited from the $x$ dependence of the incoming wave. We can write the Fourier transform of $f_{\theta}$ in terms of that of $f$ as follows: 
$$
\begin{aligned}
&f_{\theta}(x, y)=\int d k_{x} d k_{y} C\left(k_{x}, k_{y}\right) e^{i\left(k_{x} x+k_{y} y\right)} e^{i x k \sin \theta} \\
&=\int d k_{x} d k_{y} C\left(k_{x}-k \sin \theta, k_{y}\right) e^{i\left(k_{x} x+k_{y} y\right)}
 \tag{13.58} \label{eq-13-58}
\end{aligned},
$$

which implies 
$$
Cθ(kx, ky) = C(kx − k \sin θ, ky). \tag{13.59} \label{eq-13-59}
$$

This is entirely reasonable. If the maximum of $C(k_{x}, k_{y})$ occurs at $k_{x} \approx 0$, the maximum of $C_{\theta}(k_{x}, k_{y})$ occurs at $k_{x}=k \sin \theta$. Thus the diffraction pattern appears where a line through the opening in the direction of the incoming plane wave crosses the screen, just as we would expect from a skew beam.

__________________________

[^13-3-5]: See, however, the discussion on page 383.

## 13.4: Examples

### Single Slit

Suppose 
$$
f(x, y)=\left\{\begin{array}{l}
1 \text { for }-a \leq x \leq a \\
0 \text { for }|x|>a
\end{array}\right. \tag{13.60} \label{eq-13-60}
$$

independent of $y$. This is really a two-dimensional problem, because we can keep $k_{y} = 0$ and ignore it (except for a factor of $2\pi$, that we won’t worry about) by dropping the $k_{y}$ integral from [13.19](#eq-13-19). [13.24](#eq-13-24) 
$$
C\left(k_{x}, k_{y}\right)=\frac{1}{4 \pi^{2}} \int d x d y f(x, y) e^{-i\left(k_{x} x+k_{y} y\right)} \tag{13.61} \label{eq-13-61}
$$

becomes (with the $2\pi$ corrected to make it one-dimensional)[^13-4-7] 
$$
\begin{gathered}
C\left(k_{x}\right)=\frac{1}{2 \pi} \int_{-\infty}^{\infty} d x f(x) e^{-i k_{x} x} \\
=\frac{1}{2 \pi} \int_{-a}^{a} d x e^{-i k_{x} x}=\left.\frac{1}{-2 i \pi k_{x}} e^{-i k_{x} x}\right|_{-a} ^{a}=\frac{\sin k_{x} a}{\pi k_{x}} .
 \tag{13.62} \label{eq-13-62}
\end{gathered}
$$

Thus we expect that the intensity of the wave at large $z$ is proportional to $\left|C\left(k_{x}\right)\right|^{2}$, 
$$
I(x, y) \propto \frac{\sin ^{2}\left(k_{x} a\right)}{k_{x}^{2}} \tag{13.63} \label{eq-13-63}
$$

where 
$$
\frac{x}{r}=\frac{k_{x}}{k}=\frac{k_{x}}{\omega / v} \tag{13.64} \label{eq-13-64}
$$

or 
$$
k_{x}=\frac{\omega}{v} \frac{x}{r}. \tag{13.65} \label{eq-13-65}
$$

Thus if we measure the intensity of the diffracted beam, a distance $r$ from the opening, the intensity goes as follows:[^13-4-8] 
$$
I(x, y) \propto \frac{\sin ^{2}(2 \pi a x / r \lambda)}{x^{2}} \tag{13.66} \label{eq-13-66}
$$

where $\lambda$ is the wavelength of the light. A plot of $I$ as a function of $x$ is shown in [Figure 13.5](#fig-13-5). This is called a diffraction pattern. In the important case of light passing through a small aperture, the diffraction pattern can be easily observed by projecting the diffracted beam onto a screen. The features of this pattern worth noting are the large maximum at $x = 0$, with twice the width of all the other maxima, and the periodic zeros for $x=n r \lambda / 2 a$. Note also that as the width, $a$ of the slit decreases, the size of the diffraction pattern increases.

**Moral: This inverse relation between the size of the slit and the size of the diffraction pattern is another illustration of the general feature of Fourier transforms discussed in Chapter 10.**

### Near-field Diffraction

We will pause here to discuss the region for intermediate $z$, Fresnel diffraction, where the diffraction problem is complicated. All we can do is to evaluate the integral, [13.19](#eq-13-19), numerically, by computer, and find the intensity approximately at various values of $z$. For example, suppose that we take 
$$
\frac{\omega}{c}=\frac{2 \pi}{\lambda}=\frac{100}{a}, \tag{13.67} \label{eq-13-67}
$$

:::{figure} ../images/lt-32776-clipboard_ecf2ffb37b9a6ba366550983eded1f64e.png
:label: fig-13-5
:enumerator: 13.5
:alt: The intensity of the diffraction pattern as a function of x.

The intensity of the diffraction pattern as a function of $x$.
:::
corresponding to a rather small slit, with a width of only $100 / \pi \approx 32$ times the wavelength of the wave. We will then use [13.19](#eq-13-19) to calculate the intensity of the wave at various values of $z$, in units of $a$. For small $z$, the result is shown in [Figure 13.6](#fig-13-6). You can see that the basic beam shape is maintained for a while, as we expected from [13.28](#eq-13-28). However, wiggles develop immediately. The rather large wiggly diffraction is due to the sharp edges. Below, we will give another example in which the diffraction is much gentler. For intermediate $z$, shown in [Figure 13.7](#fig-13-7), the wiggles begin to coalesce and dramatically change the overall shape of the beam. At the same time, the beam begins to spread out.

:::{figure} ../images/lt-32777-clipboard_e049da0cdb02afdd195196bd92cc7c78a.png
:label: fig-13-6
:enumerator: 13.6
:alt: The intensity of a wave passing through a slit, for small z.

The intensity of a wave passing through a slit, for small $z$.
:::
Finally, in [Figure 13.8](#fig-13-8), we show the approach to the large $z$ regions, where diffraction takes over completely and the far field diffraction pattern, [13.54](#eq-13-54), appears.

:::{figure} ../images/lt-32778-clipboard_e0fead4d5e053a19d275c6422dc9793c8.png
:label: fig-13-7
:enumerator: 13.7
:alt: The intensity of a wave passing through a slit, for intermediate z.

The intensity of a wave passing through a slit, for intermediate $z$.
:::
:::{figure} ../images/lt-32779-clipboard_e3158b3fe00080c2f267550b178616961.png
:label: fig-13-8
:enumerator: 13.8
:alt: The intensity of a wave passing through a slit, as z gets large.

The intensity of a wave passing through a slit, as $z$ gets large.
:::
One more example may be interesting. Suppose that instead of being a simple hole in the opaque screen, the opening is shaded in such a way that the wave disturbance at $z = 0$ has the form 
$$
f(x, y)=e^{-|x| / a}. \tag{13.68} \label{eq-13-68}
$$

The Fourier transform here was done in Chapter 10 in [10.49](#eq-10-49)-[10.56](#eq-10-56). Substituting $\omega \rightarrow k_{x}$ and $\Gamma \rightarrow 1 / a$ in [10.56](#eq-10-56) gives 
$$
C\left(k_{x}\right)=\frac{1}{\pi} \frac{a}{1+a^{2} k_{x}^{2}}. \tag{13.69} \label{eq-13-69}
$$

This determines the intensity distribution at large $z$. However, unlike the previous example, this pattern gives very gentle diffraction. For small $z$, the intensity pattern is shown in [Figure 13.9](#fig-13-9). The sharp point in [13.56](#eq-13-56) disappears, but otherwise the change is very gradual because the initial pattern is very smooth except at $x = 0$. For intermediate and large $z$, the intensity patterns are shown in [Figure 13.10](#fig-13-10) and [Figure 13.11](#fig-13-11).

:::{figure} ../images/lt-32780-clipboard_ee71d31b2ca320b876001726b7ebc6055.png
:label: fig-13-9
:enumerator: 13.9
:alt: The intensity distribution from [13.56](#eq-13-56) for small z.

The intensity distribution from [13.56](#eq-13-56) for small $z$.
:::
:::{figure} ../images/lt-32781-clipboard_e8a07f3b49fcff0399cf568096148cf99.png
:label: fig-13-10
:enumerator: 13.10
:alt: The intensity distribution from [13.56](#eq-13-56) for intermediate z.

The intensity distribution from [13.56](#eq-13-56) for intermediate $z$.
:::
:::{figure} ../images/lt-32782-clipboard_e95b42a8e621ba7810d44c8934d3271f2.png
:label: fig-13-11
:enumerator: 13.11
:alt: The intensity distribution from [13.56](#eq-13-56) for large z.

The intensity distribution from [13.56](#eq-13-56) for large $z$.
:::
### Rectangle

Suppose 
$$
f(x, y)-\left\{\begin{array}{l}
1 \text { for }-a_{x} \leq x \leq a_{x} \text { and }-a_{y} \leq y \leq a_{y}, \\
0 \text { otherwise }.
\end{array}\right. \tag{13.70} \label{eq-13-70}
$$

This is the product of a single slit pattern in $x$ with a single slit pattern in $y$. The Fourier transform is the product of the one-dimensional Fourier transforms 
$$
\begin{aligned}
C\left(k_{x}, k_{y}\right)=& \frac{1}{4 \pi^{2}} \int_{-a_{x}}^{a_{x}} d x e^{-i k_{x} x} \int_{-a_{y}}^{a_{y}} d y e^{-i k_{y} y} \\
&=\frac{\sin \left(k_{x} a_{x}\right)}{\pi k_{x}} \frac{\sin \left(k_{y} a_{y}\right)}{\pi k_{y}}
 \tag{13.71} \label{eq-13-71}
\end{aligned}
$$

Thus the intensity looks approximately like 
$$
I(x, y) \propto \frac{\sin ^{2}\left(2 \pi a_{x} x / r \lambda\right)}{x^{2}} \frac{\sin ^{2}\left(2 \pi a_{y} y / r \lambda\right)}{y^{2}}. \tag{13.72} \label{eq-13-72}
$$

Of course, once again, because of the general properties of the Fourier transform, if the rectangle is narrow in $x$, the diffraction pattern is spread out in $k_{x}$, and similarly for $y$.

### $\delta$ “Functions”

As the slit in [13.49](#eq-13-49) gets narrower, the diffraction pattern spreads out. Of course, the intensity also decreases. The intensity at $k_{x} = 0$ is related to the Fourier transform of $f$ at zero, which is just the integral of $f$ over all $x$. As the slit gets narrower, this integral decreases. But suppose that we increase the intensity of the incoming beam, as $a$ decreases, to keep the intensity of the maximum of the diffraction pattern fixed. Ignoring the $y$ dependence, we require 
$$
f_{a}(x)=\left\{\begin{array}{l}
\frac{1}{2 a} \text { for }-a \leq x \leq a, \\
0 \text { for }|x|>a.
\end{array}\right. \tag{13.73} \label{eq-13-73}
$$

The limit of $f_{a}$ as $a \rightarrow 0$ doesn’t really exist as a function. It is zero everywhere except $x = 0$. But it goes to $\infty$ very fast at $x = 0$, so that 
$$
\lim _{a \rightarrow 0} \int d x f_{a}(x)=1 \tag{13.74} \label{eq-13-74}
$$

It is extraordinarily convenient to invent an object with these properties, called a “$\delta$-function”. That is, $\delta(x)$ has the property that it is zero except at $x = 0$, and that 
$$
\int d x \delta(x)=1. \tag{13.75} \label{eq-13-75}
$$

In fact, this object makes a kind of mathematical sense, so long as you do **not** square it. $\delta$-functions can be manipulated like ordinary functions, added together, multiplied by constants or smooth functions — $\delta$-functions of different variables can even be multiplied — just don’t square them! For example, a delta function can be multiplied by an ordinary continuous function: 
$$
f(x) \delta(x)=f(0) \delta(x) \tag{13.76} \label{eq-13-76}
$$

where the equality follows because the delta function vanishes except at $x = 0$, so that only the value of $f$ at 0 matters.

Now it should be clear from [13.63](#eq-13-63) and [13.64](#eq-13-64) that the Fourier transform of $\delta(x)$ is just a constant: 
$$
C(k)=\frac{1}{2 \pi} \int d x e^{-i k x} \delta(x)=\frac{1}{2 \pi}. \tag{13.77} \label{eq-13-77}
$$

The diffraction pattern for this thing is thus very boring. There is uniform illumination at all angles.

Of course, in physics, we can’t make $\delta$-functions. However, if $a$, in [13.61](#eq-13-61) is much smaller than the wavelength of the wave, then it might as well be a $\delta$-function, because it only matters what $C(k_{x})$ is for $k_{x}<k=2 \pi / \lambda$. Larger $k_{x}$ correspond to exponential waves that die off rapidly with $z$. But for such $k_{x}$, the product $k_{x}a$ is very small, thus 
$$
C\left(k_{x}\right)=\frac{1}{2 \pi} \frac{\sin k_{\underline{x}} a}{k_{x} a} \rightarrow \frac{1}{2 \pi}\left(1-\frac{\left(k_{\underline{x}} a\right)^{2}}{6}+\cdots\right) \approx \frac{1}{2 \pi} \tag{13.78} \label{eq-13-78}
$$

and we still get uniform diffraction over all angles.

**Moral:**$\delta$**-functions are simply a convenience. When physicists talk about** a $\delta$**-function, they mean (or at least they should mean) a function like**$f_{a}(x)$**, where**$a$ **is smaller than any physical distance that is important in the problem. Once** $a$ **gets that small, it is often easier to keep track of the math when you go all the way to the unphysical limit,** $a = 0$**.**

### Some Properties of $\delta$-Functions

The Fourier transform of a $\delta$-function is a complex exponential: 
$$
\text { if } f(x)=\delta(x-a) \text { then } C(k)=\frac{1}{2 \pi} e^{-i k a} \text { . } \tag{13.79} \label{eq-13-79}
$$

The Fourier transform of a complex exponential is a $\delta$-function: 
$$
\text { if } f(x)=e^{-i \ell x} \text { then } C(k)=\delta(k-\ell). \tag{13.80} \label{eq-13-80}
$$

A $\delta$-function can be reached as a limit in a variety of different ways. For example, from [13.68](#eq-13-68), we would expect that as $a \rightarrow \infty$, the Fourier transform of [13.49](#eq-13-49) should approach a $\delta$-function: 
$$
\lim _{a \rightarrow \infty} \frac{\sin k_{x} a}{k_{x}}=\delta\left(k_{x}\right) \text { . } \tag{13.81} \label{eq-13-81}
$$

### Dimension from Two

Using $\delta$-functions, we can say more elegantly what is meant by the statement we made above that if $f(x, y)$ does not depend on $y$, the problem is one-dimensional. If we look at the limit of [13.58](#eq-13-58) as $a_{y} \rightarrow \infty$, it goes over into [13.49](#eq-13-49). In other words, when a rectangle is infinitely long, it is a slit. In this limit, the Fourier transform, [13.59](#eq-13-59) goes into 
$$
\frac{\sin \left(k_{x} a_{x}\right)}{\pi k_{x}} \delta\left(k_{y}\right). \tag{13.82} \label{eq-13-82}
$$

This is the real meaning of [13.50](#eq-13-50). It is one-dimensional in the sense that $k_{y}$ is stuck at 0. There is no diffraction in the $y$ direction.

### Many Narrow Slits

An interesting application of δ-functions is to the diffraction pattern for several narrow slits. We will use this later in various ways. Consider a function, $f(x, y)$ of the form 
$$
\sum_{j=0}^{n-1} \delta(x-j b) \tag{13.83} \label{eq-13-83}
$$

:::{figure} ../images/lt-32783-clipboard_eaa137338f224850f55a5d87a3217eb8b.png
:label: fig-13-12
:enumerator: 13.12
:alt: If b k_{x} / k=n \lambda, the interference is constructive.

If $b k_{x} / k=n \lambda$, the interference is constructive.
:::
:::{figure} ../images/lt-32784-clipboard_ead7528801903fb72d63246526939576a.png
:label: fig-13-13
:enumerator: 13.13
:alt: The diffraction pattern for three narrow slits.

The diffraction pattern for three narrow slits.
:::
This describes a series of $n$ narrow slits[^13-4-9] at $x = 0$, $x = b$, $x = 2b$, *etc.*, up to $x = (n − 1)b$. The Fourier transform of [13.71](#eq-13-71) is a sum of contributions from the individual $\delta$-functions,

:::{figure} ../images/lt-32785-clipboard_ecc1fbcae5cb2f02ec24b1f9f2fc5fa01.png
:label: fig-13-14
:enumerator: 13.14
:alt: The diffraction pattern for 6 narrow slits.

The diffraction pattern for 6 narrow slits.
:::
from [13.67](#eq-13-67) and [13.68](#eq-13-68) 
$$
C\left(k_{x}, k_{y}\right)=\delta\left(k_{y}\right) \frac{\perp}{2 \pi} \sum_{j=0}^{n-1} e^{-i j b k_{x}}. \tag{13.84} \label{eq-13-84}
$$

But the sum is a geometric series that can be done explicitly: 
$$
\begin{gathered}
\sum_{j=0}^{n-1} e^{-i j b k_{x}}=\frac{1-e^{-i n b k_{x}}}{1-e^{-i b k_{x}}} \\
=\frac{e^{-i n b k_{x} / 2}\left(e^{i n b k_{x} / 2}-e^{-i n b k_{x} / 2}\right)}{e^{-i b k_{x} / 2}\left(e^{i b k_{x} / 2}-e^{-i b k_{x} / 2}\right)}=e^{-i(n-1) b k_{x} / 2} \frac{\sin n b k_{x} / 2}{\sin b k_{x} / 2} .
 \tag{13.85} \label{eq-13-85}
\end{gathered}
$$

Thus the diffraction pattern intensity is proportional to 
$$
\frac{\sin ^{2} n b k_{x} / 2}{\sin ^{2} b k_{x} / 2}. \tag{13.86} \label{eq-13-86}
$$

For $n = 2$, [13.74](#eq-13-74) is just 
$$
4 \cos ^{2} \frac{b k_{x}}{2}=2\left(1+\cos b k_{x}\right). \tag{13.87} \label{eq-13-87}
$$

This is the problem with which we started the chapter. When $b k_{x}=2 m \pi$ for integer $m$, then the wave from one slit travels farther than the wave from the other by $m \lambda$, where $\lambda=2 \pi / k$ is the wavelength. Thus for $b k_{x}=2 m \pi$ the interference is constructive, as illustrated in [figure 13.12](#fig-13-12).

For larger $n$, we still get constructive interference for $b k_{x}=2 m \pi$, but the maxima are sharper, because with more slits, there are more possibilities for destructive interference at other angles. In [Figure 13.13](#fig-13-13) and [Figure 13.14](#fig-13-14), we plot [13.74](#eq-13-74) versus $bk_{x}$ from (−$\pi$ to $3\pi$ so that you can see two full periods) for $n = 3$ and $6$. Notice the appearance of $n − 2$ secondary maxima between the primary maxima of the intensity. We will return to these relations when we discuss diffraction gratings.

____________________________________

<sup>6</sup>Again, this is simplistic, ignoring complications from the boundaries in the same way as [13.15](#eq-13-15).

[^13-4-7]: Note that $\sin k a / k$ is well-defined ($= a$) at $k = 0$.

[^13-4-8]: Here we are assuming small angles, so that $\sin \theta \approx \tan \theta$. In our discussion of diffraction gratings below, we will see what happens when the difference in important.

[^13-4-9]: “Narrow” here means narrow compared to the wavelength of the light — see the moral above.

## 13.5: Convolution

There is a rather simple theorem, know as the convolution theorem, that is extremely useful in dealing with Fourier transforms. Suppose that we have two functions, $f_{1}(x)$ and $f_{2}(x)$. Define the function $f_{1} \circ f_{2}$ as follows: 
$$
f_{1} \circ f_{2}(x)=\int_{-\infty}^{\infty} d y f_{1}(x-y) f_{2}(y) \tag{13.88} \label{eq-13-88}
$$

This integral will be well defined if $f_{1}(x)$ and $f_{2}(x)$ fall off fast enough at infinity (and certainly if they are nonzero only in a finite region of $x$). Note that $f_{1} \circ f_{2}$ is a function of a single variable. It is also symmetric under the exchange of the two functions, because by a simple change of variables $(y \rightarrow x-y)$ 
$$
f_{1} \circ f_{2}(x)=\int_{-\infty}^{\infty} d y f_{1}(x-y) f_{2}(y)=\int_{-\infty}^{\infty} d y f_{1}(y) f_{2}(x-y)=f_{2} \circ f_{1}(x) \tag{13.89} \label{eq-13-89}
$$

Now the theorem is that the Fourier transform of the convolution is $2\pi$ times the product of the Fourier transforms of the two functions. The proof is immediate (all integrals run from −$\infty$ to $\infty$): 
$$
\begin{aligned}
C_{f_{1} \circ f_{2}}(k)=\frac{1}{2 \pi} \int d x e^{i k x} f_{1} \circ f_{2}(x) \\
=& \frac{1}{2 \pi} \int d x e^{i k x} \int d y f_{1}(x-y) f_{2}(y)
 \tag{13.93} \label{eq-13-93}
\end{aligned}
$$

Now we substitute $x \rightarrow y+z$ and write the integral over $y$ and $z$, 
$$
\begin{gathered}
=\frac{1}{2 \pi} \int d z e^{i k(y+z)} \int d y f_{1}(x-y) f_{2}(y) \\
=\frac{1}{2 \pi} \int d z e^{i k z} f_{1}(z) \int d y e^{i k y} f_{2}(y)=2 \pi C_{f_{1}}(k) C_{f_{2}}(k) .
 \tag{13.94} \label{eq-13-94}
\end{gathered}
$$

The two-dimensional analog of [13.79](#eq-13-79) is a straightforward extension. The two-dimensional convolution is 
$$
f_{1} \circ f_{2}(x, y)=\int d x^{\prime} d y^{\prime} f_{1}\left(x-x^{\prime}, y-y^{\prime}\right) f_{2}\left(x^{\prime}, y^{\prime}\right) \tag{13.95} \label{eq-13-95}
$$

$$
C_{f_{1} \circ f_{2}}\left(k_{x}, k_{y}\right)=4 \pi^{2} C_{f_{1}}\left(k_{x}, k_{y}\right) C_{f_{2}}\left(k_{x}, k_{y}\right) \tag{13.96} \label{eq-13-96}
$$

### Repeated Patterns

The convolution theorem can be used to understand many interesting situations. Consider the following very instructive pattern of two wide slits: 
$$
f(x, y)=\left\{\begin{array}{l}
1 \text { for }-a \leq x \leq a \\
1 \text { for }-a \leq x-b \leq a \\
0 \text { otherwise }
\end{array}\right. \tag{13.97} \label{eq-13-97}
$$

for $b > 2a$. A piece of the pattern is shown in [Figure 13.15](#fig-13-15) for $b = 3.5a$.

:::{figure} ../images/lt-32786-clipboard_e0029ede73e7ad4504c928fd4e099c30c.png
:label: fig-13-15
:enumerator: 13.15
:alt: A piece of the opaque barrier with two wide slits.

A piece of the opaque barrier with two wide slits.
:::
This can be regarded as the convolution of two functions: 
$$
f=f_{1} \circ f_{2} \tag{13.98} \label{eq-13-98}
$$

where 
$$
f_{1}(x, y)=\left\{\begin{array}{l}
1 \text { for }-a \leq x \leq a \\
0 \text { otherwise }
\end{array}\right. \tag{13.99} \label{eq-13-99}
$$

and 
$$
f_{2}(x, y)=\delta(x) \delta(y)+\delta(x-b) \delta(y) \tag{13.100} \label{eq-13-100}
$$

f2(x, y) = δ(x) δ(y) + δ(x − b) δ(y). The corresponding Fourier transforms are, from [13.70](#eq-13-70) [13.84](#eq-13-84) [13.85](#eq-13-85) Cf1 (kx, ky) = sin(kxa) π kx δ(ky) [13.86](#eq-13-86) and from [13.73](#eq-13-73) Cf2 (kx, ky) = 1 4π2 cos bkx 2 e−ibkx/2 . Now applying the convolution theorem gives [13.87](#eq-13-87) Cf1◦f2 (kx, ky) = cos bkx 2 e−ibkx/2 sin(kxax) π kx δ(ky). [13.88](#eq-13-88) 13.6. PERIODIC f(x, y) 395 Because b > 2a, this describes a pattern that oscillates rapidly on the scale set by 1/b, with an amplitude that varies with the single slit diffraction pattern characterized by size 1/a. The intensity pattern on a distant screen is shown in [figure 13.16](#fig-13-16), for b = 3.5a The dotted line is the pattern for a single wide slit (compare [13.5](#eq-13-5)).

:::{figure} ../images/lt-32787-clipboard_ee41ad75fc8be672dc64f9afb7ceef4dd.png
:label: fig-13-16
:enumerator: 13.16
:alt: The diffraction pattern for two wide slits.

The diffraction pattern for two wide slits.
:::
## 13.6: Periodic f(x, y)

Suppose $f(x, y)$ is periodic in $x$ with period $a$. That is 
$$
f(x+a, y)=f(x, y). \tag{13.101} \label{eq-13-101}
$$

Then $C(k_{x}, k_{y})$ can only be nonzero if

$$
k_{x}=\frac{2 \pi n}{a}. \tag{13.90} \label{eq-13-90}
$$

To see this, insert [13.89](#eq-13-89) into [13.24](#eq-13-24),

$$
C\left(k_{x}, k_{y}\right)=\frac{1}{4 \pi^{2}} \int d x d y\, f(x+a, y) e^{i\left(k_{x} x+k_{y} y\right)}. \tag{13.91} \label{eq-13-91}
$$

If we change variables from $x \rightarrow x-a$, Equation [13.91](#eq-13-91) is

$$
\begin{align} C\left(k_{x}, k_{y}\right) &= \frac{1}{4 \pi^{2}} \int d x d y \,f(x, y) e^{i\left(k_{x} x-k_{x} a+k_{y} y\right)} \\[4pt] &= e^{-i k_{x} a} C\left(k_{x}, k_{y}\right) \tag{13.92} \label{eq-13-92} \end{align}
$$

because the constant phase factor can be taken outside the integral. Equation [13.90](#eq-13-90) follows because Equation [13.92](#eq-13-92) implies that either $C\left(k_{x}, k_{y}\right)=0$ or $e^{-i k_{x} a}=1$.

An example of this general principle is Equation [13.74](#eq-13-74). In the limit that $n \rightarrow \infty$, [13.74](#eq-13-74) goes to 0 except for $k_{x}=2 \pi m / b$ for integer $m$ (where it is infinite). This example is simple because the slits are narrow, so the intensity is independent of $m$. However, with repeated wide slits, or some more complicated pattern, we could use the convolution theorem and [13.74](#eq-13-74) to see that [13.90](#eq-13-90) emerges as $n \rightarrow \infty$. The details of the pattern of each slit will then determine the relative intensity of the diffraction pattern at different $m$.

Thus any infinite regular pattern produces a discrete sequence of $k$’s. For example, a transmission diffraction grating, that consists of lots of equally spaced lines in the $y$ direction with $x$ separation $a$ on a transparent substrate, produces a $C(k_{x}, k_{y})$ that is nonzero only for $k_{y} = 0$ (because there is no $y$ dependence at all) and $k_{x}=2 n \pi / a$. Then [13.19](#eq-13-19) becomes 
$$
\sum_{n} C_{n} e^{i\left(2 n \pi x / a+z \sqrt{\omega^{2} / v^{2}-(2 n \pi / a)^{2}}-\omega t\right)} \tag{13.102} \label{eq-13-102}
$$

This describes a linear superposition of plane waves fanning out at angles in the $x$ direction given by

$$
\sin \theta_{n}=\frac{2 \pi n v}{a \omega}=\frac{n \lambda}{a} \tag{13.103} \label{eq-13-103}
$$

as shown in [Figure 13.17](#fig-13-17).

Typically, for a transmission grating, most of the light goes into the central line, which is to say that you can see right through the grating. Note that the even spacing in $\sin \theta_{n}$ in [13.94](#eq-13-94) corresponds to an increasing spacing of the lines projected onto a screen at fixed large $z$ (for example, a screen like your retina!) because the distance along the screen is determined by 
$$
\tan \theta_{n}=\frac{n \lambda}{\sqrt{a^{2}-n^{2} \lambda^{2}}}. \tag{13.104} \label{eq-13-104}
$$

There is a maximum value of $n$, above which no propagating wave is produced (because it corresponds to $\sin \theta>1$ and thus imaginary $k_{z}$).

Note also the dependence of [13.94](#eq-13-94) on wavelength. The larger the wavelength of the light, the larger the angles in the pattern from the diffraction grating. This, of course, is why the diffraction grating is useful. It can separate light of different frequencies. The different colors of the rainbow are spread out along a line, for each value of $n$. This is illustrated in the [Figure 13.18](#fig-13-18), for three frequencies, blue light with wavelength 4300 $\text{Å}$, green light with wavelength 5200 $\text{Å}$ and red light with wavelength 6300 $\text{Å}$, incident on a diffraction grating with 10,000 lines per inch. We have shown [13.95](#eq-13-95) for $n$ = −3 to 3 and labeled the colors for the $n = 1$ secondary maximum. As you see, in a realistic grating, the angles of diffraction can be large, and it is a very bad idea to use a small angle approximation.

13.6.1 Twisting the Grating

Some interesting examples of the effects discussed in [13.48](#eq-13-48) occur when the incoming light wave comes at the grating at an angle with respect to the perpendicular. Starting with the

:::{figure} ../images/lt-32788-clipboard_edc4ae5587ab8b98725cb354e47e11c64.png
:label: fig-13-17
:enumerator: 13.17
:alt: A transmission diffraction grating splits a beam of a single frequency.

A transmission diffraction grating splits a beam of a single frequency.
:::
:::{figure} ../images/lt-32789-clipboard_efcc67eba2154eb3b9805fc46c0a4cbee.png
:label: fig-13-18
:enumerator: 13.18
:alt: The pattern of three frequencies of light from a grating.

The pattern of three frequencies of light from a grating.
:::
grating lines in the $y$ direction and the grating in the $x$-$y$ plane, there are two different effects.

#### Twisting Around the $y$ Axis

Suppose that the light comes in at an angle $\theta_{in}$ from the perpendicular in the $x$-$z$ plane. Then from [13.48](#eq-13-48), 
$$
C_{\theta_{\mathrm{in}}}\left(k_{x}, k_{y}\right)=C\left(k_{x}-k \sin \theta_{\mathrm{in}}, k_{y}\right) \tag{13.105} \label{eq-13-105}
$$

where $C$ is Fourier transform for the perpendicular grating, 
$$
C\left(k_{x}, k_{y}\right) \neq 0 \quad \text { for } \quad k_{y}=0, k_{x}=\frac{2 \pi n}{a}. \tag{13.106} \label{eq-13-106}
$$

Thus 
$$
\begin{gathered}
C_{\theta_{\text {in }}}\left(k_{x}, k_{y}\right) \neq 0 \quad \text { for } \\
k_{y}=0, k_{x}=k \sin \theta_{\text {in }}+\frac{2 \pi n}{a}
 \tag{13.107} \label{eq-13-107}
\end{gathered}
$$

or 
$$
\sin \theta=\frac{k_{x}}{k}=\sin \theta_{\mathrm{in}}+\frac{n \lambda}{a}. \tag{13.108} \label{eq-13-108}
$$

In other words, $\sin \theta$ is simply displaced by $\sin \theta_{\mathrm{in}}$. For example, this means that if $\theta=\pi / a$, the pattern is exactly the same, but the central maximum has moved over, as shown in [Figure 13.19](#fig-13-19).

#### Twisting Around the $x$ Axis

Suppose that the light comes in at an angle $\theta$ from the perpendicular in the $y$-$z$ plane. Then from [13.48](#eq-13-48). 
$$
C_{\theta_{\text {in }}}\left(k_{x}, k_{y}\right)=C\left(k_{x}, k_{y}-k \sin \theta_{\text {in }}\right) . \tag{13.109} \label{eq-13-109}
$$

Now instead of being 0, $k_{y}$ is fixed at $k \sin \theta_{\text {in }}$ 
$$
k_{y}=k \sin \theta_{\text {in }}, \quad k_{x}=\frac{2 \pi n}{a} \text { . } \tag{13.110} \label{eq-13-110}
$$

Now the diffracted waves make nontrivial angles from the perpendicular both in $x$ and in $y$ 
$$
\sin \theta_{y}=\frac{k_{y}}{\sqrt{k_{y}^{2}+k_{z}^{2}}}=\frac{k_{y}}{\sqrt{k^{2}-k_{x}^{2}}}=\frac{\sin \theta_{\mathrm{in}}}{\sqrt{1-n^{2} \lambda^{2} / a^{2}}} \tag{13.111} \label{eq-13-111}
$$
and
$$
\sin \theta_{x}=\frac{k_{x}}{\sqrt{k_{x}^{2}+k_{z}^{2}}}=\frac{k_{x}}{\sqrt{k^{2}-k_{y}^{2}}}=\frac{n \lambda}{a \cos \theta_{\mathrm{in}}}. \tag{13.112} \label{eq-13-112}
$$

Again, as in [13.95](#eq-13-95), what we see if we project the pattern onto a perpendicular screen at fixed $z$ are the tangents, 
$$
(x, y)_{\text {screen }}=z\left(\tan \theta_{x}, \tan \theta_{y}\right), \tag{13.113} \label{eq-13-113}
$$

:::{figure} ../images/lt-32790-clipboard_ef9f285ca9608a9ff6f35750b4eddaf25.png
:label: fig-13-19
:enumerator: 13.19
:alt: The pattern for a beam at an angle, \theta_{\text {in }}=\arcsin \lambda / a.

The pattern for a beam at an angle, $\theta_{\text {in }}=\arcsin \lambda / a$.
:::

where 
$$
\tan \theta_{x}=\frac{k_{x}}{k_{z}}, \quad \tan \theta_{y}=\frac{k_{y}}{k_{z}} . \tag{13.114} \label{eq-13-114}
$$

Thus the diffraction pattern appears curved. What one sees on a screen or a retina is the colors of the rainbow spread out along a curved line. This is shown in [Figure 13.20](#fig-13-20), where we plot $\tan \theta_{x}$ versus $\tan \theta_{y}$ for a light source and grating as in [13.18](#eq-13-18), above, but with $\sin \theta_{\text {in }}=0.5$. Note that the pattern has not only curved, it has spread out, compared to [13.18](#eq-13-18). Here you really see the three-dimensional $\vec{k}$ vector in action. As $\tan \theta_{y}$ increases, for fixed $k_{x}$, $\tan \theta_{x}$ increases as well, because $k_{z}$ decreases.

### Resolving Power

The discussion so far has assumed that the diffraction grating is truely periodic. But this is only possible if the grating is infinite! In a finite grating, only the middle is periodic. The edges break the periodicity. In a grating consisting of only a finite number of grooves, $n$, the diffraction peaks are not infinitely sharp. They are not delta functions. However, as discussed at the beginning of this section, we actually already know what they look like in the finite

:::{figure} ../images/lt-32791-clipboard_ed5e9440ef94715a05772719e88bfa3f8.png
:label: fig-13-20
:enumerator: 13.20
:alt: The diffraction pattern from a twisted grating.

The diffraction pattern from a twisted grating.
:::
case because we have solved the problem of diffraction from $n$ evenly spaced narrow slits, in [13.74](#eq-13-74). In the general situation for $n$ identical grooves, the intensity looks like [13.74](#eq-13-74) multiplied by some slowly varying function that depends on the shape of the grooves (by the convolution theorem, [13.79](#eq-13-79)). The important consequence of this is that the shape of a diffraction peak for an $n$-slit grating is roughly given by [13.74](#eq-13-74).

The shape of the diffraction peak is important for the following practical question. Suppose that you have a beam of light that consists of a superposition of light of two different frequencies. How close together do the frequencies have to be before their nontrivial diffraction peaks melt together, so that you cannot use your diffraction grating to distinguish them? The larger the number of grooves in the grating, the sharper the diffraction peaks and the easier it is to distinguish different frequencies.

Rayleigh’s criterion is an historically important way of answering this question. Rayleigh assumed that it would be possible to distinguish the diffraction maxima from equally intense waves of slightly different wavelengths if the maximum of one frequency coincides with the first minimum of the other. For a grating of 6 lines, this criterion is illustrated in [Figure 13.21](#fig-13-21). The solid line is the total intensity of a wave consisting of two slightly different frequencies. The contributions from the separate frequency components are indicated by the dotted and dashed lines.

Any such fixed criterion for resolving power should be regarded not as a fact about nature, but as a conventional definition that facilitates communication between experimenters. It is always possible to do better than any given definition by accumulating accurate data on the line shape and modeling the details.

:::{figure} ../images/lt-32792-clipboard_efbc7766039d7b98e2e8ec37b1286910d.png
:label: fig-13-21
:enumerator: 13.21
:alt: Rayleigh’s criterion for a grating with 6 lines.

Rayleigh’s criterion for a grating with 6 lines.
:::
### Blazed Gratings

As a spectroscope, the transmission diffraction grating has a disadvantage compared to a prism. The difficulty is that, as we noted above, most of the light impinging on the grating goes right through and is not split into its component frequencies. This is a very serious problem in devices in which the total amount of light is limited. It is often important to have the bulk of the light going into a single **nonzero** value of $n$ in [13.94](#eq-13-94). Then nearly all of the photons can be used for the measurement, rather than being wasted in the $n = 0$ maximum (which carries no information about the frequency). As we argued above, there is no theoretical reason why such a thing cannot be done. The general principles of translation invariance and local interactions determine the possible angles of diffraction, but not how much light goes to which angle.

In fact, there is a practical and widely used method in reflection gratings. A reflecting surface with a series of evenly spaced parallel lines scored into it acts as a reflection grating, as illustrated in [Figure 13.22](#fig-13-22). This shows a reflection grating in which the predominant reflection of a beam coming in perpendicular to the plane of the grating is also perpendicular. What we want instead is shown in [Figure 13.23](#fig-13-23). To construct such a grating, you can shape the grooves in the grating so that the specular reflection from the individual grooves directs the beam into the nontrivial diffraction maximum, as shown in [Figure 13.24](#fig-13-24).

To do this, you can choose the angle of the blaze to be half the angle of the first maximum, $\theta_{1}=2 \pi v / a \omega$, in [13.94](#eq-13-94), as shown in the blow-up of a groove in [figure 13.25](#fig-13-25).

:::{figure} ../images/lt-32793-clipboard_e10e9c13c7faaaa8b32a0b0c08a443a62.png
:label: fig-13-22
:enumerator: 13.22
:alt: A reflection diffraction grating splits a beam of a single frequency.

A reflection diffraction grating splits a beam of a single frequency.
:::
:::{figure} ../images/lt-32794-clipboard_e6441d7961f9137213698e667cf290c6e.png
:label: fig-13-23
:enumerator: 13.23
:alt: A blazed grating directs the beam into a nontrivial diffraction maximum.

A blazed grating directs the beam into a nontrivial diffraction maximum.
:::
:::{figure} ../images/lt-32795-clipboard_e9f70449aa6d3ea0f0f8c87bbd1b396d1.png
:label: fig-13-24
:enumerator: 13.24
:alt: The grooves of a blazed grating.

The grooves of a blazed grating.
:::
:::{figure} ../images/lt-32796-clipboard_ea27ea2f5264a2fd59bc74c5a71dd920e.png
:label: fig-13-25
:enumerator: 13.25
:alt: \theta \approx \theta_{1} / 2.

$\theta \approx \theta_{1} / 2.$
:::
## 13.7: X-ray Diffraction

A beautiful three-dimensional example of diffraction from a periodic function is x-ray diffraction from crystals. A crystal is a regular array of atoms whose positions can be described by a periodic function 
$$
f(\vec{r})=f(\vec{r}+\vec{a}) \tag{13.115} \label{eq-13-115}
$$

where $\vec{a}$ is any vector from one point on the lattice to another. Mathematically, we can define the lattice as the set of all such vectors. Note that the lattice always includes the zero vector, the point at the origin. The three-dimensional Fourier transform of $f(\vec{r})$ is nonzero **only** for wave number vectors of the form 
$$
2 \pi \sum_{j=1}^{3} n_{j} \vec{\ell}_{j} \tag{13.116} \label{eq-13-116}
$$

where $\vec{\ell}_{j}$ are the basis vectors for the **“dual”** or **“reciprocal”** lattice that satisfies 
$$
\vec{a} \cdot \vec{\ell}_{j}=\text { integer, for all } \vec{a} \tag{13.117} \label{eq-13-117}
$$

The idea here is the same as the one-dimensional discussion of the diffraction grating, that $k_{x}=2 \pi n / a$, [13.90](#eq-13-90). The derivation of [13.107](#eq-13-107) is precisely analogous to that of [13.90](#eq-13-90).

We can visualize the relation between the lattice and the dual lattice more easily for two-dimensional “crystals.” For example, consider a lattice of the form 
$$
\vec{a}=n_{x} a_{x} \hat{x}+n_{y} a_{y} \hat{y} \tag{13.118} \label{eq-13-118}
$$

shown in [Figure 13.26](#fig-13-26) (for $a_{x}=2 a_{y}$).

:::{figure} ../images/lt-32799-clipboard_e3049fff1a0568cd7cd0dc3fccbeb7011.png
:label: fig-13-26
:enumerator: 13.26
:alt: A crystal lattice.

A crystal lattice.
:::
It is clear that vectors of the form 
$$
\vec{\ell}_{1}=\frac{1}{a_{x}} \hat{x}, \quad \ell_{2}=\frac{1}{a_{y}} \hat{y}, \tag{13.119} \label{eq-13-119}
$$

satisfy [13.108](#eq-13-108). Furthermore, a little thought will convince you that these are the shortest pair of linearly independent vectors with this property. Thus we can take [13.110](#eq-13-110) to be the basis vectors for the dual lattice, so that the dual lattice looks like

$$
\vec{d}_{m}=\left(\frac{m_{x}}{a_{x}} \hat{x}+\frac{m_{y}}{a_{y}} \hat{y}\right) \tag{13.120} \label{eq-13-120}
$$

as shown in [Figure 13.27](#fig-13-27).Note that the long and short axes are interchanged, as usual in a diffraction process.

:::{figure} ../images/lt-32800-clipboard_e40208aab267211222c2409823bd6ca2c.png
:label: fig-13-27
:enumerator: 13.27
:alt: The dual lattice.

The dual lattice.
:::
Now suppose that there is a plane wave passing through the infinite lattice, 
$$
e^{i \vec{k} \cdot \vec{r}-i \omega t} . \tag{13.121} \label{eq-13-121}
$$

The wave that results from the interaction of the plane wave with the lattice then has the form 
$$
e^{i \vec{k} \cdot \vec{r}-i \omega t} g(\vec{r}), \tag{13.122} \label{eq-13-122}
$$

where $g(\vec{r})$ is a periodic function, like $f(\vec{r})$ in [13.106](#eq-13-106). To find the possible refracted waves, we must write this in the form: 
$$
e^{i \vec{k} \cdot \vec{r}-i \omega t} g(\vec{r})=\sum_{\begin{array}{c}
\text { diffracted } \atop \text { waves }, \alpha
\end{array}} C_{\alpha} e^{i \vec{k}_{\alpha} \cdot \vec{r}-i \omega t} . \tag{13.123} \label{eq-13-123}
$$

But we also know from the discussion above that the Fourier transform of $g$ is nonzero only for values of $\vec{k}$ of the form [13.107](#eq-13-107). Thus [13.114](#eq-13-114) takes the form 
$$
e^{i \vec{k} \cdot \vec{r}-i \omega t} \int d^{3} k^{\prime} e^{i \vec{k}^{\prime} \cdot \vec{r}} C_{g}\left(\vec{k}^{\prime}\right)=e^{i \vec{k} \cdot \vec{r}-i \omega t} \sum_{n_{j}} C_{n_{j}} e^{2 \pi i \sum_{j} n_{j} \vec{\ell}_{j} \cdot \vec{r}} \tag{13.124} \label{eq-13-124}
$$

Therefore, the $\vec{k}_{\alpha}$ in [13.114](#eq-13-114) must have the form 
$$
\vec{k}_{\alpha}=\vec{k} \mid 2 \pi \sum_{j} n_{j} \vec{\ell}_{j} \tag{13.125} \label{eq-13-125}
$$

But this is only possible if $\vec{k}_{\alpha}$ satisfies the dispersion relation in the material, which means, if the material is rotation invariant so that $\omega^{2}$ depends only on $|\vec{k}|^{2}$, that 
$$
\left|\vec{k}_{\alpha}\right|^{2}=|\vec{k}|^{2}. \tag{13.126} \label{eq-13-126}
$$

Thus we get a diffracted wave only for $n_{j}$ such that [13.117](#eq-13-117) is satisfied. X-ray diffraction from a crystal, therefore, can provide direct information about the dual lattice and thus about the crystal lattice itself.

There is a more physical way of thinking about the dual lattice. Consider any vector in the **dual** lattice that is not a multiple of another, 
$$
\vec{d} \equiv \sum_{j} n_{j} \vec{\ell}_{j}. \tag{13.127} \label{eq-13-127}
$$

Now look at the subset of vectors on the **lattice** that satisfy 
$$
\vec{d} \cdot \vec{a}=0. \tag{13.128} \label{eq-13-128}
$$

This subset is the set of lattice points that lie in the plane, $\vec{d} \cdot \vec{r}=0$, that is the plane perpendicular to $\vec{d}$ passing through the origin. Now consider the subset 
$$
\vec{d} \cdot \vec{a}=1. \tag{13.129} \label{eq-13-129}
$$

This subset is the set of lattice points that lie in the plane, $\vec{d} \cdot \vec{r}=1$, that is parallel to the plane $\vec{d} \cdot \vec{r}=0$, in the lattice. This plane is also perpendicular to $\vec{d}$ and passes through the point (which may not be a lattice point) 
$$
r_{1}=\frac{\vec{d}}{|\vec{d}|^{2}}. \tag{13.130} \label{eq-13-130}
$$

Therefore, the perpendicular distance (that is in the $\vec{d}$ direction) between the two planes is 
$$
\hat{d} \cdot \vec{r}_{1}=\frac{1}{|\vec{d}|}. \tag{13.131} \label{eq-13-131}
$$

We can continue this discussion to conclude that the subset of lattice points satisfying 
$$
\vec{d} \cdot \vec{a}=m \text { for integer } m=-\infty \text { to } \infty \tag{13.132} \label{eq-13-132}
$$

is the set of lattice points lying on parallel planes perpendicular to $\vec{d}$, with adjacent planes separated by $1 /|\vec{d}|$. **But this set must be all the lattice points!** This is true because $\vec{d} \cdot \vec{a}$ is an integer for all lattice points by the definition of the dual lattice. Thus all lattice points lie in one of the planes in [13.123](#eq-13-123).

:::{figure} ../images/lt-32801-clipboard_e14016968d4fed57df414248a210c2a9b.png
:label: fig-13-28
:enumerator: 13.28
:alt: A vector in the dual lattice.

A vector in the dual lattice.
:::
These considerations are illustrated in the two-dimensional crystal in the pictures below. If the vector $\vec{d}$ in the dual lattice is as shown in [Figure 13.28](#fig-13-28), then the perpendicular planes in the lattice are shown in [Figure 13.29](#fig-13-29).

:::{figure} ../images/lt-32802-clipboard_ea913d5236de5afda80f8243c1d49d227.png
:label: fig-13-29
:enumerator: 13.29
:alt: The corresponding planes in the lattice.

The corresponding planes in the lattice.
:::
Now suppose that $\vec{d}$ is one of the special points in the dual lattice that gives rise to a refracted wave, so that 
$$
|\vec{k}+2 \pi \vec{d}|^{2}=|\vec{k}|^{2} \Rightarrow \vec{d} \cdot(\vec{k}+\pi \vec{d})=0. \tag{13.133} \label{eq-13-133}
$$

This relation is shown in [Figure 13.30](#fig-13-30). This shows that the $k$ vector of the refracted wave, $\vec{k}+2 \pi \vec{d}$, is just $\vec{k}$ reflected in a plane perpendicular to $\vec{d}$. We have seen that there are an

:::{figure} ../images/lt-32803-clipboard_e90a8eebd6431d8b0be900f9a779af889.png
:label: fig-13-30
:enumerator: 13.30
:alt: The Bragg scattering condition.

The Bragg scattering condition.
:::
infinite number of such planes in the lattice, separated by $1 /|\vec{d}|$. The contribution to the scattered wave from each of these planes adds **constructively** to the refracted wave. To see this, consider the phase difference between the incoming wave, $e^{i \vec{k} \cdot \vec{r}-i \omega t}$ and the diffracted wave $e^{i \vec{k}_{\alpha} \cdot \vec{r}-i \omega t}$ for $\vec{k}_{\alpha}=\vec{k}+2 \pi \vec{d}$. Evidently, the phase difference at any point $\vec{r}$ is 
$$
2 \pi \vec{d} \cdot \vec{r}. \tag{13.134} \label{eq-13-134}
$$

This phase difference is an integral multiple of $2\pi$ on all the planes 
$$
\vec{d} \cdot \vec{r}=m \text { for integer } m=-\infty \text { to } \infty. \tag{13.135} \label{eq-13-135}
$$

Thus the contribution to scattering from all of the planes of lattice points adds constructively, because the phase relation between the incoming and diffracted wave is the same on all of them. Conversely, if $\vec{k}_{\alpha} \neq \vec{k}+2 \pi \vec{d}$, then the contribution from different planes will interfere destructively, and no diffracted wave will result.

This physical interpretation goes with the name “Bragg scattering.” The planes, [13.123](#eq-13-123) (or [13.126](#eq-13-126)) are the Bragg planes of the crystal. Note that as the vector $\vec{d}$ in the dual lattice gets longer, the corresponding Bragg planes get closer together, but they are also less dense, containing fewer scattering centers per unit area. Generally the scattering is weaker for large $|\vec{d}|$.

::::{admonition} Chapter Checklist
:class: checklist

You should now be able to:

1. Set up a diffraction problem as a forced oscillation problem and write the diffracted wave as a Fourier integral;

2. Interpret the Fourier integral in the far-field region and find the diffraction pattern;

3. Analyze the diffraction patterns in beams made with one or more slits and rectangles;

4. Use the convolution theorem to simplify the calculation of Fourier transforms;

5. Analyze the scattering from a diffraction grating and x-ray diffraction from crystals;

6. Interpret a hologram as a diffraction pattern;

7. Understand how a zone plate can focus a plane wave.
::::

## Problems

::::{exercise}
:label: prb-13-1
:enumerator: 13.1

Consider the transverse oscillations of a semi-infinite, flexible membrane with surface tension $T_{S}$ and surface mass density $\rho_{S}$. The membrane is stretched in the $z$ = 0 plane from $y = −\infty$ to $\infty$ and from $x = 0$ to $\infty$. The membrane is held fixed along the half lines, $x=z=0$, $a \leq y \leq \infty$ and $x = z = 0$, $-\infty \leq y \leq-a$. For $y$ between $a$ and $-a$, the membrane is driven with frequency $\omega$ so that the end at $x = 0$ moves with transverse displacement

$$
\psi(0, y, t)=f(y) e^{-i \omega t}
$$

where 
$$
f(y)=\left\{\begin{array}{cl}
b\left(1-\frac{y}{a}\right) & \text { for } 0 \leq y \leq a \\
b\left(1+\frac{y}{a}\right) & \text { for }-a \leq y \leq 0 \\
0 \quad & \text { for }|y| \geq a.
\end{array}\right.
$$

The transverse displacement is given by 
$$
\psi(x, y, t)=\int_{-\infty}^{\infty} d k_{y} C\left(k_{y}\right) e^{i\left(y k_{y}+x k\left(k_{y}\right)-\omega t\right)}
$$

where $k(k_{y})$ is some function of $k_{y}$ and 
$$
C\left(k_{y}\right)=\frac{1}{2 \pi} \int_{-\infty}^{\infty} d y f(y) e^{-i k_{y} y}=\frac{b}{\pi k_{y}^{2} a}\left(1-\cos k_{y} a\right).
$$

Find the function $k(k_{y})$.

If the intensity of the wave at $x = L$, $y = 0$ for large $L$ is $I_{0}$, find the intensity for $x = L$ and any value of $y$. **Hint:** Assume that you are in the far field region, and account for all the relevant factors contributing to the ratio of the intensity to $I_{0}$.

::::

::::{exercise}
:label: prb-13-2
:enumerator: 13.2

Consider an opaque barrier in the $x$-$y$ plane at $z = 0$, with a single slit along the $x$ axis of width $2a$, but with regions on either side of the slit each with width $2a$ which are partially transparent, designed to reduce the intensity by a factor of 2. When this barrier is illuminated by a plane wave in the $z$ direction, the amplitude of the oscillating field at $z = 0$ is

$$
f(x, y) e^{-i \omega t}
$$

for 
$$
f(x, y)=\left\{\begin{array}{ccc}
1 & \text { for } & |y|<a \\
1 / \sqrt{2} & \text { for } & a<|y|<3 a \\
0 & \text { for } & 3 a<|y|.
\end{array}\right.
$$

Near the slit, this just produces a beam which is less intense by a factor of two on the edges. Far away, however, the diffraction pattern is quite different from that of the single slit. At a fixed large distance $R=\sqrt{y^{2}+z^{2}}$ away from the slit, the intensity as a function of 
$$
\xi=k_{y} a=\frac{\omega y a}{c R}
$$

is shown in the graph in [Figure 13.38](#fig-13-38) for positive $\xi$. The value of the peak at $\xi = 0$ is normalized to 1, but has been suppressed in the graph to show the details of the secondary maxima.

:::{figure} ../images/lt-32812-clipboard_e6d5f90a62d0d0ed5599761593b71e13f.png
:label: fig-13-38
:enumerator: 13.38
:alt: Problem **13.2.

Problem **13.2.
:::
Find the smallest positive value of $\xi$ for which the intensity vanishes.

Find the ratio of the intensity at $\xi=\pi / 2$ to that at $\xi = 0$.

So far we have not mentioned the polarization of the light, assuming that it is irrelevant. In fact, we get the pattern shown above for any polarization, so long as the shading doesn’t effect the polarization (and $\xi$ is small). However, if the light is initially polarized in the direction $45^{\circ}$ from the $x$ axis, we could reduce the intensity by two by passing it through a perfect polarizer aligned with the $y$ axis. Suppose that our slit between $-a$ and $a$ is completely empty, but between $-3a$ and $-a$ and between $a$ and $3a$, we put such a polarizer. Now, as before, the beam close to the slit just has the intensity on the edges reduced by a factor of 2. Now, however, the diffraction pattern is quite different. As a function of $\xi$, the intensity at large fixed $R$ is 
$$
\propto \frac{1}{10}\left[\left(\frac{\sin 3 \xi}{\xi}\right)^{2}+\left(\frac{\sin \xi}{\xi}\right)^{2}\right]
$$

which looks nothing like the pattern above. Explain the difference.

::::

::::{exercise}
:label: prb-13-3
:enumerator: 13.3

Consider an opaque barrier in the $x$-$y$ plane at $z = 0$, with identical holes centered at $(x, y)=\left(n_{x} a, n_{y} a\right)$ for all integers $n_{x}$ and $n_{y}$. Suppose that the barrier is illuminated from $z<0$ by a plane wave traveling in the z direction with wavelength $\lambda=a \sqrt{3} / 2 \text { . }$.

For $z > 0$, the wave has the form 
$$
\sum_{m_{x}, m_{y}} C_{m_{x}, m_{y}} e^{i\left(m_{x} \rho x+m_{y} \rho y+k_{z}\left(m_{x}, m_{y}\right) z-\omega t\right)}
$$

where $m_{x}$ and $m_{y}$ run over all integers.

Find $\rho$.

For large $z$, only a finite number of terms in the sum are important. How many and how do you know?

Now suppose that instead of coming in the $z$ direction, a plane wave with the same wavelength is moving for $z < 0$ at $45^{\circ}$ to the $z$ axis both in the $x$-$z$ plane, and in the $y$-$z$ plane. That is 
$$
\frac{k_{x}}{k_{z}}=\frac{k_{y}}{k_{z}}=\operatorname{lan} 45^{\circ}=1 .
$$

Now for $z > 0$, the wave has the form 
$$
\sum_{m_{x}, m_{y}} C_{m_{x}, m_{y}} e^{i\left[\left(m_{x} \rho+\xi_{x}\right) x+\left(m_{y} \rho+\xi_{y}\right) y+k_{z}\left(m_{x}, m_{y}\right) z-\omega t\right]}
$$

where $m_{x}$ and $m_{y}$ run over all integers.

Find $\xi_{x}$ and $\xi_{y}$.

Again for large $z$, only a finite number of terms in the sum are important. Which ones — that is, what values of $m_{x}$ and $m_{y}$?

::::

::::{exercise}
:label: prb-13-4
:enumerator: 13.4

Describe the diffraction pattern that results when a transmission diffraction grating with line separation distance $S$ is illuminated by a plane wave of monochromatic light with wavelength $L$ that is traveling in a direction perpendicular to the grating lines and at an angle $\theta$ to the perpendicular from the surface of the grating.

::::

::::{exercise}
:label: prb-13-5
:enumerator: 13.5

An opaque screen with four narrow slits at $x=\pm 0.6 \mathrm{~mm}$ and $x=\pm 0.4 \mathrm{~mm}$ is blocking a beam of coherent light with wavelength $4 \times 10^{-5} \mathrm{~cm}$. Describe the diffraction pattern that appears on a screen 5 meters away.

::::

::::{exercise}
:label: prb-13-6
:enumerator: 13.6

A semi-infinite flexible membrane is stretched in the $z = 0$ plane for $x \geq 0$ with surface tension $T_{s}$ and surface mass density $\rho_{s}$. The membrane is clamped down at $z = 0$ along the two semi-infinite lines, $z = 0$, $x = 0$, $y \geq a$ and $z = 0$, $x = 0$, $y \leq-a$. For $-a \leq y \leq a$ and $x = 0$, the membrane is forced to oscillate with an amplitude of the form

$$
z=B e^{i \omega t} \cos \frac{\pi y}{2 a}.
$$

Draw a diagram of the $z = 0$ half plane for $x \geq 0$ and indicate where the average of the absolute value square of the transverse displacement of the membrane is large (i.e. not much smaller than $B^{2} a / r$, where $r$ is the distance from the origin). For your diagram, assume that the distance $a$ is about 5 times the wavelength of the waves.

Find the intensity of the disturbance on the membrane produced by this forced oscillation as a function of $\theta=\tan ^{-1}(y / x)$ on a large semicircle, $x^{2}+y^{2}=R^{2}$, for $R^{2}>>a^{4} \omega^{2} \rho_{s} / T_{s}$.

**Hint:** This is similar to a single slit diffraction problem. Note that even though the disturbance is a cosine, you will have to do a Fourier integral (although not a difficult one) to do part b, because the disturbance is confined to $-a \leq y \leq a$ at $x = 0$.

::::

::::{exercise}
:label: prb-13-7
:enumerator: 13.7

Suppose that a diffraction grating with line separation $d$ is etched onto the top of a thick piece of glass with index of refraction $n$. If light of frequency $\omega$ is incident on the top, coming in at an angle $\theta$ from the perpendicular to the face and perpendicular to the grating lines, find the angles of the components of the wave in the glass.

::::

::::{exercise}
:label: prb-13-8
:enumerator: 13.8

Shown in [Figure 13.39](#fig-13-39) are 4 diffraction patterns such as might be produced by shining laser light (nearly a plane wave) through a slit or slits, and projecting the pattern onto a photographic plate far away. The patterns are each produced by about 500 individual photons striking the plate with a probability density proportional to the intensity of the diffracted wave.

:::{figure} ../images/lt-32813-clipboard_e6bf523ffc58b0de6d759c12ab7c322d9.png
:label: fig-13-39
:enumerator: 13.39
:alt: Four diffraction patterns.

Four diffraction patterns.
:::
The four objects that produced these patterns were, in a random order,

1. A single slit, 1 mm wide;

2. A single slit, 0.6 mm wide;

3. Two slits, each 0.6 mm wide, with centers 1.5 mm apart;

4. Six slits, each 0.6 mm wide, with adjacent centers 1.5 mm apart.

1. Which is which?

2. How do you know?

::::

## 13.9: Fringes and Zone Plates

### Holographic Image of a Point

One of the simplest of holographic images is the image of a single point. If a plane wave encounters a very small object in its path, the object will produce a spherical wave. If the plane wave and the spherical wave then are absorbed by a photographic plate, as shown in [Figure 13.34](#fig-13-34), an interference pattern is produced in the form of concentric circles, or fringes.

Specifically, suppose that the plane wave is propagating in the $z$ direction, the photographic plate is in the $x$-$y$ plane at $z = z_{0}$ and we put the origin of our coordinate system at the position of the source of the spherical wave, as shown in [Figure 13.34](#fig-13-34). Then the linear combination of plane wave plus spherical wave has the form (ignoring polarization) 
$$
A e^{i k z}+\frac{B}{r} e^{i k r},
$$

where $r=\sqrt{x^{2}+y^{2}+z^{2}}$. We will assume, for simplicity, that $A$ and $B$ are real which means that the two waves are in phase at the object. The intensity of the wave at $z = z_{0}$, on the photographic plate is therefore 
$$
A^{2}+\frac{B^{2}}{r_{0}^{2}}+\frac{2 A B}{r_{0}} \cos \left[k\left(r_{0}-z_{0}\right)\right]
$$

where $r_{0}$ is the distance from the object for a point in the $z = z_{0}$ plane, 
$$
r_{0}=\sqrt{z_{0}^{2}+R^{2}}
$$

:::{figure} ../images/lt-32807-clipboard_e44a7d42f0180695ead15535d96c7f348.png
:label: fig-13-34
:enumerator: 13.34
:alt: Fringes.

Fringes.
:::
and 
$$
R=\sqrt{x^{2}+y^{2}}
$$

is the distance from the $z$ axis in the $x$-$y$ plane. The intensity depends only on $R$, as it must because of the symmetry of the system under rotations around the $z$ axis.

Usually, we are interested in the region, $z_{0} \gg R$, because, as we will see, the intensity pattern is most interesting for small $R$. In this region, the distance, $r_{0}$ is very nearly equal to $z_{0}$. We can ignore the variation of $r_{0}$ in the amplitude, $B / r_{0}$. However, there is interesting dependence in the cosine term in [13.133](#eq-13-133). In this term, we can expand $r_{0}$ in a Taylor series around $R=z_{0}$, 
$$
r_{0}=z_{0} \sqrt{1+R^{2} / z_{0}^{2}}=z_{0}+\frac{1}{2} \frac{R^{2}}{z_{0}}+\cdots
$$

Putting all this together, the intensity is given approximately for $z_{0} \gg R$ by 
$$
A^{2}+\frac{B^{2}}{z_{0}^{2}}+\frac{2 A B}{z_{0}} \cos \frac{k R^{2}}{2 z_{0}}.
$$

The intensity pattern, (13.137), describes concentric circular “zones” of intensity variation. The zones can be labeled by the maxima and minima of the cosine, at 
$$
\frac{k R^{2}}{2 z_{0}}=n \pi
$$

or 
$$
R^{2}=n \lambda z_{0}
$$

where $\lambda$ is the wavelength of the wave. For $n$ even, the cosine has a maximum and for $n$ odd, a minimum. The intensity variation is greatest if the plane wave and the spherical wave have approximately the same amplitude at the plate, 
$$
\frac{B}{z_{0}}=A
$$

Then the amplitude actually goes to zero at the minima. The intensity distribution as a function of $R$ is shown in [Figure 13.35](#fig-13-35). The positions of the maxima and minima, or “zones,” are shown on the $R$ axis. On the photographic plate, this intensity distribution gives rise to circular fringes.

:::{figure} ../images/lt-32808-clipboard_e1c6b97cabff798e7dd5d95d85ef2d55a.png
:label: fig-13-35
:enumerator: 13.35
:alt: The intensity distribution.

The intensity distribution.
:::
If the plate is developed and illuminated by a plane wave, the original spherical wave is reproduced along with another spherical wave moving inward toward a point on the $z$ axis a distance $z_{0}$ beyond the plate, as shown in [Figure 13.36](#fig-13-36). This wave is the real image of [Figure 13.33](#fig-13-33). When a plane wave (dotted lines) illuminates the photographic plate produced in [Figure 13.34](#fig-13-34), diverging (dotted lines) and converging (solid lines) spherical waves are produced.

### Zone Plates

The hologram of [Figure 13.34](#fig-13-34) can be used to bring part of plane wave to a focus. The converging spherical wave shown in [Figure 13.36](#fig-13-36) is much stronger than the rest of the wave disturbance at the focus, $z=2 z_{0}$, $x=y=0$, because the amplitude of this part of the wave

:::{figure} ../images/lt-32809-clipboard_ece5518fdd156d190a1417c5ca5e5b0d9.png
:label: fig-13-36
:enumerator: 13.36
:alt: A plane wave illuminating the photographic plate.

A plane wave illuminating the photographic plate.
:::
increases as it approaches the focus. It has the form 
$$
\frac{1}{r^{\prime}} e^{i k r^{\prime}}
$$

where 
$$
r^{\prime}=\sqrt{\left(z-2 z_{0}\right)^{2}+x^{2}+y^{2}}.
$$

The same effect can be produced with a cartoon version of the photographic plate made by taking a transparent plate and blacking out the zones for negative $n$ in (13.138) where the intensity distribution is less than half the maximum. For example, the first negative zone is the region $\lambda z_{0} / 2<R^{2}<3 \lambda z_{0} / 2$. The second is the region $5 \lambda z_{0} / 2<R^{2}<7 \lambda z_{0} / 2$, etc. The result is a “zone plate.” An example, produced by blacking out the first 4 negative zones is shown in [Figure 13.37](#fig-13-37). These things are quite useful, because they can be easily produced and tailored to any wavelength.

:::{figure} ../images/lt-32810-clipboard_ede916e38a947cdbc056abeda55b7ce0d.png
:label: fig-13-37
:enumerator: 13.37
:alt: A zone plate.

A zone plate.
:::
## 13.10: 13-8- Holography

Nothing prevents us from doing the analysis of a diffraction pattern from a more complicated function, $f(x, y)$, than that discussed in [13.16](#eq-13-16). A hologram is just such a diffraction pattern. One of the simplest versions of a hologram is one in which an object is illuminated by a laser, that provides essentially a plane wave. The reflected light, and a part of the laser beam (extracted by some beam splitting technique) are incident on a photographic plate at slightly different angles, as shown schematically in [Figure 13.31](#fig-13-31). The wave incident on the photographic plate has the form 
$$
e^{-i \omega t}\left(e^{i k z}+\int d k_{x} d k_{y} C\left(k_{x}, k_{y}\right) e^{i \vec{k} \cdot \vec{r}}\right)
$$

where 
$$
k=|\vec{k}|=\omega / v.
$$

[13.127](#eq-13-127) describes the two coherent parts of the light wave incident on the photographic plate. For simplicity, we will assume that the signal in which we are actually interested, the reflected wave with Fourier transform $C(k_{x}, k_{y})$, is small compared to the reference wave $e^{i k z}$. This signal is what we would see if the photographic plate were removed and we placed

:::{figure} ../images/lt-32804-clipboard_e09e8ecb09982ab0e8f8eb4d65deb7d24.png
:label: fig-13-31
:enumerator: 13.31
:alt: Making a hologram.

Making a hologram.
:::
our eyes in the path of the reflected wave, but out of the path of the laser beam, as shown in [Figure 13.32](#fig-13-32).

:::{figure} ../images/lt-32805-clipboard_e80386216468e0e99b2cb25c6d0c08dff.png
:label: fig-13-32
:enumerator: 13.32
:alt: Viewing the object.

Viewing the object.
:::
The photographic plate (we’ll assume it’s at $z$ = 0) records only the intensity of the total wave, proportional to 
$$
1+2 \operatorname{Re} \int d k_{x} d k_{y} C\left(k_{x}, k_{y}\right) e^{i\left(k_{x} x+k_{y} y\right)}+\mathcal{O}\left(C^{2}\right)
$$

We will drop the terms of order $C^{2}$, assuming that $C$ is small, although we will be able to see later that they will not actually not make any difference even if $C$ is large. If we now make a positive slide from the plate and shine through it a laser beam with the same frequency, $\omega$, the wave “gets through” where the light intensity on the plate was large and is absorbed where the intensity was small. Thus we have a forced oscillation problem of exactly the sort that we discussed above, with [13.129](#eq-13-129) playing the role of $f(x, y)$. The solution for $z > 0$ (from [13.19](#eq-13-19)-[13.24](#eq-13-24)) is
$$
e^{-i \omega t}\left(e^{i k z}+\int d k_{x} d k_{y} C\left(k_{x}, k_{y}\right) e^{i \vec{k} \cdot \vec{r}}+\text{c.c.}\right)
$$

where c.c. is the complex conjugate wave obtained by taking the complex conjugate of the signal and changing the sign of the $z$ dependence to get a wave traveling in the $+z$ direction. The important thing to note about the complex conjugate wave is that it represents a beam traveling in a different direction from either the signal or the reference beam, because the complex conjugation has changed the sign of $k_{x}$ and $k_{y}$.

The resulting system is shown schematically in [Figure 13.33](#fig-13-33). Your eye sees a reconstructed version of the reflected wave that you would have seen without the photographic plate, as in [13.32](#eq-13-32). Note that neither the reference beam nor the complex conjugate beam get in the way of your viewing, because they go off at slightly different angles. This is a hologram. Because it is not a picture but a reconstruction of the actual wave that you would have seen in [13.32](#eq-13-32), it has the surprising property of three-dimensionality that makes a hologram striking.

:::{figure} ../images/lt-32806-clipboard_eb4cceb74b2173e5128e27fa481403cb9.png
:label: fig-13-33
:enumerator: 13.33
:alt: Viewing the holographic image.

Viewing the holographic image.
:::
One might wonder why we choose the angle between the reference beam and the signal to be small. A large angle would have the advantage of getting the reference beam farther out of the way, but it would have an important disadvantage. Consider the intensity pattern on the photographic plate that records the hologram. It is an oscillating pattern with a typical wave number given by the typical value of $k_{x}$ or $k_{y}$. These are of order $k \sin \theta$, where $\theta$ is the angle between the reference beam and the signal. But the distance between neighboring maxima on the photographic plate is therefore of order 
$$
\frac{2 \pi}{k \sin \theta}=\frac{\lambda}{\sin \theta}
$$

where $\lambda$ is the wavelength of the light. Since $\lambda$ is a very small distance, it pays to pick $\theta$ small to spread out the pattern on the photographic plate.

Note, also, that the order $C^{2}$ terms that we dropped really don’t do any harm even if $C$ is not small. Because their $x$ and $y$ dependence is proportional to that of the signal times its complex conjugate, the typical $k_{x}$ and $k_{y}$ for these terms is zero and they travel roughly in the direction of the reference beam. They don’t reach your eye in [13.33](#eq-13-33).
