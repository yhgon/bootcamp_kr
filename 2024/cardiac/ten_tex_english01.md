
**A Model for Human Ventricular Tissue**
**K. H. W. J. ten Tusscher,1 D. Noble,2 P. J. Noble,2 and A. V. Panfilov1,3**
 
1Department of Theoretical Biology, Utrecht University, 3584 CH Utrecht, The Netherlands;  
2University Laboratory of Physiology, University of Oxford, Oxford OX1 3PT;  
3Division of Mathematics, University of Dundee, Dundee DD1 4HN, United Kingdom  
 
**Submitted 9 August 2003; accepted in final form 2 December 2003**
 

**Abstract**  
The experimental and clinical possibilities for studying cardiac arrhythmias in human ventricular myocardium are very limited. Therefore, the use of alternative methods such as computer simulations is of great importance. In this article, we introduce a mathematical model of the action potential of human ventricular cells that, while including a high level of electrophysiological detail, is computationally cost-effective enough to be applied in large-scale spatial simulations for the study of reentrant arrhythmias. The model is based on recent experimental data on most of the major ionic currents: the fast sodium, L-type calcium, transient outward, rapid and slow delayed rectifier, and inward rectifier currents. The model includes a basic calcium dynamics, allowing for the realistic modeling of calcium transients, calcium current inactivation, and the contraction staircase. We are able to reproduce human epicardial, endocardial, and M cell action potentials and show that differences can be explained by differences in the transient outward and slow delayed rectifier currents. Our model reproduces the experimentally observed data on action potential duration restitution, which is an important characteristic for reentrant arrhythmias. The conduction velocity restitution of our model is broader than in other models and agrees better with available data. Finally, we model the dynamics of spiral wave rotation in a two-dimensional sheet of human ventricular tissue and show that the spiral wave follows a complex meandering pattern and has a period of 265 ms. We conclude that the proposed model reproduces a variety of electrophysiological behaviors and provides a basis for studies of reentrant arrhythmias in human ventricular tissue.
**Keywords:** reentrant arrhythmias; human ventricular myocytes; restitution properties; spiral waves; computer simulation

---

**Introduction**

Here is the complete text you provided, formatted as requested:

---

**CARDIAC ARRHYTHMIAS** and sudden cardiac death are among the most common causes of death in the industrialized world. Despite decades of research, their causes are still poorly understood. Theoretical studies into the mechanisms of cardiac arrhythmias form a well-established area of research. One of the most important applications of these theoretical studies is the simulation of the human heart, which is important for a number of reasons. First, the possibilities for doing experimental and clinical studies involving human hearts are very limited. Second, animal hearts used for experimental studies may differ significantly from human hearts (heart size, heart rate, action potential (AP) shape, duration, and restitution, vulnerability to arrhythmias, etc.). Finally, cardiac arrhythmias, especially those occurring in the ventricles, are three-dimensional phenomena, whereas experimental observations are still largely constrained to surface recordings. Computer simulations of arrhythmias in the human heart can overcome some of these problems.

To perform simulation studies of reentrant arrhythmias in human ventricles, we need a mathematical model that, on the one hand, reproduces detailed properties of single human ventricular cells, such as the major ionic currents, calcium transients, and AP duration (APD) restitution (APDR), and important properties of wave propagation in human ventricular tissue, such as conduction velocity (CV) restitution (CVR). On the other hand, it should be computationally efficient enough to be applied in the large-scale spatial simulations needed to study reentrant arrhythmias.

Currently, the only existing model for human ventricular cells is the Priebe-Beuckelman (PB) model and the reduced version of this model constructed by Bernus et al. (3, 51). The PB model is largely based on the phase 2 Luo-Rudy (LR) model for guinea pig ventricular cells (38). Although the model incorporates some data on human cardiac cells and successfully reproduces basic properties of APs of normal and failing human ventricular cells, it has several limitations. First, several major ionic currents are still largely based on animal data, and second, the APD is 360 ms, which is much longer than the values typically recorded in tissue experiments (~270 ms; Ref. 36). The aim of this work was to formulate a new model for human ventricular cells that is based on recent experimental data and that is efficient for large-scale spatial simulations of reentrant phenomena.

We formulated a model in which most major ionic currents [fast Na\(^+\) current (\(I_{Na}\)), L-type Ca\(^{2+}\) current (\(I_{CaL}\)), transient outward current (\(I_{to}\)), rapid delayed rectifier current (\(I_{Kr}\)), slow delayed rectifier current (\(I_{Ks}\)), and inward rectifier K\(^+\) current (\(I_{K1}\))] are based on recent experimental data. The model includes a simple calcium dynamics that reproduces realistic calcium transients and a positive human contraction staircase and allows us to realistically model calcium-dominated \(I_{CaL}\) inactivation, while at the same time maintaining a low computational load.

The model fits experimentally measured APDR properties of human myocardium (42). In addition, the CVR properties of our model agree better with experimental data—which are currently only available for dog and guinea pig (6, 19)—than those of existing ionic models. Both APD and CV restitution are very important properties for the occurrence and stability of reentrant arrhythmias (6, 17, 31, 52, 67). Our model is able to reproduce the different AP shapes corresponding to the endo-, epi-, and midmyocardial regions of the ventricles and their different rate dependencies (9, 10, 36). Finally, we model spiral wave dynamics in a two-dimensional (2D) sheet of human ventricular tissue and study the dynamics of its rotation, the ECG manifestation of the spiral wave, and membrane potential recordings during spiral wave rotation. In conclusion, we propose a new model for human ventricular tissue that is feasible for large-scale spatial computations of reentrant sources of cardiac arrhythmias.

Here is the full text in its original structure without any omissions:

---

**MATERIALS AND METHODS**

**General**

The cell membrane is modeled as a capacitor connected in parallel with variable resistances and batteries representing the different ionic currents and pumps. The electrophysiological behavior of a single cell can hence be described with the following differential equation:

\[
\frac{dV}{dt} = \frac{I_{\text{ion}} + I_{\text{stim}}}{C_m} \tag{1}
\]

where \( V \) is voltage, \( t \) is time, \( I_{\text{ion}} \) is the sum of all transmembrane ionic currents, \( I_{\text{stim}} \) is the externally applied stimulus current, and \( C_m \) is cell capacitance per unit surface area.

Similarly, ignoring the discrete character of microscopic cardiac cell structure, a 2D sheet of cardiac cells can be modeled as a continuous system with the following partial differential equation:

\[
\frac{\partial V}{\partial t} = \frac{I_{\text{ion}} + I_{\text{stim}}}{C_m} + \frac{1}{\rho_x S_x C_m} \frac{\partial^2 V}{\partial x^2} + \frac{1}{\rho_y S_y C_m} \frac{\partial^2 V}{\partial y^2} \tag{2}
\]

where \( \rho_x \) and \( \rho_y \) are the cellular resistivity in the \( x \) and \( y \) directions, \( S_x \) and \( S_y \) are the surface-to-volume ratio in the \( x \) and \( y \) directions, and \( I_{\text{ion}} \) is the sum of all transmembrane ionic currents given by the following equation:

\[
I_{\text{ion}} = I_{\text{Na}} + I_{\text{K1}} + I_{\text{to}} + I_{\text{Kr}} + I_{\text{Ks}} + I_{\text{CaL}} + I_{\text{NaCa}} + I_{\text{NaK}} + I_{\text{pCa}} + I_{\text{pK}} + I_{\text{bCa}} + I_{\text{bNa}} \tag{3}
\]

where \( I_{\text{NaCa}} \) is Na\(^+\)/Ca\(^{2+}\) exchanger current, \( I_{\text{NaK}} \) is Na\(^+\)/K\(^+\) pump current, \( I_{\text{pCa}} \) and \( I_{\text{pK}} \) are plateau Ca\(^{2+}\) and K\(^+\) currents, and \( I_{\text{bCa}} \) and \( I_{\text{bNa}} \) are background Ca\(^{2+}\) and Na\(^+\) currents.

Physical units used in our model are as follows: time (\( t \)) in milliseconds, voltage (\( V \)) in millivolts, current densities (\( I_X \)) in picoamperes per picofarad, conductances (\( G_X \)) in nanosiemens per picofarad, and intracellular and extracellular ionic concentrations (\( X_i \), \( X_o \)) in millimoles per liter. The equations for the ionic currents are specified in **Membrane Currents**.

For one-dimensional (1D) computations cell capacitance per unit surface area is taken as \( C_m = 2.0 \ \mu \text{F/cm}^2 \) and surface-to-volume ratio is set to \( S = 0.2 \ \mu \text{m}^{-1} \), following Bernus et al. (3). To obtain a maximum planar conduction velocity (CV) of 70 cm/s, the velocity found for conductance along the fiber direction in human myocardium by Taggart et al. (61), a cellular resistivity \( \rho = 162 \ \Omega \text{cm} \) was required. This is comparable to the \( \rho = 180 \ \Omega \text{cm} \) used by Bernus et al. (3) and the \( \rho = 181 \ \Omega \text{cm} \) used by Jongsma and Wilders (29), and it results in a "diffusion" coefficient \( D = 1/(\rho S C_m) \) of 0.00154 cm\(^2\)/ms. Because in 2D we did not intend to study the effects of anisotropy, we use the same values for \( \rho_x \) and \( \rho_y \) and for \( S_x \) and \( S_y \). Parameters of the model are given in Table 1.

For 1D and 2D computations, the forward Euler method was used to integrate Eq. 1. A space step of \( \Delta x = 0.1 \)–0.2 mm and a time step of \( \Delta t = 0.01 \)–0.02 ms were used. To integrate the Hodgkin-Huxley-type equations for the gating variables of the various time-dependent currents (\( m \), \( h \), and \( j \) for \( I_{\text{Na}} \), \( r \) and \( s \) for \( I_{\text{to}} \), \( x_{r1} \) and \( x_{r2} \) for \( I_{\text{Kr}} \), \( x_s \) for \( I_{\text{Ks}} \), \( d \), \( f \), and \( f_{\text{Ca}} \) for \( I_{\text{CaL}} \), and \( g \) for \( I_{\text{rel}} \)) the Rush and Larsen scheme (54) was used.

We test the accuracy of our numerical simulations in a cable of cells by varying both the time and space steps of integration. The results of these tests are shown in Table 2. From Table 2 it follows that, with a \( \Delta x = 0.2 \) mm, decreasing \( \Delta t \) from 0.02 to 0.0025 ms leads to a 3.7% increase in CV. Similarly, with \( \Delta t = 0.02 \) ms, decreasing \( \Delta x \) from 0.2 to 0.1 mm leads to an increase in CV of 4.6%. The changes in CV occurring for changes in space and time integration steps are similar to those occurring in other models (see, for example, Ref. 52). The time and space steps used in most computations are \( \Delta t = 0.02 \) ms and \( \Delta x = 0.2 \) mm, similar to values used in other studies (3, 6, 52, 69). Major conclusions of our model were tested for smaller space and time steps; the results were only slightly different.

Action potential duration (APD) is defined as action potential duration at 90% repolarization (APD90). Two different protocols were used to determine APD restitution (APDR). The S1-S2 restitution protocol, typically used in experiments, consists of 10 S1 stimuli applied at a frequency of 1 Hz and a strength of two times the threshold value, followed by an S2 extrastimulus delivered at some diastolic interval (DI) after the AP generated by the last S1 stimulus. The APDR curve is generated by decreasing DI and plotting APD generated by the S2 stimulus against DI. The second restitution protocol is called the dynamic restitution protocol. It was first proposed by Koller et al. (32) as being a more relevant determinant of spiral wave stability than S1-S2 restitution. The protocol consists of a series of stimuli at a certain cycle length until a steady-state APD is reached; after that, cycle length is decreased. The APDR curve is obtained by plotting steady-state APDs against steady-state DIs. CV restitution (CVR) was simulated in a linear strand of 400 cells by pacing it at one end at various frequencies and measuring CV in the middle of the cable.

Spiral waves were initiated in 2D sheets of ventricular tissue with the S1-S2 protocol. We first applied a single S1 stimulus along the entire length of one side of the tissue, producing a planar wave front propagating in one direction. When the refractory tail of this wave crossed the middle of the medium, a second S2 stimulus was applied in the middle of the medium, parallel to the S1 wave front but only over three-quarters of the length of the medium. This produces a second wave front with a free end around which it curls, thus producing a spiral wave. Stimulus currents lasted for 2 (S1) and 5 (S2) ms and were two times diastolic threshold. The trajectory of the spiral tip was traced with an algorithm suggested by Fenton and Karma (16). It is based on the idea that the spiral tip is defined as the point where excitation wave front and repolarization wave back meet. This point can be found as the intersection point of an isopotential line (in our case, −35 mV) and the \( dV/dt = 0 \) line.

Electrograms of spiral wave activity were simulated in 2D by calculating the dipole source density of the membrane potential \( V \) in each element, assuming an infinite volume conductor (50). The electrogram was recorded with a single electrode located 10 cm above the center of the sheet of tissue

.

All simulations were written in C++. Single-cell and cable simulations were run on a PC Intel Pentium III 800-MHz CPU; 2D simulations were run on 32 500-MHz processors of a SGI Origin 3800 shared-memory machine, using OpenMP for parallelization (Source code available at http://www-binf.bio.uu.nl/khwjtuss/HVM).

A description of the membrane currents of the model and the experimental data on which they are based is given in **Membrane Currents**. For most currents, a comparison is made with the formulations used in existing models for human ventricular myocytes by Priebe and Beuckelmann (51)—for the rest of the text referred to as the PB model—and for human atrial myocytes by Courtemanche and coworkers (8)—for the rest of the text referred to as the CRN model. For the fast Na\(^+\) current, a comparison is made to the widely used \( I_{\text{Na}} \) formulation first used in phase 1 of the Luo-Rudy (LR) model (37) that is used in both the PB and CRN models. The LR \( I_{\text{Na}} \) formulation is largely based on the \( I_{\text{Na}} \) formulation by Ebihara and Johnson (11), which is fitted to data from embryonic chicken heart cells to which a slow inactivation gate \( j \), as first proposed by Beeler and Reuter (1), was added. A detailed listing of all equations can be found in the APPENDIX. 
 
Here is the full text with corrected mathematical notation, formatted to match the original document as closely as possible:

---

**Membrane Currents**

**Fast Na\(^+\) current: \( I_{Na} \).** We use the three-gate formulation of \( I_{Na} \) first introduced by Beeler and Reuter (1):

\[
I_{Na} = G_{Na} m^3 h j (V - E_{Na})
\]

where \( m \) is an activation gate, \( h \) is a fast inactivation gate, and \( j \) is a slow inactivation gate. Each of these gates is governed by Hodgkin-Huxley-type equations for gating variables and characterized by a steady-state value and a time constant for reaching this steady-state value, both of which are functions of membrane potential (see Appendix).

The steady-state activation curve (\( m_{\infty}^3 \)) is fitted to data on steady-state activation of wild-type human Na\(^+\) channels expressed in HEK-293 cells from Nagatomo et al. (44). Experimental data were extrapolated to 37°C. Because there is no equivalent to the \( Q_{10} \) values used to extrapolate time constants to different temperatures, a linear extrapolation was used based on a comparison of values obtained at 23°C and 33°C. Note that similar Na\(^+\) channel activation data were obtained by others (64, 40, 55). Figure 1A shows the steady-state activation curve used in our model. For comparison, temperature-corrected experimental data are added.

The steady-state curve for inactivation (\( h_{\infty} j_{\infty} \)) is fitted to steady-state inactivation data from Nagatomo et al. (44). Again, data were extrapolated to 37°C. Similar inactivation data were obtained by others (55, 64). Figure 1B shows the steady-state inactivation curve used in our model together with temperature-corrected experimental data. Note that for resting membrane potentials the \( h \) and \( j \) gates are partially inactivated.

The time constants \( \tau_h \) and \( \tau_j \) are derived from current decay (typically \( V > -50 \, \text{mV} \)) and current recovery experiments (typically \( V < -80 \, \text{mV} \)) (40, 44, 55, 58, 63–65). In both types of experiments, a double-exponential fit is made to the data, allowing interpretation of the fast and slow inactivation time constants as \( \tau_h \) and \( \tau_j \), respectively. To convert all data to 37°C, a \( Q_{10} = 2.79 \) (derived from a comparison of fast inactivation time constants obtained at 23°C and 33°C by Nagatomo et al.) was used. Figure 1D shows our fit for the fast inactivation time constants, and Fig. 1E shows our fit for the slow inactivation time constants of the model. Temperature-adjusted experimental data points are added for comparison.

Activation time constants are derived from time-to-peak data from Nagatomo et al., converted as discussed above to 37°C. \( \tau_m \) can be calculated from the peak time (where \( dI_{Na}/dt = 0 \)), assuming that \( j \) is constant and knowing \( m_{\infty} \), \( h_{\infty} \), and \( \tau_h \). Figure 1C shows our fit of \( \tau_m \) together with experimentally derived, temperature-corrected time constants.

In Fig. 1F, the time course of recovery from inactivation for our \( I_{Na} \) is shown. Recovery from inactivation was established by applying a double-pulse protocol: from the holding potential, a 1-second duration pulse to -20 mV was applied to fully inactivate \( I_{Na} \); the voltage was then stepped back to the holding potential to allow \( I_{Na} \) to recover for variable durations, and finally, a second 30-ms pulse to -20 mV was applied. The \( I_{Na} \) elicited during the second pulse is normalized relative to the \( I_{Na} \) elicited during the first pulse to establish the amount of recovery. Figure 1F shows normalized \( I_{Na} \) as a function of the duration of the recovery interval between the two pulses for various values of the holding potential. Similar to experimental observations by Viswanathan et al. (63), Nagatomo et al. (44), Schneider et al. (58), and Makita et al. (40), recovery is slower for higher recovery potentials and has a sigmoid shape when plotted on a logarithmic scale. Note that in experiments, \( I_{Na} \) recovery is often slower than observed in our model, because our model is at physiological temperature whereas most experiments are performed at room temperature.

Figure 1G displays the rate dependence of the \( I_{Na} \) current. Rate dependence was tested by applying 500-ms pulses to -10 mV from a holding potential of -100 mV with different interpulse intervals. Steady-state current was normalized to the current elicited by the first pulse. The graph shows that for increasing frequency (decreasing interpulse interval) \( I_{Na} \) decreases and that this decrease is considerably faster for 21°C than for 37°C. Experiments performed by Wang et al. (65) at 32°C with an interpulse interval of 20 ms (1.92 Hz) show a reduction to 0.17 of the original current level, which lies between the reduction to 0.5 we measure at 37°C and the reduction to 0.13 we measure at 21°C.

For comparison purposes, we also added LR \( m_{\infty} \), \( h_{\infty} \), \( \tau_m \), \( \tau_h \), and \( \tau_j \) curves to Fig. 1A–E. The following observations can be made. Our steady-state activation curve lies 8 mV more negative (Fig. 1A). Our steady-state inactivation curve lies 12 mV more negative (Fig. 1B). Activation time constants are in the same range of values (Fig. 1C). Our \( \tau_h \) curve has a similar shape, but for voltages smaller than -40 mV, time constants are a factor of 1.6 larger, resulting in slower recovery dynamics (Fig. 1D). Similarly, our \( \tau_j \) is a factor of 3–5 larger for voltages smaller than -30 mV, leading to a considerably slower recovery from inactivation (Fig. 1E). \( G_{Na} \) was fitted to reproduce a \( \dot{V}_{\text{max}} = 260 \, \text{mV/ms} \), which is in the range of experimental data found by Drouin et al. (10).

**L-type Ca\(^2+\) current: \( I_{CaL} \).** The L-type calcium current is described by the following equation:

\[
I_{CaL} = G_{CaL} d f f_{Ca} 4 \frac{VF^2}{RT} \frac{Ca_i e^{2VF/RT} - 0.341 Ca_o}{e^{2VF/RT} - 1}
\]

where \( d \) is a voltage-dependent activation gate, \( f \) is a voltage-dependent inactivation gate, \( f_{Ca} \) is an intracellular calcium-dependent inactivation gate, and the driving force is modeled with a Goldman-Hodgkin-Katz equation.

The steady-state activation \( d_{\infty} \) and steady-state voltage inactivation curve \( f_{\infty} \) are fitted to \( I_{CaL} \) steady-state data from human ventricular myocytes reported by Benitah et al. (2), Mewes and Ravens (41), Pelzmann et al. (46), and Magyar et al. (39). Figure 2A shows the steady-state activation, and Fig. 2B shows the steady-state inactivation curve of our model together with experimental data from Pelzmann et al. (46).

Experimental data show that calcium-mediated inactivation is rapid, increases with calcium concentration, but is never complete (20, 60). More quantitative data about the precise dependence of amount and speed of inactivation on calcium concentration are unavailable and hard to obtain because intracellular calcium cannot be clamped to a constant value. As shown in Fig. 2C, our \( f_{Ca_{\infty}} \) curve has a switch-like shape, switching from no inactivation to considerable but incomplete inactivation if calcium concentration exceeds a certain threshold. For suprathreshold concentrations, the amount of inactivation depends mildly on calcium concentration.

Continuing from where it left off:

---

There are hardly any experimental data on activation times of \( I_{CaL} \) in human myocytes. Therefore, as was done in the CRN model, we used the curve from the phase-2 LR model. Limited data on \( I_{CaL} \) activation times from Pelzmann et al. (46) were used to adjust the shape of the \( \tau_d \) curve of the LR model. Figure 2D displays the voltage-dependent activation time constant of our model.

The time constant \( \tau_{fCa} \) is derived from experiments performed by Sun et al. (60). They show that during current decay experiments, a fast and a slow time constant can be distinguished, with the fast time constant being independent of voltage and depending only on calcium, allowing interpretation as \( \tau_{fCa} \). Sun et al. (60) find a time constant of ~12 ms at 23°C; no data on the concentration dependence of the time constant is available. We assumed a single time constant of 2 ms to be reasonable at 37°C, comparable to the immediate inactivation used in the PB model and the 2-ms time constant used in the CRN model.

The time constants \( \tau_f \) are derived from experiments on calcium current decay and recovery in human ventricular and atrial myocytes by Beuckelmann et al. (4), Benitah et al. (2), Mewes et al. (41), Sun et al. (60), Li and Nattel (35), Pelzmann et al. (46), and Magyar et al. (39). Sun et al. (60) show that during current decay experiments, the slow inactivation time constant depends on both voltage and extracellular calcium. After removal of extracellular calcium, an even slower, purely voltage-dependent inactivation time constant arises. This time constant should be interpreted as \( \tau_f \). Therefore, slow inactivation time constants found in current decay experiments were converted to 37°C with a \( Q_{10} = 2.1 \) (based on a comparison of time constants obtained by Li et al. and Pelzmann et al. at physiological temperatures and data obtained by Benitah et al. at 21°C) and were also corrected for the presence of extracellular \( Ca^{2+} \) with a slowing-down correction factor of 2.2 (based on a comparison of time constants obtained under normal conditions and under conditions in which extracellular \( Ca^{2+} \) was replaced by \( Sr^{2+} \), performed by Sun et al.).

In current recovery experiments, two time constants are derived. However, assuming that recovery from calcium inactivation is fast and given the clear voltage dependence of both fast and slow recovery time constants, both can be considered voltage-dependent time constants. Because our formulation of \( I_{CaL} \) incorporates only a single voltage-dependent inactivation gate, our \( \tau_f \) is constructed to form an intermediate between these fast and slow recovery time constants (\(-40 \le V \le -80 \, \text{mV}\)). Figure 2E displays the voltage-dependent inactivation time constant of our model. For comparison, experimentally found inactivation time constants are added.

For comparison purposes, we also added LR phase-2, PB, and CRN model curves for \( d_{\infty} \), \( f_{\infty} \), \( f_{Ca_{\infty}} \), \( \tau_d \), and \( \tau_f \) to Fig. 2A–E. The following observations can be made. Our steady-state activation curve is similar to the curves used in the LR and CRN models. The PB model has, for unknown reasons, a curve with a somewhat different shape (Fig. 2A). Our steady-state inactivation curve inactivates completely, similar to the curve used in the CRN model, whereas the LR and PB models use incompletely inactivating curves (Fig. 2B). In experiments, inactivation is more complete if prepulse duration is longer or temperature is higher (35, 60), implying that inactivation is slow rather than incomplete.

Our \( f_{Ca_{\infty}} \) curve has a switch shape, with a high level of inactivation beyond the threshold, whereas the LR, PB, and CRN curves are gradually declining functions of calcium (Fig. 2C). The high level of calcium inactivation, together with slow voltage inactivation, causes calcium to be the dominant mechanism of \( I_{CaL} \) inactivation in our model. This agrees well with experimental data. Incorporating calcium-dominated inactivation in models without local control may easily result in AP instability: in a local control model (21, 53)—in which individual \( I_{CaL} \) and calcium-induced calcium release (CICR) channels interact in subspaces—a smaller \( I_{CaL} \) current implies fewer open channels and hence fewer local calcium transients (sparks); the individual sparks still have the same effectiveness in closing nearby calcium channels. However, in a nonlocal control model, a smaller \( I_{CaL} \) generates a smaller global calcium transient that might be less effective in inactivating the \( I_{CaL} \) current. By using a switch shape for \( f_{Ca_{\infty}} \), we ensure effective calcium inactivation for a wide range of systolic calcium levels in our model.

The \( \tau_d \) curve of our model has a similar shape as that used in the PB model but with a factor of 2–3 shorter time constants and is a minor adaptation of the curves used in the LR and CRN models (Fig. 2D). Our \( \tau_f \) curve, which is fitted to the experimental data, has a maximum between -50 and 0 mV, whereas the curves used in the LR, PB, and CRN models have a minimum in this voltage region, in strong contrast with the experimental data (Fig. 2E). The \( f \) gate inactivation in our model is much slower than in the LR and PB models; \( f \) gate inactivation in the CRN model is even slower. The slow \( f \) gate inactivation in our model and the CRN model is important for making calcium the dominant mechanism of \( I_{CaL} \) inactivation. The \( f \) gate recovery in our model is similar to that in the LR and PB models and a factor of 4 faster than in the CRN model. It plays an important role in determining APD restitution (APDR), which in our model agrees well with experimental data (see Fig. 8). \( P_{CaL} \) is fitted to reproduce peak current values found by Li et al. (35) under physiological temperatures.

We modeled the driving force of the calcium current with the Goldman-Hodgkin-Katz equation. For simplicity, we ignored the small permeability the channel also has for sodium and potassium ions. In the Luo-Rudy phase-2 model, a Goldman-Hodgkin-Katz-like equation for calcium, sodium, and potassium is used. In the PB and CRN models, a constant-valued reversal potential is used.

**Transient outward current: \( I_{to} \).** For \( I_{to} \) the following formulation is used:

\[
I_{to} = G_{to} r s (V - E_K)
\]

where \( r \) is a voltage-dependent activation gate and \( s \) is a voltage-dependent inactivation gate.

The steady-state activation curve (\( r_{\infty} \)) is fitted to data on steady-state activation of \( I_{to} \) current in human ventricular myocytes of epicardial and endocardial origin at 35°C from Nabauer et al. (43). Because no significant difference between activation in epicardial and endocardial cells was found, a single formulation was used. Figure 3A shows the steady-state activation curve used in the model together with experimental data. A 10-mV positive shift was performed on the experimental data to account for the use of \( \text{Cd}^{2+} \) to block \( I_{CaL} \) current, similar to the approach taken by Courtemanche et al. (8). The greater steepness of the model curve relative to the experimental curve was necessary to make sure that no significant reactivation of \( I_{to} \) occurs on repolarization.

The steady-state inactivation curve (\( s_{\infty} \)) is fitted to data on steady-state inactivation from Nabauer et al. Because of significant differences between curves obtained for epicardial and endocardial cells, two separate model formulations were used. Figure 3B shows the steady-state inactivation curves used in the model together with \( \text{Cd}^{2+} \)-corrected experimental data.

Inactivation time constants are fitted to data from Nabauer et al. (43) and Wettwer et al. (68). Current decay experiments show similar time constants for epicardial and endocardial \( I_{to} \), whereas current recovery experiments show much slower recovery from inactivation for endocardial than epicardial \( I_{to} \), thus making two separate formulations for \( \tau_s \) necessary. Figure 3D shows our fits for epicardial \( \tau_s \), and Fig. 3E shows our fit for endocardial \( \tau_s \). For comparison, experimental inactivation time constants are added.
 
Continuing from where it left off:

---

Activation time constants are derived from time-to-peak data from the expression of hKv4.3-2—encoding an epicardial type transient outward channel—in mouse fibroblast cells by Greenstein et al. (22) in a manner similar to the derivation of \( \tau_m \). Figure 3C shows our \( \tau_r \) curve together with experimentally derived time constants.

For comparison purposes, we also added PB and CRN model curves for \( r_{\infty} \), \( s_{\infty} \), \( \tau_r \), and \( \tau_s \) to Fig. 3A–D. From this, the following observations can be made. The steady-state activation of our model almost coincides with that of the PB model and has a steeper slope and more positive half-activation point than that of the CRN model (Fig. 3A). In our model, we distinguish epicardial and endocardial steady-state inactivation, whereas the PB and CRN models only have a single steady-state inactivation curve. The epicardial steady-state inactivation of our model lies 15 and 25 mV to more positive potentials than the curves used in the PB and CRN models, respectively. For the endocardial steady-state inactivation of our model, these numbers are 8 and 18 mV, respectively (Fig. 3B).

The activation time constant of our model results in faster inactivation and slower recovery than that of the PB model, whereas it is a factor of 2 slower than the CRN model time constant (Fig. 3C). However, in the CRN model, three activation gates are used (\( r^3 \)), causing net activation to be slower and net deactivation to be faster than that of a single gate and thus complicating the comparison. In our model, we distinguish epicardial and endocardial inactivation time constants, whereas the PB and CRN models only have a single inactivation time constant. The inactivation time constant of the PB model resembles our epicardial inactivation time constant in magnitude but has hardly any voltage dependence. The inactivation time constant of the CRN model is similar to our epicardial inactivation time constant (Fig. 3D).

\( G_{to} \) is fitted to experimental data on current density from Wettwer et al. (68) and Nabauer et al. (43). Both show large differences in \( I_{to} \) size between epicardial and endocardial cells. We use \( G_{to} = 0.294 \, \text{nS/pF} \) for epicardial and \( G_{to} = 0.073 \, \text{nS/pF} \) for endocardial cells (25% of the value for epicardial cells). Figure 4 shows the current voltage (I-V) relationships for epicardial (Fig. 4A) and endocardial (Fig. 4B) \( I_{to} \) together with experimental data from Nabauer et al. (43).

We assume that \( I_{to} \) is specific for potassium ions and used the reversal potential \( E_K \). A similar approach is taken in the CRN model, whereas in the PB model, it is assumed that the channel is also permeable to sodium ions.

**Slow delayed rectifier current: \( I_{Ks} \).** For the slow delayed rectifier current, the following formulation is used:

\[
I_{Ks} = G_{Ks} x_s^2 (V - E_{Ks})
\]

where \( x_s \) is an activation gate and \( E_{Ks} \) is a reversal potential determined by a large permeability to potassium and a small permeability to sodium ions (see APPENDIX).

The steady-state activation curve (\( x_{s_{\infty}}^2 \)) is fitted to \( I_{Ks} \) activation data obtained for human ventricular myocytes at 36°C from Li et al. (34). In Fig. 5A, the steady-state activation curve used in the model is shown together with the experimental data.

Activation time constants are based on data from Virag et al. (62) and Wang et al. (66). Both sets of data were obtained in human ventricular myocytes at physiological temperatures. Figure 5B shows our fit of \( \tau_{x_s} \). Experimentally obtained activation time constants are added for comparison.

Fitting \( G_{Ks} \) to experimentally obtained current densities would result in a small \( I_{Ks} \) that has little effect on APD: simulating M cells by a 75% reduction in \( I_{Ks} \) density (the principal difference with epicardial cells) would result in M cell APD being only 10 ms longer than epicardial APD, in strong contrast with the 100-ms difference in APD found experimentally (9, 36). Thus, there is a discrepancy between current density measured in voltage-clamp experiments and the apparent contribution of the current to APD. This discrepancy is probably due to the sensitivity of \( I_{Ks} \) channels to the cell isolation procedures used for voltage-clamp experiments (70), resulting in considerable degradation of \( I_{Ks} \) channels before current density measurements. Therefore, instead of fitting \( G_{Ks} \) to voltage-clamp data, we based it on APD measurements: by using \( G_{Ks} = 0.327 \, \text{nS/pF} \) for epicardial cells and \( G_{Ks} = 0.082 \, \text{nS/pF} \) in M cells, we get an epicardial APD at 1 Hz of 276 ms and an M cell APD of 336 ms, resulting in an APD difference of 60 ms, which is in the range of experimental values (9, 36). This approach of basing a conductance value on electrophysiological properties rather than measured current density is also used in the development of other models; e.g., in the CRN model, \( G_{Na} \) is fitted to get the right \( \dot{V}_{\max} \), \( G_{to} \) to get the right AP morphology, and \( G_{Kr} \) and \( G_{Ks} \) to get the right APD (8) and in a later version of the LR model in which \( I_{K} \) was replaced by \( I_{Kr} \) and \( I_{Ks} \), \( G_{Ks} \) was fitted to get the right APD prolongation if \( I_{Ks} \) current is blocked (71). In addition, the values used for \( G_{Ks} \) and \( G_{Kr} \) in the CRN model and the LR model are similar to the values we use in our model. In Fig. 5C, the I-V relationship of \( I_{Ks} \) is shown together with rescaled experimental data from Li et al.

We use a sodium-to-potassium permeability ratio of \( p_{KNa} = 0.03 \), resulting in a reversal potential \( E_{Ks} \) that forms a compromise between reversal potentials found experimentally (34, 62). In the PB model, a permeability ratio of 0.018 is used, whereas in the CRN model, it is assumed that \( I_{Ks} \) is permeable to potassium ions only. Our steady-state activation curve lies 5 and 15 mV to more positive potentials than the curves used in the CRN and PB models, respectively. Compared with the \( \tau_{x_s} \) formulations used by both of these models, our \( I_{Ks} \) displays slower activation and more rapid deactivation.

**Rapid delayed rectifier current: \( I_{Kr} \).** The rapid delayed rectifier current is described by the following equation:

\[
I_{Kr} = G_{Kr} \sqrt{\frac{[K_o]}{5.4}} x_{r1} x_{r2} (V - E_K)
\]

where \( x_{r1} \) is an activation gate and \( x_{r2} \) is an inactivation gate. \( \sqrt{\frac{[K_o]}{5.4}} \) represents the \( K_o \) dependence of the current. Note that because no data are available on the \( K_o \) dependence of human ventricular \( I_{Kr} \), a similar dependence as measured in and implemented for animal myocytes is assumed (38).

The steady-state activation curve (\( x_{r1_{\infty}} \)) is fitted to activation data on the expression of HERG channels in HEK 293 cells by Zhou et al. (72), in Chinese hamster ovary cells by Johnson et al. (28), and in Xenopus oocytes by Smith and Yellen (59). Steady-state inactivation (\( x_{r2_{\infty}} \)) is fitted to data from Johnson et al. (28) and Smith and Yellen (59). Figure 6A shows steady-state curves of the model together with experimental data.

Activation time constants (\( \tau_{x_{r1}} \)) are fitted to data from Zhou et al. (72) obtained at physiological temperatures. \( \tau_{x_{r2}} \) is fitted to inactivation time constants obtained at physiological temperatures by Johnson et al. (28). Figure 6B shows our fit of \( \tau_{x_{r1}} \), and Fig. 6C shows our fit of \(

 \tau_{x_{r2}} \). Experimentally obtained time constants are added for comparison.

Fitting \( G_{Kr} \) to experimentally obtained current densities would result in an \( I_{Kr} \) that has a lower contribution to APD than suggested by experiments in which \( I_{Kr} \) is blocked (34). Therefore, similar to our approach for \( G_{Ks} \), we used such a value for \( G_{Kr} \) (0.128 nS/pF) that a complete blocking of \( I_{Kr} \) leads to 44 ms of APD prolongation, which is in the range of values found experimentally by Li et al. (34). The I-V relationship of \( I_{Kr} \) is shown in Fig. 6D. For comparison, rescaled experimental data from Iost et al. (25) and Li et al. (34) are added.

Note that our model curve is shifted toward more negative potentials relative to the experimental curves. This difference may be due to the fact that we fitted \( I_{Kr} \) to data from expression experiments in hamster and Xenopus cells, whereas the experimental I-V curves are from experiments on human cardiac cells.
 
Continuing from where it left off:

---

The steady-state activation curve of our \( I_{Kr} \) lies 10 and 20 mV to more negative potentials than the curves used in the PB and CRN models, respectively. \( \tau_{x_{r1}} \) has a size and a shape similar to those used in these two models. We modeled inward rectification as a time-dependent inactivation gate, whereas the PB and the CRN model implemented this inactivation as being instantaneous. Our steady-state inactivation curve lies 50 and 60 mV to more negative potentials than the inward rectification curves used in the PB and CRN models, which seem to have no clear experimental basis.

**Inward rectifier K\(^+\) current: \( I_{K1} \).** For \( I_{K1} \), the following formulation is used:

\[
I_{K1} = G_{K1} \sqrt{\frac{[K_o]}{5.4}} x_{K1_{\infty}} (V - E_K)
\]

where \( x_{K1_{\infty}} \) is a time-independent inward rectification factor that is a function of voltage. \( \sqrt{\frac{[K_o]}{5.4}} \) represents the \( K_o \) dependence of the current. As for \( I_{Kr} \), because of a lack of data on \( K_o \) dependence of human \( I_{K1} \), we assumed a dependence similar to that in animal myocytes.

Experimental data on \( I_{K1} \) current size are highly variable, as previously discussed by Courtemanche et al. (8). We used the formulation for \( I_{K1} \) used in the PB model but increased \( G_{K1} \) by a factor of 2 to account for the larger current densities found by Koumi et al. (33) in the \( I_{K1} \)-relevant voltage range (\(-90\) mV to \(-40\) mV). This results in a value for \( G_{K1} \) that is approximately five times larger than in the CRN model, which agrees with data from Koumi et al. (33) showing that \( I_{K1} \) is a factor of 5.6 higher in human ventricular than in atrial myocytes.

**Na\(^+\)/Ca\(^{2+}\) exchanger current, Na\(^+\)/K\(^+\) pump current, and plateau and background currents.** For \( I_{NaCa} \), the following equation is used:

\[
I_{NaCa} = k_{NaCa} \frac{e^{\frac{VF}{RT}} [Na_i]^3 [Ca_o] - e^{\left(\frac{1}{\beta} - 1\right) \frac{VF}{RT}} [Na_o]^3 [Ca_i]}{\left( K_{mNa_i}^3 + [Na_i]^3 \right) \left( K_{mCa} + [Ca_o] \right) \left( 1 + k_{sat} e^{\left(\frac{1}{\beta} - 1\right) \frac{VF}{RT}} \right)}
\]

This formulation is similar to the equation used in the LR model, except for the extra factor \( \beta \) (≈ 2.5) that accounts for the higher concentration of calcium in the subspace close to the sarcolemmal membrane where the Na\(^+\)/Ca\(^{2+}\) exchanger is actually operating. Our approach is similar to that used in the Noble et al. model with diadic subspace (45), where \( I_{NaCa} \) was made dependent on diadic calcium rather than bulk cytoplasmic calcium. Otherwise, during the AP plateau phase, the increase in bulk cytoplasmic calcium is not enough to counteract the increase in voltage, and \( I_{NaCa} \) current becomes outward oriented during a long period of the plateau phase, which is unrealistic (27).

For \( I_{NaK} \), we use the following formulation:

\[
I_{NaK} = R_{NaK} \frac{[K_o] [Na_i]}{\left( K_{mK} + [K_o] \right) \left( K_{mNa} + [Na_i] \right) \left( 1 + 0.1245 e^{-0.1VF/RT} + 0.0353 e^{-VF/RT} \right)}
\]

This formulation is similar to the formulations used in the LR, PB, and CRN models.

For \( I_{pCa} \), the following commonly applied equation is used:

\[
I_{pCa} = G_{pCa} \frac{[Ca_i]}{K_{pCa} + [Ca_i]}
\]

For \( I_{pK} \), the following equation is used:

\[
I_{pK} = G_{pK} \frac{V - E_K}{1 + e^{(25 - V)/5.98}}
\]

This is similar to the equation used by Luo and Rudy. The background sodium and calcium leakage currents are given by the following equations:

\[
I_{bNa} = G_{bNa} (V - E_{Na})
\]

\[
I_{bCa} = G_{bCa} (V - E_{Ca})
\]

For \( P_{NaCa} \), \( P_{NaK} \), \( G_{pCa} \), \( G_{pK} \), \( G_{bNa} \), and \( G_{bCa} \), values were chosen such that a frequency change results in \( Na_i \), \( K_i \), and \( Ca_i \) transients with a time scale of approximately 10 minutes, similar to experimental recordings (5) and which result in equilibrium concentrations for different frequencies that lie in the range of experimental observations (49). The values used lie in the range of values used in the PB and CRN models (for parameter values, see Table 1).

**Intracellular ion dynamics.** The calcium dynamics of our model are described using the following set of equations:

\[
I_{leak} = V_{leak} (Ca_{sr} - Ca_i)
\]

\[
I_{up} = \frac{V_{maxup}}{1 + \left( \frac{K_{up}}{Ca_i} \right)^2}
\]

\[
I_{rel} = a_{rel} \frac{Ca_{sr}^2}{b_{rel}^2 + Ca_{sr}^2} c_{rel} d g
\]

\[
Ca_{i,bufc} = Ca_i + Buf_c \frac{Ca_i}{K_{bufc} + Ca_i}
\]

\[
\frac{dCa_{i,total}}{dt} = \frac{I_{CaL} + I_{bCa} + I_{pCa} - 2 I_{NaCa}}{2 V_c F} - I_{leak} + I_{up} - I_{rel}
\]

\[
Ca_{sr,bufsr} = Ca_{sr} + Buf_{sr} \frac{Ca_{sr}}{K_{bufsr} + Ca_{sr}}
\]

\[
\frac{dCa_{sr,total}}{dt} = \frac{V_c}{V_{SR}} \left( I_{leak} - I_{up} + I_{rel} \right)
\]

where \( I_{leak} \) is a leakage current from the sarcoplasmic reticulum to the cytoplasm, \( I_{up} \) is a pump current taking up calcium in the SR, and \( I_{rel} \) is the calcium-induced calcium release (CICR) current. \( d \) is the activation gate of \( I_{CaL} \), reused as the activation gate of \( I_{rel} \), following a similar approach as in Chudin et al. (7), and \( g \) is the calcium-dependent inactivation gate of \( I_{rel} \). \( Ca_{i,total} \) is the total calcium in the cytoplasm, consisting of \( Ca_{i,bufc} \), the buffered calcium in the cytoplasm, and \( Ca_i \), the free calcium in the cytoplasm. Similarly, \( Ca_{sr,total} \) is the total calcium in the SR, consisting of \( Ca_{sr,bufsr} \), the buffered calcium in the SR, and \( Ca_{sr} \), the free calcium in the SR. Ratios between free and buffered calcium are analytically computed assuming a steady-state for the buffering reaction (Eqs. 19 and 21), following the same approach as first used by Zeng et al. (71) (for a description and values of the parameters, see Table 1). Our model for calcium dynamics has a complexity similar to that of most of the current models used to study the dynamics of wave propagation in cardiac tissue (LR, CRN, and PB models). Recently, complex models for intracellular calcium handling have been developed that model individual L-type calcium and ryanodine channels, discrete calcium release subunits, and sparks (53, 21). Due to their high computational demands, these models for calcium dynamics have not yet been incorporated into models for cardiac wave propagation.

The changes in the intracellular sodium (\( Na_i \)) and potassium (\( K_i \)) concentrations are governed by the following equations:



\[
\frac{dNa_i}{dt} = \frac{I_{Na} + I_{bNa} - 3 I_{NaK} - 3 I_{NaCa}}{V_c F}
\]

\[
\frac{dK_i}{dt} = \frac{I_{K1} + I_{to} + I_{Kr} + I_{Ks} - 2 I_{NaK} - I_{pK} + I_{stim} + I_{ax}}{V_c F}
\]

To avoid the model being overdetermined, as is the case for many second-generation electrophysiological models (13, 14, 24), we followed the approach suggested by Hund et al. (24) and accounted for the external stimulus current (\( I_{stim} \)) and the axial current flow (\( I_{ax} \)) in the equation for \( K_i \) dynamics. As mentioned above, conductances of background leakage, plateau, and pump currents were chosen such that transient time scales and equilibrium concentrations lie within the range of experimental observations.
 
Thank you for providing the images and text. I will generate the text with the corrected math formulas based on the content you’ve provided in this section. Here is the full, corrected text for the "RESULTS" section:

---

**RESULTS**  
**Single Cell**  
Figure 7 shows an AP, a calcium transient, and the major ionic currents generated by the model under 1-Hz pacing for a parameter setting corresponding to a human epicardial ventricular cell. The AP shows the characteristic spike-notch-dome architecture found for epicardial cells. Resting potential is \(-87.3\) mV, maximum plateau potential is \(21.7\) mV, and \(\dot{V}_{\text{max}} = 288\) mV/ms, all in agreement with experimental data \([10, 36]\). The calcium transient shows the characteristic rounded-off triangular shape found in experiments. Diastolic calcium level is \(0.07\ \mu M\) and maximum systolic calcium level under 1-Hz pacing is \(1.0\ \mu M\), comparable to values in the PB model and experimentally obtained values by Beuckelmann et al. \([26]\). The ionic currents presented in Fig. 7 have shapes and values similar to those recorded experimentally. Note that the initial spikelike increase of \(I_{\text{Kr}}\) in our model is absent in the PB and CRN models. This initial increase is also observed in experiments \([18, 72]\) and is achieved by modeling the inward rectification as a time-dependent process.

Figure 8 shows the APDR curve for a single epicardial cell obtained with the S1-S2 restitution protocol (see **MATERIALS AND METHODS**) with a basic cycle length (BCL) of 1000 ms. For comparison, experimental data found by Morgan and coworkers \([42]\) are added. It can be seen that the APDR curve of our model in a wide range closely matches the experimentally measured curve.

Figure 9A shows the change in diastolic and systolic calcium levels when pacing frequency is increased in a stepwise fashion from \(0.25\) to \(0.5\) to \(1\) to \(1.5\) to \(2\) to \(2.5\) to \(3\) Hz. From the figure, it can be seen that systolic calcium level first increases substantially up to a frequency of \(2\) Hz, saturates, and then starts to decrease. In Fig. 9B the corresponding increase in intracellular sodium levels with increasing pacing frequency is shown. It can be seen that sodium keeps increasing but the speed of increase decreases for higher frequencies. Sodium concentrations for different frequencies are in the range of values measured by Pieske et al. \([49]\). Figure 9C shows the normalized systolic calcium level as a function of pacing frequency. Assuming that generated force is linearly dependent on systolic calcium, the calcium frequency staircase of our model is similar to the force-frequency relationship obtained experimentally for human myocardial cells by Pieske et al. \([48, 49]\) and Schmidt et al. \([57]\).
**Different Cell Types**  
The parameter setting in *Single Cell* reproduces the AP of an epicardial cell. By changing a few parameters, our model is capable of reproducing the AP shapes of the two other ventricular cell types: endocardial and M cells.

In our model, endocardial cells differ from epicardial cells in their lower \(I_{\text{to}}\) density (\(G_{\text{to}} = 0.073\) nS/pF instead of \(0.294\) nS/pF, a factor of 4 difference) and in their slower recovery from inactivation (different \(\tau_s\), see APPENDIX). These differences are based on data from Nabauer et al. \([43]\) and Wettwer et al. \([68]\). According to Pereon et al. \([47]\), \(I_{\text{Ks}}\) of epicardial and endocardial cells are similar. In our model, M cells differ from epicardial and endocardial cells by having an \(I_{\text{Ks}}\) density of \(0.062\) instead of \(0.245\) nS/pF (a factor of 4 difference). This is based on data from Pereon et al. \([47]\). M cells have \(I_{\text{to}}\) density and dynamics similar to those of epicardial cells \([36]\).

Figure 10 shows APs recorded under steady-state conditions at BCLs of \(1,000\), \(2,000\), and \(5,000\) ms for epicardial (Fig. 10A), endocardial (Fig. 10B), and M (Fig. 10C) cells. From a comparison of Fig. 10, A and B, it follows that the smaller \(I_{\text{to}}\) of endocardial cells results in the virtual absence of the notch that is clearly present in the APs of epicardial and M cells. From a comparison of Fig. 10, A and C, it follows that the smaller \(I_{\text{Ks}}\) of M cells results in a longer APD relative to epicardial and endocardial cells (336 ms in M cells vs. 276 ms in epicardial and 282 ms in endocardial cells for BCL = 1,000 ms) and in a stronger rate dependence of M cell APD.

Note that simulated APD and rate dependence differences between M cells and epi- and endocardial cells are a bit smaller than the experimentally observed differences \([9, 36]\). This is probably due to the fact that M cells differ from the other cell types not only in their \(I_{\text{Ks}}\) density but also with respect to other current densities. Currently, differences in the late component of \(I_{\text{Na}}\) have been described for guinea pig \([56]\) and canine myocardium \([73]\), with guinea pig M cells having a smaller and canine M cells having a larger \(I_{\text{NaL}}\) than the other cell types, and differences in the density of \(I_{\text{NaCa}}\) have been described for canine myocardium \([74]\), with M cells having a larger exchanger current. Because of the partially contradictory nature of the data and the lack of data for human myocardium, we decided not to incorporate any of these other differences in our M cell description in the current version of our model.

Figure 10D shows restitution curves for epicardial, endocardial, and M cells obtained with the dynamic restitution protocol. Again, the longer APD and stronger rate dependence of M cells can be observed. In addition, we can see that the APD of endocardial cells is slightly longer than that of epicardial cells, because of the lower \(I_{\text{to}}\) density, and their APD rate dependence is slightly different, because of the slower \(I_{\text{to}}\) recovery dynamics. Results are very similar to experimentally obtained restitution curves by Drouin et al. \([10]\).

**1D Propagation**  
Figure 11 shows CV restitution curves for a cable of 400 cells. We plotted results for our model and for the PB model, which uses the LR formulation of \(I_{\text{Na}}\) dynamics. For comparison, we also added experimental CV data. Because no experimental data on human CVR are available, guinea pig CV data measured by Girouard et al. \([19]\) were used. It can be seen that the CVR of our model agrees much better with experimental data; it declines less steeply and over a much broader range of diastolic intervals than is the case with the LR \(I_{\text{Na}}\) formulation. Essential for the shape of the CVR curve is the recovery of \(I_{\text{Na}}\), which is mainly determined by the recovery time constant of the slow inactivation gate \(j\). Slowing down the dynamics of the \(j\) gate in the LR \(I_{\text{Na}}\) formulation makes CVR less steep and similar to that of our model \([6]\). Note, however, that our CVR curve was not obtained by rescaling of a time constant but is based on our \(\tau_j\) formulation, which fits experimental data on human \(I_{\text{Na}}\).

**Spiral Waves**  
The 2D simulations were performed on a \(600 \times 600\) square lattice of epicardial ventricular cells with \(\Delta x = 200\ \mu m\). Spiral waves were initiated with the S1-S2 stimulation protocol described in **MATERIALS AND METHODS**. The results of these computations are shown in Fig. 12. Figure 12A shows a typical spiral wave pattern after an initial period of spiral formation and stabilization (at 1.38 s after the S2 stimulus). The average period of the spiral wave is \(264.71 \pm 10.49\) ms, with an average APD of \(217.36 \pm 9.19\) ms and an average diastolic interval of \(47.21 \pm 6.13\) ms. The spiral wave meanders with a typical tip trajectory shown in Fig. 12B; the size of the core is \(\approx 3\) cm; the rotation type is similar to the “Z” core (see Fig. 12C) described by Fast et al. \([15]\) and Efimov et al. \([12]\), which combines regions of fast rotation of the tip (see Fig. 12C, A-B-C and D-E-F), typical of a circular core, with regions of laminar motion (see Fig. 12C, C-D) typical of a linear core.

Figure 13A shows an ECG recorded during spiral wave rotation. The ECG is similar to ECGs recorded during ventricular tachycardia. Figure 13B and C show recordings of membrane voltage in a point far away from the spiral core (star in Fig. 12A) and close to the spiral core (circle in Fig. 12B), respectively. Note the regular AP pattern in the point far from the core and the irregular pattern recorded close to the spiral core.

Similar results were obtained for simulations of sheets of endocardial and M cells. Wave patterns, tip trajectories, and ECG and membrane potential recordings were very similar (data not shown), the only real difference being the period of spiral wave rotation, which is \(264.23 \pm 10.37\) ms for endocardial and \(285.60 \pm 6.70\) ms for M cell tissue.

**DISCUSSION**  
In this paper, we propose a model for human ventricular tissue. An important feature of our model is that all major ionic currents are fitted to recent data on human ventricular myocytes and expression experiments of human cardiac channels. This results in several important differences between our and previous models, the most important of which are the following: slower recovery dynamics of the fast sodium current, leading to a more gradual CVR that agrees better with available experimental data; differentiated formulations for epicardial and endocardial transient outward current, allowing the modeling of these different cell types; and an L-type calcium current with a fast, dominant, and stable calcium inactivation and slow voltage inactivation dynamics. In Table 3, the most important differences between the major ionic currents in our model and the LR, PB, and CRN models are summarized together with their electrophysiological consequences. In addition, conductance parameters used for these currents in our model and the other models are compared.

Our model reproduces three different cell types: endocardial, epicardial, and M cells with different characteristic action potential morphologies and rate dependencies. The APDR of our model closely matches experimentally obtained APDR curves. In addition, the CVR of our model resembles experimentally obtained CVR curves, which are currently only available for animal cardiac tissue, much closer than CVR curves generated with models using the Luo-Rudy \(I_{\text{Na}}\) formulation. Both APDR and CVR are very important determinants for the stability of reentrant arrhythmias. Our calcium dynamics formulation is of a complexity comparable to that of the LR, PB, and CRN models and allows us to simulate a realistic calcium transient and a typical positive human contraction staircase.

The feasibility of spatial simulations is demonstrated with a simulation of a reentrant spiral wave in a 2D sheet of epicardial tissue. The period of spiral wave rotation is \(254\) ms, vs. \(304\) ms in the reduced PB model \([3]\), because of the shorter APD in our model. The spiral wave tip trajectory is somewhat different from the linear

 tip trajectory found by Bernus et al. \([3]\), because of the larger horizontal parts of the Z-type core. Another difference is that in the model by Bernus et al. \([3]\), the core pattern has a cross-section of \(\approx 5\) cm, whereas in our model the core pattern has a cross-section of \(\approx 3\) cm, again because of the shorter APD in our model.

**Limitations**  
A limitation of our model is that differences in APD and rate dependence between M cells and epicardial and endocardial cells in our model are smaller than the experimentally observed differences. This is because of the limited current knowledge of basic electrophysiological differences between M cells and the other cell types causing these differences. If these differences are further characterized, they can be easily incorporated in our model in terms of different current densities and/or dynamics for M cells, similar to what already has been done for \(I_{\text{Ks}}\) density differences.

We put considerable effort into obtaining, evaluating, rescaling to physiological conditions, and fitting of experimental data to get a model closely resembling true human ventricular cells. However, limitations are unavoidable because of the limited availability of data, the extensive variability among experimental data, the considerable variation in experimental conditions, and the potentially deleterious effects of cell isolation procedures used in voltage-clamp experiments.

There were no data available on \(I_{\text{CaL}}\) activation time constants, so formulations from another model based on animal experiments had to be used. The precise nature of calcium-mediated inactivation of the L-type calcium current is unknown. We used a simple description with a constant-valued time constant and a dependence on intracellular calcium only, although data suggest that extracellular calcium also plays a role in inactivation \([60]\). Finally, no data were available on the nature of calcium dynamics under high frequencies. We assumed calcium dynamics to stay stable under high frequencies. In addition, we assumed CICR to depend in a saturating manner on sarcoplasmic reticulum calcium content.

There is no agreement on experimental data regarding steady-state inactivation of \(I_{\text{Na}}\). Some researchers give a value of \(-85\) mV for the voltage of half-inactivation \([44, 55, 64]\), whereas others give a value of around \(-65\) mV \([30, 40, 58]\). Rather than making a compromise, we based our steady-state inactivation curves on data from Nagatomo et al. \([44]\) because we also used their data for steady-state activation and time constants and wanted to maintain consistency.

Experiments are often performed at different temperatures. This is especially true for \(I_{\text{Na}}\) voltage-clamp experiments, where the temperature is usually below the physiological temperature to slow dynamics and limit current size. We derived a single \(Q_{10}\) factor and used this to rescale all \(I_{\text{Na}}\) time constants to \(37^{\circ}\). Because it is not clear how steady-state curves change with temperature, we performed a linear extrapolation of the half-(in)activation voltages and slopes.

Experiments are also performed in the presence of different combinations of pharmacological agents used to suppress other currents. It is known that some of these chemicals have an impact on the dynamics of the measured current, e.g., \(Cd^{2+}\) used to block L-type calcium current is known to influence steady-state curves of \(I_{\text{to}}\) current. We corrected experimental steady-state curves of \(I_{\text{to}}\) for the presence of \(Cd^{2+}\) by shifting them 10 mV in the positive direction.

To perform single-cell voltage-clamp experiments, cells must be isolated. These isolation procedures can have profound effects on the density of particular currents. A clear example of this is the \(I_{\text{Ks}}\) and \(I_{\text{Kr}}\) currents. \(I_{\text{Ks}}\) and \(I_{\text{Kr}}\) current densities found during voltage-clamp experiments are in sharp contrast with the clear relevance of these currents for action potential duration and restitution and the different behavior of M cells. We therefore decided to apply current densities for \(I_{\text{Ks}}\) and \(I_{\text{Kr}}\) that are substantially larger than experimentally measured densities and that allow us to realistically simulate the consequences of \(I_{\text{Kr}}\) block and the behavior of M cells.

In conclusion, we propose a new model for human ventricular epicardial, endocardial, and M cells based on ionic currents measured in human ventricular cells or measured in expression experiments using human cardiac channels. The model reproduces a number of experimental observations, ranging from voltage-clamp current traces and I-V curves to AP morphology, as well as APD and CV restitution curves and the contraction staircase. Because of its relative computational simplicity, the model is suitable for application in large-scale spatial simulations, which are necessary for investigating the dynamics of reentrant arrhythmias. The latter is illustrated with the simulation of a reentrant spiral wave in a 2D sheet of epicardial ventricular tissue.


