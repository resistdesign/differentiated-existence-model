# DEM Toy Model 01 — Clock/Geometry Budget

**Status:** calculational toy model; exact recovery of selected special-relativistic kinematics under explicit assumptions  
**Purpose:** turn one DEM intuition into mathematics that can be checked, criticized, and rejected if necessary  
**Not claimed:** derivation of our universe, proof of DEM, new experimental physics, or a derivation of the numerical value of `c`

## 1. Target

DEM currently proposes that:

- time may be an operational serialization/comparison of physical change rather than an ontologically primitive axis;
- different resolved modes may carry different metric weights;
- observed motion, duration, momentum, and energy may be projections of deeper correlated change;
- the invariant speed `c` may be characteristic of an effective relativistic resolution rather than an unexplained primitive of all existence.

The first toy model should therefore do something narrow and unforgiving:

> Recover the special-relativistic proper-time relation from a model containing geometric change, clock-process change, and an arbitrary bookkeeping parameter, while making the effective invariant speed arise as a ratio of mode metrics.

This model does exactly that. It does **not** yet explain why nature chooses the model's core quadratic constraint.

---

## 2. Primitive mathematical ingredients

Consider one geometric mode `x` and one internal clock-process mode `κ`.

Let `q` be any monotonic parameter used only to order calculations. `q` is explicitly **not** interpreted as physical time.

For a curve through the resolved state space, write

\[
\dot x = \frac{dx}{dq}, \qquad
\dot\kappa = \frac{d\kappa}{dq}.
\]

Introduce two positive constant metric weights

\[
g_x > 0, \qquad g_\kappa > 0.
\]

They convert change in the two modes into a common quadratic norm. Their ratio will determine the effective causal speed.

A homogeneous inertial reference clock process has reading `T(q)`. `T` is also physical process change, not a fundamental external time variable.

### Core toy-model postulate

For a free stable structure, impose the local mode-norm constraint

\[
\boxed{
 g_\kappa\dot\kappa^2 + g_x\dot x^2
 = g_\kappa\dot T^2
}
\tag{1}
\]

Interpretation: relative to an inertial reference process, resolved change can appear in the internal clock mode, the geometric mode, or both, while the weighted quadratic magnitude is fixed.

This is the model's **major assumption**. It is chosen because it is minimal, reparameterization-compatible, and testable against the desired recovery target. A deeper DEM model would have to derive or replace it.

---

## 3. `q` is bookkeeping, not observable time

Under any monotonic reparameterization

\[
q \mapsto q' = f(q),
\]

all three derivatives in (1) acquire the same factor `dq/dq'`. Therefore the equation retains the same form.

The observables below depend on ratios of physical changes and not on the numerical value assigned to `q`.

This is important: the model can be calculated using an evolution parameter without promoting that parameter into ontology.

---

## 4. Operational definitions

Define the duration recorded by the moving structure's internal clock as

\[
d\tau \equiv d\kappa.
\]

Define the duration recorded by the inertial reference clock as

\[
dt \equiv dT.
\]

Define resolved geometric velocity relative to that reference clock by

\[
v \equiv \frac{dx}{dt}.
\]

Finally define

\[
\boxed{
c_*^2 \equiv \frac{g_\kappa}{g_x}}
\tag{2}
\]

so `c_*` has dimensions of speed when `κ`/`T` have dimensions of duration and `x` has dimensions of length.

The star is deliberate: this model does not assume in advance that `c_*` is numerically the measured vacuum speed of light. Matching the relativistic regime of our universe would require `c_* = c` experimentally.

---

## 5. Result 1 — exact time-dilation relation

Divide (1) by `g_κ \dot T²`:

\[
\left(\frac{d\tau}{dt}\right)^2
+
\frac{g_x}{g_\kappa}
\left(\frac{dx}{dt}\right)^2
=1.
\]

Using (2),

\[
\boxed{
\left(\frac{d\tau}{dt}\right)^2
+
\frac{v^2}{c_*^2}
=1
}
\tag{3}
\]

and therefore

\[
\boxed{
d\tau = dt\sqrt{1-\frac{v^2}{c_*^2}}.}
\tag{4}
\]

For constant `v`,

\[
\Delta\tau = \Delta t\sqrt{1-\frac{v^2}{c_*^2}}.
\]

This is exactly the special-relativistic time-dilation law after identifying `c_*` with `c`.

### DEM interpretation

The model does not say that a moving clock is mechanically slowed by motion through a medium. It says only that the resolved clock-process component and resolved geometric component satisfy one invariant quadratic relation.

In DEM language, the observable clock rate changes because the same resolved relation has different component expression across modes.

---

## 6. Result 2 — an effective Lorentzian interval

Rearrange (3):

\[
\boxed{
c_*^2 d\tau^2 = c_*^2 dt^2 - dx^2.}
\tag{5}
\]

The left side is measured by the physical clock process carried along the trajectory. The right side has Lorentzian signature even though the starting mode budget in (1) used positive weights.

Define

\[
ds^2 \equiv c_*^2dt^2-dx^2.
\]

Then

\[
ds^2 = c_*^2d\tau^2.
\]

So the model recovers the standard `1+1`-dimensional Minkowski proper-time interval as an **effective relation among resolved observables**.

This is the first concrete realization of the DEM idea that a familiar spacetime metric can be downstream of a deeper relation among differentiated modes.

---

## 7. Result 3 — an invariant speed bound

Because a real clock-process increment satisfies

\[
d\tau^2 \ge 0,
\]

(5) implies

\[
dx^2 \le c_*^2dt^2
\]

and therefore

\[
\boxed{|v|\le c_* .}
\tag{6}
\]

At the boundary,

\[
d\tau = 0 \quad \Longleftrightarrow \quad |v|=c_*.
\]

Thus the model's limiting speed is not inserted as a separate speed-limit rule. It follows from the positivity of the clock-mode contribution plus the metric ratio in (2).

What *is* still inserted is the quadratic mode-norm relation itself and its constant coefficients.

---

## 8. Result 4 — Lorentz transformations preserve the recovered interval

Once (5) has been obtained, consider linear inertial-coordinate transformations that preserve the interval, spatial orientation, and the origin.

For relative speed `u`, define

\[
\gamma_u = \frac{1}{\sqrt{1-u^2/c_*^2}}.
\]

Then

\[
\boxed{
 x' = \gamma_u(x-ut)
}
\tag{7}
\]

\[
\boxed{
 t' = \gamma_u\left(t-\frac{ux}{c_*^2}\right)
}
\tag{8}
\]

satisfy

\[
c_*^2dt'^2-dx'^2 = c_*^2dt^2-dx^2.
\]

So the standard Lorentz transformation is compatible with—and is the standard linear interval-preserving transformation of—the effective metric recovered by the model.

### Important limitation

Equations (7)–(8) are **not yet derived solely from DEM ontology**. To select the Lorentz group as the inertial chart-change group, this toy model additionally uses the usual effective assumptions of homogeneity/linearity and interval preservation.

The next model must explain why those conditions arise from deeper dynamics rather than simply adopting them after the interval appears.

---

## 9. Result 5 — free relativistic particle dynamics

A minimal free-particle action can be built from accumulated proper clock change:

\[
\boxed{
S = -mc_*^2\int d\tau.
}
\tag{9}
\]

Using (4) and parameterizing the calculation by the reference-clock reading `t`,

\[
S
= -mc_*^2\int dt\sqrt{1-\frac{v^2}{c_*^2}}.
\]

Hence

\[
L = -mc_*^2\sqrt{1-\frac{v^2}{c_*^2}}.
\tag{10}
\]

The conjugate momentum is

\[
\boxed{p = \frac{\partial L}{\partial v}=\gamma mv}
\tag{11}
\]

with

\[
\gamma = \frac{1}{\sqrt{1-v^2/c_*^2}}.
\]

The Hamiltonian is

\[
\boxed{E = pv-L=\gamma mc_*^2.}
\tag{12}
\]

Therefore

\[
\boxed{E^2-p^2c_*^2=m^2c_*^4.}
\tag{13}
\]

The low-speed expansion is

\[
L = -mc_*^2 + \frac12mv^2 + O(v^4/c_*^2),
\]

recovering Newtonian free-particle mechanics up to the usual constant rest-energy term.

This section adds one further postulate: that the free action is proportional to accumulated proper clock change. That is standard relativistic particle mechanics expressed in the language of this toy model; it is not yet a new DEM prediction.

---

## 10. What has actually been achieved

This model is deliberately small, but it moves DEM one step beyond metaphor.

From the explicit core constraint (1), it derives:

1. an operational proper-time relation;
2. the exact special-relativistic time-dilation factor;
3. a Lorentzian effective interval;
4. an effective limiting speed;
5. the interpretation
   \[
   c_*^2=g_\kappa/g_x
   \]
   as a ratio of metric weights between clock-process and geometric modes;
6. compatibility with Lorentz transformations;
7. with the standard free-action postulate, relativistic momentum, energy, dispersion, and the Newtonian limit.

The model also demonstrates that the arbitrary sequencing parameter `q` can disappear from all final observables.

That is useful evidence that DEM's statement “a computational ordering parameter need not be ontological time” can be made mathematically coherent in at least one toy construction.

---

## 11. What has *not* been achieved

The model does **not** yet:

- derive the quadratic constraint (1) from deeper DEM primitives;
- derive the values of `g_κ` or `g_x`;
- derive the measured numerical value of `c`;
- derive Lorentz symmetry uniquely without additional effective assumptions;
- derive relativity of simultaneity from a physical clock-network construction;
- explain interactions or forces;
- explain gravity;
- explain quantum behavior;
- explain why all particle species share one causal metric;
- derive mass, spin, charge, or Standard Model structure;
- establish that physical time is ontologically non-fundamental;
- distinguish DEM experimentally from ordinary special relativity.

At this stage it is an **exact reconstruction of a slice of known physics under a DEM-compatible ontology**, not new physics.

That is intentional. A first toy model should prove we can calculate before we try to predict.

---

## 12. Falsification / rejection conditions for this model

This construction should be discarded or revised if any of the following occurs:

1. the reparameterization claim fails under a consistent formal treatment;
2. the operational definitions require a hidden fundamental time variable after all;
3. the recovered interval cannot support a consistent inertial-frame construction;
4. extending the model to multiple spatial dimensions produces incompatible causal scales or preferred-direction effects without evidence;
5. no deeper dynamics can motivate the core quadratic constraint except by simply rewriting Minkowski spacetime in disguised notation;
6. the metric-ratio interpretation of `c_*` adds no leverage for any later derivation or discriminant.

Condition 5 is particularly important. If this remains only a relabeling of special relativity, it has served as a useful consistency exercise but not as a physical advance.

---

## 13. Immediate next mathematical questions

### A. Derive rather than postulate the mode norm

Find the smallest underlying action, symmetry, conservation law, or coherent-field dynamics for which

\[
g_\kappa\dot\kappa^2+g_x\dot x^2=g_\kappa\dot T^2
\]

is a first integral rather than an axiom.

### B. Replace one reference clock with a clock network

Construct operational inertial coordinates from many local physical clock processes and derive synchronization/relativity of simultaneity without quietly assuming a global time field.

### C. Generalize to `3+1`

Test

\[
d\tau^2=dt^2-\frac{d\mathbf{x}\cdot d\mathbf{x}}{c_*^2}
\]

while deriving spatial isotropy from the underlying metric rather than inserting it by hand.

### D. Allow metric participation to vary

Promote

\[
g_\kappa,\;g_x
\]

to state-dependent quantities and determine whether any variation is a real coordinate-invariant observable or merely a reparameterization artifact.

### E. Connect to stable objecthood

Replace the point-like free structure with an explicit stable extended configuration—potentially a coherent-field soliton or vortex—and test whether its collective coordinates obey this kinematic model.

This is the point where the fluid/vortex research track could become a concrete implementation rather than analogy.

---

## 14. Relationship to established mathematics

The recovered equations in Sections 5–9 are standard special-relativistic equations. The model makes no priority claim over those equations.

Relevant neighboring machinery includes:

- reparameterization-invariant relativistic point-particle actions;
- proper time as invariant worldline length;
- generalized coordinates and metric configuration spaces;
- analogue/emergent Lorentzian geometry, where effective relativistic metrics arise for excitations of deeper systems.

The DEM-specific research question is whether this toy reconstruction can be embedded in a deeper model where its assumptions are *derived* and where the metric ratio `g_κ/g_x` has independent calculational meaning.

Useful references:

- David Tong, *General Relativity*, section on relativistic particle actions and reparameterization invariance: https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S1.html
- C. Barceló, S. Liberati, M. Visser, “Analog gravity from field theory normal modes?”: https://arxiv.org/abs/gr-qc/0104001
- C. Barceló, S. Liberati, M. Visser, “Analogue Gravity”: https://arxiv.org/abs/gr-qc/0505065

---

## 15. Compact model summary

The entire kinematic core is:

\[
\boxed{
 g_\kappa\dot\kappa^2+g_x\dot x^2=g_\kappa\dot T^2
}
\]

with

\[
\boxed{
d\tau=d\kappa,\quad dt=dT,\quad c_*^2=g_\kappa/g_x.}
\]

Therefore

\[
\boxed{
d\tau^2=dt^2-dx^2/c_*^2.}
\]

Everything after that is a consequence of the recovered effective Lorentzian structure plus clearly stated additional assumptions.

That is the first mathematical foothold. The next job is to explain **why equation (1) should exist at all**.