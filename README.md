Abstract:

Atomistic simulations serve as a pivotal tool at the microscopic scale, delving into the behavior of individual atoms or molecules, offering insights into intricate phenomena such as protein folding, alloy structures, and crack propagation. This project focuses on fundamental atomistic applications, specifically computing lattice and elastic constants for simple crystals at absolute zero and simulating bond breaking in a carbon nanotube. Emphasizing practical application over intricate numerical frameworks, the project aims to uncover potential pitfalls while acknowledging the significance of understanding underlying numerical methodologies for result interpretation.

The essential components of an atomistic simulation encompass defining the initial configuration, specifying boundary conditions, selecting an appropriate potential function to derive forces, and employing a numerical solver. While briefly discussing these elements, the primary emphasis is on the criticality of choosing and validating a suitable potential.

System definition and boundary conditions dictate the problem scope and constraints, ranging from free movement to prescribed forces or restricted degrees of freedom. Understanding ensembles such as the microcanonical (NVE) or canonical (NVT) becomes imperative for conserving fundamental quantities like energy, number of atoms, and volume, or controlling temperature and pressure through thermostat methodologies.

The crux of atomistic simulations lies in the judicious selection of a potential, especially concerning empirical or semi-empirical potentials. Parameters like accuracy, transferability, and computational efficiency guide this choice, with no definitive answer, but rather a system-specific evaluation. Smaller-scale problems necessitate higher accuracy in potential selection, while larger simulations prioritize computational expediency, exemplified by the varying needs between calculating molecular bonding energies and simulating crack propagation.

Abstract Continued:

Defining the numerical solving scheme in atomistic simulations involves evaluating particle positions by considering interacting forces, typically addressed through solving Newton's second law using time integration. For dynamic systems, the velocity-Verlet integration is prevalent, while static simulations employ non-linear optimizers like the BFGS solver to seek minimum energy states in complex, non-linear energy landscapes.

Applying atomistic codes in a real-life scenario involves using a copper lattice as an example with the atomistic simulation environment ASE. Considering the promising potential EMT tailored for copper, compatibility with ASE is verified, allowing for seamless integration.

The verification of the chosen potential precedes its use in simulations, typically involving comparisons with experimental data. Molecular statics simulations serve as a simplified approach to examining potential energies within crystal lattices, forming a basis for validating the chosen potential.

Determining crystal structures, lattice constants, and elastic constants of materials like copper involves analyzing potential energy minimization, crystal structures, and measuring mechanical properties through strain and stress calculations. Utilizing Voigt notation and prescribed deformations, the stiffness tensor, and elastic constants are computed, aligning with experimental measurements.

Moving beyond static simulations, exploring non-zero temperatures becomes imperative, especially in scenarios like studying carbon nanotube (CNT) behavior at varying energies induced through mechanical work. Utilizing the Boltzmann constant, the average kinetic energy relates to temperature, necessitating a shift from static energy minimization to dynamic simulations.

For investigating the bond-breaking in carbon nanotubes, the Brenner-Potential, a common choice for CNTs, is a potential avenue to explore. Understanding the system's behavior under varying mechanical work and temperatures paves the way for comprehensive studies on bond-breaking phenomena in CNTs.
