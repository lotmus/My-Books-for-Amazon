**Mathematical foundations for quantum states, operators, spinors, and fields**

Course edition 1.0

# Lesson 1 Complex Numbers and Linear Algebra

# How to use this lesson

Quantum electrodynamics is written in the language of complex vector spaces and linear operators. This lesson develops that language from first principles. The emphasis is not only on calculation, but on recognizing the structures that return later as quantum states, observables, spinors, polarization vectors, and field modes.

Work through the examples with pencil and paper. Attempt the exercises before reading the solutions. A learner comfortable with algebra can complete the lesson in six to ten focused hours; mastery comes from repeating the calculations until the notation feels ordinary.

## Learning objectives

- Compute with complex numbers in Cartesian, polar, and exponential form.

- Use complex conjugation and modulus to construct real, nonnegative quantities.

- Interpret vectors abstractly and distinguish vectors from their coordinate columns.

- Use inner products, norms, orthogonality, and orthonormal bases.

- Represent linear maps by matrices and understand how representations change with basis.

- Find eigenvalues and eigenvectors and recognize Hermitian and unitary operators.

- Read elementary bra-ket notation and connect it to ordinary matrix algebra.

- Apply the Pauli matrices as the first concrete bridge to spin and QED.

## Notation and conventions

  ------------------------------------------------------------------------
  **Symbol**                          **Meaning**
  ----------------------------------- ------------------------------------
  i                                   Imaginary unit, i² = -1

  z\*                                 Complex conjugate of z

  ℂⁿ                                  Complex n-dimensional vector space

  v†                                  Conjugate transpose of v

  ⟨u\|v⟩                              Inner product

  I                                   Identity operator

  A⁻¹                                 Inverse of A, when it exists
  ------------------------------------------------------------------------

# 1 Complex numbers

## 1.1 Why quantum theory uses complex numbers

A real number describes magnitude along one line. A complex number carries two real components and, crucially, a phase. Quantum amplitudes interfere: phases can reinforce or cancel even when measurable probabilities remain real. Complex numbers provide the smallest algebraic system that naturally encodes this behavior.

## 1.2 Cartesian form

A complex number has a real part and an imaginary part.

$$z\  = \ a\  + \ ib,\ \ \ \ a,b\  \in \ {\mathbb{R}},\ \ \ \ i²\  = \  - 1$$

Addition is componentwise. Multiplication follows ordinary distributivity together with i² = -1.

$$(a + ib)(c + id)\  = \ (ac - bd)\  + \ i(ad + bc)$$

### Worked example 1

Let z = 3 + 2i and w = 1 - 4i. Then z + w = 4 - 2i. For the product,

$$zw\  = \ (3 + 2i)(1 - 4i)\  = \ 11 - 10i$$

The term (2i)(-4i) equals +8 because i² = -1.

## 1.3 Conjugation and modulus

Complex conjugation reverses the sign of the imaginary part. Multiplying a number by its conjugate removes its phase and produces a nonnegative real number.

$$z*\  = \ a - ib,\ \ \ \ |z|²\  = \ z*z\  = \ a² + b²$$

- (z+w)\* = z\*+w\*

- (zw)\* = z\*w\*

- \|zw\| = \|z\|\|w\|

- z⁻¹ = z\*/\|z\|² for z ≠ 0

### Worked example 2

For z = 3 + 4i, the modulus is \|z\| = 5. Its inverse is

$$1/z\  = \ (3 - 4i)/25$$

The pattern amplitude times complex-conjugate amplitude will later become central: probabilities and cross sections are built from expressions such as \|M\|².

## 1.4 Polar form and Euler formula

$$eⁱᶿ\  = \ cos\ \theta\  + \ i\ sin\ \theta$$

Every nonzero complex number can be written as z = r e\^(iθ), where r = \|z\| and θ is the argument or phase. Multiplication then multiplies moduli and adds phases; division divides moduli and subtracts phases.

$$(r\ eⁱᶿ)(s\ eⁱᵠ)\  = \ rs\ eⁱ⁽ᶿ⁺ᵠ⁾$$

### Worked example 3

The number 1 + i has modulus √2 and argument π/4, so 1 + i = √2 e\^(iπ/4). Squaring gives 2e\^(iπ/2) = 2i.

## 1.5 Phase and interference

Suppose two alternatives contribute amplitudes A₁ and A₂. The measurable intensity is not usually \|A₁\|² + \|A₂\|²; it is

$$|A₁ + A₂|²\  = \ |A₁|² + |A₂|² + 2\ Re(A₁*A₂)$$

The final term is interference. A relative phase of zero gives reinforcement; a relative phase of π gives cancellation. An overall common phase cancels from the modulus squared, anticipating the physical importance of relative rather than absolute phase.

# 2 Vectors and vector spaces

## 2.1 Abstract vectors

A vector is an object that can be added to another vector and multiplied by a scalar while satisfying the vector-space rules. An arrow in ordinary space is one example, but a polynomial, wave function, spinor, or field configuration can also be a vector. In quantum mechanics the scalars are normally complex numbers.

## 2.2 Coordinates and bases

A basis is an ordered set of linearly independent vectors that spans the space. Once a basis {e₁,...,eₙ} is chosen, a vector v can be represented by a coordinate column.

$$v\  = \ v₁e₁ + \cdots + vₙeₙ\ \  \leftrightarrow \ \ \lbrack v₁\ \ldots\ vₙ\rbrack ᵀ$$

The vector is the abstract object; the column is its representation in a chosen basis. Changing basis changes the components, not the vector.

## 2.3 Linear independence span and dimension

- A set spans a space if every vector in the space is a linear combination of the set.

- A set is linearly independent if the only combination that equals zero has every coefficient equal to zero.

- A basis is both spanning and linearly independent.

- The dimension is the number of elements in any basis of a finite-dimensional space.

### Worked example 4

In ℂ², e₁ = (1,0)ᵀ and e₂ = (0,1)ᵀ form the standard basis. The vectors f₁ = (1,1)ᵀ and f₂ = (1,-1)ᵀ also form a basis because neither is a scalar multiple of the other. The vector v = (3,1)ᵀ becomes v = 2f₁ + f₂.

# 3 Inner products and geometry

## 3.1 The complex inner product

For columns u and v in ℂⁿ, the standard inner product conjugates the first vector.

$$\langle u|v\rangle\  = \ u \dagger v\  = \ \Sigma ⱼ\ uⱼ*\ vⱼ$$

Conjugation guarantees that ⟨v\|v⟩ is real and nonnegative. The inner product is conjugate symmetric: ⟨u\|v⟩ = ⟨v\|u⟩\*. Conventions differ about which slot is linear; physics bra-ket notation is linear in the ket.

## 3.2 Norm orthogonality and normalization

$$\| v\|\  = \ \sqrt{}\langle v|v\rangle$$

Vectors are orthogonal when ⟨u\|v⟩ = 0. A vector is normalized when its norm is one. A basis is orthonormal when every basis vector has unit norm and distinct basis vectors are orthogonal.

### Worked example 5

Let v = (1,i)ᵀ. Then v† = (1,-i), so ⟨v\|v⟩ = 1 + (-i)i = 2. The normalized vector is v/√2.

## 3.3 Completeness in finite dimensions

If {\|eⱼ⟩} is an orthonormal basis, every vector can be reconstructed from its projections.

$$|v\rangle\  = \ \Sigma ⱼ\ |eⱼ\rangle\langle eⱼ|v\rangle,\ \ \ \ \Sigma ⱼ\ |eⱼ\rangle\langle eⱼ|\  = \ I$$

This resolution of the identity later becomes a sum over spin states, polarization states, or intermediate modes.

## 3.4 Gram Schmidt orthonormalization

Given independent vectors v₁ and v₂, normalize the first, subtract from the second its component along the first, and normalize what remains.

$$e₁\  = \ v₁/\| v₁\|,\ \ \ \ u₂\  = \ v₂ - e₁\langle e₁|v₂\rangle,\ \ \ \ e₂\  = \ u₂/\| u₂\|$$

# 4 Linear operators and matrices

## 4.1 Linearity

A map A is linear if A(αu+βv) = αAu+βAv. Once bases are chosen, a linear map is represented by a matrix. Matrix multiplication represents composition of maps; in general AB differs from BA.

## 4.2 Matrix action and composition

$$(Av)ᵢ\  = \ \Sigma ⱼ\ Aᵢⱼvⱼ,\ \ \ \ (AB)ᵢₖ\  = \ \Sigma ⱼ\ AᵢⱼBⱼₖ$$

## 4.3 Identity inverse determinant and trace

  ---------------------------------------------------------------------------------------------------------
  **Object**                          **Meaning**
  ----------------------------------- ---------------------------------------------------------------------
  Identity I                          Iv = v

  Inverse A⁻¹                         A⁻¹A = AA⁻¹ = I

  Determinant det A                   Measures invertibility and oriented volume scaling

  Trace tr A                          Sum of diagonal entries; invariant under similarity transformations
  ---------------------------------------------------------------------------------------------------------

A square matrix is invertible exactly when its determinant is nonzero. For a 2 × 2 matrix,

$$A\  = \ \lbrack a\ b;\ c\ d\rbrack,\ \ \ \ A⁻¹\  = \ (1/(ad - bc))\lbrack d\  - b;\  - c\ a\rbrack$$

## 4.4 Change of basis

Let S have the new basis vectors as its columns, expressed in the old basis. Coordinates transform as \[v\]old = S\[v\]new, and an operator transforms by similarity.

$$\lbrack A\rbrack new\  = \ S⁻¹\lbrack A\rbrack old\ S$$

Similarity changes a matrix representation without changing the underlying linear operator. Trace, determinant, and eigenvalues therefore remain unchanged.

# 5 Eigenvalues eigenvectors and diagonalization

## 5.1 The eigenvalue equation

$$A|v\rangle\  = \ \lambda|v\rangle$$

An eigenvector is a direction whose only change under A is multiplication by λ. Nonzero solutions exist when det(A - λI) = 0. This characteristic equation determines the eigenvalues.

### Worked example 6

For A = \[\[2,1\],\[1,2\]\], the characteristic polynomial is (2-λ)² - 1, giving λ = 3 and λ = 1. Corresponding normalized eigenvectors are (1,1)ᵀ/√2 and (1,-1)ᵀ/√2.

## 5.2 Diagonalization

If an n × n matrix has n independent eigenvectors, put them into the columns of S. Then S⁻¹AS is diagonal, with eigenvalues on the diagonal. Diagonal form makes powers, exponentials, and differential equations easier to compute.

$$A\  = \ S\Lambda S⁻¹\ \  \Rightarrow \ \ f(A)\  = \ Sf(\Lambda)S⁻¹$$

## 5.3 Degeneracy and commuting operators

An eigenvalue is degenerate when more than one independent eigenvector shares it. If two diagonalizable operators commute and suitable regularity conditions hold, one can choose a common eigenbasis. In quantum theory, commuting observables can be assigned simultaneous definite values.

# 6 Adjoint Hermitian and unitary operators

## 6.1 The adjoint

The adjoint A† is the conjugate transpose of a matrix. Abstractly, it is defined by ⟨u\|Av⟩ = ⟨A†u\|v⟩.

- (AB)† = B†A†

- (A†)† = A

- (A⁻¹)† = (A†)⁻¹ when A is invertible

## 6.2 Hermitian operators

$$A \dagger \  = \ A$$

Hermitian operators have real eigenvalues, and eigenvectors belonging to distinct eigenvalues are orthogonal. These facts make Hermitian operators suitable representations of observables.

## 6.3 Unitary operators

$$U \dagger U\  = \ UU \dagger \  = \ I$$

Unitary operators preserve inner products, lengths, angles, and total probability. A change between orthonormal bases is unitary. Time evolution in an isolated quantum system is unitary.

## 6.4 Projectors

$$P²\  = \ P,\ \ \ \ P \dagger \  = \ P$$

For a normalized state \|u⟩, the operator P = \|u⟩⟨u\| projects a vector onto the direction u. Measurement probabilities will be expressed using such projections.

# 7 Bra ket notation

## 7.1 Kets and bras

A ket \|ψ⟩ denotes a vector. Its dual bra ⟨ψ\| is the conjugate transpose. Their product in one order is a scalar and in the reverse order is an operator.

$$\langle\varphi|\psi\rangle\ is\ a\ scalar,\ \ \ \ |\psi\rangle\langle\varphi|\ is\ an\ operator$$

## 7.2 Matrix elements

The scalar ⟨φ\|A\|ψ⟩ is a matrix element of A. It describes how A connects the input state \|ψ⟩ with the output direction \|φ⟩. In QED, scattering amplitudes are built from chains of operators and spinors with exactly this structure.

## 7.3 Expectation values

$$\langle A\rangle\psi\  = \ \langle\psi|A|\psi\rangle,\ \ \ \ \langle\psi|\psi\rangle\  = \ 1$$

For Hermitian A, the expectation value is real. It is an average prediction for repeated measurements on identically prepared systems, not necessarily an eigenvalue from one individual measurement.

# 8 Pauli matrices as a preview of spin

The Pauli matrices act on two-component complex vectors and form the basic algebra of spin one-half. They will reappear in the Dirac equation and in relativistic spinor calculations.

$$\sigma ₓ\  = \ \lbrack 0\ 1;\ 1\ 0\rbrack,\ \ \ \ \sigma ᵧ\  = \ \lbrack 0\  - i;\ i\ 0\rbrack,\ \ \ \ \sigma\_ z\  = \ \lbrack 1\ 0;\ 0\  - 1\rbrack$$

Each Pauli matrix is Hermitian and unitary, has trace zero and determinant -1, and has eigenvalues +1 and -1. Their products satisfy

$$\sigma ᵢ\sigma ⱼ\  = \ \delta ᵢⱼI\  + \ i\ \varepsilon ᵢⱼₖ\sigma ₖ,\ \ \ \ \lbrack\sigma ᵢ,\sigma ⱼ\rbrack\  = \ 2i\ \varepsilon ᵢⱼₖ\sigma ₖ$$

### Worked example 7

The eigenvectors of σ_z are \|+z⟩ = (1,0)ᵀ and \|-z⟩ = (0,1)ᵀ. The +1 eigenvector of σₓ is \|+x⟩ = (1,1)ᵀ/√2. Therefore \|⟨+z\|+x⟩\|² = 1/2: a system prepared with positive x-spin yields either z-spin result with equal probability.

# 9 Connections to QED

  ----------------------------------------------------------------------------------------------------------
  **Mathematical idea**               **Later role in QED**
  ----------------------------------- ----------------------------------------------------------------------
  Complex phase                       Quantum interference and U(1) transformations

  Inner product                       Probabilities, normalizations, and amplitudes

  Linear operator                     Observables, symmetry generators, and propagators

  Eigenvector                         Definite spin, momentum, or energy state

  Unitary map                         Symmetry transformations and quantum evolution

  Hermitian matrix                    Observable or generator with real physical values

  Basis change                        Moving among spin, polarization, position, and momentum descriptions

  Pauli matrices                      Spin algebra and building blocks of Dirac gamma matrices
  ----------------------------------------------------------------------------------------------------------

The local phase transformation at the heart of QED begins with the simple global rule \|ψ⟩ → e\^(iα)\|ψ⟩. Because the factor has unit modulus, inner products and probabilities are unchanged. Requiring invariance when α varies from point to point ultimately forces the introduction of the electromagnetic potential. The algebra learned here is therefore not preliminary decoration; it is part of the mechanism that generates the interaction.

# 10 Summary

1.  Complex numbers encode magnitude and phase; conjugation turns amplitudes into real probabilities.

2.  A vector is independent of its coordinates, while a basis supplies a coordinate representation.

3.  Inner products define norm, angle, orthogonality, and projection.

4.  Matrices represent linear operators; changing basis changes the matrix by similarity.

5.  Eigenvectors identify directions of definite operator action.

6.  Hermitian operators have real eigenvalues; unitary operators preserve inner products.

7.  Bra-ket notation is compact matrix algebra adapted to quantum theory.

8.  The Pauli matrices provide the first concrete model of spin-one-half structure.

# Exercises

  ---------------------------------------------------------------------------------------------------------------------------------------------------------
  **No**                              **Problem**
  ----------------------------------- ---------------------------------------------------------------------------------------------------------------------
  1                                   Compute (2+3i)+(4−i), (2+3i)(4−i), and (2+3i)/(4−i).

  2                                   Write −1+i√3 in polar form using a principal argument in (−π,π\].

  3                                   Show directly that \|zw\|² = \|z\|²\|w\|².

  4                                   Let A₁ = 1 and A₂ = e\^(iφ). Find \|A₁+A₂\|² and evaluate it at φ = 0, π/2, and π.

  5                                   Determine whether (1,i)ᵀ and (i,1)ᵀ are orthogonal in ℂ².

  6                                   Normalize v = (1,1+i,2i)ᵀ.

  7                                   Express (5,1)ᵀ as a combination of f₁=(1,1)ᵀ and f₂=(1,−1)ᵀ.

  8                                   Apply Gram Schmidt to v₁=(1,1)ᵀ and v₂=(1,0)ᵀ.

  9                                   For A=\[\[1,2\],\[3,4\]\], compute det A, tr A, and A⁻¹.

  10                                  Find the eigenvalues and normalized eigenvectors of \[\[4,0\],\[0,−2\]\].

  11                                  Show that eigenvalues of a unitary matrix have modulus one.

  12                                  Show that an expectation value ⟨ψ\|A\|ψ⟩ is real when A is Hermitian.

  13                                  Compute σₓσᵧ and σᵧσₓ, then find \[σₓ,σᵧ\].

  14                                  Find normalized eigenvectors of σᵧ for eigenvalues +1 and −1.

  15                                  Let \|ψ⟩=(cos(θ/2), e\^(iφ)sin(θ/2))ᵀ. Verify normalization and compute ⟨σ_z⟩.

  16                                  Challenge: prove the Cauchy Schwarz inequality \|⟨u\|v⟩\|² ≤ ⟨u\|u⟩⟨v\|v⟩ by considering ‖u−cv‖² with a suitable c.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------

# Solutions

**1.** 6+2i; 11+10i; (5+14i)/17.

**2.** The modulus is 2 and the principal argument is 2π/3, so z=2e\^(2πi/3).

**3.** (zw)\*(zw)=z\*w\*zw=(z\*z)(w\*w), using commutativity of complex multiplication.

**4.** 2+2cosφ. The values are 4, 2, and 0.

**5.** Their inner product is (1,−i)·(i,1)=i−i=0, so they are orthogonal.

**6.** The squared norm is 1+\|1+i\|²+\|2i\|²=7. Thus v/√7 is normalized.

**7.** Solve a+b=5 and a−b=1: a=3 and b=2.

**8.** e₁=(1,1)ᵀ/√2. Subtraction gives u₂=(1/2,−1/2)ᵀ, so e₂=(1,−1)ᵀ/√2.

**9.** det A=−2, tr A=5, and A⁻¹=\[\[-2,1\],\[3/2,−1/2\]\].

**10.** The eigenvalues are 4 and −2, with eigenvectors (1,0)ᵀ and (0,1)ᵀ.

**11.** If Uv=λv, then ‖v‖=‖Uv‖=‖λv‖=\|λ\|‖v‖. For nonzero v, \|λ\|=1.

**12.** Let x=⟨ψ\|A\|ψ⟩. Then x\*=⟨ψ\|A†\|ψ⟩=⟨ψ\|A\|ψ⟩=x, hence x is real.

**13.** σₓσᵧ=iσ_z and σᵧσₓ=−iσ_z, so \[σₓ,σᵧ\]=2iσ_z.

**14.** For +1 use (1,i)ᵀ/√2; for −1 use (1,−i)ᵀ/√2. Overall phases are physically equivalent.

**15.** The norm is cos²(θ/2)+sin²(θ/2)=1. The expectation is cos²(θ/2)−sin²(θ/2)=cosθ.

**16.** For v≠0 choose c=⟨v\|u⟩/⟨v\|v⟩. Expanding 0≤‖u−cv‖² gives ⟨u\|u⟩−\|⟨v\|u⟩\|²/⟨v\|v⟩≥0. Rearrangement proves the claim; v=0 is immediate.

# Mastery checklist

- I can move freely between Cartesian and polar forms of a complex number.

- I automatically conjugate the bra when calculating a complex inner product.

- I can normalize a vector and construct a projector from it.

- I can find eigenvalues and eigenvectors of a 2 × 2 matrix.

- I can test whether a matrix is Hermitian or unitary.

- I can translate simple bra-ket expressions into matrix multiplication.

- I can calculate with Pauli matrices without treating them as mysterious symbols.

# Next lesson

Lesson 2 develops calculus and differential equations, emphasizing derivatives, gradients, Fourier ideas, ordinary differential equations, and the partial differential equations that govern waves and fields.

# Part I Prerequisites

# Lesson 2 Calculus and Differential Equations

This lesson develops calculus and differential equations as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in calculus and differential equations.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$d/dx\ exp(kx) = k\ exp(kx);\ \ \nabla ²\varphi - \partial ²\varphi/\partial t² = 0$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which calculus and differential equations appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

9.  State the symmetry, dynamical principle, or algebraic definition.

10. Write the most general expression compatible with the assumptions.

11. Apply the defining relation and simplify without dropping boundary or sign terms.

12. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for calculus and differential equations on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Calculus and Differential Equations contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

13. Derive the core relation for calculus and differential equations from the definitions used in this lesson.

14. Construct a simple example and verify the relation numerically or component by component.

15. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 3 Special Relativity

This lesson develops special relativity as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in special relativity.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$E² - |p|² = m²$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which special relativity appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

16. State the symmetry, dynamical principle, or algebraic definition.

17. Write the most general expression compatible with the assumptions.

18. Apply the defining relation and simplify without dropping boundary or sign terms.

19. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for special relativity on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Special Relativity contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

20. Derive the core relation for special relativity from the definitions used in this lesson.

21. Construct a simple example and verify the relation numerically or component by component.

22. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 4 Four Vectors and Lorentz Transformations

This lesson develops four vectors and lorentz transformations as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in four vectors and lorentz transformations.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$x'\mu = \Lambda\mu\nu x\nu;\ \ \Lambda Tg\Lambda = g$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which four vectors and lorentz transformations appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

23. State the symmetry, dynamical principle, or algebraic definition.

24. Write the most general expression compatible with the assumptions.

25. Apply the defining relation and simplify without dropping boundary or sign terms.

26. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for four vectors and lorentz transformations on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Four Vectors and Lorentz Transformations contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

27. Derive the core relation for four vectors and lorentz transformations from the definitions used in this lesson.

28. Construct a simple example and verify the relation numerically or component by component.

29. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 5 Classical Mechanics and Lagrangians

This lesson develops classical mechanics and lagrangians as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in classical mechanics and lagrangians.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$d/dt(\partial L/\partial q\dot{}) - \partial L/\partial q = 0$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which classical mechanics and lagrangians appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

30. State the symmetry, dynamical principle, or algebraic definition.

31. Write the most general expression compatible with the assumptions.

32. Apply the defining relation and simplify without dropping boundary or sign terms.

33. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for classical mechanics and lagrangians on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Classical Mechanics and Lagrangians contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

34. Derive the core relation for classical mechanics and lagrangians from the definitions used in this lesson.

35. Construct a simple example and verify the relation numerically or component by component.

36. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 6 Hamiltonian Mechanics

This lesson develops hamiltonian mechanics as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in hamiltonian mechanics.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$H = pq\dot{} - L;\ \ q\dot{} = \partial H/\partial p;\ \ p\dot{} = - \partial H/\partial q$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which hamiltonian mechanics appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

37. State the symmetry, dynamical principle, or algebraic definition.

38. Write the most general expression compatible with the assumptions.

39. Apply the defining relation and simplify without dropping boundary or sign terms.

40. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for hamiltonian mechanics on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Hamiltonian Mechanics contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

41. Derive the core relation for hamiltonian mechanics from the definitions used in this lesson.

42. Construct a simple example and verify the relation numerically or component by component.

43. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 7 Maxwell Equations

This lesson develops maxwell equations as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in maxwell equations.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\partial\mu F\mu\nu = j\nu;\ \ \partial\lbrack\alpha F\beta\gamma\rbrack = 0$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which maxwell equations appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

44. State the symmetry, dynamical principle, or algebraic definition.

45. Write the most general expression compatible with the assumptions.

46. Apply the defining relation and simplify without dropping boundary or sign terms.

47. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for maxwell equations on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Maxwell Equations contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

48. Derive the core relation for maxwell equations from the definitions used in this lesson.

49. Construct a simple example and verify the relation numerically or component by component.

50. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 8 Electromagnetic Potentials and Gauge Freedom

This lesson develops electromagnetic potentials and gauge freedom as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in electromagnetic potentials and gauge freedom.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$A\mu \rightarrow A\mu + \partial\mu\alpha$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which electromagnetic potentials and gauge freedom appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

51. State the symmetry, dynamical principle, or algebraic definition.

52. Write the most general expression compatible with the assumptions.

53. Apply the defining relation and simplify without dropping boundary or sign terms.

54. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for electromagnetic potentials and gauge freedom on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Electromagnetic Potentials and Gauge Freedom contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

55. Derive the core relation for electromagnetic potentials and gauge freedom from the definitions used in this lesson.

56. Construct a simple example and verify the relation numerically or component by component.

57. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Part II Quantum Mechanics

# Lesson 9 Wave Functions and Hilbert Spaces

This lesson develops wave functions and hilbert spaces as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in wave functions and hilbert spaces.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\langle\psi|\psi\rangle = 1$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which wave functions and hilbert spaces appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

58. State the symmetry, dynamical principle, or algebraic definition.

59. Write the most general expression compatible with the assumptions.

60. Apply the defining relation and simplify without dropping boundary or sign terms.

61. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for wave functions and hilbert spaces on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Wave Functions and Hilbert Spaces contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

62. Derive the core relation for wave functions and hilbert spaces from the definitions used in this lesson.

63. Construct a simple example and verify the relation numerically or component by component.

64. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 10 Operators and Observables

This lesson develops operators and observables as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in operators and observables.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$A \dagger = A$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which operators and observables appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

65. State the symmetry, dynamical principle, or algebraic definition.

66. Write the most general expression compatible with the assumptions.

67. Apply the defining relation and simplify without dropping boundary or sign terms.

68. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for operators and observables on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Operators and Observables contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

69. Derive the core relation for operators and observables from the definitions used in this lesson.

70. Construct a simple example and verify the relation numerically or component by component.

71. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 11 Schrodinger Equation

This lesson develops schrodinger equation as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in schrodinger equation.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$i\partial t|\psi\rangle = H|\psi\rangle$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which schrodinger equation appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

72. State the symmetry, dynamical principle, or algebraic definition.

73. Write the most general expression compatible with the assumptions.

74. Apply the defining relation and simplify without dropping boundary or sign terms.

75. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for schrodinger equation on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Schrodinger Equation contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

76. Derive the core relation for schrodinger equation from the definitions used in this lesson.

77. Construct a simple example and verify the relation numerically or component by component.

78. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 12 Momentum and Position

This lesson develops momentum and position as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in momentum and position.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\lbrack xᵢ,pⱼ\rbrack = i\delta ᵢⱼ$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which momentum and position appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

79. State the symmetry, dynamical principle, or algebraic definition.

80. Write the most general expression compatible with the assumptions.

81. Apply the defining relation and simplify without dropping boundary or sign terms.

82. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for momentum and position on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Momentum and Position contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

83. Derive the core relation for momentum and position from the definitions used in this lesson.

84. Construct a simple example and verify the relation numerically or component by component.

85. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 13 Angular Momentum

This lesson develops angular momentum as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in angular momentum.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\lbrack Lᵢ,Lⱼ\rbrack = i\varepsilon ᵢⱼₖLₖ$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which angular momentum appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

86. State the symmetry, dynamical principle, or algebraic definition.

87. Write the most general expression compatible with the assumptions.

88. Apply the defining relation and simplify without dropping boundary or sign terms.

89. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for angular momentum on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Angular Momentum contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

90. Derive the core relation for angular momentum from the definitions used in this lesson.

91. Construct a simple example and verify the relation numerically or component by component.

92. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 14 Spin and Pauli Matrices

This lesson develops spin and pauli matrices as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in spin and pauli matrices.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$S = \sigma/2$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which spin and pauli matrices appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

93. State the symmetry, dynamical principle, or algebraic definition.

94. Write the most general expression compatible with the assumptions.

95. Apply the defining relation and simplify without dropping boundary or sign terms.

96. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for spin and pauli matrices on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Spin and Pauli Matrices contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

97. Derive the core relation for spin and pauli matrices from the definitions used in this lesson.

98. Construct a simple example and verify the relation numerically or component by component.

99. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 15 Perturbation Theory

This lesson develops perturbation theory as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in perturbation theory.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$Eₙ(1) = \langle n|V|n\rangle$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which perturbation theory appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

100. State the symmetry, dynamical principle, or algebraic definition.

101. Write the most general expression compatible with the assumptions.

102. Apply the defining relation and simplify without dropping boundary or sign terms.

103. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for perturbation theory on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Perturbation Theory contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

104. Derive the core relation for perturbation theory from the definitions used in this lesson.

105. Construct a simple example and verify the relation numerically or component by component.

106. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 16 Identical Particles

This lesson develops identical particles as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in identical particles.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$|\psi(1,2)\rangle = \pm |\psi(2,1)\rangle$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which identical particles appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

107. State the symmetry, dynamical principle, or algebraic definition.

108. Write the most general expression compatible with the assumptions.

109. Apply the defining relation and simplify without dropping boundary or sign terms.

110. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for identical particles on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Identical Particles contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

111. Derive the core relation for identical particles from the definitions used in this lesson.

112. Construct a simple example and verify the relation numerically or component by component.

113. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Part III Relativistic Quantum Mechanics

# Lesson 17 Klein Gordon Equation

This lesson develops klein gordon equation as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in klein gordon equation.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$(\square + m²)\varphi = 0$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which klein gordon equation appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

114. State the symmetry, dynamical principle, or algebraic definition.

115. Write the most general expression compatible with the assumptions.

116. Apply the defining relation and simplify without dropping boundary or sign terms.

117. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for klein gordon equation on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Klein Gordon Equation contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

118. Derive the core relation for klein gordon equation from the definitions used in this lesson.

119. Construct a simple example and verify the relation numerically or component by component.

120. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 18 Why the Schrodinger Equation Is Not Enough

This lesson develops why the schrodinger equation is not enough as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in why the schrodinger equation is not enough.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$E² = p² + m²$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which why the schrodinger equation is not enough appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

121. State the symmetry, dynamical principle, or algebraic definition.

122. Write the most general expression compatible with the assumptions.

123. Apply the defining relation and simplify without dropping boundary or sign terms.

124. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for why the schrodinger equation is not enough on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Why the Schrodinger Equation Is Not Enough contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

125. Derive the core relation for why the schrodinger equation is not enough from the definitions used in this lesson.

126. Construct a simple example and verify the relation numerically or component by component.

127. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 19 Dirac Equation

This lesson develops dirac equation as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in dirac equation.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$(i\gamma\mu\partial\mu - m)\psi = 0$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which dirac equation appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

128. State the symmetry, dynamical principle, or algebraic definition.

129. Write the most general expression compatible with the assumptions.

130. Apply the defining relation and simplify without dropping boundary or sign terms.

131. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for dirac equation on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Dirac Equation contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

132. Derive the core relation for dirac equation from the definitions used in this lesson.

133. Construct a simple example and verify the relation numerically or component by component.

134. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 20 Gamma Matrices

This lesson develops gamma matrices as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in gamma matrices.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\{\gamma\mu,\gamma\nu\} = 2g\mu\nu$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which gamma matrices appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

135. State the symmetry, dynamical principle, or algebraic definition.

136. Write the most general expression compatible with the assumptions.

137. Apply the defining relation and simplify without dropping boundary or sign terms.

138. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for gamma matrices on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Gamma Matrices contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

139. Derive the core relation for gamma matrices from the definitions used in this lesson.

140. Construct a simple example and verify the relation numerically or component by component.

141. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 21 Dirac Spinors

This lesson develops dirac spinors as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in dirac spinors.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\Sigma s\ u\_ s(p)u\bar{}\_ s(p) = p\not{} + m$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which dirac spinors appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

142. State the symmetry, dynamical principle, or algebraic definition.

143. Write the most general expression compatible with the assumptions.

144. Apply the defining relation and simplify without dropping boundary or sign terms.

145. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for dirac spinors on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Dirac Spinors contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

146. Derive the core relation for dirac spinors from the definitions used in this lesson.

147. Construct a simple example and verify the relation numerically or component by component.

148. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 22 Antiparticles

This lesson develops antiparticles as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in antiparticles.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\psi\ contains\ particle\ and\ antiparticle\ modes$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which antiparticles appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

149. State the symmetry, dynamical principle, or algebraic definition.

150. Write the most general expression compatible with the assumptions.

151. Apply the defining relation and simplify without dropping boundary or sign terms.

152. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for antiparticles on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Antiparticles contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

153. Derive the core relation for antiparticles from the definitions used in this lesson.

154. Construct a simple example and verify the relation numerically or component by component.

155. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 23 Relativistic Probability and Current

This lesson develops relativistic probability and current as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in relativistic probability and current.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$j\mu = \psi\bar{}\gamma\mu\psi;\ \ \partial\mu j\mu = 0$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which relativistic probability and current appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

156. State the symmetry, dynamical principle, or algebraic definition.

157. Write the most general expression compatible with the assumptions.

158. Apply the defining relation and simplify without dropping boundary or sign terms.

159. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for relativistic probability and current on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Relativistic Probability and Current contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

160. Derive the core relation for relativistic probability and current from the definitions used in this lesson.

161. Construct a simple example and verify the relation numerically or component by component.

162. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Part IV Classical Field Theory

# Lesson 24 Fields as Dynamical Systems

This lesson develops fields as dynamical systems as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in fields as dynamical systems.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\varphi = \varphi(x)$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which fields as dynamical systems appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

163. State the symmetry, dynamical principle, or algebraic definition.

164. Write the most general expression compatible with the assumptions.

165. Apply the defining relation and simplify without dropping boundary or sign terms.

166. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for fields as dynamical systems on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Fields as Dynamical Systems contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

167. Derive the core relation for fields as dynamical systems from the definitions used in this lesson.

168. Construct a simple example and verify the relation numerically or component by component.

169. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 25 Lagrangian Density

This lesson develops lagrangian density as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in lagrangian density.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$S = \int d⁴x\ \mathcal{L}$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which lagrangian density appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

170. State the symmetry, dynamical principle, or algebraic definition.

171. Write the most general expression compatible with the assumptions.

172. Apply the defining relation and simplify without dropping boundary or sign terms.

173. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for lagrangian density on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Lagrangian Density contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

174. Derive the core relation for lagrangian density from the definitions used in this lesson.

175. Construct a simple example and verify the relation numerically or component by component.

176. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 26 Euler Lagrange Equations for Fields

This lesson develops euler lagrange equations for fields as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in euler lagrange equations for fields.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\partial\mathcal{L}/\partial\varphi - \partial\mu\lbrack\partial\mathcal{L}/\partial(\partial\mu\varphi)\rbrack = 0$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which euler lagrange equations for fields appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

177. State the symmetry, dynamical principle, or algebraic definition.

178. Write the most general expression compatible with the assumptions.

179. Apply the defining relation and simplify without dropping boundary or sign terms.

180. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for euler lagrange equations for fields on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Euler Lagrange Equations for Fields contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

181. Derive the core relation for euler lagrange equations for fields from the definitions used in this lesson.

182. Construct a simple example and verify the relation numerically or component by component.

183. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 27 Noether Theorem

This lesson develops noether theorem as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in noether theorem.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$continuous\ symmetry\  \Rightarrow \ conserved\ current$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which noether theorem appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

184. State the symmetry, dynamical principle, or algebraic definition.

185. Write the most general expression compatible with the assumptions.

186. Apply the defining relation and simplify without dropping boundary or sign terms.

187. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for noether theorem on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Noether Theorem contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

188. Derive the core relation for noether theorem from the definitions used in this lesson.

189. Construct a simple example and verify the relation numerically or component by component.

190. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 28 Continuous Symmetries

This lesson develops continuous symmetries as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in continuous symmetries.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\delta\varphi = \varepsilon\Delta\varphi$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which continuous symmetries appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

191. State the symmetry, dynamical principle, or algebraic definition.

192. Write the most general expression compatible with the assumptions.

193. Apply the defining relation and simplify without dropping boundary or sign terms.

194. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for continuous symmetries on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Continuous Symmetries contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

195. Derive the core relation for continuous symmetries from the definitions used in this lesson.

196. Construct a simple example and verify the relation numerically or component by component.

197. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 29 Conserved Currents

This lesson develops conserved currents as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in conserved currents.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\partial\mu j\mu = 0$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which conserved currents appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

198. State the symmetry, dynamical principle, or algebraic definition.

199. Write the most general expression compatible with the assumptions.

200. Apply the defining relation and simplify without dropping boundary or sign terms.

201. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for conserved currents on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Conserved Currents contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

202. Derive the core relation for conserved currents from the definitions used in this lesson.

203. Construct a simple example and verify the relation numerically or component by component.

204. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 30 Global U 1 Symmetry

This lesson develops global u 1 symmetry as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in global u 1 symmetry.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\psi \rightarrow e\hat{}(i\alpha)\psi$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which global u 1 symmetry appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

205. State the symmetry, dynamical principle, or algebraic definition.

206. Write the most general expression compatible with the assumptions.

207. Apply the defining relation and simplify without dropping boundary or sign terms.

208. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for global u 1 symmetry on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Global U 1 Symmetry contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

209. Derive the core relation for global u 1 symmetry from the definitions used in this lesson.

210. Construct a simple example and verify the relation numerically or component by component.

211. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Part V Quantum Field Theory

# Lesson 31 Why Particles Become Fields

This lesson develops why particles become fields as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in why particles become fields.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$relativity\ plus\ creation\ implies\ field\ degrees\ of\ freedom$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which why particles become fields appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

212. State the symmetry, dynamical principle, or algebraic definition.

213. Write the most general expression compatible with the assumptions.

214. Apply the defining relation and simplify without dropping boundary or sign terms.

215. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for why particles become fields on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Why Particles Become Fields contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

216. Derive the core relation for why particles become fields from the definitions used in this lesson.

217. Construct a simple example and verify the relation numerically or component by component.

218. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 32 Quantizing the Scalar Field

This lesson develops quantizing the scalar field as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in quantizing the scalar field.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\lbrack\varphi(t,x),\pi(t,y)\rbrack = i\delta ³(x - y)$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which quantizing the scalar field appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

219. State the symmetry, dynamical principle, or algebraic definition.

220. Write the most general expression compatible with the assumptions.

221. Apply the defining relation and simplify without dropping boundary or sign terms.

222. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for quantizing the scalar field on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Quantizing the Scalar Field contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

223. Derive the core relation for quantizing the scalar field from the definitions used in this lesson.

224. Construct a simple example and verify the relation numerically or component by component.

225. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 33 Creation and Annihilation Operators

This lesson develops creation and annihilation operators as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in creation and annihilation operators.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\lbrack a\_ p,a \dagger \_ q\rbrack = (2\pi)³\delta ³(p - q)$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which creation and annihilation operators appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

226. State the symmetry, dynamical principle, or algebraic definition.

227. Write the most general expression compatible with the assumptions.

228. Apply the defining relation and simplify without dropping boundary or sign terms.

229. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for creation and annihilation operators on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Creation and Annihilation Operators contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

230. Derive the core relation for creation and annihilation operators from the definitions used in this lesson.

231. Construct a simple example and verify the relation numerically or component by component.

232. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 34 Fock Space

This lesson develops fock space as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in fock space.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$|n\rangle = (a \dagger )ⁿ|0\rangle/\sqrt{}n!$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which fock space appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

233. State the symmetry, dynamical principle, or algebraic definition.

234. Write the most general expression compatible with the assumptions.

235. Apply the defining relation and simplify without dropping boundary or sign terms.

236. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for fock space on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Fock Space contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

237. Derive the core relation for fock space from the definitions used in this lesson.

238. Construct a simple example and verify the relation numerically or component by component.

239. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 35 Quantizing the Dirac Field

This lesson develops quantizing the dirac field as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in quantizing the dirac field.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\psi(x) = particle\ modes\  + \ antiparticle\ modes$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which quantizing the dirac field appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

240. State the symmetry, dynamical principle, or algebraic definition.

241. Write the most general expression compatible with the assumptions.

242. Apply the defining relation and simplify without dropping boundary or sign terms.

243. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for quantizing the dirac field on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Quantizing the Dirac Field contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

244. Derive the core relation for quantizing the dirac field from the definitions used in this lesson.

245. Construct a simple example and verify the relation numerically or component by component.

246. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 36 Anticommutation Relations

This lesson develops anticommutation relations as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in anticommutation relations.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\{ b\_ p,b \dagger \_ q\} = (2\pi)³\delta ³(p - q)$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which anticommutation relations appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

247. State the symmetry, dynamical principle, or algebraic definition.

248. Write the most general expression compatible with the assumptions.

249. Apply the defining relation and simplify without dropping boundary or sign terms.

250. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for anticommutation relations on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Anticommutation Relations contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

251. Derive the core relation for anticommutation relations from the definitions used in this lesson.

252. Construct a simple example and verify the relation numerically or component by component.

253. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 37 Quantizing the Electromagnetic Field

This lesson develops quantizing the electromagnetic field as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in quantizing the electromagnetic field.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$A\mu(x) = \Sigma\lambda\int d³k\ \lbrack a\lambda\varepsilon\mu e\hat{}( - ikx) + h.c.\rbrack$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which quantizing the electromagnetic field appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

254. State the symmetry, dynamical principle, or algebraic definition.

255. Write the most general expression compatible with the assumptions.

256. Apply the defining relation and simplify without dropping boundary or sign terms.

257. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for quantizing the electromagnetic field on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Quantizing the Electromagnetic Field contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

258. Derive the core relation for quantizing the electromagnetic field from the definitions used in this lesson.

259. Construct a simple example and verify the relation numerically or component by component.

260. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Part VI QED

# Lesson 38 Local U 1 Gauge Symmetry

This lesson develops local u 1 gauge symmetry as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in local u 1 gauge symmetry.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\psi(x) \rightarrow e\hat{}(ie\alpha(x))\psi(x)$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which local u 1 gauge symmetry appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

261. State the symmetry, dynamical principle, or algebraic definition.

262. Write the most general expression compatible with the assumptions.

263. Apply the defining relation and simplify without dropping boundary or sign terms.

264. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for local u 1 gauge symmetry on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Local U 1 Gauge Symmetry contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

265. Derive the core relation for local u 1 gauge symmetry from the definitions used in this lesson.

266. Construct a simple example and verify the relation numerically or component by component.

267. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 39 Deriving the Electromagnetic Interaction

This lesson develops deriving the electromagnetic interaction as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in deriving the electromagnetic interaction.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\mathcal{L}int = - e\psi\bar{}\gamma\mu\psi A\mu$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which deriving the electromagnetic interaction appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

268. State the symmetry, dynamical principle, or algebraic definition.

269. Write the most general expression compatible with the assumptions.

270. Apply the defining relation and simplify without dropping boundary or sign terms.

271. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for deriving the electromagnetic interaction on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Deriving the Electromagnetic Interaction contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

272. Derive the core relation for deriving the electromagnetic interaction from the definitions used in this lesson.

273. Construct a simple example and verify the relation numerically or component by component.

274. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 40 The Covariant Derivative

This lesson develops the covariant derivative as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in the covariant derivative.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$D\mu = \partial\mu + ieA\mu$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which the covariant derivative appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

275. State the symmetry, dynamical principle, or algebraic definition.

276. Write the most general expression compatible with the assumptions.

277. Apply the defining relation and simplify without dropping boundary or sign terms.

278. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for the covariant derivative on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

The Covariant Derivative contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

279. Derive the core relation for the covariant derivative from the definitions used in this lesson.

280. Construct a simple example and verify the relation numerically or component by component.

281. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 41 The QED Lagrangian

This lesson develops the qed lagrangian as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in the qed lagrangian.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\mathcal{L}QED = \psi\bar{}(i\gamma\mu D\mu - m)\psi - ¼F\mu\nu F\mu\nu$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which the qed lagrangian appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

282. State the symmetry, dynamical principle, or algebraic definition.

283. Write the most general expression compatible with the assumptions.

284. Apply the defining relation and simplify without dropping boundary or sign terms.

285. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for the qed lagrangian on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

The QED Lagrangian contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

286. Derive the core relation for the qed lagrangian from the definitions used in this lesson.

287. Construct a simple example and verify the relation numerically or component by component.

288. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 42 The Electromagnetic Field Tensor

This lesson develops the electromagnetic field tensor as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in the electromagnetic field tensor.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$F\mu\nu = \partial\mu A\nu - \partial\nu A\mu$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which the electromagnetic field tensor appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

289. State the symmetry, dynamical principle, or algebraic definition.

290. Write the most general expression compatible with the assumptions.

291. Apply the defining relation and simplify without dropping boundary or sign terms.

292. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for the electromagnetic field tensor on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

The Electromagnetic Field Tensor contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

293. Derive the core relation for the electromagnetic field tensor from the definitions used in this lesson.

294. Construct a simple example and verify the relation numerically or component by component.

295. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 43 Electric Charge as a Coupling Constant

This lesson develops electric charge as a coupling constant as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in electric charge as a coupling constant.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\alpha = e²/(4\pi) \approx 1/137$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which electric charge as a coupling constant appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

296. State the symmetry, dynamical principle, or algebraic definition.

297. Write the most general expression compatible with the assumptions.

298. Apply the defining relation and simplify without dropping boundary or sign terms.

299. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for electric charge as a coupling constant on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Electric Charge as a Coupling Constant contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

300. Derive the core relation for electric charge as a coupling constant from the definitions used in this lesson.

301. Construct a simple example and verify the relation numerically or component by component.

302. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 44 The Electron Photon Vertex

This lesson develops the electron photon vertex as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in the electron photon vertex.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$vertex\ factor\  - ie\gamma\mu$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which the electron photon vertex appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

303. State the symmetry, dynamical principle, or algebraic definition.

304. Write the most general expression compatible with the assumptions.

305. Apply the defining relation and simplify without dropping boundary or sign terms.

306. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for the electron photon vertex on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

The Electron Photon Vertex contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

307. Derive the core relation for the electron photon vertex from the definitions used in this lesson.

308. Construct a simple example and verify the relation numerically or component by component.

309. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Part VII Feynman Diagrams

# Lesson 45 Propagators

This lesson develops propagators as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in propagators.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$propagator\  = \ inverse\ of\ the\ quadratic\ kinetic\ operator$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which propagators appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

310. State the symmetry, dynamical principle, or algebraic definition.

311. Write the most general expression compatible with the assumptions.

312. Apply the defining relation and simplify without dropping boundary or sign terms.

313. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for propagators on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Propagators contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

314. Derive the core relation for propagators from the definitions used in this lesson.

315. Construct a simple example and verify the relation numerically or component by component.

316. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 46 Electron Propagator

This lesson develops electron propagator as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in electron propagator.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$S\_ F(p) = i(p\not{} + m)/(p² - m² + i\varepsilon)$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which electron propagator appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

317. State the symmetry, dynamical principle, or algebraic definition.

318. Write the most general expression compatible with the assumptions.

319. Apply the defining relation and simplify without dropping boundary or sign terms.

320. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for electron propagator on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Electron Propagator contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

321. Derive the core relation for electron propagator from the definitions used in this lesson.

322. Construct a simple example and verify the relation numerically or component by component.

323. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 47 Photon Propagator

This lesson develops photon propagator as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in photon propagator.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$D\mu\nu(q) = - ig\mu\nu/(q² + i\varepsilon)\ in\ Feynman\ gauge$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which photon propagator appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

324. State the symmetry, dynamical principle, or algebraic definition.

325. Write the most general expression compatible with the assumptions.

326. Apply the defining relation and simplify without dropping boundary or sign terms.

327. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for photon propagator on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Photon Propagator contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

328. Derive the core relation for photon propagator from the definitions used in this lesson.

329. Construct a simple example and verify the relation numerically or component by component.

330. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 48 Interaction Vertices

This lesson develops interaction vertices as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in interaction vertices.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$each\ QED\ vertex\ joins\ two\ fermion\ legs\ and\ one\ photon\ leg$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which interaction vertices appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

331. State the symmetry, dynamical principle, or algebraic definition.

332. Write the most general expression compatible with the assumptions.

333. Apply the defining relation and simplify without dropping boundary or sign terms.

334. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for interaction vertices on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Interaction Vertices contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

335. Derive the core relation for interaction vertices from the definitions used in this lesson.

336. Construct a simple example and verify the relation numerically or component by component.

337. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 49 Feynman Rules

This lesson develops feynman rules as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in feynman rules.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$diagram\ topology\ maps\ to\ algebraic\ factors$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which feynman rules appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

338. State the symmetry, dynamical principle, or algebraic definition.

339. Write the most general expression compatible with the assumptions.

340. Apply the defining relation and simplify without dropping boundary or sign terms.

341. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for feynman rules on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Feynman Rules contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

342. Derive the core relation for feynman rules from the definitions used in this lesson.

343. Construct a simple example and verify the relation numerically or component by component.

344. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 50 Scattering Amplitudes

This lesson develops scattering amplitudes as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in scattering amplitudes.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\langle f|S|i\rangle = i(2\pi)⁴\delta ⁴(pf - pi)\mathcal{M}$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which scattering amplitudes appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

345. State the symmetry, dynamical principle, or algebraic definition.

346. Write the most general expression compatible with the assumptions.

347. Apply the defining relation and simplify without dropping boundary or sign terms.

348. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for scattering amplitudes on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Scattering Amplitudes contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

349. Derive the core relation for scattering amplitudes from the definitions used in this lesson.

350. Construct a simple example and verify the relation numerically or component by component.

351. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 51 External Spinors and Polarization

This lesson develops external spinors and polarization as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in external spinors and polarization.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$u,\ u\bar{},\ v,\ v\bar{},\ and\ \varepsilon\mu\ represent\ external\ states$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which external spinors and polarization appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

352. State the symmetry, dynamical principle, or algebraic definition.

353. Write the most general expression compatible with the assumptions.

354. Apply the defining relation and simplify without dropping boundary or sign terms.

355. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for external spinors and polarization on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

External Spinors and Polarization contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

356. Derive the core relation for external spinors and polarization from the definitions used in this lesson.

357. Construct a simple example and verify the relation numerically or component by component.

358. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 52 Momentum Conservation

This lesson develops momentum conservation as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in momentum conservation.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\Sigma\ pin = \Sigma\ pout$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which momentum conservation appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

359. State the symmetry, dynamical principle, or algebraic definition.

360. Write the most general expression compatible with the assumptions.

361. Apply the defining relation and simplify without dropping boundary or sign terms.

362. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for momentum conservation on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Momentum Conservation contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

363. Derive the core relation for momentum conservation from the definitions used in this lesson.

364. Construct a simple example and verify the relation numerically or component by component.

365. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Part VIII Real Calculations

# Lesson 53 Electron Muon Scattering

This lesson develops electron muon scattering as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in electron muon scattering.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\mathcal{M} \propto \lbrack u\bar{}e\gamma\mu ue\rbrack( - g\mu\nu/q²)\lbrack u\bar{}\mu\gamma\nu u\mu\rbrack$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which electron muon scattering appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

366. State the symmetry, dynamical principle, or algebraic definition.

367. Write the most general expression compatible with the assumptions.

368. Apply the defining relation and simplify without dropping boundary or sign terms.

369. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for electron muon scattering on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Electron Muon Scattering contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

370. Derive the core relation for electron muon scattering from the definitions used in this lesson.

371. Construct a simple example and verify the relation numerically or component by component.

372. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 54 Electron Electron Scattering

This lesson develops electron electron scattering as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in electron electron scattering.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\mathcal{M} = \mathcal{M}t - \mathcal{M}u$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which electron electron scattering appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

373. State the symmetry, dynamical principle, or algebraic definition.

374. Write the most general expression compatible with the assumptions.

375. Apply the defining relation and simplify without dropping boundary or sign terms.

376. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for electron electron scattering on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Electron Electron Scattering contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

377. Derive the core relation for electron electron scattering from the definitions used in this lesson.

378. Construct a simple example and verify the relation numerically or component by component.

379. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 55 Electron Positron Annihilation

This lesson develops electron positron annihilation as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in electron positron annihilation.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$e⁺e⁻ \rightarrow \gamma* \rightarrow f\ f\bar{}$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which electron positron annihilation appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

380. State the symmetry, dynamical principle, or algebraic definition.

381. Write the most general expression compatible with the assumptions.

382. Apply the defining relation and simplify without dropping boundary or sign terms.

383. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for electron positron annihilation on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Electron Positron Annihilation contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

384. Derive the core relation for electron positron annihilation from the definitions used in this lesson.

385. Construct a simple example and verify the relation numerically or component by component.

386. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 56 Compton Scattering

This lesson develops compton scattering as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in compton scattering.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\mathcal{M} = \mathcal{M}s + \mathcal{M}u$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which compton scattering appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

387. State the symmetry, dynamical principle, or algebraic definition.

388. Write the most general expression compatible with the assumptions.

389. Apply the defining relation and simplify without dropping boundary or sign terms.

390. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for compton scattering on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Compton Scattering contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

391. Derive the core relation for compton scattering from the definitions used in this lesson.

392. Construct a simple example and verify the relation numerically or component by component.

393. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 57 Pair Production

This lesson develops pair production as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in pair production.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\gamma\gamma \rightarrow e⁺e⁻$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which pair production appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

394. State the symmetry, dynamical principle, or algebraic definition.

395. Write the most general expression compatible with the assumptions.

396. Apply the defining relation and simplify without dropping boundary or sign terms.

397. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for pair production on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Pair Production contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

398. Derive the core relation for pair production from the definitions used in this lesson.

399. Construct a simple example and verify the relation numerically or component by component.

400. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 58 From Amplitude to Cross Section

This lesson develops from amplitude to cross section as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in from amplitude to cross section.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$d\sigma = (1/4F)|\mathcal{M}|²d\Phi$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which from amplitude to cross section appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

401. State the symmetry, dynamical principle, or algebraic definition.

402. Write the most general expression compatible with the assumptions.

403. Apply the defining relation and simplify without dropping boundary or sign terms.

404. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for from amplitude to cross section on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

From Amplitude to Cross Section contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

405. Derive the core relation for from amplitude to cross section from the definitions used in this lesson.

406. Construct a simple example and verify the relation numerically or component by component.

407. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 59 Decay Rates

This lesson develops decay rates as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in decay rates.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$d\Gamma = (1/2M)|\mathcal{M}|²d\Phi n$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which decay rates appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

408. State the symmetry, dynamical principle, or algebraic definition.

409. Write the most general expression compatible with the assumptions.

410. Apply the defining relation and simplify without dropping boundary or sign terms.

411. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for decay rates on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Decay Rates contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

412. Derive the core relation for decay rates from the definitions used in this lesson.

413. Construct a simple example and verify the relation numerically or component by component.

414. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 60 Experimental Predictions

This lesson develops experimental predictions as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in experimental predictions.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$prediction\  = \ amplitude\ squared\  \times \ phase\ space\  \times \ detector\ definition$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which experimental predictions appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

415. State the symmetry, dynamical principle, or algebraic definition.

416. Write the most general expression compatible with the assumptions.

417. Apply the defining relation and simplify without dropping boundary or sign terms.

418. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for experimental predictions on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Experimental Predictions contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

419. Derive the core relation for experimental predictions from the definitions used in this lesson.

420. Construct a simple example and verify the relation numerically or component by component.

421. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Part IX Quantum Corrections

# Lesson 61 Loop Diagrams

This lesson develops loop diagrams as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in loop diagrams.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$each\ loop\ introduces\ \int d⁴k/(2\pi)⁴$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which loop diagrams appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

422. State the symmetry, dynamical principle, or algebraic definition.

423. Write the most general expression compatible with the assumptions.

424. Apply the defining relation and simplify without dropping boundary or sign terms.

425. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for loop diagrams on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Loop Diagrams contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

426. Derive the core relation for loop diagrams from the definitions used in this lesson.

427. Construct a simple example and verify the relation numerically or component by component.

428. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 62 Vacuum Polarization

This lesson develops vacuum polarization as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in vacuum polarization.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\Pi\mu\nu(q) = (q\mu q\nu - q²g\mu\nu)\Pi(q²)$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which vacuum polarization appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

429. State the symmetry, dynamical principle, or algebraic definition.

430. Write the most general expression compatible with the assumptions.

431. Apply the defining relation and simplify without dropping boundary or sign terms.

432. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for vacuum polarization on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Vacuum Polarization contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

433. Derive the core relation for vacuum polarization from the definitions used in this lesson.

434. Construct a simple example and verify the relation numerically or component by component.

435. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 63 Electron Self Energy

This lesson develops electron self energy as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in electron self energy.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$S⁻¹(p) = p\not{} - m - \Sigma(p)$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which electron self energy appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

436. State the symmetry, dynamical principle, or algebraic definition.

437. Write the most general expression compatible with the assumptions.

438. Apply the defining relation and simplify without dropping boundary or sign terms.

439. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for electron self energy on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Electron Self Energy contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

440. Derive the core relation for electron self energy from the definitions used in this lesson.

441. Construct a simple example and verify the relation numerically or component by component.

442. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 64 Vertex Corrections

This lesson develops vertex corrections as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in vertex corrections.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\Gamma\mu = \gamma\mu + \Lambda\mu$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which vertex corrections appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

443. State the symmetry, dynamical principle, or algebraic definition.

444. Write the most general expression compatible with the assumptions.

445. Apply the defining relation and simplify without dropping boundary or sign terms.

446. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for vertex corrections on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Vertex Corrections contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

447. Derive the core relation for vertex corrections from the definitions used in this lesson.

448. Construct a simple example and verify the relation numerically or component by component.

449. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 65 Ultraviolet Divergences

This lesson develops ultraviolet divergences as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in ultraviolet divergences.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$large\ loop\ momentum\ can\ make\ integrals\ divergent$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which ultraviolet divergences appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

450. State the symmetry, dynamical principle, or algebraic definition.

451. Write the most general expression compatible with the assumptions.

452. Apply the defining relation and simplify without dropping boundary or sign terms.

453. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for ultraviolet divergences on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Ultraviolet Divergences contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

454. Derive the core relation for ultraviolet divergences from the definitions used in this lesson.

455. Construct a simple example and verify the relation numerically or component by component.

456. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 66 Regularization

This lesson develops regularization as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in regularization.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$d = 4 - 2\varepsilon\ in\ dimensional\ regularization$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which regularization appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

457. State the symmetry, dynamical principle, or algebraic definition.

458. Write the most general expression compatible with the assumptions.

459. Apply the defining relation and simplify without dropping boundary or sign terms.

460. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for regularization on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Regularization contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

461. Derive the core relation for regularization from the definitions used in this lesson.

462. Construct a simple example and verify the relation numerically or component by component.

463. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 67 Renormalization

This lesson develops renormalization as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in renormalization.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$m0 = m + \delta m;\ \ \psi 0 = \sqrt{}Z2\ \psi$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which renormalization appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

464. State the symmetry, dynamical principle, or algebraic definition.

465. Write the most general expression compatible with the assumptions.

466. Apply the defining relation and simplify without dropping boundary or sign terms.

467. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for renormalization on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Renormalization contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

468. Derive the core relation for renormalization from the definitions used in this lesson.

469. Construct a simple example and verify the relation numerically or component by component.

470. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 68 Running Electric Charge

This lesson develops running electric charge as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in running electric charge.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$e = e(\mu)$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which running electric charge appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

471. State the symmetry, dynamical principle, or algebraic definition.

472. Write the most general expression compatible with the assumptions.

473. Apply the defining relation and simplify without dropping boundary or sign terms.

474. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for running electric charge on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Running Electric Charge contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

475. Derive the core relation for running electric charge from the definitions used in this lesson.

476. Construct a simple example and verify the relation numerically or component by component.

477. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 69 Renormalization Group

This lesson develops renormalization group as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in renormalization group.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\mu\ d\ e/d\mu = \beta(e)$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which renormalization group appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

478. State the symmetry, dynamical principle, or algebraic definition.

479. Write the most general expression compatible with the assumptions.

480. Apply the defining relation and simplify without dropping boundary or sign terms.

481. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for renormalization group on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Renormalization Group contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

482. Derive the core relation for renormalization group from the definitions used in this lesson.

483. Construct a simple example and verify the relation numerically or component by component.

484. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Part X Deep QED

# Lesson 70 Gauge Fixing

This lesson develops gauge fixing as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in gauge fixing.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\mathcal{L}gf = - (\partial\mu A\mu)²/(2\xi)$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which gauge fixing appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

485. State the symmetry, dynamical principle, or algebraic definition.

486. Write the most general expression compatible with the assumptions.

487. Apply the defining relation and simplify without dropping boundary or sign terms.

488. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for gauge fixing on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Gauge Fixing contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

489. Derive the core relation for gauge fixing from the definitions used in this lesson.

490. Construct a simple example and verify the relation numerically or component by component.

491. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 71 Ward Identities

This lesson develops ward identities as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in ward identities.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$q\mu\Gamma\mu = S⁻¹(p + q) - S⁻¹(p)$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which ward identities appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

492. State the symmetry, dynamical principle, or algebraic definition.

493. Write the most general expression compatible with the assumptions.

494. Apply the defining relation and simplify without dropping boundary or sign terms.

495. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for ward identities on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Ward Identities contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

496. Derive the core relation for ward identities from the definitions used in this lesson.

497. Construct a simple example and verify the relation numerically or component by component.

498. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 72 Gauge Invariance

This lesson develops gauge invariance as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in gauge invariance.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$physical\ observables\ are\ independent\ of\ gauge\ choice$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which gauge invariance appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

499. State the symmetry, dynamical principle, or algebraic definition.

500. Write the most general expression compatible with the assumptions.

501. Apply the defining relation and simplify without dropping boundary or sign terms.

502. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for gauge invariance on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Gauge Invariance contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

503. Derive the core relation for gauge invariance from the definitions used in this lesson.

504. Construct a simple example and verify the relation numerically or component by component.

505. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 73 Infrared Divergences

This lesson develops infrared divergences as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in infrared divergences.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$soft\ or\ collinear\ limits\ require\ inclusive\ observables$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which infrared divergences appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

506. State the symmetry, dynamical principle, or algebraic definition.

507. Write the most general expression compatible with the assumptions.

508. Apply the defining relation and simplify without dropping boundary or sign terms.

509. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for infrared divergences on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Infrared Divergences contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

510. Derive the core relation for infrared divergences from the definitions used in this lesson.

511. Construct a simple example and verify the relation numerically or component by component.

512. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 74 Soft Photons

This lesson develops soft photons as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in soft photons.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$virtual\ IR\ terms\ cancel\ real\ soft\ emission$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which soft photons appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

513. State the symmetry, dynamical principle, or algebraic definition.

514. Write the most general expression compatible with the assumptions.

515. Apply the defining relation and simplify without dropping boundary or sign terms.

516. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for soft photons on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Soft Photons contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

517. Derive the core relation for soft photons from the definitions used in this lesson.

518. Construct a simple example and verify the relation numerically or component by component.

519. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 75 The Anomalous Magnetic Moment

This lesson develops the anomalous magnetic moment as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in the anomalous magnetic moment.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$a\_ e = (g - 2)/2 = \alpha/(2\pi) + \ldots$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which the anomalous magnetic moment appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

520. State the symmetry, dynamical principle, or algebraic definition.

521. Write the most general expression compatible with the assumptions.

522. Apply the defining relation and simplify without dropping boundary or sign terms.

523. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for the anomalous magnetic moment on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

The Anomalous Magnetic Moment contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

524. Derive the core relation for the anomalous magnetic moment from the definitions used in this lesson.

525. Construct a simple example and verify the relation numerically or component by component.

526. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 76 Lamb Shift

This lesson develops lamb shift as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in lamb shift.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$radiative\ corrections\ split\ otherwise\ degenerate\ atomic\ levels$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which lamb shift appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

527. State the symmetry, dynamical principle, or algebraic definition.

528. Write the most general expression compatible with the assumptions.

529. Apply the defining relation and simplify without dropping boundary or sign terms.

530. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for lamb shift on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Lamb Shift contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

531. Derive the core relation for lamb shift from the definitions used in this lesson.

532. Construct a simple example and verify the relation numerically or component by component.

533. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 77 Vacuum Polarization and Precision

This lesson develops vacuum polarization and precision as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in vacuum polarization and precision.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$screening\ makes\ the\ effective\ charge\ scale\ dependent$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which vacuum polarization and precision appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

534. State the symmetry, dynamical principle, or algebraic definition.

535. Write the most general expression compatible with the assumptions.

536. Apply the defining relation and simplify without dropping boundary or sign terms.

537. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for vacuum polarization and precision on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Vacuum Polarization and Precision contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

538. Derive the core relation for vacuum polarization and precision from the definitions used in this lesson.

539. Construct a simple example and verify the relation numerically or component by component.

540. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 78 Precision Tests of QED

This lesson develops precision tests of qed as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in precision tests of qed.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$compare\ consistently\ defined\ theory\ and\ measurement$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which precision tests of qed appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

541. State the symmetry, dynamical principle, or algebraic definition.

542. Write the most general expression compatible with the assumptions.

543. Apply the defining relation and simplify without dropping boundary or sign terms.

544. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for precision tests of qed on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Precision Tests of QED contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

545. Derive the core relation for precision tests of qed from the definitions used in this lesson.

546. Construct a simple example and verify the relation numerically or component by component.

547. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Part XI Beyond the Basic Course

# Lesson 79 Path Integrals

This lesson develops path integrals as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in path integrals.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$Z = \int D\varphi\ exp(iS\lbrack\varphi\rbrack)$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which path integrals appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

548. State the symmetry, dynamical principle, or algebraic definition.

549. Write the most general expression compatible with the assumptions.

550. Apply the defining relation and simplify without dropping boundary or sign terms.

551. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for path integrals on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Path Integrals contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

552. Derive the core relation for path integrals from the definitions used in this lesson.

553. Construct a simple example and verify the relation numerically or component by component.

554. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 80 Generating Functionals

This lesson develops generating functionals as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in generating functionals.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$correlators\ come\ from\ functional\ derivatives\ of\ Z\lbrack J\rbrack$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which generating functionals appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

555. State the symmetry, dynamical principle, or algebraic definition.

556. Write the most general expression compatible with the assumptions.

557. Apply the defining relation and simplify without dropping boundary or sign terms.

558. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for generating functionals on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Generating Functionals contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

559. Derive the core relation for generating functionals from the definitions used in this lesson.

560. Construct a simple example and verify the relation numerically or component by component.

561. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 81 Effective Actions

This lesson develops effective actions as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in effective actions.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\Gamma\lbrack\varphi\rbrack\ generates\ one\ particle\ irreducible\ functions$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which effective actions appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

562. State the symmetry, dynamical principle, or algebraic definition.

563. Write the most general expression compatible with the assumptions.

564. Apply the defining relation and simplify without dropping boundary or sign terms.

565. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for effective actions on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Effective Actions contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

566. Derive the core relation for effective actions from the definitions used in this lesson.

567. Construct a simple example and verify the relation numerically or component by component.

568. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 82 Functional Methods

This lesson develops functional methods as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in functional methods.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$\delta Z/\delta J\ inserts\ a\ field$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which functional methods appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

569. State the symmetry, dynamical principle, or algebraic definition.

570. Write the most general expression compatible with the assumptions.

571. Apply the defining relation and simplify without dropping boundary or sign terms.

572. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for functional methods on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Functional Methods contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

573. Derive the core relation for functional methods from the definitions used in this lesson.

574. Construct a simple example and verify the relation numerically or component by component.

575. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 83 Feynman Rules from the Path Integral

This lesson develops feynman rules from the path integral as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in feynman rules from the path integral.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$expand\ exp(iSint)\ and\ contract\ Gaussian\ fields$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which feynman rules from the path integral appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

576. State the symmetry, dynamical principle, or algebraic definition.

577. Write the most general expression compatible with the assumptions.

578. Apply the defining relation and simplify without dropping boundary or sign terms.

579. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for feynman rules from the path integral on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Feynman Rules from the Path Integral contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

580. Derive the core relation for feynman rules from the path integral from the definitions used in this lesson.

581. Construct a simple example and verify the relation numerically or component by component.

582. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 84 QED at Finite Temperature

This lesson develops qed at finite temperature as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in qed at finite temperature.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$Euclidean\ time\ is\ periodic\ with\ period\ 1/T$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which qed at finite temperature appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

583. State the symmetry, dynamical principle, or algebraic definition.

584. Write the most general expression compatible with the assumptions.

585. Apply the defining relation and simplify without dropping boundary or sign terms.

586. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for qed at finite temperature on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

QED at Finite Temperature contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

587. Derive the core relation for qed at finite temperature from the definitions used in this lesson.

588. Construct a simple example and verify the relation numerically or component by component.

589. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 85 QED in External Fields

This lesson develops qed in external fields as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in qed in external fields.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$replace\ A\mu\ by\ background\ plus\ quantum\ fluctuation$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which qed in external fields appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

590. State the symmetry, dynamical principle, or algebraic definition.

591. Write the most general expression compatible with the assumptions.

592. Apply the defining relation and simplify without dropping boundary or sign terms.

593. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for qed in external fields on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

QED in External Fields contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

594. Derive the core relation for qed in external fields from the definitions used in this lesson.

595. Construct a simple example and verify the relation numerically or component by component.

596. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Lesson 86 Connection to the Standard Model

This lesson develops connection to the standard model as part of the path from elementary mathematics to quantum electrodynamics. The goal is to make the central objects usable in derivations, not merely recognizable in formulas.

## Learning objectives

- Define the essential objects used in connection to the standard model.

- Derive the central relation from stated assumptions and conventions.

- Recognize how the result enters later quantum electrodynamics calculations.

## Core statement

$$U(1)em\ emerges\ after\ electroweak\ symmetry\ breaking$$

The displayed relation is the working center of this lesson. Read every symbol as an operation on a specified mathematical object. Check dimensions, signs, indices, and transformation properties before using it. In field theory, these checks often reveal an error earlier than a long calculation does.

## Development

Start from the simplest setting in which connection to the standard model appears. Separate definitions from consequences: a definition fixes notation, while a consequence must be proved. Then test the construction on a low-dimensional or free-field example. Finally, identify which assumptions survive when interactions are introduced.

Keep the distinction between an abstract object and its representation. A state is not its coordinate column, an operator is not tied to one matrix, and a field equation is not tied to one inertial frame or gauge. This distinction is especially important when changing basis, frame, gauge, or representation.

## Derivation workflow

597. State the symmetry, dynamical principle, or algebraic definition.

598. Write the most general expression compatible with the assumptions.

599. Apply the defining relation and simplify without dropping boundary or sign terms.

600. Check a special case, limiting case, and invariant quantity.

## Worked checkpoint

Reproduce the core statement for connection to the standard model on a blank page. Explain which step is a definition, which step uses a physical assumption, and which step is algebra. If the result carries indices, verify the free indices match on both sides. If it is an operator identity, apply both sides to an arbitrary test state.

## QED connection

Connection to the Standard Model contributes to the chain gauge symmetry to covariant dynamics to quantized fields to amplitudes to observables. Later lessons will reuse this result without rederiving every preliminary step, so fluency here reduces the apparent complexity of Feynman rules and radiative corrections.

## Exercises

601. Derive the core relation for connection to the standard model from the definitions used in this lesson.

602. Construct a simple example and verify the relation numerically or component by component.

603. Identify one convention change that alters intermediate signs but not a measurable prediction.

## Solution guidance

A complete solution should name every assumption, show the intermediate algebra, and end with at least one independent check. For the convention question, compare the full set of related definitions rather than changing one sign in isolation.

# Course capstone

Starting from a free Dirac field, impose local U 1 phase invariance, introduce the covariant derivative and electromagnetic field, derive the QED Lagrangian, quantize the free fields, read off propagators and the vertex, construct a tree level scattering amplitude, convert it to a cross section, and explain how regularization and renormalization modify the result at one loop. The capstone is complete only when each arrow in this chain is justified in words and equations.

# Consolidated formula index

**Calculus and Differential Equations:** d/dx exp(kx)=k exp(kx); ∇²φ−∂²φ/∂t²=0

**Special Relativity:** E²−\|p\|²=m²

**Four Vectors and Lorentz Transformations:** x′μ=Λμνxν; ΛTgΛ=g

**Classical Mechanics and Lagrangians:** d/dt(∂L/∂q̇)−∂L/∂q=0

**Hamiltonian Mechanics:** H=pq̇−L; q̇=∂H/∂p; ṗ=−∂H/∂q

**Maxwell Equations:** ∂μFμν=jν; ∂\[αFβγ\]=0

**Electromagnetic Potentials and Gauge Freedom:** Aμ→Aμ+∂μα

**Wave Functions and Hilbert Spaces:** ⟨ψ\|ψ⟩=1

**Operators and Observables:** A†=A

**Schrodinger Equation:** i∂t\|ψ⟩=H\|ψ⟩

**Momentum and Position:** \[xᵢ,pⱼ\]=iδᵢⱼ

**Angular Momentum:** \[Lᵢ,Lⱼ\]=iεᵢⱼₖLₖ

**Spin and Pauli Matrices:** S=σ/2

**Perturbation Theory:** Eₙ(1)=⟨n\|V\|n⟩

**Identical Particles:** \|ψ(1,2)⟩=±\|ψ(2,1)⟩

**Klein Gordon Equation:** (□+m²)φ=0

**Why the Schrodinger Equation Is Not Enough:** E²=p²+m²

**Dirac Equation:** (iγμ∂μ−m)ψ=0

**Gamma Matrices:** {γμ,γν}=2gμν

**Dirac Spinors:** Σs u_s(p)ū\_s(p)=p̸+m

**Antiparticles:** ψ contains particle and antiparticle modes

**Relativistic Probability and Current:** jμ=ψ̄γμψ; ∂μjμ=0

**Fields as Dynamical Systems:** φ=φ(x)

**Lagrangian Density:** S=∫d⁴x ℒ

**Euler Lagrange Equations for Fields:** ∂ℒ/∂φ−∂μ\[∂ℒ/∂(∂μφ)\]=0

**Noether Theorem:** continuous symmetry ⇒ conserved current

**Continuous Symmetries:** δφ=εΔφ

**Conserved Currents:** ∂μjμ=0

**Global U 1 Symmetry:** ψ→e\^(iα)ψ

**Why Particles Become Fields:** relativity plus creation implies field degrees of freedom

**Quantizing the Scalar Field:** \[φ(t,x),π(t,y)\]=iδ³(x−y)

**Creation and Annihilation Operators:** \[a_p,a†\_q\]=(2π)³δ³(p−q)

**Fock Space:** \|n⟩=(a†)ⁿ\|0⟩/√n!

**Quantizing the Dirac Field:** ψ(x)=particle modes + antiparticle modes

**Anticommutation Relations:** {b_p,b†\_q}=(2π)³δ³(p−q)

**Quantizing the Electromagnetic Field:** Aμ(x)=Σλ∫d³k \[aλεμe\^(−ikx)+h.c.\]

**Local U 1 Gauge Symmetry:** ψ(x)→e\^(ieα(x))ψ(x)

**Deriving the Electromagnetic Interaction:** ℒint=−eψ̄γμψAμ

**The Covariant Derivative:** Dμ=∂μ+ieAμ

**The QED Lagrangian:** ℒQED=ψ̄(iγμDμ−m)ψ−¼FμνFμν

**The Electromagnetic Field Tensor:** Fμν=∂μAν−∂νAμ

**Electric Charge as a Coupling Constant:** α=e²/(4π)≈1/137

**The Electron Photon Vertex:** vertex factor −ieγμ

**Propagators:** propagator = inverse of the quadratic kinetic operator

**Electron Propagator:** S_F(p)=i(p̸+m)/(p²−m²+iε)

**Photon Propagator:** Dμν(q)=−igμν/(q²+iε) in Feynman gauge

**Interaction Vertices:** each QED vertex joins two fermion legs and one photon leg

**Feynman Rules:** diagram topology maps to algebraic factors

**Scattering Amplitudes:** ⟨f\|S\|i⟩=i(2π)⁴δ⁴(pf−pi)ℳ

**External Spinors and Polarization:** u, ū, v, v̄, and εμ represent external states

**Momentum Conservation:** Σ pin=Σ pout

**Electron Muon Scattering:** ℳ∝\[ūeγμue\](−gμν/q²)\[ūμγνuμ\]

**Electron Electron Scattering:** ℳ=ℳt−ℳu

**Electron Positron Annihilation:** e⁺e⁻→γ\*→f f̄

**Compton Scattering:** ℳ=ℳs+ℳu

**Pair Production:** γγ→e⁺e⁻

**From Amplitude to Cross Section:** dσ=(1/4F)\|ℳ\|²dΦ

**Decay Rates:** dΓ=(1/2M)\|ℳ\|²dΦn

**Experimental Predictions:** prediction = amplitude squared × phase space × detector definition

**Loop Diagrams:** each loop introduces ∫d⁴k/(2π)⁴

**Vacuum Polarization:** Πμν(q)=(qμqν−q²gμν)Π(q²)

**Electron Self Energy:** S⁻¹(p)=p̸−m−Σ(p)

**Vertex Corrections:** Γμ=γμ+Λμ

**Ultraviolet Divergences:** large loop momentum can make integrals divergent

**Regularization:** d=4−2ε in dimensional regularization

**Renormalization:** m0=m+δm; ψ0=√Z2 ψ

**Running Electric Charge:** e=e(μ)

**Renormalization Group:** μ d e/dμ=β(e)

**Gauge Fixing:** ℒgf=−(∂μAμ)²/(2ξ)

**Ward Identities:** qμΓμ=S⁻¹(p+q)−S⁻¹(p)

**Gauge Invariance:** physical observables are independent of gauge choice

**Infrared Divergences:** soft or collinear limits require inclusive observables

**Soft Photons:** virtual IR terms cancel real soft emission

**The Anomalous Magnetic Moment:** a_e=(g−2)/2=α/(2π)+...

**Lamb Shift:** radiative corrections split otherwise degenerate atomic levels

**Vacuum Polarization and Precision:** screening makes the effective charge scale dependent

**Precision Tests of QED:** compare consistently defined theory and measurement

**Path Integrals:** Z=∫Dφ exp(iS\[φ\])

**Generating Functionals:** correlators come from functional derivatives of Z\[J\]

**Effective Actions:** Γ\[φ\] generates one particle irreducible functions

**Functional Methods:** δZ/δJ inserts a field

**Feynman Rules from the Path Integral:** expand exp(iSint) and contract Gaussian fields

**QED at Finite Temperature:** Euclidean time is periodic with period 1/T

**QED in External Fields:** replace Aμ by background plus quantum fluctuation

**Connection to the Standard Model:** U(1)em emerges after electroweak symmetry breaking
