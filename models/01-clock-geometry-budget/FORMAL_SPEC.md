# Formal Specification — DEM Toy Model 01

This document states the Clock/Geometry Budget model in a compact form suitable for mathematical review.

The explanatory derivation is in [`README.md`](README.md).

## 1. Model data

Work on an inertial segment represented by a smooth comparison curve

\[
z:q\mapsto (x(q),\kappa(q),T(q))\in\mathbb R^3,
\]

where:

- `q` is an arbitrary orientation-preserving curve parameter;
- `x` is one resolved geometric designation;
- `κ` is the carried structure's physical clock-process coordinate;
- `T` is the physical clock-process coordinate used as the inertial reference;
- `g_x>0` and `g_κ>0` are constant mode-metric coefficients.

Assume `dT/dq > 0` on the segment so `T` can be used as an operational comparison coordinate.

Define

\[
c_*^2\equiv\frac{g_\kappa}{g_x}.
\]

## 2. Constraint surface

Allowed tangent vectors satisfy

\[
F(z,\dot z)
=
 g_\kappa\dot\kappa^2
 +g_x\dot x^2
 -g_\kappa\dot T^2
=0.
\tag{C1}
\]

For the forward-clock branch choose

\[
\dot\kappa\ge0.
\]

Equivalently,

\[
\dot\kappa
=
\sqrt{\dot T^2-\frac{\dot x^2}{c_*^2}}.
\tag{C2}
\]

The radicand condition defines the admissible clock-bearing sector:

\[
\dot T^2-\frac{\dot x^2}{c_*^2}\ge0.
\tag{C3}
\]

## 3. Gauge freedom

The parameter `q` is gauge/bookkeeping.

Let

\[
q'=f(q),\qquad f'(q)>0.
\]

Then

\[
\frac{dz}{dq'}
=
\frac{dq}{dq'}\frac{dz}{dq}.
\]

Therefore

\[
F'=
\left(\frac{dq}{dq'}\right)^2F.
\]

Hence

\[
F=0\iff F'=0.
\]

The constraint surface is invariant under orientation-preserving reparameterization.

No observable duration is assigned to an interval `dq`.

## 4. Resolution into operational observables

On a segment with `Ṫ>0`, define the reference-clock resolution

\[
R_T[z]
=
\{x(T),\kappa(T)\}.
\]

Operational observables are

\[
t\equiv T,
\qquad
\tau\equiv\kappa,
\qquad
v\equiv\frac{dx}{dT},
\qquad
r\equiv\frac{d\kappa}{dT}.
\]

All are independent of the choice of `q`.

Dividing (C1) by `g_κ Ṫ²` gives

\[
r^2+\frac{v^2}{c_*^2}=1.
\tag{O1}
\]

Thus

\[
\boxed{
\frac{d\tau}{dt}
=
\sqrt{1-\frac{v^2}{c_*^2}}
}
\tag{O2}
\]

for the forward branch.

## 5. Effective interval theorem

From (O1),

\[
\boxed{
c_*^2d\tau^2=c_*^2dt^2-dx^2.}
\tag{I1}
\]

Define

\[
ds^2\equiv c_*^2dt^2-dx^2.
\]

Then

\[
ds^2=c_*^2d\tau^2.
\]

The operational resolution therefore carries a Lorentzian quadratic form

\[
\eta
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}
\]

on dimensionless coordinates

\[
y=
\begin{pmatrix}
c_*t\\x\end{pmatrix}.
\]

This theorem is conditional on (C1). It does not derive (C1).

## 6. Limiting-speed theorem

For real forward clock accumulation,

\[
d\tau^2\ge0.
\]

By (I1),

\[
\left|\frac{dx}{dt}\right|\le c_*.
\]

Therefore

\[
\boxed{|v|\le c_*}
\tag{V1}
\]

for structures represented by the clock-bearing sector of this model.

The null boundary is

\[
d\tau=0
\quad\Longleftrightarrow\quad
|v|=c_*.
\]

## 7. Linear interval-preserving frame maps

Let

\[
\beta=\frac{u}{c_*},
\qquad
\gamma_u=\frac1{\sqrt{1-\beta^2}}.
\]

Define

\[
\Lambda(u)
=
\begin{pmatrix}
\gamma_u&-\gamma_u\beta\\
-\gamma_u\beta&\gamma_u
\end{pmatrix}.
\]

Then

\[
\Lambda^T\eta\Lambda=\eta.
\]

Thus

\[
y'=\Lambda y
\]

preserves (I1), yielding

\[
x'=\gamma_u(x-ut),
\]

\[
t'=\gamma_u\left(t-\frac{ux}{c_*^2}\right).
\]

This establishes compatibility with the `1+1` Lorentz group.

It does **not** establish that DEM alone uniquely selects this group. Linearity, inertial homogeneity, and interval preservation are effective assumptions at this stage.

## 8. Free action after eliminating the constrained clock mode

Using (C2), accumulated carried-clock change is

\[
\int d\kappa
=
\int dq\sqrt{\dot T^2-\frac{\dot x^2}{c_*^2}}.
\]

Adopt the free action

\[
\boxed{
S[x,T]
=
-mc_*^2
\int dq
\sqrt{\dot T^2-\frac{\dot x^2}{c_*^2}}.
}
\tag{A1}
\]

This action is homogeneous of degree one in the curve velocities and is therefore invariant under orientation-preserving reparameterization.

In the gauge `q=T=t`,

\[
L(v)
=
-mc_*^2\sqrt{1-\frac{v^2}{c_*^2}}.
\tag{A2}
\]

The spatial canonical momentum is

\[
p
=
\frac{\partial L}{\partial v}
=
\gamma mv.
\tag{A3}
\]

The Hamiltonian is

\[
E
=pv-L
=
\gamma mc_*^2.
\tag{A4}
\]

Therefore

\[
\boxed{
E^2-p^2c_*^2=m^2c_*^4.
}
\tag{A5}
\]

For `|v| << c_*`,

\[
L
=
-mc_*^2
+\frac12mv^2
+O\left(\frac{v^4}{c_*^2}\right).
\tag{A6}
\]

The non-relativistic free-particle action is recovered up to an additive constant.

## 9. Degrees of freedom and what is redundant

The written curve uses three functions `x(q)`, `κ(q)`, and `T(q)`, but they are not three unconstrained physical coordinates:

1. `q` is gauge;
2. `κ` is constrained by (C1) once `x` and `T` are supplied on the chosen branch;
3. choosing `T` as the operational clock gives the usual single free spatial trajectory `x(t)` in `1+1` kinematics.

Thus the construction does not gain physical predictive freedom by hiding an extra observable time coordinate in `q`.

A deeper DEM model should ideally formulate the same content directly in terms of unparameterized relations so even the bookkeeping parameter becomes optional notation.

## 10. Equivalence statement

After imposing (C1), identifying

\[
c_*=c,
\]

and adopting (A1), the model is mathematically equivalent to the standard free relativistic point particle in `1+1` dimensions for the observables treated here.

That equivalence is a feature of Model 01, not something to conceal:

> Model 01 is a **recovery/consistency construction**, not yet a competing physical theory.

Its DEM content lies in the factorization

\[
c_*^2=\frac{g_\kappa}{g_x}
\]

and in treating `t` and `τ` as comparisons of physical process change while `q` remains non-observable gauge.

## 11. Exact next burden

The next formal model must make the constraint

\[
g_\kappa\dot\kappa^2+g_x\dot x^2=g_\kappa\dot T^2
\]

less arbitrary.

A meaningful advance would derive it as a first integral or symmetry consequence of a smaller structure, for example:

- a variational principle on differentiated modes;
- a conserved norm/current;
- a coherent-field or soliton collective-coordinate model;
- a symmetry of an underlying state space;
- another dynamics that does not begin by assuming a Lorentzian spacetime metric.

Until that occurs, Model 01 demonstrates **coherence and exact recovery**, not physical derivation of relativity.